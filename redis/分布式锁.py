
#!/usr/bin/env python
# coding=utf-8
 
import time
import redis
 
class RedisLock(object):
    def __init__(self, key):
        self.rdcon = redis.Redis(host='', port=6379, password="", db=1)
        self._lock = 0
        self.lock_key = "%s_dynamic_test" % key
 
    @staticmethod
    def get_lock(cls, timeout=10):
        while cls._lock != 1:
            timestamp = time.time() + timeout + 1
            cls._lock = cls.rdcon.setnx(cls.lock_key, timestamp)
            if cls._lock == 1 or (time.time() > cls.rdcon.get(cls.lock_key) and time.time() > cls.rdcon.getset(cls.lock_key, timestamp)):
                print "get lock"
                break
            else:
                time.sleep(0.3)
 
    @staticmethod
    def release(cls):
        if time.time() < cls.rdcon.get(cls.lock_key):
            print "release lock"
            cls.rdcon.delete(cls.lock_key)
 
def deco(cls):
    def _deco(func):
        def __deco(*args, **kwargs):
            print "before %s called [%s]."%(func.__name__, cls)
            cls.get_lock(cls)
            try:
                return func(*args, **kwargs)
            finally:
                cls.release(cls)
        return __deco
    return _deco
 
@deco(RedisLock("112233"))
def lock():
    time.sleep(20)
 
 
if __name__ == "__main__":
    lock()

