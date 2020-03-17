import requests
import json, pprint

#Our POST JSON Data
data = {
    
    "labId": 1003,
    "locationId": 100,
    "locationName": "Refrizirator-2",
    "minTemperature": 12,
    "maxTemperature": 32,
    "tempUnitId": 10,
    "tempUnitTypeName": "Celsius",
    "minHumidity": 35,
    "maxHumidity": 80,
    "humUnitId": 20,
    "humUnitTypeName": "g/m3",
}

#Login Details
data2={
    "userName": "suneel@demolab.com",
    "password": "Temp@123"
}

global token

#Function to generate the token
def token_generator():
    try:
        t=requests.post('https://deviceinsights.io/api/v2/default/login/auth',json=data2,verify=False)

        # print(t.text)
        response=json.loads(t.text)
       
        token=response['data']['access_token']
        # print(response)
        print("Token has been generated successfully\n\n")
        return token

    except:
        print("Please enter the correct data format")

token = token_generator()

#Header for POST Request
headers = {
    "Authorization": "Bearer "+token,
    "Content-Type":"application/json",
}

#Function to Perform the GET Request for the provided endpoint
def get_request():
    try:
        r= requests.get('https://deviceinsights.io/api/v2/QualityControl/settings/instruments/?searchText=&labId=1003', headers=headers, verify=False)

        print ("The response code is : %s"%(r.status_code))
        pprint.pprint(r.text)
        print("\n\n")

    except:
        print("Please check the Data Format and try again")


#Function to perform POST operation for the provided endpoint
def post_request():
    try:
        s= requests.post('https://deviceinsights.io/api/v2/SmartLab/settings/smartLabLocation/update',headers=headers, json=data,verify=False)

        print(s.text)
        print("Data has been posted successfully")

    except:
        print("Check the data format and try again")


get_request()
post_request()









