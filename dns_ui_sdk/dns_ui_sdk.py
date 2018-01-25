import requests
import json


class DnsUiSdk(object):
    def __init__(self, api_url=None, auth_name=None, auth_pass=None):
        self.main_session = requests.Session()
        self.main_session.auth = (auth_name, auth_pass)
        self.base_url = api_url

    def handle_exceptions(fn):
        from functools import wraps

        @wraps(fn)
        def wrapper(self, *args, **kw):
            data = {}
            try:
                data = fn(self, *args, **kw)
                return data.json()
            except Exception:
                print("Error in request with status code {0}".format(data))

        return wrapper

    @handle_exceptions
    def list_zones(self):
        return self.main_session.get(url=self.base_url+'api/v2/zones')

    @handle_exceptions
    def get_zone(self, zone_name=None):
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name)

    def change_zone(self, zone_name=None, data=None):
        new_data = {"comment": "A comment for this update", "actions": []}
        new_data['actions'].append(data)
        return self.main_session.patch(url=self.base_url + 'api/v2/zones/' + zone_name, data=json.dumps(new_data))

    @handle_exceptions
    def list_zone_changes(self, zone_name=None):
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name + '/changes/')

    @handle_exceptions
    def get_zone_change(self, zone_name=None, change_id=None):
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name + '/changes/' + str(change_id))
