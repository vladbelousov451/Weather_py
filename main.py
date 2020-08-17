import requests
import json
from twilio.rest import Client


API_KEY = "6228f7541bf40756eb2b5cfaa4e6f45f"
API = "https://api.openweathermap.org/data/2.5/weather?q=Netanya,IL&appid=6228f7541bf40756eb2b5cfaa4e6f45f"
response = requests.get(API)


weather_repo = int((json.loads(response.content)["main"]["temp_max"]) - 273.13)
wind_speed = float(json.loads(response.content)["wind"]["speed"])

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number = "whatsapp:+14155238886"
# from_whatsapp_number = "whatsapp:+972535303588"
# replace this number with your own WhatsApp Messaging number
numbers = ["whatsapp:+972535303588", "whatsapp:+972547245344"]


if weather_repo < 18:
    weather_body = "*weather* for today in Netanya is : {0} Degrees  Wear something hot and The wind Speed is {1} Km\h".format(
        weather_repo, wind_speed
    )

else:
    weather_body = "*The* Weather For today In Netanya is : {0} Degrees Wear Gufiya and The wind Speed is {1} Km\h".format(
        weather_repo, wind_speed
    )
for number in numbers:
    client.messages.create(body=weather_body, from_=from_whatsapp_number, to=number)
