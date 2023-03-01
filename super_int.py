import requests
from pprint import pprint
def int_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    data = response.json()
    maximum = 0
    max_name = ''
    for line in data:
        if line['name'] == 'Hulk' or line['name'] == 'Captain America' or line['name'] == 'Thanos' and line['powerstats']['intelligence'] > maximum:
            maximum = line['powerstats']['intelligence']
            max_name = line['name']
    print(max_name, maximum)




if __name__ == '__main__':
    int_request()
