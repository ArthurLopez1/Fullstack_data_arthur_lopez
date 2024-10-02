import pandas as pd
from components.constants import SUMMER_GAMES_PATH


class SummerGames:
    def __init__(self) -> None:
        self.df = pd.read_csv(SUMMER_GAMES_PATH, index_col=0)


class MedalsSummer(SummerGames):
    def __init__(self) -> None:
        super().__init__()
        self.df = self.df[self.df["Medal"].notna()]

    @property
    def data(self):
        return self.df


class MedalsPerCountry:
    def __init__(self) -> None:
        self.df_summer_medals = MedalsSummer().data

    @property
    def summer_noc(self):
        medals_per_country = (
            self.df_summer_medals.groupby("NOC")["Medal"]
            .count()
            .sort_values(ascending=False)
        )

        return medals_per_country

    @property
    def summer_medals_type(self):
        return (
            self.df_summer_medals.groupby(["NOC", "Medal"]).size().unstack(fill_value=0)
        )
