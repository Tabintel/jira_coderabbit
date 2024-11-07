from google.oauth2 import id_token
   from google.auth.transport import requests
   from typing import Optional
   
   class AuthService:
       def __init__(self):
           self.client_id = os.getenv('GOOGLE_CLIENT_ID')
           self.client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
   
       async def validate_token(self, token: str) -> Optional[dict]:
           try:
               request = requests.Request()
               idinfo = id_token.verify_oauth2_token(
                   token,
                   request,
                   self.client_id
               )
               




               return idinfo if idinfo['aud'] == self.client_id else None
           except ValueError:

               return None       async def refresh_token(self, refresh_token: str) -> Optional[str]:
try:
               response = requests.post(
                   'https://oauth2.googleapis.com/token',
                   data={
                       'client_id': self.client_id,
                       'client_secret': self.client_secret,
                       'refresh_token': refresh_token,
                       'grant_type': 'refresh_token'
                   }
               )
               
               return response.json().get('access_token') if response.status_code == 200 else None
           except Exception:
               return None


           try:
               # Make request to Google OAuth2 token endpoint
               response = requests.post(
                   'https://oauth2.googleapis.com/token',
                   data={
                       'client_id': self.client_id,
                       'client_secret': self.client_secret,
                       'refresh_token': refresh_token,
                       'grant_type': 'refresh_token'
                   }
               )
               
               if response.status_code == 200:
                   return response.json().get('access_token')
               return None
           except Exception:
               return None       
       import os
       from google.oauth2 import id_token
       from google.auth.transport import requests
       from typing import Optional
       
       class AuthService:
           def __init__(self):
               self.client_id = os.getenv('GOOGLE_CLIENT_ID')
               self.client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
               self.token_endpoint = 'https://oauth2.googleapis.com/token'
       
           async def validate_token(self, token: str) -> Optional[dict]:
               try:
                   request = requests.Request()
                   idinfo = id_token.verify_oauth2_token(
                       token,
                       request,
                       self.client_id
                   )
                   return idinfo if idinfo['aud'] == self.client_id else None
               except ValueError:
                   return None
       
           async def refresh_token(self, refresh_token: str) -> Optional[str]:
               try:
                   response = requests.post(
                       self.token_endpoint,
                       data={
                           'client_id': self.client_id,
                           'client_secret': self.client_secret,
                           'refresh_token': refresh_token,
                           'grant_type': 'refresh_token'
                       }
                   )
                   return response.json().get('access_token') if response.status_code == 200 else None
               except Exception:
                   return None
       