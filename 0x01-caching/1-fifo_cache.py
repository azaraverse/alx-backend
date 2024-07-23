#!/usr/bin/env python3
"""FIFO Caching module"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCaching system that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialised method that calls the cooperative superclass
            method.
        """
        super().__init__()

    def put(self, key, item):
        """ Assigns to a dictionary the item value for the key
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_element = next(iter(self.cache_data))
                self.cache_data.pop(first_element)
                print(f'DISCARD: {first_element}')
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to key in the dictionary
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
