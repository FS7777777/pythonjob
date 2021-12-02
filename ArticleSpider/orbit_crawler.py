import requests
import asyncio
import random
import functools
import redis

global POOL


def init_redis_pool():
    global POOL
    POOL = redis.ConnectionPool(host='192.168.160.247', port=6379,
                                db=0, password='W03wx2020@redis')


def fake_header():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95',
        'Safari/537.36 OPR/26.0.1656.60',
        'Opera/8.0 (Windows NT 5.1; U; en)',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 '
        '(maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 '
        '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    ]
    UserAgent = random.choice(user_agent_list)
    header = {'User-Agent': UserAgent}
    return header


async def http_client(host):
    # 获取tle数据
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(
        None, functools.partial(requests.get, host, headers=fake_header()))
    response = await future
    if response.status_code == 200:
        # 解析tle
        list_tle = parse_tle(response.text)
        storage_tle(list_tle)
    else:
        print('down load tle error')


def storage_tle(list_tle):
    global POOL
    r = redis.Redis(connection_pool=POOL)
    try:
        for temp in list_tle:
            # 判断两行的有效性可以再完善下此处只做了长度校验
            if len(temp) == 3:
                # 获取两行第二行noradid
                key = temp[2].split()[1]
                r.hset('orbit_global_tle', key, '\n'.join(temp))
    finally:
        r.close()


def parse_tle(context):
    list_original = context.split('\n')
    # 把list分为长度为5的4段
    list_tle = []
    for i in range(0, len(list_original), 3):
        list_tle.append(list_original[i:i+3])
    return list_tle


if __name__ == "__main__":
    # 初始化redis连接
    init_redis_pool()
    # 获取数据
    loop = asyncio.get_event_loop()
    tasks = [http_client(host)
             for host in ['https://www.celestrak.com/NORAD/elements/tle-new.txt', 'https://www.celestrak.com/NORAD/elements/stations.txt',
                          'https://www.celestrak.com/NORAD/elements/visual.txt', 'https://www.celestrak.com/NORAD/elements/active.txt',
                          'https://www.celestrak.com/NORAD/elements/analyst.txt', 'https://www.celestrak.com/NORAD/elements/2019-006.txt',
                          'https://www.celestrak.com/NORAD/elements/1999-025.txt', 'https://www.celestrak.com/NORAD/elements/iridium-33-debris.txt',
                          'https://www.celestrak.com/NORAD/elements/cosmos-2251-debris.txt', 'https://www.celestrak.com/NORAD/elements/weather.txt',
                          'https://www.celestrak.com/NORAD/elements/noaa.txt', 'https://www.celestrak.com/NORAD/elements/goes.txt',
                          'https://www.celestrak.com/NORAD/elements/resource.txt', 'https://www.celestrak.com/NORAD/elements/sarsat.txt',
                          'https://www.celestrak.com/NORAD/elements/dmc.txt', 'https://www.celestrak.com/NORAD/elements/tdrss.txt',
                          'https://www.celestrak.com/NORAD/elements/argos.txt', 'https://www.celestrak.com/NORAD/elements/planet.txt',
                          'https://www.celestrak.com/NORAD/elements/spire.txt', 'https://www.celestrak.com/NORAD/elements/geo.txt',
                          'https://www.celestrak.com/satcat/gpz.php', 'https://www.celestrak.com/satcat/gpz-plus.php',
                          'https://www.celestrak.com/NORAD/elements/intelsat.txt', 'https://www.celestrak.com/NORAD/elements/ses.txt',
                          'https://www.celestrak.com/NORAD/elements/iridium.txt', 'https://www.celestrak.com/NORAD/elements/iridium-NEXT.txt',
                          'https://www.celestrak.com/NORAD/elements/starlink.txt', 'https://www.celestrak.com/NORAD/elements/oneweb.txt',
                          'https://www.celestrak.com/NORAD/elements/orbcomm.txt', 'https://www.celestrak.com/NORAD/elements/globalstar.txt',
                          'https://www.celestrak.com/NORAD/elements/amateur.txt', 'https://www.celestrak.com/NORAD/elements/x-comm.txt',
                          'https://www.celestrak.com/NORAD/elements/other-comm.txt', 'https://www.celestrak.com/NORAD/elements/satnogs.txt',
                          'https://www.celestrak.com/NORAD/elements/gorizont.txt', 'https://www.celestrak.com/NORAD/elements/raduga.txt',
                          'https://www.celestrak.com/NORAD/elements/molniya.txt', 'https://www.celestrak.com/NORAD/elements/gps-ops.txt',
                          'https://www.celestrak.com/NORAD/elements/glo-ops.txt', 'https://www.celestrak.com/NORAD/elements/beidou.txt',
                          'https://www.celestrak.com/NORAD/elements/galileo.txt', 'https://www.celestrak.com/NORAD/elements/sbas.txt',
                          'https://www.celestrak.com/NORAD/elements/nnss.txt', 'https://www.celestrak.com/NORAD/elements/musson.txt',
                          'https://www.celestrak.com/NORAD/elements/science.txt', 'https://www.celestrak.com/NORAD/elements/geodetic.txt',
                          'https://www.celestrak.com/NORAD/elements/engineering.txt', 'https://www.celestrak.com/NORAD/elements/education.txt',
                          'https://www.celestrak.com/NORAD/elements/military.txt', 'https://www.celestrak.com/NORAD/elements/radar.txt',
                          'https://www.celestrak.com/NORAD/elements/cubesat.txt', 'https://www.celestrak.com/NORAD/elements/other.txt']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
