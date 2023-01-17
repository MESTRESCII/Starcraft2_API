from blizzardApi import BlizzardAPI
from blizzardToken import GetJson
from blizzardToken import GetJsonToken
from grandMaster import GetGrandMaster
from refactorJson import RefactorJson
from refactorTable import RefactorTable
from newTable import BuildNewTable
from buildFinalTable import FinalTable


# Variables


class Running:

    def __init__(self):
        self.api = BlizzardAPI()
        self.getJson = GetJson()
        self.getToken = GetJsonToken()
        self.grandmaster = GetGrandMaster()
        self.refactor = RefactorJson()
        self.refactorTable = RefactorTable()
        self.buildNewTable = BuildNewTable()
        self.generatetable = FinalTable()
        self.path = str(self.refactor.filepath)

    def run_api(self):
        self.access = self.api.create_access_token()

    def run_token(self):
        self.token = self.getJson.jsons(self.api.response.json(), self.api.get_clientID(), self.api.get_clientPW())
        self.getToken = self.getToken.get_json_token(self.token)

    def run_grandmaster(self):
        self.getGmAm = self.grandmaster.get_grandmaster(self.getToken, region='us', regionID=1)
        self.getGmEu = self.grandmaster.get_grandmaster(self.getToken, region='eu', regionID=2)
        self.getGmKr = self.grandmaster.get_grandmaster(self.getToken, region='kr', regionID=3)

    def run_refactor_json(self):
        self.jsonAm = self.refactor.get_json(self.getGmAm)
        self.writeAm = self.refactor.write_json(self.jsonAm,
                                                name=self.path + '/America.json')

        self.jsonEu = self.refactor.get_json(self.getGmEu)
        self.writeEu = self.refactor.write_json(self.jsonEu,
                                                name=self.path  + '/Europe.json')

        self.jsonKr = self.refactor.get_json(self.getGmKr)
        self.writeKr = self.refactor.write_json(self.jsonKr,
                                                name=self.path  + '/Korea.json')

    def run_normalize_json(self):
        self.normalizeAm = self.refactor.normalize_json(self.getGmAm,
                                                        name=self.path+'/America.json')

        self.normalizeEu = self.refactor.normalize_json(self.getGmEu,
                                                        name=self.path+'/Europe.json')

        self.normalizeKr = self.refactor.normalize_json(self.getGmKr,
                                                        name=self.path+'/Korea.json')

    def run_refactor_table(self):
        self.refactTableAm = self.refactorTable.refactor_table(self.normalizeAm)
        self.refactTableEu = self.refactorTable.refactor_table(self.normalizeEu)
        self.refactTableKr = self.refactorTable.refactor_table(self.normalizeKr)

    def run_build_new_table(self):
        self.setBuildAm =  self.buildNewTable.set_table(self.path + '/America.json')
        self.buildTableAm = self.buildNewTable.build_table()
        self.refactAm = self.buildNewTable.refactor_table()

        self.setBuildEu = self.buildNewTable.set_table(self.path + '/Europe.json')
        self.buildTableEu = self.buildNewTable.build_table()
        self.refactEu = self.buildNewTable.refactor_table()

        self.setBuildKr = self.buildNewTable.set_table(self.path + '/Korea.json')
        self.buildTableKr = self.buildNewTable.build_table()
        self.refactKr = self.buildNewTable.refactor_table()

    def run_table_generator(self):
        self.tableAm = self.generatetable.create_final_table(self.refactAm, self.refactTableAm)
        self.tableEu = self.generatetable.create_final_table(self.refactEu, self.refactTableEu)
        self.tableKr = self.generatetable.create_final_table(self.refactKr, self.refactTableKr)

        self.createTableAm = self.generatetable.write_table('/GMAmerica')
        self.createTableEu = self.generatetable.write_table('/GMEurope')
        self.createTableKr = self.generatetable.write_table('/GMKorea')
