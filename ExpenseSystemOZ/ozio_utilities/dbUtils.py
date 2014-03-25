'''
Created on 18/03/2014

@author: edwin
'''

import os.path
import logging
import datetime
#from ozio_utilities import configs_notinuse as configs
            
def insert_mapping(db_h, mapping):
    db_curs = db_h.db_conn.cursor()
    #Id, keywords, type, cate, subcate, priority
    query = """
        INSERT INTO keyword_mapping 
        VALUES (NULL, ?, ?, ?, ?, ?)"""
    
    logging.debug("Execute Query: " + query + "\n@" + str(mapping)) 
    
    db_curs.execute(query, mapping)
    db_h.db_conn.commit()
    db_curs.close()

def is_new_mapping(db_h, keywords):
    
    #try:
    db_curs = db_h.db_conn.cursor()
    db_curs.execute("""
        SELECT * 
        FROM keyword_mapping 
        WHERE keywords = '""" + keywords + "'")
    db_h.db_conn.commit()
    result = db_curs.fetchall()
    db_curs.close()
    #except:
    #    logging.error("Exception Raised when trying to check table: source_file")
    #    return True #Skip the file
    
    return True if len(result) == 0 else False    



def is_new_file(db_h, root, file_name):
    assert(os.path.isfile(root + '/' + file_name))
    
    result = []
    try:
        db_cursor = db_h.connection.cursor()
        query = """
                 SELECT * 
                 FROM source_file 
                 WHERE file_name = '%s'""" % file_name
        db_cursor.execute(query)
        result = db_cursor.fetchall()
        
        db_h.connection.commit()
        
        db_cursor.close()
    except Exception as e:
        print(e)
        print("ERROR!!!!")
        
    return True if len(result) == 0 else False


def insert_file(db_h, file_name):
    db_cursor = db_h.connection.cursor()
    query = """
        INSERT INTO source_file (`file_name`, `import_time`) 
        VALUES ('%s',%s)""" % (file_name, 'now()' )
    
    logging.debug("Execute Query: " + query)
    
    db_cursor.execute(query)  
    db_h.connection.commit()
    file_id = db_cursor.getlastrowid()
    db_cursor.close()

    return file_id

def is_new_record(db_h, exp_record):
    [date, amount, desc, orig_desc, file_id] = exp_record
    
    try:
        # If record with the same date, amount and orig_desc exist, consider it the same records
        # Skip!
        db_cursor = db_h.connection.cursor()
        # id, date, amount, type, cate, subcate, desc, orig_desc, source_file_name
        query = """
            SELECT * FROM record
            WHERE date = '%s' and amount = '%s' and orig_desc = '%s'""" % (date, amount, orig_desc)
        
        logging.debug("Execute Query: " + query) 
            
        db_cursor.execute(query)
        result = db_cursor.fetchall()
        db_h.connection.commit()
        db_cursor.close()
        
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
        db_cursor = db_h.connection.cursor()
        query = """
            INSERT INTO record (`date`, `amount`, `desc`, `orig_desc`, `source_file_id`)
            VALUES ('%s', %s, '%s', '%s', %s)""" % tuple(exp_record)
        
        logging.debug("Execute Query: " + query) 
        
        db_cursor.execute(query)
        db_h.connection.commit()
        db_cursor.close()
    except Exception as e:
        print(e)
        print("DB ERROR!!!")
        #logging.error("Exception Raised when inserting record to table: record")
    
    
def fetch_mappings(db_h):
    db_curs = db_h.db_conn.cursor()
    query = """
        SELECT * FROM keyword_mapping 
        ORDER BY priority"""
    
    logging.debug("Execute Query: " + query)
    
    db_curs.execute(query)
    db_h.db_conn.commit()
    
    result = db_curs.fetchall()
    db_curs.close()
    
    return result

def fetch_TBC(db_h):
    db_curs = db_h.db_conn.cursor()
    query = """
        SELECT * FROM record 
        WHERE keywords = 'TBC'"""
    
    logging.debug("Execute Query: " + query)
    
    db_curs.execute(query)
    db_h.db_conn.commit()
    
    result = db_curs.fetchall()
    db_curs.close()
    
    return result


#===============================================================================
# def fetch_unpaired_internals(db_h):
#     db_curs = db_h.db_conn.cursor()
#     query = """
#         SELECT * FROM record 
#         WHERE keywords = 'TBC' and desc like '%TRANSFER FROM SHUQIN%' or desc like '%TRANSFER FROM WENZHEN%'"""
#     
#     logging.debug("Execute Query: " + query)
#     
#     db_curs.execute(query)
#     db_h.db_conn.commit()
#     
#     result = db_curs.fetchall()
#     db_curs.close()
#     
#     return result
#===============================================================================


#===============================================================================
# def pair_internal(db_h, amount, pattern):
#     db_curs = db_h.db_conn.cursor()
#     query = """
#         SELECT * FROM record 
#         WHERE amount = '""" + amount + "' and desc = '" + pattern + "'"
#     
#     logging.debug("Execute Query: " + query)
#     
#     db_curs.execute(query)
#     db_h.db_conn.commit()
#     
#     result = db_curs.fetchall()
#     db_curs.close()
#     
#     return result
#===============================================================================


def update_TBC_by_mapping(db_h, mapping):
    [id, keywords, type, cate, sub_cate, priority]  = mapping
    
    db_curs = db_h.db_conn.cursor()
    
    query = """
        UPDATE record
        SET type = '""" + type + "', cate = '" + cate + "', sub_cate = '" + sub_cate + "', keywords = '" + keywords + """'
        WHERE desc like '%""" + keywords + "%' and keywords = 'TBC'" 
    
    logging.debug("Execute Query: " + query)
    
    db_curs.execute(query)
    db_h.db_conn.commit()
    db_curs.close()
    
    
#===============================================================================
# def update_TBC_by_paired_internals(db_h, id1, id2):
#     
#     db_curs = db_h.db_conn.cursor()
#     type = '1'
#     cate = '4'
#     sub_cate = '1'
#     keywords = '2'
#     
#     query = """
#         UPDATE record
#         SET type = '""" + type + "', cate = '" + cate + "', sub_cate = '" + sub_cate + "', keywords = '" + keywords + """' 
#         WHERE id = """ + str(id1) + " or id = " + str(id2)
#     
#     logging.debug("Execute Query: " + query)
#     
#     db_curs.execute(query)
#     db_h.db_conn.commit()
#     db_curs.close()
#===============================================================================
    
def retrieve_all_records(db_h, query):
    db_curs = db_h.db_conn.cursor()
    
    logging.debug("Execute Query: " + query)
    
    db_curs.execute(query)
    result = db_curs.fetchall()
    columns = [i[0] for i in db_curs.description]
    db_h.db_conn.commit()
    db_curs.close()
    
    return columns,result

def retrieve_for_pie_chart(db_h, where_clause, group_by):
    db_curs = db_h.db_conn.cursor()
    
    query = """
        SELECT """ + group_by + """, sum(amount) 
        FROM record 
        WHERE """ + where_clause
    
    logging.debug("Execute Query: " + query)
    
    db_curs.execute(query)
    result = db_curs.fetchall()
    db_h.db_conn.commit()
    db_curs.close()
    
    return result

    