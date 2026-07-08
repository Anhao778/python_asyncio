import asyncio
from nt import read

class Reader(object):
	''' 自定义异步迭代器 （同时也是异步迭代对象）'''
	def __init__(self):
		self.count = 0
		
	async def readline(self):
		self.count += 1
		if self.count == 100:
			return None
		return self.count
	
	def __aiter__(self):
		return self
	
	async def __anext__(self):
		val = await self.readline()
		if val == None:
			raise stopAsyncIteration 
		return val

async def func():
    reader = Reader()
    async for item in reader:
        print(item)

asyncio.run(func())