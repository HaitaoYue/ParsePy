from parse_client.connection import API_ROOT
from parse_client.datatypes import ParseResource


class Config(ParseResource):
    ENDPOINT_ROOT = '/'.join([API_ROOT, 'config'])

    @classmethod
    def get(cls):
        return cls.GET('').get('params')

