from twilio.twiml.messaging_response import (Body, Media, Message,
                                             MessagingResponse)
import requests


# A dictionary for the API keys of various APIs you want to add.
api_keys = {
    'metal_api': '15f0e892-4f6f-4e5e-be3d-e8847e3c9a8d'
}

# A dictionary for the base URL of various APIs you want to add.
api_base_urls = {
    'metal_api': 'http://em.wemakesites.net'
}


# A function that returns an SMS response with info on a random band.
def get_random_band_info():
    url = '{}/band/random'.format(api_base_urls['metal_api'])
    params = { 'api_key': api_keys['metal_api'] }

    # Make the request to the metal API.
    # Convert the response JSON to a dictionary we can work with.
    response = requests.get(url, params).json()

    # Grab the relevant data from the JSON response.
    name = response['data']['band_name']
    photo = response['data']['photo']
    genre = response['data']['details']['genre']
    country = response['data']['details']['country of origin']

    # Create a TwiML response object for a Twilio SMS response.
    response = MessagingResponse()
    message = Message()

    # Write out the body of the text message.
    message.body('Check out this {} band from {} named {}'
                 .format(genre, country, name))

    # Add the band's photo to the message. This is just a URL to an image.
    message.media(photo)

    # Add our message object to the TwiML response and return the object.
    response.append(message)
    return response
