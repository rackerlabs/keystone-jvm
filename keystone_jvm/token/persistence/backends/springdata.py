import copy
from keystone import exception
from keystone import token
from keystone.token import provider

from keystone_jvm.common import beans
from keystone_jvm.common import converters
from keystone.common import models


class Token(token.Driver):

    def __init__(self, conf=None):
        super(Token, self).__init__()
        self.token = beans.token
        self.token_converter = converters.TokenConverter()

    def get_token(self, token_id):
        if token_id is None:
            raise exception.TokenNotFound(token_id=token_id)
        token_ref = self.token_converter.to_keystone(
            self.token.findOne(token_id))
        if not token_ref:
            raise exception.TokenNotFound(token_id=token_id)

        return token_ref

    def create_token(self, token_id, data):
        data_copy = copy.deepcopy(data)
        if not data_copy.get('expires'):
            data_copy['expires'] = provider.default_expire_time()
        if not data_copy.get('user_id'):
            data_copy['user_id'] = data_copy['user']['id']

        java_token_ref = self.token_converter.from_keystone(data_copy)
        self.token.save(java_token_ref)
        return self.token_converter.to_keystone(java_token_ref)

    def delete_token(self, token_id):
        raise exception.NotImplemented()

    def delete_tokens(self, user_id, tenant_id=None, trust_id=None,
                      consumer_id=None):
        raise exception.NotImplemented()

    def _list_tokens(self, user_id, tenant_id=None, trust_id=None,
                     consumer_id=None):
        raise exception.NotImplemented()

    def list_revoked_tokens(self):
        raise exception.NotImplemented()

    def flush_expired_tokens(self):
        raise exception.NotImplemented()
