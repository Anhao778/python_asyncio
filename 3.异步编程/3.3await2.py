import asyncio

async def others():
	print("start")
	await asyncio.sleep(2)
	print("end")
	return "返回值"

async def func():
	print("执行协程内部代码")
	#遇到IO操作挂起当前协程，等IO操作完成之后再继续往下执行，当协程挂起时，事件循环可以去执行其他任务（协程）
	response = await others() 
	print("IO 请求结束，结果为：",response)
	
asyncio.run(func())