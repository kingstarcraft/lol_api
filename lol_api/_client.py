# encoding: utf-8
from lol_api.api._champion import Champion
from lol_api.api._championmastery import ChampionMastery
from lol_api.api._current_game import CurrentGame
from lol_api.api._featured_games import FeaturedGames
from lol_api.api._game import Game
from lol_api.api._league import League
from lol_api.api._lol_status import LolStatus
from lol_api.api._match import Match
from lol_api.api._matchlist import Matchlist
from lol_api.api._stats import Stats
from lol_api.api._summoner import Summoner
from lol_api.api._team import Team

from lol_api.api._lol_static_data import LolStaticData
from lol_api._local_data import LocalData
from lol_api._utils import RateLimitWatcher
from lol_api._utils import region_validation


class Client:
    def __init__(self, api_key, region_default, production=False, unlimited=False, server=()):
        self.api_key = api_key
        self.server = server
        self.region_default = region_validation(region_default)
        self.watcher = RateLimitWatcher(production, unlimited=unlimited)

        self.LolStaticData = LolStaticData(api_key=self.api_key, region_default=self.region_default)
        self.LocalData = LocalData(self.LolStaticData)
        self.LolStatus = LolStatus(region_default=self.region_default)

        parameters = {'api_key': self.api_key,
                      'watcher': self.watcher,
                      'region_default': self.region_default,
                      'server': self.server}

        self.Championmastery = ChampionMastery(**parameters)
        self.Champion = Champion(**parameters)
        self.CurrentGame = CurrentGame(**parameters)
        self.FeaturedGames = FeaturedGames(**parameters)
        self.Game = Game(**parameters)
        self.League = League(**parameters)
        self.Match = Match(**parameters)
        self.Matchlist = Matchlist(**parameters)
        self.Stats = Stats(**parameters)
        self.Summoner = Summoner(**parameters)
        self.Team = Team(**parameters)

