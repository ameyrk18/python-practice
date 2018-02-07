# for i in range(1000,10000,1000):
#        print(i)


#print(2/1)

import redis
r = redis.StrictRedis(host='192.168.99.100', port=6379, db=0)
for key in r.scan_iter("key_pattern*"):
    print (key)