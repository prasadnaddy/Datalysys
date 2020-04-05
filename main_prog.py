from dbo import *
from claims_predictor_rest import *

connect_db()                #Connecting to DB

calc_logic()                #Data is extracted and posted to the JSON file 

db_operations2()            #Inserting the values into the HeaderClaims Table

dboperations3()             #Inserting the values into the LineClaims Table

