import requests

url = 'https://www.example.com' 
response = requests.get(url) 
if response.status_code == 200:  
    headers = response.headers 
    print("Response Headers:")
    for header in headers: 
        print(f"{header}: {headers[header]}") 
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
