from datetime import datetime

class LRUCache:
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__cache = {}

    def get(self, key: str) -> str:
        value = self.__cache.get(key, '')
        if value != '':
            self.__cache[key] = (value[0], datetime.now())
            return value[0]

        return value

    def __lru(self) -> str:
        lru_time = list(self.__cache.values())[0][1]
        lru_key = list(self.__cache.keys())[0]
        for key, value in self.__cache.items():
            if value[1] < lru_time:
                lru_key = key

        return lru_key


    def set(self, key: str, value: str) -> None:
        if len(self.__cache.keys()) == self.__capacity:
            self.__cache.pop(self.__lru())

        self.__cache[key] = (value, datetime.now())

    def delete(self, key: str) -> None:
        self.__cache.pop(key, "")
