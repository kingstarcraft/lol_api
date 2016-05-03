# encoding: utf-8
import pytest

from riotApi import Client
from riotApi.data import region_default, api_versions
from riotApi._utils import base_url
from utils import test_api_key, BaseTestClass

summoner = Client(test_api_key, unlimited=True).Summoner

version = api_versions['summoner']
api_url = '{}/api/lol/{}/{}/summoner/'.format(base_url, region_default, version)


class TestByName(BaseTestClass):
    control_url = '{}by-name/test name1,name 2'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.by_name(['test name1', 'name 2'])


class TestById(BaseTestClass):
    control_url = '{}333,444'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.by_id([333, 444])


class TestMasteries(BaseTestClass):
    control_url = '{}123/masteries'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.masteries(123)


class TestName(BaseTestClass):
    control_url = '{}333,444/name'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.name([333, 444])


class TestRunes(BaseTestClass):
    control_url = '{}333,444/runes'.format(api_url)

    @pytest.fixture
    def data(self):
        return summoner.runes([333, 444])
