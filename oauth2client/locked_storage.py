# Copyright 2015 Google Inc. All rights reserved.
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

"""TODO"""

import os
import threading

from oauth2client.client import Storage as Storage


class LockedStorage(Storage):
    """TODO"""

    def __init__(self, storage, lock=None):
        """TODO"""
        self._storage = storage

        if lock is None:
            lock = threading.Lock()

        self._lock = lock

    def get(self, *args, **kwargs):
        """TODO"""
        with self._lock:
            return self._storage.get(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """TODO"""
        with self._lock:
            return self._storage.delete(*args, **kwargs)

    def put(self, *args, **kwargs):
        """TODO"""
        with self._lock:
            return self._storage.put(*args, **kwargs)
