'''
Created on 16/03/2014

@author: edwin
'''

from system import configs
from system import fileUtils, mainUtils, reportUtils
    
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
    
    # Display status
    mainUtils.display_status()
    
    # Display unhandled records
    mainUtils.display_TBC(db_handler)
    
    # Display reports
    #reportUtils.plot_bar_chart_sample()
    #reportUtils.plot_table_chart_sample()
    reportUtils.plot_stackplot_sample()
    #reportUtils.plot_pie_chart(db_handler)
    #reportUtils.plot_pie_chart(db_handler, cate = configs.cates.living)
    #reportUtils.plot_pie_chart(db_handler, cate = configs.cates.living, date_range = ('2014-03-01', '2014-03-31'))

if __name__ == '__main__':
    main()
    
    