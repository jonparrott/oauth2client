# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests for oauth2client.dictionary_storage"""

import unittest

from oauth2client import GOOGLE_TOKEN_URI
from oauth2client.client import OAuth2Credentials
from oauth2client.contrib.dictionary_storage import DictionaryStorage


__author__ = 'jonwayne@google.com (Jon Wayne Parrott)'


class DictionaryStorageTests(unittest.TestCase):

    def _generate_credentials(self, scopes=None):
        return OAuth2Credentials(
            'access_tokenz',
            'client_idz',
            'client_secretz',
            'refresh_tokenz',
            '3600',
            GOOGLE_TOKEN_URI,
            'Test',
            id_token={
                'sub': '123',
                'email': 'user@example.com'
            },
            scopes=scopes)

    def test_string_key(self):
        dictionary = {}
        key = 'credentials'
        credentials = self._generate_credentials()
        storage = DictionaryStorage(dictionary, key)

        storage.put(credentials)

        self.assertTrue(key in dictionary)

        retrieved = storage.get()

        self.assertEqual(retrieved.access_token, credentials.access_token)

        storage.delete()

        self.assertTrue(key not in dictionary)
        self.assertTrue(storage.get() is None)


if __name__ == '__main__':  # pragma: NO COVER
    unittest.main()
