# encoding: utf-8
import pytest
from tests.utils import test_api_key, BaseTestClass

from riotApi import Client
from riotApi._utils import base_url, region_default, api_versions

matchlist = Client(test_api_key, unlimited=True).Matchlist


version = api_versions['matchlist']
api_url = '{}/api/lol/{}/{}/matchlist/'.format(base_url, region_default, version)


class TestBySummoner(BaseTestClass):
    control_url = '{}by-summoner/123'.format(api_url)

    @pytest.fixture
    def data(self):
        return matchlist.by_summoner(123)