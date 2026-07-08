#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import asyncio

import aioredis

async def execute(address, password):
    print("start execute redis")
    
    #网络io操作，创建redis连接
    redis = await aioredis.create_redis(address, password=password)
    #网络io操作：在redis中设置哈希值car，内部再设置三个键值对，即{’car‘:{'key1':'1','key2':'2','key3':'3'}}
    await redis.hmset_dict('car',key1 = 1,key2 = 2,key3 = 3)
    #网络io操作：从redis中获取哈希值car的所有键值对
    result = await redis.hgetall('car',encoding='utf-8')
    print(result)
    #网络io操作：关闭redis连接
    await redis.close()
    #网络io操作：等待redis连接关闭完成
    await redis.wait_closed()
    print("end execute redis")

asyncio.run(execute('redis://localhost:6379', '123456'))
