import requests
from pprint import pprint


class Asteroid:
    BASE_API_URL = 'https://www.neowsapp.com/rest/v1/neo/{}?api_key=yCLfQ36chJZj3O2ShMZpd57wasWP2WBjOLov5shH'

    def __init__(self, spk_id):
        self.api_url = self.BASE_API_URL.format(spk_id)

    def get_data(self):
        return requests.get(self.api_url).json()

    @property
    def name(self):
        return self.get_data()['name']

    @property
    def diameter(self):
        return int(self.get_data()['estimated_diameter']['meters']['estimated_diameter_max'])


# asteroid = Asteroid(2440012)
# pprint(asteroid.get_data())
# print(asteroid.name)
# print(asteroid.diameter)
