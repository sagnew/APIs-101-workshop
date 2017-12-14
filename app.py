from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.twiml.voice_response import VoiceResponse, Dial
from flask import Flask, request

import utils


app = Flask(__name__)
api_keywords = {
    'metal': utils.get_random_metal_band_info()
}


@app.route('/sms', methods=['POST'])
def sms_reply():
    message_body = request.form['Body'].lower()

    if message_body in api_keywords:
        response = api_keywords[message_body]()
    else:
        response = MessagingResponse()
        message = Message()

        message.body('Thanks for joining my demo! Questions? @Sagnewshreds or Sagnew@Twilio.com')
        response.append(message)

    return str(response)


@app.route('/voice', methods=['POST'])
def voice_reply():
    response = VoiceResponse()
    dial = Dial()

    dial.conference('NYU')
    response.append(dial)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
