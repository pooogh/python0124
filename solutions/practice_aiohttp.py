import asyncio
import aiohttp

# task 1
async def fetch_with_params():
    url = "https://httpbin.org/get"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={"key":"value", "another_key":"another_value"}) as response:
            data = await response.json()
            print(f"Params:\n{data.get('args')}")

asyncio.run(fetch_with_params())

# task 2
async def submit_form():
    url = "https://httpbin.org/post"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data={"username": "admin", "password": "secret"}) as response:
            data = await response.json()
            print(f"Прочитано:\n{data.get('form')}")

asyncio.run(submit_form())

# task 3

async def login_basic(url, username, password):
    async with aiohttp.ClientSession() as session:
        auth_data = aiohttp.BasicAuth(username, password)
        async with session.get(url, auth=auth_data) as response:
            status = response.status
            print(status)
            try:
                data = await response.json()
                print(f"Code: {status}\nAuth: {data}")
            except:
                print('Auth was false')

asyncio.run(login_basic("https://httpbin.org/basic-auth/Aladdin/opensesame", 'Aladdin', 'open'))


# task 4
async def send_cookies(url, **cookie):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, cookies=cookie) as response:
            data = await response.json()
            print(data) #add format

asyncio.run(send_cookies("https://httpbin.org/cookies", name="user", secret="secret_hash"))

