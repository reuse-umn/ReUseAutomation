import requests
import os
from base64 import b64encode
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def main():
    post_json = {
        "HDDSerialNumber": "N/A",
        "SerialNumber": "HV751M2",
        "Substate": "5207",
        "X500": f"---\n {datetime.now()}\nReceived by ReUse.\nOperator: russe823\n---"
    }
    post_headers = {
        "x-api-key" : os.getenv('TEST_KEY'),
        "Authorization" : basic_auth(os.getenv('TEST_USER'), os.getenv('TEST_PASS'))
    }
    response = requests.post(url=os.getenv('TEST_UPDATE_ENDPOINT'), json=post_json, headers=post_headers)
    print(response.text)
    return


def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'


if __name__ == "__main__":
    main()