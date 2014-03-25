'''
Created on 19/03/2014

@author: edwin
'''

from ozio_base import db, config
from ozio_utilities import fileUtils, dbUtils, reportUtils
import pandas as pd
import logging
import re
import datetime

def load_config(config_file):
    return config.CONFIG(config_file)

def init_log(cfg_h):
    
    log_file_name = cfg_h.log_config['log_files_loc'] + '.' +\
                    cfg_h.log_config['log_file_initial'] + '_' +\
                    datetime.datetime.now().strftime(cfg_h.log_config['log_file_datetime_format']) + '.' +\
                    cfg_h.log_config['log_file_ext']
                    
    logging.basicConfig(filename=log_file_name,
                        filemode='a',
                        format=cfg_h.log_config['log_format'],
                        datefmt=cfg_h.misc_config['date_time_format'],
                        level=logging.DEBUG)

    logging.info("-----------------------------------------")
    logging.info(cfg_h.misc_config['version'] + " - Edwin He - " + cfg_h.misc_config['update_date'])
    logging.info("-----------------------------------------")
    logging.info("Initializing Expense Analysis OZ...")
    logging.info("")
    
def init_db(db_config):
    #logging.info("Initializing DB...")
    try:
        db_h = db.DB(db_config)
        logging.info("MySQL Connected!")
        return db_h
    except Exception as e:
        logging.critical(e)
            
def refresh_records(db_h, cfg_h):
    # Import the records after: 
    # 1. Change date format
    # 2. Split on Super Market Cash Out
    # 3. Set date to Value Date for Credit a/c expense
    # 4. Set Type, Cate, SubCate and KeyWords to TBC and Insert into table 
    import_list = fileUtils.search_file(db_h, cfg_h)
    for (root, file_name) in import_list:
        fileUtils.import_file(db_h, root, file_name)
            
            
def fill_out_TBC(db_h):
    '''
    fill_out_TBC(db_handler)
    Resolve TBC fields in several ways:
    1. By mappings defined in configs.py
    2. By pairing up internal transfer made between Ed and Co
    '''
    
    # 1
    mappings = dbUtils.fetch_mappings(db_h)
    for mapping in mappings:
        logging.debug("Updating " + mapping[1] + " records with key words: " + mapping[2])
        dbUtils.update_TBC_by_mapping(db_h, mapping)
    
    # 2
    internals = dbUtils.fetch_unpaired_internals(db_h)
    for internal in internals:
        # 0   1     2       3     4     5         6     7          8          9  
        #[id, date, amount, type, cate, sub_cate, desc, orig_desc, file_name, keywords] = internal
        logging.info("Pairing internal transfer: " + ',' + str(internal[1]) + ',' + str(internal[2]) + ',' + str(internal[6]))
        
        lookfor_pattern = 'TRANSFER TO CBA A/C NETBANK ' + re.sub('TRANSFER FROM (.)+ NETBANK ','',internal[6])
        neg_amount = str(-1 * float(internal[2]))
        paired_internals = dbUtils.pair_internal(db_h, neg_amount, lookfor_pattern)
        if len(paired_internals) != 1:
            logging.warning("Failed to pair. " + str(len(paired_internals)) + " pair found! TBC not updated for record id = " + str(internal[0]))
        else:
            [paired_internal] = paired_internals
            logging.info("Paired: " + ',' + str(paired_internal[1]) + ',' + str(paired_internal[2]) + ',' + str(paired_internal[6]))
            dbUtils.update_TBC_by_paired_internals(db_h, internal[0], paired_internal[0])
    
def display_TBC(db_h):
    TBC_records = dbUtils.fetch_TBC(db_h)
    print("=====================================================")
    
    if len(TBC_records) == 0:
        print("No outstanding records to be categorized. Well done!")
        return
    
    for records in TBC_records:
        print(records[1:3],records[6:8])
       
#===============================================================================
# def fetch_records_as_panda(db_h):
#     filters = ' AND '.join([f for f in configs.report_filters])
#     query = """SELECT SUBSTR(date,1,7) as date, amount, type, cate, sub_cate, desc
#            FROM record
#            WHERE """ + filters
#            
#     columns, all_records =  dbUtils.retrieve_all_records(db_h, query)
#     records = pd.DataFrame(all_records)
#     records.columns = columns
#     
#     return records
#===============================================================================


#===============================================================================
# def plot_table_by(records, date = None, cate = None, sub_cate = None, date_range = None):
#     
#     pv_filters = []
#     if cate:
#         pv_cols = 'sub_cate'
#         pv_filters.append("(records.cate == '" + cate + "')")  
#     else:
#         pv_cols = 'cate'
#     
#     
#     if date_range:
#         (start, end) = date_range
#         if start and end:
#             pv_filters.append("(records.date >= '" + start + "')")
#             pv_filters.append("(records.date <= '" + end + "')")
#         elif start:
#             pv_filters.append("(records.date >= '" + start + "')")
#         else:
#             pv_filters.append("(records.date <= '" + end + "')")
#     
#     if len(pv_filters) == 0:
#         pv_table = records.pivot_table('amount', rows = 'date', cols = pv_cols, aggfunc = 'sum').fillna(-0.0) * -1
#     else:
#         pv_table = records[eval(' & '.join(pv_filters))].pivot_table('amount', rows = 'date', cols = pv_cols, aggfunc = 'sum').fillna(-0.0) * -1
#     
#     reportUtils.plot_table_chart(pv_table)
#===============================================================================
