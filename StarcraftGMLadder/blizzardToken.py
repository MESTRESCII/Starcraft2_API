import requests


class GetJson():

    def jsons(self, response, clientID: str, clientPW: str):
        self.data = response
        URL = (f"https://{clientID}:{clientPW}@us.battle.net/oauth/token")
        PARAMS = {'grant_type': 'client_credentials'}
        self.resp = requests.post(url=URL, params=PARAMS)
        return self.resp


class GetJsonToken():

    def get_json_token(self, response):
        self.data = response.json()
        self.access_token = self.data["access_token"]
        return self.access_token
