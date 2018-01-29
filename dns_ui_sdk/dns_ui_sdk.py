"""This module illustrates how to write your docstring in OpenAlea
and other projects related to OpenAlea."""
from __future__ import print_function
import json
import requests


def handle_exceptions(func):
    # pylint: disable=W0703
    """This module illustrates how to write your docstring in OpenAlea
    and other projects related to OpenAlea."""
    from functools import wraps

    @wraps(func)
    def wrapper(self, *args, **kw):
        """This module illustrates how to write your docstring in OpenAlea
        and other projects related to OpenAlea."""
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
    """This module illustrates how to write your docstring in OpenAlea
    and other projects related to OpenAlea."""
    def __init__(self, api_url=None, auth_name=None, auth_pass=None):
        self.main_session = requests.Session()
        self.main_session.auth = (auth_name, auth_pass)
        self.base_url = api_url

    @handle_exceptions
    def list_zones(self):
        """This module illustrates how to write your docstring in OpenAlea
        and other projects related to OpenAlea."""
        return self.main_session.get(url=self.base_url + 'api/v2/zones')

    @handle_exceptions
    def get_zone(self, zone_name=None):
        """This module illustrates how to write your docstring in OpenAlea
        and other projects related to OpenAlea."""
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name)

    def change_zone(self, zone_name=None, data=None):
        """This module illustrates how to write your docstring in OpenAlea
        and other projects related to OpenAlea."""
        new_data = {"comment": "A comment for this update", "actions": []}
        new_data['actions'].append(data)
        return self.main_session.patch(url=self.base_url + 'api/v2/zones/' + zone_name, data=json.dumps(new_data))

    @handle_exceptions
    def list_zone_changes(self, zone_name=None):
        """This module illustrates how to write your docstring in OpenAlea
        and other projects related to OpenAlea."""
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name + '/changes/')

    @handle_exceptions
    def get_zone_change(self, zone_name=None, change_id=None):
        """This module illustrates how to write your docstring in OpenAlea
        and other projects related to OpenAlea."""
        return self.main_session.get(url=self.base_url + 'api/v2/zones/' + zone_name + '/changes/' + str(change_id))
