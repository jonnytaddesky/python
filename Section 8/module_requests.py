from requests.adapters import HTTPAdapter
from getpass import getpass
import json
import requests
from requests.models import HTTPError
from requests.exceptions import Timeout

response = requests.get("https://www.engineerspock.com/")
# print(response)

# print(type(response))

# print(response.status_code)

if response:
    print('Works!')

# for url in ["https://www.engineerspock.com/", "https://www.engineerspock.com/inexistent"]:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()

#     except HTTPError as http_err:
#         print(f'Error: {http_err}')
#     except Exception as err:
#         print(f'Unknown erro: {err}')
#     else:
#         print('Connected Successfully!')

# response = requests.get("https://www.engineerspock.com/")
# print(response.content)
# response.encoding = 'utf-8'
# print(response.content)
# response = requests.get("https://api.github.com")
# print(response.text)
# data = respon'se.json()
# print(data)
# blog_response = requests.get("https://www.engineerspock.com/")
# github_response = requests.get("https://api.github.com/")

# print(blog_response.headers, end='\n')
# print('')
# print(github_response.headers, end='\n')
# print('')
# print(blog_response.headers['content-type'])
# placeholder_response = requests.get(
#     "https://jsonplaceholder.typicode.com/comments", params=b'postId=1')
# print(placeholder_response.text)


class Tournament:

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


class ChessPlayer:

    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data["tournaments"]))
        return cls(tournaments)


t1 = Tournament("Aeroflot Open", 2010)
t2 = Tournament("FIDE Wordl Cup", 2018)
t3 = Tournament("FIDE Grand Prox", 2016)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(
    p1, default=lambda obj: obj.__dict__, indent=4, sort_keys=True)

response = requests.post("https://httpbin.org/post", json=json_data)
json_response = response.json()

print(json_response['data'])
print(json_response['headers']['Content-Type'])


# auth_response = requests.get(
#     "https://api.github.com/user", auth=("jonnytaddesky", getpass()))
# print(auth_response.text)
# уточнить этот вопрос

# try:
#     response = requests.get("https://www.engineerspock.com/", timeout=1)
# except Timeout:
#     print("The request time outed")

# print(response)

with requests.Session() as session:
    session.auth = ("jonnytaddesky", getpass())

    response = session.get("https://api.github.com/user")

# do a lot of staff

print(response.json)

adapter = HTTPAdapter(max_retries=3)
with requests.Session() as session:
    session.mount('https://api.github.com/', adapter)
    session.auth = ("jonnytaddesky", getpass())

    try:
        session.get("https://api.github.com/user")
    except ConnectionError as err:
        print(f'Failed to connect: {err}')
    else:
        print('Ok')
