from pathlib import Path
import pandas as pd
from datetime import date
from os.path import exists as file_exists


class FinalTable():

    def __init__(self):
        self.path = str(Path(r'SC2Ladders/'))

    def create_final_table(self, table_1, table_2):
        cols = ['id', 'realm', 'region', 'displayName',
                'favoriteRace', 'clanTag', 'previousRank',
                'points', 'wins', 'losses', 'mmr', 'joinTimestamp']

        self.df = pd.concat([table_1, table_2], axis=1, ignore_index=True)
        self.df.columns = self.df.columns.map(str)
        self.df.columns = cols
        return self.df

    def write_table(self, name: str):
        if not file_exists(f"{self.path}{name}-{date.today()}.csv"):
            filepath = Path(f'{self.path}{name}-{date.today()}.csv')
            filepath.parent.mkdir(parents=True, exist_ok=True)
            self.df.to_csv(filepath)
