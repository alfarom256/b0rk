from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

approved_number = ""
bork_string = "test"


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    resp_msg = check_message(message_body)
    
    resp = MessagingResponse()
    msg = resp.message(resp_msg[0])
    if resp_msg[1]:
        msg.media(resp_msg[1])

    return str(resp)

def check_message(message_body):
    if "Danny Deleto" in message_body:
        # Delete the server
        return ("BORK BORK BORK", "https://pics.me.me/bork-bork-bork-bork-bork-bork-19308709.png")
    else:
        return ("Thank you, you have just subscribed to cat facts", "")




if __name__ == '__main__':
    app.run()


