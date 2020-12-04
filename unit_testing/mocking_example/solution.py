import requests
import time


def get_task():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()


def my_daily_todo():
    return [get_task()]


if __name__ == "__main__":
    start = time.time()
    print(my_daily_todo())
    print(time.time() - start)