import requests
from datetime import datetime

post_data = { 'query': '50' } #A dictionary of your post data

start_time = datetime.now()
for i in range(10):
    response = requests.post("http://localhost:8888/factorial", data=post_data)
    print(response.text)
print(f'Time taken - {(datetime.now() - start_time).total_seconds() * 10**3} ms')