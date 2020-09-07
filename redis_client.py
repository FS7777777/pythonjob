import redis


pool = redis.ConnectionPool(host='192.168.160.247', port=6379,
                            db=0, password='GRePZdx3')
r = redis.Redis(connection_pool=pool)


tle = r.hget('orbit_global_tle', '44884')
print(tle)
