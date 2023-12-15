import pandas as pd
import requests
import json


# class PetSearch:
#     def __init__(self, location):
#         self.location = location

client_id = '9njCg54NUXMmCULunxDofAhiTinYi4F0c1PLJvTsRRqsr8hl0l'
client_secret = 'ZyP0vsHCAc1c0d95xKfLsyBjm3ZGPhNYRPTSu3Yo'
grant_type = {"grant_type": "client_credentials"}
auth_url = 'https://api.petfinder.com/v2/oauth2/token'
token_response = requests.post(url=auth_url, data=grant_type, auth=(client_id, client_secret)).json()

print(token_response['access_token'])

# df = pd.read_json()
