import requests 
from getpass import getpass

data ={'Name':'Prasad','Company':'Datalysys'}

# # # Making a PATCH request 
# t= requests.patch('https://httpbin.org/patch', data ={'Name':'Prasad','Company':'Datalysys'}) 

#Making a GET Request
r= requests.get('https://api.github.com/users/prasadnaddy/hovercard', auth=('prasadnaddy',getpass()))          #After typing the password we get the JSON values

# #Making a POST Request
# s = requests.post('https://api.github.com/user/keys/', auth=('prasadnaddy',getpass()),data=data)

# print (r.content)
# print (r.status_code)

print(r.content)
print(r.status_code)