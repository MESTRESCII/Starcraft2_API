import requests

from blizzardToken import GetJsonToken


class GetGrandMaster():

    def get_grandmaster(self, token: GetJsonToken, region: str, regionID: int):
        url = f"https://{region}.api.blizzard.com/sc2/ladder/grandmaster/{regionID}?access_token={token}"
        self.session = requests.Session()
        self.session.get(url)
        response = requests.get(url, timeout=5)
        response.close()
        return response.json()