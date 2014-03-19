'''
Created on 16/03/2014

@author: edwin
'''

from system import fileUtils, mainUtils
    
def main():
    # Initialize
    mainUtils.init_log()
    db_handler = mainUtils.init_db()
    
    # Check for new mappings and add
    mainUtils.refresh_mapping(db_handler)

    # Search for new expense files and import
    mainUtils.refresh_records(db_handler)

    # Try to fill out the TBC columns 
    mainUtils.fill_out_TBC(db_handler)
    
    # Display unhandled records
    mainUtils.display_TBC(db_handler)
    

if __name__ == '__main__':
    main()
    
    