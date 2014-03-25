'''
Created on 18/03/2014

@author: edwin
'''

#from ozio_utilities import configs_notinuse as configs
from ozio_utilities import dbUtils
import logging
import os.path
import re

def parse_record(line):    
    #logging.debug('+++++++++++++++++++++++++++++++++++++++++')
    logging.info('Processing: ' + line)
    
    line = re.sub('"', '', line)
    [date, amount, orig_desc, balance] = line.split(',')
    balance = balance.replace('\n','')
    
    # Removing extra spaces and double quotes
    desc = re.sub(" +", " ", orig_desc).upper()
    orig_desc = orig_desc + ' Balance:' + balance
    
    # ======= Possible date manipulation put in here =======
    # If Value Date found, the transaction happened at Value Date
    # Then Set date to Value Date
    pos = desc.find('VALUE DATE:')
    if pos != -1:
        # Value Date means credit account was used, and Cash Out should be allowed from saving account only 
        assert desc.find('CASH OUT') == -1 
        date = desc[pos+12:pos+22]
        desc = desc[:pos] + desc[pos+22:]
    
    # ======= No date manipulation Onwards =======
    # Change Date format from dd/mm/yyyy to yyyy-mm-dd
    date = date[6:10] + '-' + date[3:5] + '-' + date[0:2]
    
    transactions = []
    # If Cash Out found, the transaction needed to be break into two transactions
    pos_cashout = desc.find('CASH OUT')
    pos_purchase = desc.find('PURCHASE')
    
    if pos_cashout != -1 and pos_purchase != -1:
        cash_out_amount = '-' + desc[pos_cashout+10:pos_purchase-1]
        cash_out_desc = 'CASH OUT'
        
        purchase_amount = '-' + desc[pos_purchase+10:]
        purchase_desc = desc[:pos_cashout]
        
        transactions.append([date, cash_out_amount, cash_out_desc, orig_desc+':Split'])
        transactions.append([date, purchase_amount, purchase_desc, orig_desc])
    else:
        transactions.append([date, amount, desc, orig_desc])
    
    return transactions
    

def import_file(db_h, root, file_name):
    logging.info('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    logging.info('Start processing file: ' + file_name)
    
    for line in open(root + '/' + file_name, 'r'):
        for record in parse_record(line):
            if dbUtils.is_new_record(db_h, record + [file_name]):
                dbUtils.insert_record(db_h, record + [file_name])
            
    dbUtils.insert_file(db_h, file_name)
    logging.info('Finished processing file: ' + file_name)
    
    

def search_file(db_h, cfg_h):
    assert os.path.exists(cfg_h.file_config['expense_source_loc'])
    logging.info("Searching for new expense source file...")
        
    file_list = []
    for root, _, files in os.walk(cfg_h.file_config['expense_source_loc']):
        for file_name in files:
            if file_name.find('.csv') == -1:
                continue
            
            logging.debug("Looping to file: " + file_name)
            
            if dbUtils.is_new_file(db_h, root, file_name):
                logging.debug("New file found, preparing for import: " + file_name)
                file_list.append((root, file_name))
            else:
                logging.debug(file_name + " has been imported. Skipped.")
    
    return file_list
                
        