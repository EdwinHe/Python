'''
Created on 18/03/2014

@author: edwin
'''

import os.path
import logging
import datetime
#from ozio_utilities import configs_notinuse as configs
            
def insert_mapping(db_h, mapping):
    db_cursor = db_h.connection.cursor()
    #Id, keywords, type, cate, subcate, priority
    query = """
        INSERT INTO keyword_mapping 
        VALUES (NULL, ?, ?, ?, ?, ?)"""
    
    logging.debug("Execute Query: " + query + "\n@" + str(mapping)) 
    
    db_cursor.execute(query, mapping)
    db_h.connection.commit()
    db_cursor.close()

def is_new_mapping(db_h, keywords):
    
    #try:
    db_cursor = db_h.connection.cursor()
    db_cursor.execute("""
        SELECT * 
        FROM keyword_mapping 
        WHERE keywords = '""" + keywords + "'")
    db_h.connection.commit()
    result = db_cursor.fetchall()
    db_cursor.close()
    #except:
    #    logging.error("Exception Raised when trying to check table: source_file")
    #    return True #Skip the file
    
    return True if len(result) == 0 else False    



def is_new_file(db_h, root, file_name):
    assert(os.path.isfile(root + '/' + file_name))
    
    result = []
    try:
        db_cursoror = db_h.connection.cursor()
        query = """
                 SELECT * 
                 FROM source_file 
                 WHERE file_name = '%s'""" % file_name
        db_cursoror.execute(query)
        result = db_cursoror.fetchall()
        
        db_h.connection.commit()
        
        db_cursoror.close()
    except Exception as e:
        print(e)
        print("ERROR!!!!")
        
    return True if len(result) == 0 else False


def insert_file(db_h, file_name):
    db_cursoror = db_h.connection.cursor()
    query = """
        INSERT INTO source_file (`file_name`, `import_time`) 
        VALUES ('%s',%s)""" % (file_name, 'now()' )
    
    logging.debug("Execute Query: " + query)
    
    db_cursoror.execute(query)  
    db_h.connection.commit()
    file_id = db_cursoror.getlastrowid()
    db_cursoror.close()

    return file_id

def is_new_record(db_h, exp_record):
    [date, amount, desc, orig_desc, file_id] = exp_record
    
    try:
        # If record with the same date, amount and orig_desc exist, consider it the same records
        # Skip!
        db_cursoror = db_h.connection.cursor()
        # id, date, amount, type, cate, subcate, desc, orig_desc, source_file_name
        query = """
            SELECT * FROM record
            WHERE date = '%s' and amount = '%s' and orig_desc = '%s'""" % (date, amount, orig_desc)
        
        logging.debug("Execute Query: " + query) 
            
        db_cursoror.execute(query)
        result = db_cursoror.fetchall()
        db_h.connection.commit()
        db_cursoror.close()
        
        if len(result) == 0:
            logging.debug('Record is new.')
            return True
        else:
            logging.debug('Record (['+date+'],['+amount+'],[' + orig_desc + ']) exist. Passed!')
            return False
    except Exception as e:
        print(e)
        print("DB ERROR!!!")
        return False

def insert_record(db_h, exp_record):
    #[date, amount, desc, orig_desc, file_id] = exp_record
    try:
        db_cursoror = db_h.connection.cursor()
        query = """
            INSERT INTO record (`date`, `amount`, `desc`, `orig_desc`, `source_file_id`)
            VALUES ('%s', %s, '%s', '%s', %s)""" % tuple(exp_record)
        
        logging.debug("Execute Query: " + query) 
        
        db_cursoror.execute(query)
        db_h.connection.commit()
        db_cursoror.close()
    except Exception as e:
        print(e)
        print("DB ERROR!!!")
        #logging.error("Exception Raised when inserting record to table: record")
    
    
def fetch_mappings(db_h):
    db_cursor = db_h.connection.cursor()
    query = """
        SELECT * FROM keyword_mapping 
        ORDER BY priority"""
    
    logging.debug("Execute Query: " + query)
    
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db_h.connection.commit()
    db_cursor.close()
    
    return result

def fetch_TBC(db_h):
    db_cursor = db_h.connection.cursor()
    query = """
        SELECT * FROM record 
        WHERE keyword_id is null"""
    
    logging.debug("Execute Query: " + query)
    
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db_h.connection.commit()
    db_cursor.close()
    
    return result


def fetch_unpaired_internals(db_h):
    db_cursor = db_h.connection.cursor()
    query = """
        SELECT * FROM record 
        WHERE keyword_id is null AND 
        ( `desc` like '%TRANSFER FROM SHUQIN%' or `desc` like '%TRANSFER FROM WENZHEN%' )"""
     
    logging.debug("Execute Query: " + query)
     
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db_h.connection.commit() 
    db_cursor.close()
     
    return result


def pair_internal(db_h, amount, pattern):
    db_cursor = db_h.connection.cursor()
    query = """
        SELECT * FROM record 
        WHERE amount = %s and `desc` = '%s'""" % (amount, pattern)
     
    logging.debug("Execute Query: " + query)
     
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db_h.connection.commit()
    db_cursor.close()
     
    return result


def update_TBC_by_mapping(db_h, mapping):
    [id, keywords, type_id, cate_id, sub_cate_id, priority, mapping_desc]  = mapping
    
    db_cursor = db_h.connection.cursor()
    
    query = """
        UPDATE record SET `keyword_id` = '%s'
        WHERE `desc` like '%%%s%%' and keyword_id is null """  % (id, keywords)
    
    logging.debug("Execute Query: " + query)
    
    db_cursor.execute(query)
    db_h.connection.commit()
    db_cursor.close()
    
    
def update_TBC_by_paired_internals(db_h, id1, id2):
     
    db_cursor = db_h.connection.cursor()
    keyword_id = 2
     
    query = """
        UPDATE record
        SET keyword_id = %s 
        WHERE id = %s or id = %s""" % (keyword_id, id1, id2)
     
    logging.debug("Execute Query: " + query)
     
    db_cursor.execute(query)
    db_h.connection.commit()
    db_cursor.close()
    
def retrieve_all_records(db_h, query):
    db_cursor = db_h.connection.cursor()
    
    logging.debug("Execute Query: " + query)
    
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    columns = [i[0] for i in db_cursor.description]
    db_h.connection.commit()
    db_cursor.close()
    
    return columns,result

def retrieve_for_pie_chart(db_h, where_clause, group_by):
    db_cursor = db_h.connection.cursor()
    
    query = """
        SELECT """ + group_by + """, sum(amount) 
        FROM record 
        WHERE """ + where_clause
    
    logging.debug("Execute Query: " + query)
    
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db_h.connection.commit()
    db_cursor.close()
    
    return result

    