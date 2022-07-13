from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import garbageday_calc as gbc
import os

app = Flask("GarbageDaySMS")

# Always point your Twilio webhook to /sms
@app.route("/sms", methods =["POST"])
def sms():
    
    # Collect crucial sms request information to evaluate
    print(str(request))
    number = request.form['From']
    message_body = request.form['Body']

    # Generate response values
    trash_stats = gbc.find_trash_person(number)
    print(trash_stats)

    # Create a response using TWIML
    resp = MessagingResponse()
    
    # Generate a response based on if the requester is a tenant and it's their trash week, else tell them to pound sand
    # but if they message a compliment, say something nice back.
    if 'good bot' in message_body.lower():
        resp.message('Thanks! I\'m trying my best.')
    elif trash_stats['requester_is_tenant'] and trash_stats["requester_trash_person_status"]:
        resp.message('Congratulations {}, you live in Apt {}, so it is your trash week!'.format(trash_stats["requester_name"], trash_stats["week_of_month"]))
    elif trash_stats['requester_is_tenant'] and not trash_stats["requester_trash_person_status"]:
        resp.message('Congratulations {}, it\'s the sucker in Apt {}\'s trash week!'.format(trash_stats["requester_name"], trash_stats["week_of_month"]))
    elif not trash_stats['requester_is_tenant']:
        resp.message('Unfortunately {}, you do not live in a supported building, but we wish you luck on your trash endevours!'.format(number))
    else: resp.message('Unfortunately {}, I don\'t know what to tell you!'.format(number))
    
    # Reponse to Twilio API
    return str(resp)

# Flask main app
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))