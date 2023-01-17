class RefactorTable():

    @staticmethod
    def get_table(table):
        return table

    def refactor_table(self, normalized_json):
        self.table = normalized_json
        self.tableColumns = self.table.columns.to_list()
        self.table = self.table.drop(columns=['teamMembers'], axis=1)
        return self.table