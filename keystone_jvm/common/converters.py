import json
import pytz
from datetime import datetime
from keystone.common import models

from java.lang import Iterable
from java.util import Date
from java.util import HashSet
from java.util import ArrayList
from org.openstack import Token


class BaseConverter(object):
    attribute_array = []
    attribute_mapping = {}
    model = None
    java_model = None

    def to_datetime(self, date):
        m_sec = date.getTime() % 1000L
        time = datetime.fromtimestamp(
            date.time / 1000, pytz.utc).replace(tzinfo=None)
        return time.replace(microsecond=m_sec * 1000)

    def _to_keystone(self, obj):
        result = self.model()
        for key, value in self.attribute_mapping.items():
            if value and getattr(obj, value) is not None:
                if key in self.attribute_array:
                    result[key] = []
                    for item in getattr(obj, value):
                        result[key].append(item)
                else:
                    if isinstance(getattr(obj, value), Date):
                        date = getattr(obj, value)
                        result[key] = self.to_datetime(date)
                    else:
                        if isinstance(getattr(obj, value), int):
                            result[key] = str(getattr(obj, value))
                        else:
                            result[key] = getattr(obj, value)
                            try:
                                result[key] = json.loads(result[key])
                            except:
                                pass
        return result

    def to_keystone(self, obj):
        if obj is None:
            return None
        if isinstance(obj, Iterable):
            result = []
            for item in obj:
                result.append(self._to_keystone(item))
            return result
        else:
            return self._to_keystone(obj)

    def from_datetime(self, date):
        td = date - datetime(1970, 1, 1)
        epoch = (1000 * (td.microseconds +
                 (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6)
        return Date(epoch)

    def from_keystone(self, obj):
        result = self.java_model()
        for key, value in self.attribute_mapping.items():
            if value and key in obj.keys() and obj[key] is not None:
                if key in self.attribute_array:
                    try:
                        values = HashSet()
                        setattr(result, value, values)
                    except:
                        values = ArrayList()
                        setattr(result, value, values)
                    for item in obj[key]:
                        values.add(item)
                else:
                    if isinstance(obj[key], datetime):
                        setattr(result, value, self.from_datetime(obj[key]))
                    elif isinstance(obj[key], dict):
                        setattr(result, value, json.dumps(obj[key]))
                    else:
                        try:
                            setattr(result, value, obj[key])
                        except:
                            setattr(result, value, int(obj[key]))

        return result


class TokenConverter(BaseConverter):
    model = models.Token
    java_model = Token
    attribute_mapping = {'id': 'id',
                        'expires': 'expires',
                        'user': 'user',
                        'tenant': 'tenant',
                        'metadata': 'metadata',
                        'trust_id': 'trustId',
                        'key': 'key',
                        'token_data': 'tokenData',
                        'user_id': 'userId',
                        'token_version': 'tokenVersion'}
