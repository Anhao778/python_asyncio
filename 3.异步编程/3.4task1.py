import asyncio

async def func():
	print (1)
	await asyncio.sleep(1)
	print(2)
	return "返回值"
	
async def main():
	print("main start .")
	
	#创建协程，将协程封装到task对象中并立即添加到事件循环的任务列表中，等待事件循环执行（默认就绪态）
	task_list = [
			asyncio.create_task(func(),name = 'n1'),
			asyncio.create_task(func(),name = 'n2')
		]
		
	print("main end ")
	done,pending = await asyncio.wait(task_list,timeout = None)
	print(done)

asyncio.run(main())