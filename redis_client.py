import redis


pool = redis.ConnectionPool(host='192.168.160.247', port=6379,
                            db=0, password='W03wx2020@redis')
r = redis.Redis(connection_pool=pool)


tle = r.hget('orbit_global_tle', '46232')
print(tle)
