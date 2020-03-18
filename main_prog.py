import dbo
from dbo import *
from claims_predictor_rest import *

connect_db()                #Connecting to DB
calc_logic()                #Data is extracted and posted to the JSON file 

post_request()              # JSON file is taken and it is POSTED to the API and the response is recorded back

db_operations2()            #Inserting the values into the HeaderClaims Table
