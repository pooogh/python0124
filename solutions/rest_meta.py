import asyncio
import aiohttp

#task 1
async def update_resource(url, data, data_to_update):
    async with aiohttp.ClientSession() as session:
        post_id = 0
        async with session.post(url, json=data) as response:
            if response.status < 400:
                response_data = await response.json()
                print(f"Response: {response_data}")
                post_id = response_data.get('id')
                print(post_id)
            else:
                print("Post error")
                return
        new_path = f"{url}/1"
        async with session.patch(new_path, json=data_to_update) as response:
            if response.status < 400:
                print(f"Response: {await response.json()}")
            else:
                print("Update error")
                return


asyncio.run(update_resource("https://jsonplaceholder.typicode.com/posts", {"title": "Новый пост", "body": "Текст", "userId": 1}, {"title": "Обновленный заголовок"}))

# task 2

async def fetch_secure_data(url):
    headers = {
        "Authorization": "Bearer secret_token_777", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            # print(response.status)
            if response.status < 400:
                data = await response.json()
                print(data)
            else:
                print(f"error: {response.status}")

asyncio.run(fetch_secure_data("https://httpbin.org/bearer2"))

# task 3
async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # print(await response.read())
            image = await response.read()
            with open("test_image.jpg", "wb") as f:
                f.write(image)

asyncio.run(download_image("https://httpbin.org/image/jpeg"))

# task 4

# task 5
async def fetch_pages(url):
    all_posts = []
    
    async with aiohttp.ClientSession() as session:
        for i in range(1, 4):
            params = {"_page": i, "_limit": 5}

            async with session.get(url, params=params) as response:
                post = await response.json()
                all_posts.extend(post)

                print(f"Page {i} loaded, get {len(post)} posts")

        print(f"Total posts: {len(all_posts)}")

asyncio.run(fetch_pages("https://jsonplaceholder.typicode.com/posts"))