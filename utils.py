from twilio.twiml.messaging_response import MessagingResponse, Message
import requests


api_keys = {
    'metal': '15f0e892-4f6f-4e5e-be3d-e8847e3c9a8d'
}


def get_random_metal_band_info():
    url = 'http://em.wemakesites.net/band/random'
    params = { 'api_key': api_keys['metal'] }

    api_response = requests.get(url, params).json()
    name = api_response['data']['band_name']
    genre = api_response['data']['details']['genre']
    country = api_response['data']['details']['country of origin']
    photo = api_response['data']['photo']

    response = MessagingResponse()
    message = Message()
    message.body('Check out this {} band from {} named {}!'
                 .format(genre, country, name))
    message.media(photo)
    response.append(message)

    return response
