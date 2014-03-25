'''
Created on 18/03/2014

@author: edwin
'''

import logging
import mysql.connector
from mysql.connector import errorcode

class DB:
    def __init__(self, db_config):
        try:
            self.connection = mysql.connector.connect(**db_config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.critical("Incorrect User Name Or Password!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.critical("Database Does Not Exists!")
            elif err.errno == errorcode.CR_CONN_HOST_ERROR:
                logging.critical("MySQL Is Stopped or Wrong Host Name!")
            else:
                print(err)
            raise Exception('DB Connection Failed!')
    
    def wipe_data(self):
        pass
        
