'''example 1  '''
import asyncio 

async def func():
	print("12313")
	response = await asyncio.sleep(2) #模拟IO 等待，切换到其他任务
	print ("end:",response)

asyncio.run(func())
	