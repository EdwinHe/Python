'''
Created on 18/03/2014

@author: edwin
'''

# import datetime

# # MISC
# date_time_format = '%Y-%m-%d %H:%M:%S'
# date_time_now = """datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')"""
# version = 'Ver. 0.1'
# update_date = 'March 2014'
# 
# # CSV Files
# expense_source_loc = '/Users/edwin/Programming/Python/ExpenseSystemOZ/ExpenseSource'
# 
# # LOG Files
# log_files_loc = '/Users/edwin/Programming/Python/ExpenseSystemOZ/Logs'
# log_file = log_files_loc + '/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.log'
# log_format = '[%(asctime)s @ %(levelname)-5s] %(message)s'

# DB
# db_file = '/Users/edwin/Programming/Python/ExpenseSystemOZ/DB/ExpenseSystemOZ.db'

# Reports
# report_filters = ["type <> 'OFF_BALANCE_SHEET'", 
#            "cate <> 'INTERNAL'", 
#            "cate <> 'CREDIT_INTEREST'", 
#            "cate <> 'PROPERTIES'",
#            "cate <> 'CASH'"]

#TYPES
# class types:
#     off_balance = 'OFF_BALANCE_SHEET'
#     span_1y = 'SPAN_1_YEAR'
#     span_to_next = 'SPAN_TO_NEXT'
#     one_off = 'ONE_OFF_EXPENSE'

#Outflow Category
# class cates:
#     living = 'LIVING'
#     insurace = 'INSURANCE'
#     transport = 'TRANSPORT'
#     cash = 'CASH'
#     rent = 'RENT' 
#     social = 'SOCIAL'
#     travel = 'TRAVEL'
#     mobile = 'MOBILE'
#     internal = 'INTERNAL'
#     cloth = 'CLOTHING'
#     tax = 'TAX'
#     properties = 'PROPERTIES'
#     credit_interest = 'CREDIT_INTEREST'
#     salary = 'SALARY'
#     oversea_saving = 'OVERSEA_SAVING'

#Outflow Sub Category
# class sub_cates:
#     living_food_n_drink = 'FOOD&DRINK'
#     living_must = 'MUST_DO'
#     living_misc = 'MISC'
#     insurance_car = 'CAR'
#     insurance_life = 'LIFE'
#     transport_train = 'TRAIN'
#     transport_opal = 'OPAL'
#     transport_petrol = 'PETROL'
#     transport_car_main = 'CAR_MAINTAIN'
#     transport_car_park = 'CAR_PARK'
#     transport_toll_road = 'TOLL_ROAD'
#     transport_misc = 'MISC'
#     cash_misc = 'MISC'
#     cash_depo = 'CASH_DEPOSITE'
#     rent_room = 'ROOM' 
#     social_misc = 'MISC'
#     travel_misc = 'MISC'
#     mobile_misc = 'MISC'
#     internal_misc = 'MISC'
#     cloth_misc = 'MISC'
#     tax_tfn = 'TFN_WITHHOLDING_TAX'
#     properties_car = 'CAR'
#     credit_int_na = 'N/A'
#     salary_na = 'N/A'
#     oversea_saving_na = 'N/A'
    
    
    
#('IN/OUT', 'KEYWORD1%KEYWORD2%...%KEYWORDn',TYPE,CATE,SUBCATE, PRIORITY)
# keyword_mappings = (#OUT
                     #Priority 4
#                      ('RTA%ETOLL', types.one_off, cates.transport, sub_cates.transport_toll_road, 4),
#                      ('TRANSFER TO%CASH OUT', types.one_off, cates.cash, sub_cates.cash_misc, 4),
#                      ('TRANSFER TO%RENT FEE', types.span_to_next, cates.rent, sub_cates.rent_room, 4),
#                      ('TRANSFER%XX7456', types.off_balance, cates.internal, sub_cates.internal_misc, 4),
#                      ('TRANSFER%XX4978', types.off_balance, cates.internal, sub_cates.internal_misc, 4),
#                      ('TRANSFER%XX8088', types.off_balance, cates.internal, sub_cates.internal_misc, 4),
#                      ('TRANSFER%XX8096', types.off_balance, cates.internal, sub_cates.internal_misc, 4),
#                      ('TRANSFER%XX4986', types.off_balance, cates.internal, sub_cates.internal_misc, 4),
#                      ('WENZHEN%REF', types.off_balance, cates.oversea_saving, sub_cates.oversea_saving_na, 4),
#                      ('SHUQIN%REF', types.off_balance, cates.oversea_saving, sub_cates.oversea_saving_na, 4),
#                      ('CALTEX', types.one_off, cates.transport, sub_cates.transport_petrol, 4),
#                      
#                      #Priority 5
#                      ('COLES', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('WOOLWORTHS', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('TONG LI', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('TONGLI', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('SOUQ FRESH', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('COUNTRY GROWERS', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('TEMPUS TWO', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('MR LIQUOR', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('CELLARBRATIONS', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('SUBWAY SANDWICHES', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('COFFEE', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('LUNCH FEE', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('SEAFOOD BUYFOOD', types.one_off, cates.living, sub_cates.living_food_n_drink, 5),
#                      ('DAVID JONES', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('DICK SMITH', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('BUNNINGS', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('HOME AND KITCHEN', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('HANDYWAY WORLD KITC', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('HANSANG TRADING', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('KMART', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('TARGET', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('CHEMIST', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('DAISO', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('PAYPAL', types.one_off, cates.living, sub_cates.living_misc, 5),
#                      ('CASH OUT', types.one_off, cates.cash, sub_cates.cash_misc, 5),
#                      ('ATM', types.one_off, cates.cash, sub_cates.cash_misc, 5),
#                      ('HANDYWAY RAIL', types.one_off, cates.transport, sub_cates.transport_train, 5),
#                      ('SYDNEY TRAINS', types.one_off, cates.transport, sub_cates.transport_train, 5),
#                      ('TRANSPORT FOR NSW CHIPPENDALE', types.one_off, cates.transport, sub_cates.transport_train, 5),
#                      ('RENT FEE', types.span_to_next, cates.rent, sub_cates.rent_room, 5),
#                      ('SOCIAL', types.one_off, cates.social, sub_cates.social_misc, 5),
#                      ('TRAVEL', types.one_off, cates.travel, sub_cates.travel_misc, 5),
#                      ('VODAFONE', types.span_to_next, cates.mobile, sub_cates.mobile_misc, 5),
#                      ('TELSTRA', types.span_to_next, cates.mobile, sub_cates.mobile_misc, 5),
#                      ('PARKING', types.one_off, cates.transport, sub_cates.transport_car_park, 5),
#                      ('PETROL', types.one_off, cates.transport, sub_cates.transport_petrol, 5),
#                      ('N R M A', types.span_to_next, cates.insurace, sub_cates.insurance_car, 5),
#                      ('NRMA', types.span_to_next, cates.insurace, sub_cates.insurance_car, 5),
#                      ('NEW BALANCE', types.one_off, cates.cloth, sub_cates.cloth_misc, 5),
#                      ('REBEL SPORT', types.one_off, cates.cloth, sub_cates.cloth_misc, 5),
#                      ('MD AUBURN 132', types.one_off, cates.cloth, sub_cates.cloth_misc, 5),
#                      ('COTTON ON', types.one_off, cates.cloth, sub_cates.cloth_misc, 5),
#                      ('TFN WITHHOLDING TAX', types.one_off, cates.tax, sub_cates.tax_tfn, 5),
#                      ('DRIVING LESSON', types.one_off, cates.living, sub_cates.living_must, 5),
#                      ('RTA', types.one_off, cates.living, sub_cates.living_must, 5),
#                      ('COMMUNITY RELATIONS', types.one_off, cates.living, sub_cates.living_must, 5),
#                      ('CREDIT INTEREST', types.one_off, cates.credit_interest, sub_cates.credit_int_na, 5), 
#                      ('CASH DEPOSIT', types.one_off, cates.cash, sub_cates.cash_depo, 5),     
#                      # VERY GENERAL
#                      ('GENERAL TRANSPORT', types.one_off, cates.transport, sub_cates.transport_misc, 8),
#                      ('GENERAL FOOD', types.one_off, cates.living, sub_cates.living_food_n_drink, 8),
#                      ('GENERAL CASH', types.one_off, cates.cash, sub_cates.cash_misc, 8),
#                      # ONE OFF - NOT RECURRING 
#                      ('WDL BRANCH 116 BURWOOD RD', types.one_off, cates.properties, sub_cates.properties_car, 10),
#                      ('ROCKDALE MAZDA ARNCLIFFE NS AUS CARD XX1940', types.one_off, cates.properties, sub_cates.properties_car, 10),
#                      )
