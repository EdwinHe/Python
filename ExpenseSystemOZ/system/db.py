'''
Created on 18/03/2014

@author: edwin
'''

from system import configs
import sqlite3
import logging
import os.path

class DB:
    def __init__(self, db_file):
        if not os.path.isfile(db_file):
            self.create()
        else:
            self.db_conn = sqlite3.connect(configs.db_file)
    
    def wipe_expense_data(self):
        db_curs = self.db_conn.cursor()
        db_curs.execute('TRUNCATE TABLE expense_source_file')
        db_curs.execute('TRUNCATE TABLE expense_record')
        self.db_conn.commit()
        db_curs.close()
        
        
    def create(self):
        logging.info("First time running, creating DBs...") 
        
        self.db_conn = sqlite3.connect(configs.db_file)
        db_curs = self.db_conn.cursor()
        
        # Create Table expense_source_file
        # Fields: #Source File Name#, #Import Time#
        db_curs.execute('''
            CREATE TABLE source_file (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_file_name TEXT,
            import_time TEXT 
            )
            ''')
        
        # Create table expense_record
        db_curs.execute('''
            CREATE TABLE record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            type TEXT,
            cate TEXT,
            sub_cate TEXT,
            desc TEXT,
            orig_desc TEXT,
            source_file_name TEXT,
            keywords TEXT
            )
            ''')
        
        #Create table keyword_mapping
        db_curs.execute('''
            CREATE TABLE keyword_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keywords TEXT,
            type TEXT,
            cate TEXT,
            sub_cate TEXT,
            priority REAL
            )
            ''')
        
        self.db_conn.commit()
        db_curs.close()
    
    
