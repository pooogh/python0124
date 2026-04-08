# task 1
def create_profile(username, email, **extra):
    profile = {
        'username': username,
        'email': email,
        **extra
    }
    # profile.update(extra)
    return profile

# task 2
get_status_text = lambda code: 'Success' if code < 400 else 'Error'
# code < 400 ? 'Success' : 'Error'

# task 3
from functools import reduce
def build_url(base, *path):
    # return f"{base}/{'/'.join(path)}"

    # ans = base
    # for i in path:
    #     ans += '/' + i
    # return ans

    # path_ans = reduce(lambda acc, i: acc + '/' + i, path, base)
    # path = ['site', 'page1', 'page2']
    # 1: acc = 'https://google.com', i = 'site'
    # 2: acc = 'https://google.com/site', i = 'page1'
    # 3: acc = 'https://google.com/site/page1', i = 'page2'
    # return path_ans
    pass

# task 4
def validate_users(users_list):
    valid_users = filter(lambda user: user['age'] >= 18 and user['is_active'], users_list)
    print_format = list(map(lambda user: f"User: {user['name']}, Age: {user['age']}", valid_users))
    return print_format

# task 5
def apply_settings(default, user):
    new_settings = {**default, **user}
    return new_settings

# default_config = {"theme": "light", "lang": "ru", "notifications": True}
# user_config = {"theme": "dark", "notifications": False}

# final_config = apply_settings(default_config, user_config)

# print(final_config) 

# taks 6
