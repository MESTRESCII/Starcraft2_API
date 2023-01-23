import requests
from requests.auth import HTTPBasicAuth


class BlizzardAPI:

    def __init__(self):
        self.__clientID: str = input("Enter client ID: ")
        self.__clientPW: str = input(f"Enter client PW: ")
        self.region: str = input(f"Enter client Region: ")

    def get_clientID(self):
        return self.__clientID

    def get_clientPW(self):
        return self.__clientPW

    def get_region(self):
        return self.region

    def create_access_token(self):
        url = f"https://{self.region}.battle.net/oauth/token"
        body = {"grant_type": 'client_credentials'}
        auth = HTTPBasicAuth(self.__clientID, self.__clientPW)
        self.response = requests.post(url, data=body, auth=auth)
        return self.response.json()

