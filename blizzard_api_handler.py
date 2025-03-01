import requests
from decouple import config


def get_auth_token():
    url = "https://oauth.battle.net/token"
    data = {"grant_type": "client_credentials"}
    auth = (config('CLIENT_ID'), config('CLIENT_SECRET'))

    response = requests.post(
        url=url,
        data=data,
        auth=auth,
    )

    token = None
    if response.status_code == 200:
        token_data = response.json()
        token = token_data["access_token"]
    else:
        print("Ошибка:", response.status_code, response.text)

    return token


def get_realm_data(token, region, realm_id, namespace, locale):
    pass


def get_auction_data(access_token, region, realm_id, namespace):
    url = f"https://{region}.api.blizzard.com/data/wow/connected-realm/{realm_id}/auctions?namespace={namespace}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(
        url=url,
        headers=headers
    )

    auction_data = response.json().get("auctions", [])
    return auction_data
