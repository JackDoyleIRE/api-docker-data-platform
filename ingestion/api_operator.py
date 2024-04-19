import requests
import json
from datetime import datetime
import re

class ApiOperator:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def call_api_and_save_response(self, endpoint: str) -> None:
        url = self.base_url + endpoint
        headers = {"X-AUTH-KEY": self.api_key}

        response = requests.get(url, headers=headers)
        # Clean endpoint name for file construction
        endpoint_name = re.sub(r'[^\w]', '_', endpoint)
        if response.status_code == 200:
            current_datetime = datetime.now().strftime("%Y-%m-%d")
            file_name = f"object_store/{endpoint_name}_{current_datetime}.json"

            with open(file_name, "w") as file:
                json.dump(response.json(), file)
                print(f"Response data written to {file_name}")
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

    