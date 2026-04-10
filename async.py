# асинхрон

# script_ads.py 500kb - 2s
# script_news.py 1000kb - 4s
# --ads----news
# ----news--ads

# --ads
# ----news

# subs.csv 1mb - 5s
# profile.csv 500kb - 2.5s
# -----subs---profile
# ---profile-----subs

# ---prof
# -----subs

# async await
# promise - объект состояния асинх ф-ции, всегда возвращает другой промис
# pending - ф-ция еще в работе, fulfilled - успех, rejected - ошибка
# .then((result, e) => {}) - возрвращает promise

import asyncio
import time

# def read_file():
#     print('Файл A прочитан')
#     time.sleep(5)
#     print('Файл Б прочитан')

# read_file()

# async def async_read_file():
#     print('Файл A прочитан async')
#     await asyncio.sleep(5)
#     print('Файл Б прочитан async')

# asyncio.run(async_read_file())

async def power(num):
    print(num ** 2)
    await asyncio.sleep(3)
    print('power calculated')

async def sqrt(num):
    print(num ** 0.5)
    await asyncio.sleep(2)
    print('sqrt calculated')

# async def math():
#     task_pow = asyncio.create_task(power(9))
#     task_sqrt = asyncio.create_task(sqrt(9))

#     await task_pow
#     await task_sqrt

async def math():
    await asyncio.gather(power(9), sqrt(9))

# asyncio.run(math())
# print(type(sqrt(3)))
# coroutine (корутина) - рез-т асинх ф-ции
# f != f()
# асинхронная ф-ция в просто вызове возвращает внутренний объект (по аналогии с фвп)
# для получения обрабатываемого результата асинх ф-ции нужно запустить ранер из asyncio
# print(sqrt(3))

# event loop (через метод .gather())
# a_f1 -> дошли до await -> ставим в очередь
# a_f2 -> дошли до await -> ставим в очередь
# a_f1 готова -> 
# a_f3 -> 
# a_fN

# task 
# event_loop -> task -> coroutine
# task - это обертка вокруг корутины, чтобы event_loop мог взять ее в работу

# Задача 1
'''
Пишем асинхронный таймер. 
На вход идет имя таймера и кол-во секунд. 
timer('test', 5)
5
4
3
2
1
test истек
'''
async def timer(name, duration):
    for i in range(duration, 0, -1):
        print(i)
        await asyncio.sleep(1)
    print(f"{name} is over")

# asyncio.run(timer('timer 1', 10))

# Задача 2
'''
Написать ф-цию для проверки доступа к сайтам.
На вход идет массив url адресов, ф-ция отправляет get запрос к сайту и если статус
запроса 200, то напротив вывода адреса ставится "OK", в противном случае ставится
"Not allowed"
['https://www.google.com', 'https://www.djfdsjlfs.org']
https://www.google.com OK
https://www.djfdsjlfs.org Not allowed

sitenames.get(url) as response - возвращает объект со свойством status
'''

import aiohttp
# проверяем конкретную ссылку
async def check_status(session, url):
    try:
        async with session.get(url) as response:
            # print(response)
            # /cite -> /site code 300
            return f"{url} OK" if response.status < 400 else f"{url} Not allowed"
    except:
        return f"Connection witn error to {url}"
    
async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [check_status(session, url) for url in urls]
        result = await asyncio.gather(*tasks)
        # print('\n'.join(result))
        print(*result, sep='\n')

asyncio.run(main(['https://www.google.com', 
                  'https://www.python.org',
                  'https://dfkdjfjs.org']))

# обработать ошибки и сделать вывод красивым