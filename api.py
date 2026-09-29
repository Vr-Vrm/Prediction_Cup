import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY=os.getenv("API_KEY")


response = requests.get("https://www.thesuper.market/api/v1/markets",
                        headers={
                            "Authorization": f"Bearer {API_KEY}"
                        },
                        params={
                            "limit": "1",
                            "status": "open"
                        }
)
print("Status code:")
print(response.status_code)

print("Response Headers:")
print(response.headers)

print("Response Text:")
print(response.text)

print("Response Content:")
print(response.content)

print("Response JSON:")
print(response.json())