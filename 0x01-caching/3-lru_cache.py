#!/usr/bin/env python3
"""LRU Caching module"""
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """ FIFOCaching system that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialise the class and call the cooperative superclass
            method.
        """
        super().__init__()
        self.access_time = {}

    def put(self, key, item):
        """ Assigns to a dictionary the item value for the key
        """
        if key and item:
            # if cache is full, remove the least recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = min(self.access_time, key=self.access_time.get)
                del self.cache_data[lru_key]
                del self.access_time[lru_key]
                print(f'DISCARD: {lru_key}')
            # update the access time and cache data
            self.access_time[key] = datetime.now()
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to key in the dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        # update the access time for the key
        self.access_time[key] = datetime.now()
        return self.cache_data.get(key)
