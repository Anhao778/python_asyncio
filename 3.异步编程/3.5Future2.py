import asyncio

async def set_after(fut):
	await asyncio.sleep(2)
	fut.set_result('666')
	
async def main():
#获取当前事件循环
	loop = asyncio.get_running_loop()
	# 创建一个future 对象，这个任务什么都不做
	fut = loop.create_future()
	
	#等待2s之后，通过手动赋值来结束await
	await loop_create_task(set_after(fut))
	
	data = await fut
	print (data)

asyncio.run(main())

