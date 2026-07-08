async def main():
	#获取当前事件循环
	loop = asyncio.get_running_loop()
	# 创建一个future 对象，这个任务什么都不做
	fut = loop.create_future()
	#等待任务最终结果（Future对象），没有结果则会一直等待结果
	await fut
asyncio.run(main())