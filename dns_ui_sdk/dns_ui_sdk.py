"""SDK for work with https://github.com/operasoftware/dns-ui """
from __future__ import print_function
import json
import requests


def handle_exceptions(func):
    # pylint: disable=W0703
    """Decorator for all function"""
    from functools import wraps

    @wraps(func)
    def wrapper(self, *args, **kw):
        """Function wrapper, run and json decode
        """
        data = {}
        try:
            data = func(self, *args, **kw)
            return data.json()
        except ValueError:
            print("Error in request with status code {0}".format(data))
        except Exception:
            print("Unexpected error")

    return wrapper


class DnsUiSdk(object):
    """Main class for SDK
    """
    def __init__(self, api_url=None, auth_name=None, auth_pass=None):
        self.main_session = requests.Session()
        self.main_session.auth = (auth_name, auth_pass)
        self.base_url = api_url

    @handle_exceptions
    def list_zones(self):
        """Function list all dns zones avialable via UI
        """
        return self.main_session.get(url=self.base_url + 'api/v2/zones')

    @handle_exceptions
    def get_zone(self, zone_name=None):
        """Get all records in specific zone.
        Notice: Zone name must be with dot at the end. e.g. 'example.com.'."""
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name)

    def change_zone(self, zone_name=None, data=None):
        """ Method for add/update/delete record.
        Data for add record
        data = {}
        data['action'] = 'add'
        data['name'] = 'record' + str(random.randint(100,200))
        data['type'] = 'A'
        data['ttl'] = '1D'
        data['comment'] = 'MyIssue'
        data['records'] = []
        records = {}
        records['content'] = "10.10.10.13"
        records['enabled'] = True
        data['records'].append(records)

        change_zone(zone_name='example.com.', data=data)
        E.G. valid json:{"actions": ["action": "add", "name": "record2", "type": "A", "ttl": "1D", "comment": "Issue",
        "records": [{"content": "10.10.10.10","enabled": true}]}],"comment": "Comm"}"""
        new_data = {"comment": "A comment for this update", "actions": []}
        new_data['actions'].append(data)
        return self.main_session.patch(url=self.base_url + 'api/v2/zones/' + zone_name, data=json.dumps(new_data))

    @handle_exceptions
    def list_zone_changes(self, zone_name=None):
        """List all changes in zone.
        Notice: Zone name must be with dot at the end. e.g. 'example.com.'."""
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name + '/changes/')

    @handle_exceptions
    def get_zone_change(self, zone_name=None, change_id=None):
        """Get information about changes by id.
        """
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name + '/changes/' + str(change_id))
