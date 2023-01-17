import json
import pandas as pd
from pathlib import Path


class RefactorJson:

    def __init__(self):
        self.filepath = Path(r'Jsons/')

    @staticmethod
    def get_json(json_obj):
        return json_obj

    def write_json(self, json_obj, name: str = 'data.json'):
        self.jsonString = json.dumps(json_obj)
        self.jsonFile = open(name, "w")
        self.jsonFile = self.jsonFile.write(self.jsonString)
        return self.jsonFile

    def normalize_json(self, json_obj, name: str = 'data.json'):
        with open(name, 'r'):
            self.json_obj = pd.json_normalize(json_obj,
                                              record_path=['ladderTeams'],
                                              errors='ignore')

        return self.json_obj