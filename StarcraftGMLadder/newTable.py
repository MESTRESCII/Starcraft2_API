import  pandas as pd

class BuildNewTable():

    def set_table(self, name):
        self.name = pd.read_json(name)

    def get_table(self):
        return self.name

    def build_table(self):
        tableList = []
        for elem in self.name['ladderTeams']:
            tableList.append(elem['teamMembers'])

        self.table = pd.DataFrame(tableList, columns=['col'])
        return self.table

    def refactor_table(self):
        tableColumns = ['id', 'realm', 'region', 'displayName', 'favoriteRace', 'clanTag']
        self.table = pd.json_normalize(data=self.table.col,
                                       meta=tableColumns)
        return self.table