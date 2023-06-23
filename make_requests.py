import requests
from datetime import datetime

data = {'query': '10000000'}

start_time = datetime.now()

response = requests.get("http://localhost:8888/pi", data=data)
print(response.text)
print(f'Time taken - {(datetime.now() - start_time).total_seconds() * 10**3} ms')