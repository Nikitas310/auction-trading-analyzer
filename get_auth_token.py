import requests
from decouple import config


url = "https://oauth.battle.net/token"
data = {"grant_type": "client_credentials"}
auth = (config('CLIENT_ID'), config('CLIENT_SECRET'))

response = requests.post(
    url=url,
    data=data,
    auth=auth,
)

if response.status_code == 200:
    token_data = response.json()
    print("Токен:", token_data["access_token"])
else:
    print("Ошибка:", response.status_code, response.text)