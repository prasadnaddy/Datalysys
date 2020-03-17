import requests

r = requests.get("https://httpbin.org/cookies",verify=True)          #Posting the data to the github website.
print(r.url)                                        #Getting the URL redirection Status code.
print(r.history)
print(r.status_code)                                #Getting the HTTP Response
print(r.content)