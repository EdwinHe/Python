'''
Created on 25/03/2014

@author: edwin
'''
import unittest
from ozio_base import config


class Test(unittest.TestCase):


    def testConfig(self):
        config_handle = config.CONFIG('/Users/edwin/Programming/Python/ExpenseSystemOZ/ozio.cfg')
        for key in config_handle.db_config:
            print(key, "=", config_handle.db_config[key])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()