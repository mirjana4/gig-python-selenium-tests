import requests


class BaseRestClient:
    """ Base REST client class that will be extended by specific REST client enpoints """
    _base_url: str

    def __init__(self):
        self._base_url = 'https://gorest.co.in/public'

    def request_get(self, path, params=None, **kwargs):
        url: str = self._base_url + path
        return requests.get(url=url, params=params, **kwargs)
