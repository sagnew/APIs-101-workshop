# APIs-101-workshop
Code for a workshop I am giving to a class of NYU students

## Getting Started

To install all of the requirements, create a virtualenv and run the following command:

```
pip install -r requirements.txt
```

## APIs

To find a bunch of cool APIs in general, check out [ProgrammableWeb](https://www.programmableweb.com/)

You already know about [Twilio](https://www.twilio.com/docs/quickstart/python/sms), so here are some example REST APIs that are easy to work with, and some code to get started.

### NASA

[NASA has a bunch of APIs](https://api.nasa.gov/api.html). Here's some code to work with the Astronomy Picture of the Day API:

```
import requests

url = 'https://api.nasa.gov/planetary/apod'
params = { 'api_key': 'DEMO_KEY' }
response = requests.get(url, params).json()

print(response['url'], response['explanation'])
```

### Star Wars

There is a [Star Wars API](https://swapi.co/documentation). Here's some code to grab data on Luke Skywalker.

```
import requests

url = 'https://swapi.co/api/people/1/'
response = requests.get(url).json()

print(response['name']) # Luke Skywalker
```

### Pokemon

There is also a [Pokemon API](https://pokeapi.co/), made by the same person who did the Star Wars API.

```
import requests

url = 'http://pokeapi.co/api/v2/pokemon/112'
response = requests.get(url).json()

print(response['name']) # Rhydon is my favorite Pokemon.
```

### Giphy

I'm sure you've all heard of Giphy. But they have an [easy to use API](https://developers.giphy.com/docs/) as well! Here is some code to grab random SNES GIFs:

```
import requests

url = 'https://api.giphy.com/v1/gifs/search'
params = { 'api_key': 'dc6zaTOxFJmzC', 'q': 'SNES' } # That's the default API demo key. Don't commit your credentials!
response = requests.get(url, params).json()

# Prints the URL to the first GIF in a search for Super Nintendo GIFs.
print(response['data'][0]["images"]["downsized"]["url"])
```

### RhymeBrain

[Rhymebrain](http://rhymebrain.com/api.html) is a cool API that you can use to write poetry. Here's some code to find words that rhyme the most with "python":

```
import requests

url = 'http://rhymebrain.com/talk'
params = { 'function': 'getRhymes', 'word': 'python' }
response = requests.get(url, params).json()

# Prints the word that rhymes the most with Python.
print(response[0]['word'])
```
