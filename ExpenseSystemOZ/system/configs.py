'''
Created on 18/03/2014

@author: edwin
'''

import datetime

# MISC
date_time_format = '%Y-%m-%d %H:%M:%S'
date_time_now = """datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')"""
version = 'Ver. 0.1'
update_date = 'March 2014'

# CSV Files
expense_source_loc = '/Users/edwin/Programming/Python/ExpenseSystemOZ/ExpenseSource'

# LOG Files
log_files_loc = '/Users/edwin/Programming/Python/ExpenseSystemOZ/Logs'
log_file = log_files_loc + '/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.log'
log_format = '[%(asctime)s @ %(levelname)-5s] %(message)s'

# DB
db_file = '/Users/edwin/Programming/Python/ExpenseSystemOZ/DB/ExpenseSystemOZ.db'

#TYPES
class types:
    off_balance = 'OFF_BALANCE_SHEET'
    span_1y = 'SPAN_1_YEAR'
    span_to_next = 'SPAN_TO_NEXT'
    one_off = 'ONE_OFF_EXPENSE'

#Outflow Category
class out_cates:
    living = 'LIVING'
    insurace = 'INSURANCE'
    transport = 'TRANSPORTATION'
    cash = 'CASH'
    rent = 'RENT' 
    social = 'SOCIAL'
    travel = 'TRAVEL'
    mobile = 'MOBILE'
    internal = 'INTERNAL'
    cloth = 'CLOTHING'
    tax = 'TAX'
    properties = 'PROPERTIES'

#Outflow Sub Category
class out_sub_cates:
    living_food_n_drink = 'FOOD&DRINK'
    living_misc = 'MISC'
    insurance_car = 'CAR'
    insurance_life = 'LIFE'
    transport_train = 'TRAIN'
    transport_opal = 'OPAL'
    transport_petrol = 'PETROL'
    transport_car_main = 'CAR_MAINTAIN'
    transport_car_park = 'CAR_PARK'
    transport_toll_road = 'TOLL_ROAD'
    transport_misc = 'MISC'
    cash_misc = 'MISC'
    rent_room = 'ROOM' 
    social_misc = 'MISC'
    travel_misc = 'MISC'
    mobile_misc = 'MISC'
    internal_misc = 'MISC'
    cloth_misc = 'MISC'
    tax_tfn = 'TFN_WITHHOLDING_TAX'
    properties_car = 'CAR'
    
#Inflow Cate
class in_cates:
    credit_interest = 'CREDIT_INTEREST'
    salary = 'SALARY'
    oversea_saving = 'OVERSEA_SAVING'

#Inflow Sub Cate
class in_sub_cates:
    credit_int_na = 'N/A'
    salary_na = 'N/A'
    oversea_saving_na = 'N/A'
    
    
#('IN/OUT', 'KEYWORD1%KEYWORD2%...%KEYWORDn',TYPE,CATE,SUBCATE, PRIORITY)
keyword_mappings = (#OUT
                     #Priority 4
                     ('OUT', 'RTA%ETOLL', types.one_off, out_cates.transport, out_sub_cates.transport_toll_road, 4),
                     ('OUT','TRANSFER TO%CASH OUT', types.one_off, out_cates.cash, out_sub_cates.cash_misc, 4),
                     ('OUT','TRANSFER TO%RENT FEE', types.span_to_next, out_cates.rent, out_sub_cates.rent_room, 4),
                     ('OUT','TRANSFER%XX7456', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('OUT','TRANSFER%XX4978', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('OUT','TRANSFER%XX8088', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('OUT','TRANSFER%XX8096', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('OUT','TRANSFER%XX4986', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('IN','TRANSFER%XX7456', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('IN','TRANSFER%XX4978', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('IN','TRANSFER%XX8088', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('IN','TRANSFER%XX8096', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('IN','TRANSFER%XX4986', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 4),
                     ('IN', 'WENZHEN%REF', types.off_balance, in_cates.oversea_saving, in_sub_cates.oversea_saving_na, 4),
                     ('IN', 'SHUQIN%REF', types.off_balance, in_cates.oversea_saving, in_sub_cates.oversea_saving_na, 4),
                     #Priority 5
                     ('OUT', 'COLES', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'WOOLWORTHS', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'TONG LI', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'TONGLI', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'SOUQ FRESH', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'COUNTRY GROWERS', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'TEMPUS TWO', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'MR LIQUOR', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'CELLARBRATIONS', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'SUBWAY SANDWICHES', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'LUNCH FEE', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'SEAFOOD BUYFOOD', types.one_off, out_cates.living, out_sub_cates.living_food_n_drink, 5),
                     ('OUT', 'DAVID JONES', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'BUNNINGS', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'HOME AND KITCHEN', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'HANDYWAY WORLD KITC', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'HANSANG TRADING', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'KMART', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'TARGET', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'CHEMIST', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'DAISO', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'PAYPAL', types.one_off, out_cates.living, out_sub_cates.living_misc, 5),
                     ('OUT', 'CASH OUT', types.one_off, out_cates.cash, out_sub_cates.cash_misc, 5),
                     ('OUT', 'ATM', types.one_off, out_cates.cash, out_sub_cates.cash_misc, 5),
                     ('OUT', 'HANDYWAY RAIL', types.one_off, out_cates.transport, out_sub_cates.transport_train, 5),
                     ('OUT', 'SYDNEY TRAINS', types.one_off, out_cates.transport, out_sub_cates.transport_train, 5),
                     ('OUT', 'TRANSPORT FOR NSW CHIPPENDALE', types.one_off, out_cates.transport, out_sub_cates.transport_train, 5),
                     ('OUT', 'RENT FEE', types.span_to_next, out_cates.rent, out_sub_cates.rent_room, 5),
                     ('OUT', 'SOCIAL', types.one_off, out_cates.social, out_sub_cates.social_misc, 5),
                     ('OUT', 'TRAVEL', types.one_off, out_cates.travel, out_sub_cates.travel_misc, 5),
                     ('OUT', 'VODAFONE', types.span_to_next, out_cates.mobile, out_sub_cates.mobile_misc, 5),
                     ('OUT', 'TELSTRA', types.span_to_next, out_cates.mobile, out_sub_cates.mobile_misc, 5),
                     ('OUT', 'PARKING', types.one_off, out_cates.transport, out_sub_cates.transport_car_park, 5),
                     ('OUT', 'PETROL', types.one_off, out_cates.transport, out_sub_cates.transport_petrol, 5),
                     ('OUT', 'N R M A', types.span_to_next, out_cates.insurace, out_sub_cates.insurance_car, 5),
                     ('OUT', 'NRMA', types.span_to_next, out_cates.insurace, out_sub_cates.insurance_car, 5),
                     ('OUT', 'NEW BALANCE', types.one_off, out_cates.cloth, out_sub_cates.cloth_misc, 5),
                     ('OUT', 'REBEL SPORT', types.one_off, out_cates.cloth, out_sub_cates.cloth_misc, 5),
                     ('OUT', 'MD AUBURN 132', types.one_off, out_cates.cloth, out_sub_cates.cloth_misc, 5),
                     ('OUT', 'COTTON ON', types.one_off, out_cates.cloth, out_sub_cates.cloth_misc, 5),
                     ('OUT', 'TFN WITHHOLDING TAX', types.one_off, out_cates.tax, out_sub_cates.tax_tfn, 5),
                     ('OUT', 'RTA', types.one_off, out_cates.transport, out_sub_cates.transport_misc, 5),
                     ('OUT', 'COMMUNITY RELATIONS', types.one_off, out_cates.transport, out_sub_cates.transport_misc, 5),
                     #IN
                     #('IN', 'TRANSFER FROM WENZHEN HE', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 5),
                     #('IN', 'TRANSFER FROM SHUQIN ZENG', types.off_balance, out_cates.internal, out_sub_cates.internal_misc, 5),
                     ('IN', 'CREDIT INTEREST', types.one_off, in_cates.credit_interest, in_sub_cates.credit_int_na, 5),
                     ('IN', 'CASH DEPOSIT', types.off_balance, in_cates.oversea_saving, in_sub_cates.oversea_saving_na, 5),
                     
                     # ONE OFF - NOT RECURRING 
                     ('OUT', 'WDL BRANCH 116 BURWOOD RD', types.one_off, out_cates.properties, out_sub_cates.properties_car, 10),
                     ('OUT', 'ROCKDALE MAZDA ARNCLIFFE NS AUS CARD XX1940', types.one_off, out_cates.properties, out_sub_cates.properties_car, 10),
                     )
