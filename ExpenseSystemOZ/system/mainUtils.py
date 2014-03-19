'''
Created on 19/03/2014

@author: edwin
'''

from system import configs
from system import db, fileUtils, dbUtils
import logging
import re

def init_log():
    logging.basicConfig(filename=configs.log_file,
                        filemode='a',
                        format=configs.log_format,
                        datefmt=configs.date_time_format,
                        level=logging.DEBUG)

    logging.info("-----------------------------------------")
    logging.info(configs.version + " - Edwin He - " + configs.update_date)
    logging.info("-----------------------------------------")
    logging.info("Initializing Expense Analysis OZ...")
    logging.info("")
    
def init_db():
    logging.info("Initializing DB...")
    return db.DB(configs.db_file)

def refresh_mapping(db_h):
    for mapping in configs.keyword_mappings:
        logging.debug("Checking mapping: " + str(mapping))
        if dbUtils.is_new_mapping(db_h, mapping[0], mapping[1]):
            dbUtils.insert_mapping(db_h, mapping)
            
def refresh_records(db_h):
    # Import the records after: 
    # 1. Change date format
    # 2. Split on Super Market Cash Out
    # 3. Set date to Value Date for Credit a/c expense
    # 4. Set Type, Cate, SubCate and KeyWords to TBC and Insert into table 
    import_list = fileUtils.search_file(db_h)
    for (root, file_name) in import_list:
        fileUtils.import_file(db_h, root, file_name)
            
            
def fill_out_TBC(db_h):
    '''
    fill_out_TBC(db_handler)
    Resolve TBC fields in several ways:
    1. By mappings defined in configs.py
    2. By pairing up internal transfer made between Ed and Co
    3. Search for inflow with keywords Refund, Return. Pair them and make them off-balance 
    '''
    
    # 1
    mappings = dbUtils.fetch_mappings(db_h)
    for mapping in mappings:
        logging.debug("Updating " + mapping[1] + " records with key words: " + mapping[2])
        dbUtils.update_TBC_by_mapping(db_h, mapping)
    
    # 2
    internals = dbUtils.fetch_unpaired_internals(db_h)
    for internal in internals:
        # 0   1   2     3       4     5     6         7     8          9          10  
        #[id, io, date, amount, type, cate, sub_cate, desc, orig_desc, file_name, keywords] = internal
        logging.debug("Pairing internal transfer: " + ',' + str(internal[2]) + ',' + str(internal[3]) + ',' + str(internal[7]))
        
        lookfor_pattern = 'TRANSFER TO CBA A/C NETBANK ' + re.sub('TRANSFER FROM (.)+ NETBANK ','',internal[7])
        neg_amount = str(-1 * float(internal[3]))
        paired_internals = dbUtils.pair_internal(db_h, neg_amount, lookfor_pattern)
        if len(paired_internals) != 1:
            logging.warning("Failed to pair. " + str(len(paired_internals)) + " pair found! TBC not updated for record id = " + str(internal[0]))
        else:
            [paired_internal] = paired_internals
            logging.info("Paired: " + ',' + str(paired_internal[2]) + ',' + str(paired_internal[3]) + ',' + str(paired_internal[7]))
            dbUtils.update_TBC_by_paired_internals(db_h, internal[0], paired_internal[0])
            
    # 3
    
    
def display_TBC(db_h):
    TBC_records = dbUtils.fetch_TBC(db_h)
    for records in TBC_records:
        print(records[1:4],records[7:9])