from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import garbageday_calc as gbc

app = Flask("GarbageDaySMS")

@app.route("/sms", methods =["POST"])
def sms():
    print(str(request))
    number = request.form['From']
    #message_body = request.form['Body']
    # replyText = getReply(message_body)
    trash_stats = gbc.find_trash_person(number)
    print(trash_stats)

    #TWIML
    resp = MessagingResponse()
  
    if trash_stats["sender_trash_person_status"]:
        resp.message('Congratulations {}, you live in Apt {}, so it is your trash week!'.format(number, trash_stats["week_of_month"]))
    else:
        resp.message('Congratulations {}, it\'s the sucker in Apt {}\'s trash week!'.format(number, trash_stats["week_of_month"]))
    return str(resp)

if __name__ == "__main__":
    app.run()