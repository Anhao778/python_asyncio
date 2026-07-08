import asyncio
async def func():
	print("12313")

result = func()

"""
#生成或获取一个事件循环
loop = asyncio.get_event_loop()
#将任务放入任务列表
loop.run_until_complete(result)
"""
asyncio.run(result) #py3.7 之后