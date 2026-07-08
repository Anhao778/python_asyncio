import asyncio

class AsyncContextManager:
	def __init__(self):
		self.conn = None
	
	async def do_something(self):
		#异步操作数据库
		return 666
		
	async def __aenter__(self):
		#异步链接数据库
		self.conn = await asyncio.sleep(1)#异步链接数据库
		print(self.conn)
		return self 
		
	async def __aexit__(self,exc_type,exc_val,tb):
		#异步关闭数据库链接
		await asyncio.sleep(1)
		
async def func():		
	async with AsyncContextManager() as f:
		result = await f.do_something()
		print(result)

asyncio.run(func())
