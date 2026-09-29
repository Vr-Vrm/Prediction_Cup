## proly should not do this but api key for `practise 1` - ace_ff6b6f164788f7c7e39eb2f6eb658ae91d40a61b

import requests



response = requests.get("https://www.thesuper.market/api/v1/markets",
                        headers={
                            "Authorization":"Bearer ace_ff6b6f164788f7c7e39eb2f6eb658ae91d40a61b" 
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