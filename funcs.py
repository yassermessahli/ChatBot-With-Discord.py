import requests
import json
from googletrans import Translator
import random


def get_quote():
    emtxt = 'ð§,â,ïļðĶ,â ,â,ðĐ,â,ïļð§,ââ,ïļðĪ ,ð,ðĶ,ð§,ââ,ïļâ,ïļð,ð ,âĶ,ïļð,ðū,ð―,ðĪ,ðļ,ðē,ðĶ,ð·,ïļðļ,ïļð§ ,ðĶŋ,ðĻ,ðī,ðĐ,âðĶģ,ðĐ,âðĶ°,ðģ,ââ,ïļð§,ðĨ·,ðĻ,ââ,ïļ,ðĻ,âðŦ,ðĻ,ââ,ïļ,ðĻ,âð­,ð§,âðŽ,ðĐ,âðŦ,ðĻ,âðŽ,ðĻ,ââ,ïļ,,âðž,ðĶđ,ââ,ïļðĶļ,ð§,â,ïļ,ð,ââ,ïļð,ââ,ïļ,ðĪ·,ââ,ïļð§,âðĶ―,ðĐ,âðĶž,ð,ðĪ,ðĪ,ð,ðĪļ,ðĪļ,ââ,ïļðŠ,ðĪ,ðĪ,ð,ð,ð,ð,ð'
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
    emtxt = 'ð,ð,ð,ð,ð,ðĪĢ,ð,ð,ð,ðĨē,ð,ð,ðĪ,ðŠ,ðī,ð,ðĨą,ð,ð,ð,ðĪŠ,ðĨī,ðĨļ,ðĪĨ,ðĪ,ðĪĄ,ðĪ­,ðĩ,ð'
    emojis = emtxt.split(',')
    response = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
    json_data = json.loads(response.text)
    return json_data['joke'] + ' ' + random.choice(emojis)