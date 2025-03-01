from blizzard_api_handler import get_auth_token, get_auction_data
from database import insert_to_db

access_token = get_auth_token()
auction_data = get_auction_data(access_token=access_token, region='eu', realm_id='1080', namespace='dynamic-eu')

db = 'auction_db.csv'
insert_to_db(data=auction_data, file_path=db)