import requests

url = 'https://www.example.com' #this is the target url
response = requests.get(url) 
if response.status_code == 200:  ## 200 response code indicates that the request has succeed
    headers = response.headers 
    print("Response Headers:")
    for header in headers: 
        print(f"{header}: {headers[header]}") 
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
