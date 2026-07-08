import asyncio
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

#编写asyncio代码，事件循环已切换至uvloop

asyncio.run(...)