from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json

# CONDITIONS
API = "https://api.openweathermap.org/data/2.5/weather?q=Netanya,IL&appid=6228f7541bf40756eb2b5cfaa4e6f45f"


app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if "weather" in incoming_msg:
        temp = Get_weather()
        msg.body(temp)
        responded = True
    if "quote" in incoming_msg:
        # return a quote
        r = requests.get("https://api.quotable.io/random")
        if r.status_code == 200:
            data = r.json()
            quote = "{0} {1}".format(data["content"], data["author"])
        else:
            quote = "I could not retrieve a quote at this time, sorry."
        msg.body(quote)
        responded = True
    if "cat" in incoming_msg:
        # return a cat pic
        msg.media("https://cataas.com/cat")
        responded = True
    if not responded:
        msg.body("Text Me Something else Please")
    return str(resp)


def Get_weather():
    weather = requests.get(API)
    weather1 = json.loads(weather.content)
    tempature = int((weather1["main"]["temp_max"]) - 273.13)
    wind_speed = float(weather1["wind"]["speed"])
    weater_quote = "The tempature is {0} and the wind speed is {1} Km/h".format(
        tempature, wind_speed
    )
    return weater_quote


if __name__ == "__main__":
    app.run()
