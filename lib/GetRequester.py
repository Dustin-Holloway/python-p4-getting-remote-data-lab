import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = self.url

        response = requests.get(url)
        return response.content

    def load_json(self):
        list = []
        list_items = json.loads(self.get_response_body())
        for thing in list_items:
            list.append(thing)

        return list


requester = GetRequester(
    url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
)

thing = requester.load_json()

print(thing)
