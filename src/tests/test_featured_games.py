# encoding: utf-8
import pytest

from riotApi import Client
from riotApi.data import region_default
from utils import test_api_key, BaseTestClass

featured_games = Client(test_api_key, unlimited=True).FeaturedGames


class TestFeaturedGames(BaseTestClass):
    control_url = 'https://{}.api.pvp.net/observer-mode/rest/featured'.format(region_default)

    @pytest.fixture
    def data(self):
        return featured_games.featured()
