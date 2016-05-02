import sys
import os
from time import time

import pytest
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from riotApi._utils import check_response_code, RateLimitWatcher, count_request, get_champion_id
from riotApi.exceptions import RateLimitExceededError


def test_check_response_code():
    check_response_code(200)


def test_bad_response_code():
    with pytest.raises(requests.RequestException):
        check_response_code(500)


class TestRateLimitWatcher:

    @pytest.fixture
    def watcher(self):
        return RateLimitWatcher(production=False)

    def test_add_request(self, watcher):
        watcher.add_request()
        assert len(watcher.made_requests) == 1

    def test_reload(self, watcher):
        watcher.made_requests.append(time() - 900)
        watcher.made_requests.append(time())
        watcher._reload()
        assert len(watcher.made_requests) == 1

    def test_request_available(self, watcher):
        assert watcher.request_available() is True

    def test_request_unavailable(self, watcher):
        for _ in range(500):
            watcher.add_request()
        assert watcher.request_available() is False

    def test_short_request_unavailable(self, watcher):
        for _ in range(10):
            watcher.add_request()
        assert watcher.request_available() is False

    def test_production(self):
        watcher = RateLimitWatcher(production=True)
        for _ in range(40):
            watcher.add_request()
        assert watcher.request_available() is True


class TestCountRequest:
    message = 'test'

    watcher = RateLimitWatcher(production=False)

    @count_request
    def api_func(self):
        return self.message

    @pytest.fixture(autouse=True)
    def set_watcher(self):
        self.watcher = RateLimitWatcher(production=False)

    def test_return(self):
        assert self.api_func() == self.message

    def test_counter(self):
        self.api_func()
        self.api_func()
        assert len(self.watcher.made_requests) == 2

    def test_rate_limit_exceeded_error_rise(self):
        for _ in range(10):
            self.api_func()
        with pytest.raises(RateLimitExceededError):
            self.api_func()


def test_get_champion_id():
    assert get_champion_id(5) == 5

    with pytest.raises(NotImplementedError):
        get_champion_id('annie')