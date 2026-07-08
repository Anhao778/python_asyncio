import time 
import asyncio
import cocurrent.futures

def func1():
	time.sleep(1)
	return 'SB'

async def main():
	loop = asyncio.get_runnig_loop()
	#1.Run in the default loop's executor ( ThreadPoolExecutor)
	#step1 : 内部会先调用 ThreadPoolExecutor 的 submit 方法去线程池中申请一个线程
	#去执行func1 函数，并返回一个 concurrent.futures.Future对象
	#step2： 调用asyncio.wrap_future 将concurrent.futures.Future对象 包装为asyncio.Future obj
	# Since the concurrent.futures.Future obj does not support the await syntax,it can only be wrapped inasyncio.Future obj
		
	fut = loop.run_in_executor(None,func1)
	result = await fut
	print("default thread pool ",result)
	#2. Run in a custom thread pool:
	'''
		with concurrent.futures.ThreadPoolExecutor() as pool:
	     result = await loop.run_in_executor (
						pool,func1)
				print("custom thread pool ",result)
	'''  
	
	#2. Run in a custom process pool:
	'''
		with concurrent.futures.ProcessPoolExecutor() as pool:
	     result = await loop.run_in_executor (
						pool,func1)
				print("custom process pool ",result)
	'''  
	
	asyncio.run(main())
	