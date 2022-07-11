# garbageday_sms
A Twilio sms flask app that keeps my neighbors from forgetting who's week it is to take out the garbage.

If you are one of my neighbors, just text the web app number and you'll get a response back telling you if it is your trash week or not!


Quick and dirty dev environment:
1. Create a Twilio account and phone number
2. Clone this repo
3. Set your debug to change directories to the folder you are running python scripts in
4. Download [ngrok](https://ngrok.com), add your authentication
5. From your terminal, run ngrok http 5000
5. Point your Twilio number's webhook to the ngrok link

To Run the Server:
1. Populate your neighbors in **gd_config.json**
2. Run **gd_sms_bot.py**
3. Text the number from one of the phone numbers in the config json
