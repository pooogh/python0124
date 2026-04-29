import asyncio
import aiohttp
import json

# task 1
async def export_users(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            # file = open(...)
            with open('users_export.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

# asyncio.run(export_users("https://jsonplaceholder.typicode.com/users"))

# task 2
async def import_and_send(url):
    file = open('users_export.json', 'r', encoding='utf-8')
    # print(file)
    users = json.load(file)
    # print(users)
    target = users[0]
    target['name'] = 'Иван Иванов'
    target.pop('id')

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=target) as response:
            data = await response.json()
            print(data)

# asyncio.run(import_and_send('https://jsonplaceholder.typicode.com/users'))
    
# task 3
async def create_one_task(session, url, title):
    async with session.post(url, json=title) as response:
        print(f"{response.status}\n{await response.json()}")

async def bulk_create_tasks(url, file_path):
    try:
        file = open(file_path, 'r', encoding='utf-8')
        raw_file = file.readlines()
        cleaned_file = list(map(lambda string: {"title":string.strip(), "completed": False, "userId": 1}, raw_file))
        
        async with aiohttp.ClientSession() as session:
            tasks = [create_one_task(session, url, task) for task in cleaned_file]
            await asyncio.gather(*tasks)
    except:
        print('File error')

asyncio.run(bulk_create_tasks('https://jsonplaceholder.typicode.com/todos', 'tasks.txt'))
