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
