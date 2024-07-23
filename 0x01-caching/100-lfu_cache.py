#!/usr/bin/env python3
"""LFU Caching module"""
from base_caching import BaseCaching
from datetime import datetime


class LFUCache(BaseCaching):
    """ LFUCaching system that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialise the class and call the cooperative superclass
            method.
        """
        super().__init__()
        self.access_time = {}
        self.frequency = {}

    def put(self, key, item):
        """ Assigns to a dictionary the item value for the key
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # discard the least frequency used item (lfu algo)
                min_freq = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == min_freq:
                        lfu_keys.append(k)
                # if you find more than 1 item to discard, use lru algo
                # to discard only the least recently used
                if len(lfu_keys) > 1:
                    lru_key = min(lfu_keys, key=self.access_time.get)
                else:
                    lru_key = lfu_keys[0]

                # remove the data, access times and freq either lfu or lru
                del self.cache_data[lru_key]
                del self.access_time[lru_key]
                del self.frequency[lru_key]
                # print DISCARD: key
                print(f'DISCARD: {lru_key}')
            # update the access time, cache data and frequency
            self.cache_data[key] = item
            self.access_time[key] = datetime.now()
            if key in self.frequency:
                self.frequency[key] += 1
            self.frequency[key] = 1

    def get(self, key):
        """ Returns the value linked to key in the dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        # update the access time and frequency
        self.access_time[key] = datetime.now()
        self.frequency[key] += 1
        return self.cache_data.get(key)
