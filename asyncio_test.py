import aiohttp
import time
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as response:
            assert response.status == 200

    return response.text()

async def get_one_html(url):
    result = await get(url) # 由于asyncio不支持http请求，所以需要用aiohttp来封装一个get
    return result

if __name__  == "__main__":
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/65.0.3325.183 Safari/537.36 "
                             "Vivaldi/1.96.1147.64"}

    #urls = [
    #    "http://www.baidu.com", "http://www.sina.com.cn",
    #    "http://www.163.com", "http://www.sohu.com",
    #    "http://www.csdn.net", "http://www.jobbole.com",
    #    "http://www.qq.com", "http://weixin.qq.com",
    #    "http://www.jb51.net", "https://m.qidian.com"
    #]
    urls = [ "http://www.88dushu.cc/shu/108" ]
    # 构建tasks列表
    tasks = [asyncio.ensure_future(get_one_html(url)) for url in urls]
	
    start = time.time()
	
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    end = time.time() - start
    print(end)
	
    for task in tasks:
        print(task.result())
