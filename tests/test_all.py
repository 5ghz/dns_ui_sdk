#!/usr/bin/env python
import unittest
import dns_ui
import random


class TestRequestsCall(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.c = dns_ui.DnsUiSdk(api_url='https://dnsui.xiven.com/', auth_name='testadmin', auth_pass='testadmin')

    def test_0_list_zones(self):
        data = self.c.list_zones()
        self.assertIsNotNone(data)

    def test_1_get_zone(self):
        data = self.c.get_zone("example.com.")
        self.assertIsNotNone(data)

    def test_2_list_changes(self):
        data = self.c.list_zone_changes("example.com.")
        self.assertIsNotNone(data)

    def test_3_list_zones(self):
        data = self.c.get_zone_change(zone_name="example.com.", change_id=1)
        self.assertIsNotNone(data)

    def test_4_change_zone(self):
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
        data = self.c.change_zone(zone_name='example.com.', data=data)
        self.assertEqual(data.status_code,200)


if __name__ == '__main__':
    unittest.main()