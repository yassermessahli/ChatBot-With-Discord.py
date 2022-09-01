import requests
import json
from googletrans import Translator
import random


def get_quote():
    emtxt = '🧜,♂,️🦄,♠,✔,👩,✈,️🧚,‍♀,️🤠,😇,🦀,🧙,‍♂,️☁,️🍑,💠,♦,️😎,👾,👽,🤖,🐸,🐲,🦉,🕷,️🕸,️🧠,🦿,👨,👴,👩,‍🦳,👩,‍🦰,👳,‍♂,️🧔,🥷,👨,‍⚕,️,👨,‍🏫,👨,‍✈,️,👨,‍🏭,🧑,‍🔬,👩,‍🏫,👨,‍🔬,👨,‍✈,️,,‍🍼,🦹,‍♀,️🦸,🧚,♂,️,🙍,‍♂,️💁,‍♀,️,🤷,‍♂,️🧑,‍🦽,👩,‍🦼,👌,🤙,🤞,👆,🤸,🤸,‍♂,️💪,🤚,🤟,👐,🙏,🎈,🎊,🎃'
    emojis = emtxt.split(',')
    response = requests.get('https://api.quotable.io/random')
    json_data = json.loads(response.text)
    return json_data['content'] + ' ' + random.choice(emojis)


t = Translator()
def translate(text, lang):
    return t.translate(text, dest=lang).text

def get_meme():
    response = requests.get('https://api.imgflip.com/get_memes')
    json_data = json.loads(response.text)
    return random.choice(json_data['data']['memes'])

def get_dog():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    json_data = json.loads(response.text)
    return json_data['message']

def get_cat():
    response = requests.get('https://aws.random.cat/meow')
    json_data = json.loads(response.text)
    return json_data['file']

def get_joke():
    emtxt = '😀,😁,😂,😄,😃,🤣,😅,😆,😉,🥲,🙄,😑,🤐,😪,😴,😌,🥱,😓,🙃,😒,🤪,🥴,🥸,🤥,🤓,🤡,🤭,🐵,🐒'
    emojis = emtxt.split(',')
    response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
    json_data = json.loads(response.text)
    return json_data['joke'] + ' ' + random.choice(emojis)