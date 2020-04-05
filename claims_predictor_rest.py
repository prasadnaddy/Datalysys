import requests
import json

with open("Request_Json_File.json", "r", encoding="utf-8") as readJsonfile:         #Opening the Written Request and Response File for Insertions
        requestJson=json.load(readJsonfile)

#Login Details
data2={
    "client_id": "CG4HmDLlVfoXZmH8SrB70P8EG5C8bL38",
    "client_secret": "8iLetYBRyJbRAb6j",
    "grant_type": "client_credentials"
}

#Function to generate the token
def token_generator():
    try:
        t=requests.post('https://apis.changehealthcare.com/apip/auth/v2/token',json=data2,verify=False)

        # print(t.text)
        response=json.loads(t.text)
       
        token = response['access_token']
        # print(token)
        print("\nToken has been generated successfully\n\n")
        return token

    except:
        print("Please enter the correct data format")

token = token_generator()

#Header for POST Request
headers = {
    "Authorization": "Bearer "+token,
    "Content-Type":"application/json",
}


#Function to perform POST operation for the provided endpoint
def post_request():
    try:
        s= requests.post('https://apis.changehealthcare.com/ai/claims-lifecycle/medical-network/v2/prediction',headers=headers, json=requestJson,verify=False)

        response = json.loads(s.text)
        # print(response)

        
        with open("Response_Json_File.json", "w", encoding="utf-8") as writeJsonfile:
            json.dump(response, writeJsonfile, indent=4)
        

    except:
        print("Check the data format and try again")

post_request()









