![A man from the movie Silent Night, Deadly Night 2 shouts "Garbage Day!"](https://c.tenor.com/G6pkG9_0Um0AAAAC/garbage-day.gif "GARBAGE DAY!")
# garbageday_sms
A Twilio SMS Flask app that keeps my neighbors (but mostly myself) from forgetting who's week it is to take out the garbage!

Extensively documenting this project to serve as a beginner-friendly template for developing and deploying a cloud-run Twilio app.

 
## If you are one of my neighbors:
1. Just text the web app number and you'll get a response back telling you if it is your trash week or not!
2. If this is helpful, let the bot know you care! Text "Good bot!"
 
 
## To create a quick and dirty dev environment:
1. Create a Twilio account and a phone number setup for sms
2. Clone this repo
3. In your IDE, set your debug environment to change directories to the folder you are running python scripts in
4. Download [ngrok](https://ngrok.com)
    - Create an ngrok account, and add your authentication to the ngrok application
    - From your terminal, run ngrok http 8080
5. Edit your Twilio number's webhook to point to the ngrok link with sms:  https://xxxx.ngrok.io/sms
 
 
## To Run the Server locally:
1. Rename gd_config_sample.json to **gd_config.json** and populate your neighbors' information.
2. Run **gd_sms_bot.py**
3. Text the number you set up with Twilio (w/ngrok as a webhook)
 
 
## To Deploy to Google Cloud Run:
1. Create a Cloud project
2. Submit a build
3. Deploy the build
4. Edit your Twilio number's webhook to point to the Google Cloud app url with /sms:  https://xxxx.a.run.app/sms
5. Text the number you set up with Twilio