'''
Created on 16/03/2014

@author: edwin
'''

from ozio_utilities import mainUtils
    
def main():
    
    # Init
    cfg_h = mainUtils.load_config('/Users/edwin/Programming/Python/ExpenseSystemOZ/ozio.cfg')
    mainUtils.init_log(cfg_h)
    db_h = mainUtils.init_db(cfg_h.db_config)

    # Search for new expense files and import
    #mainUtils.refresh_records(db_h, cfg_h)

    # Try to fill out the TBC columns 
    mainUtils.fill_out_TBC(db_h)

    # Display unhandled records
    mainUtils.display_TBC(db_h)
    
    #records = mainUtils.fetch_records_as_panda(db_h)
    #mainUtils.plot_table_by(records)
    #mainUtils.plot_table_by(records,cate = 'LIVING', date_range = ('2014-01','2014-02'))
    
    # Display reports
    #reportUtils.plot_bar_chart_sample()
    #reportUtils.plot_table_chart_sample()
    #reportUtils.plot_stackplot_sample()
    #reportUtils.plot_pie_chart(db_handler)
    #reportUtils.plot_pie_chart(db_handler, cate = configs.cates.living)
    #reportUtils.plot_pie_chart(db_handler, cate = configs.cates.living, date_range = ('2014-03-01', '2014-03-31'))

if __name__ == '__main__':
    main()
    
    