# rest_client.py
import requests

def run():
    r = requests.post('http://localhost:5000/add', json={'a': 123, 'b': 456})
    print("JSON Add result:", r.json()['result'])

if __name__ == '__main__':
    run()
