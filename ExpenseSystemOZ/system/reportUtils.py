'''
Created on 20/03/2014

@author: edwin
'''

import matplotlib.pyplot as plt
import numpy as np
from system import configs
from system import dbUtils
from math import ceil

def plot_stackplot_sample():
    fnx = lambda : np.random.randint(5, 50, 10)
    y = np.row_stack((fnx(), fnx(), fnx()))
    x = np.arange(10)
    
    y1, y2, y3 = fnx(), fnx(), fnx()
    
    fig, ax = plt.subplots()
    ax.stackplot(x, y)
    plt.show()
    
    fig, ax = plt.subplots()
    ax.stackplot(x, y1, y2, y3)
    plt.show()

def plot_table_chart_sample():
    data = [[  66386,  174296,   75131,  577908,   32015],
            [  58230,  381139,   78045,   99308,  160454],
            [  89135,   80552,  152558,  497981,  603535],
            [  78415,   81858,  150656,  193263,   69638],
            [ 139361,  331509,  343164,  781380,   52269]]
    
    columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
    rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
    
    values = np.arange(0, 2500, 500)
    value_increment = 1000
    
    # Get some pastel shades for the colors
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(columns)))
    n_rows = len(data)
    
    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4
    
    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.array([0.0] * len(columns))
    
    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        cell_text.append(['%1.1f' % (x/1000.0) for x in y_offset])
    # Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
    cell_text.reverse()
    
    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                          rowLabels=rows,
                          rowColours=colors,
                          colLabels=columns,
                          loc='bottom')
    
    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)
    
    plt.ylabel("Loss in ${0}'s".format(value_increment))
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.title('Loss by Disaster')
    
    plt.show()

def plot_bar_chart_sample():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    menStd =   (2, 3, 4, 1, 2)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)
    
    womenMeans = (25, 32, 34, 20, 25)
    womenStd =   (3, 5, 2, 3, 3)
    rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)
    
    # add some
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
    
    ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
    
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    plt.show()

def plot_pie_chart_sample():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()
    
    
def plot_pie_chart(db_h, date = None, cate = None, sub_cate = None, date_range = None):
    
    # Default filters
    filters = configs.report_filters
    
    if cate:
        group_by = 'sub_cate'
        filters.append("cate = '" + cate + "'")
        title = 'Expense in Category: ' + cate
    else:
        group_by = 'cate'
        title = 'Expense for all Category'
    
    where_clause = ' AND '.join(filters)
    
    if date_range:
        (start, end) = date_range
        if start and end:
            where_clause += " AND date >= '" + start + "' and date <= '" + end + "'"
            title += '\n between ' + start + ' and ' + end
        elif start:
            where_clause += " AND date >= '" + start + "'"
            title += '\n since ' + start
        else:
            where_clause += " AND date <= '" + end + "'"
            title += '\n up till ' + end
    
    where_clause += ' GROUP BY ' + group_by
    
    result = dbUtils.retrieve_for_pie_chart(db_h, where_clause, group_by)
    labels = [lable for (lable, value) in result]
    values = [value * -1 for (lable, value) in result]
     
    #colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    #explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
    
    #plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    #        autopct='%1.1f%%', shadow=True, startangle=90)
    
    plt.pie(values, labels=labels, autopct='%1.2f%%', shadow=True, startangle=90)
    
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.title(title)
    plt.show()
    

def plot_table_chart(pv_table):
    
    to_listoftuples = list(pv_table.T.itertuples())
    
    data = [r[1:] for r in to_listoftuples]
    
    columns = list(pv_table.T.columns)
    rows = [r[0] for r in to_listoftuples]
    
    column_sum = [ceil(amount) for amount in list(pv_table.T.sum())]
    
    values = np.arange(0, ceil( max([sum(d[1:]) for d in list(pv_table.itertuples())]) / 100) * 100, 200)
    
    # Get some pastel shades for the colors
    colors = plt.cm.Accent(np.linspace(0, 1, len(rows)))
    n_rows = len(data)
    
    index = np.arange(len(columns)) + 0.3
    bar_width = 0.6
    
    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.array([0.0] * len(columns))
    
    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        #y_offset = data[n_rows - row - 1]
        cell_text.append(['%1.1f' % (x) for x in data[row]])
    # Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
    cell_text.reverse()
    
    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                          rowLabels=rows[::-1],
                          rowColours=colors,
                          colLabels=[col +' ($' + str(amount) + ')' for (col,amount) in zip(columns, column_sum)],
                          loc='bottom')
    
    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.25)
    
    #plt.ylabel("In AUD $")
    plt.yticks(values, ['$%d' % val for val in values])
    plt.xticks([])
    plt.title('Expense By Month')
    
    plt.show()