'''
Created on 25/03/2014

@author: edwin
'''

import configparser

class CONFIG(object):
    '''
    Class to store configs 
    '''


    def __init__(self, config_file):
        '''
        Constructor
        '''
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        
        self.db_config = dict(self.config['DB_CONFIG'])
        self.db_config['raise_on_warnings'] = self.config.getboolean('DB_CONFIG','raise_on_warnings')
        
        self.misc_config = dict(self.config['MISC_CONFIG'])
        self.file_config = dict(self.config['FILE_CONFIG'])
        self.log_config = dict(self.config['LOG_CONFIG'])
        
    
        
        
        