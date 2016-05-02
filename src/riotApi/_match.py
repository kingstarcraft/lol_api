# encoding: utf-8
from riotApi._base_api_class import BaseApiClass
from riotApi._utils import count_request, base_url
from riotApi.data import region_default, api_versions

version = api_versions['match']
api_url = '{}/api/lol/'.format(base_url)


class Match(BaseApiClass):

    @count_request
    def match(self, match_id, region=region_default, **kwargs):
        """
        Retrieve match by match ID.
        https://developer.riotgames.com/api/methods#!/1064/3671
        """
        url = '{}{}/{}/match/{}'.format(api_url, region, version, match_id)
        return self._get_data(url, **kwargs)



