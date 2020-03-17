import requests 
from getpass import getpass



# # Making a PATCH request 
t= requests.patch('https://httpbin.org/patch', data ={'Name':'Prasad','Company':'Datalysys'}) 

#Making a GET Request
r= requests.get('https://api.github.com/user', auth=('prasadnaddy',getpass()))          #After typing the password we get the JSON values

#Making a POST Request
s = requests.post('https://httpbin.org/post',data={'Name':'Naddy','Company':'Datalysys','Phone':'8722357140'})

print (r.text)
print (r.status_code)
print (r.url)
print("\n\n")

print(s.text)
print(s.status_code)
print("\n\n")
print(t.text)
print(t.status_code)