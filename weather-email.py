"""
This program calls on weather API to access data, formats the data, and then sends the data to an email when the program is run

Malachi Ashley
4/2/2021
"""
import requests , json
import smtplib , ssl

#get_city = str(input("Input a zipcode or city name to find the current weather of that area: "))

api_key = "caecea5b70654d1baa4161300212203"

url = "http://api.weatherapi.com/v1/forecast.json?key=caecea5b70654d1baa4161300212203&q=06459&days=1&aqi=no&alerts=no"

response = requests.get(url)

data = response.json()
name = data['location']['name']
state = data['location']['region']
current_temp = data['current']["temp_f"]
condition = data['forecast']["forecastday"]["day"]["condition"]["text"]
max_temp = data['forecast']["forecastday"]["day"]["maxtemp_f"]
min_tmep = data['forecast']["forecastday"]["day"]["mintemp_f"]
chance_of_rain = data['forecast']["forecastday"]["day"]["daily_will_it_rain"]


def compose_message():
    if max_temp>=40:
        "Subject: Weather for Today \n\n Good Morning Gentlemen! The weather for today in " + name + ", " + state + " is " + str(temp) + " degrees Farenheit"+ " and " \
    + condition.lower() + " and feels like " + str(feels_like) + " degrees Farenheit. \n\n This message is sent from Python"
    elif max_temp>=60:
        "Subject: Weather for Today \n\n The weather in " + name + ", " + state + " is " + str(temp) + " degrees Farenheit"+ " and " \
    + condition.lower() + " and feels like " + str(feels_like) + " degrees Farenheit. \n\n This message is sent from Python"
    elif max_temp>=70:
        "Subject: Weather for Today \n\n The weather in " + name + ", " + state + " is " + str(temp) + " degrees Farenheit"+ " and " \
    + condition.lower() + " and feels like " + str(feels_like) + " degrees Farenheit. \n\n This message is sent from Python"
    else: 
        "Subject: Weather for Today \n\n The weather in " + name + ", " + state + " is " + str(temp) + " degrees Farenheit"+ " and " \
    + condition.lower() + " and feels like " + str(feels_like) + " degrees Farenheit. \n\n This message is sent from Python"


message = "Subject: Weather for Today \n\n The weather in " + name + ", " + state + " is " + str(temp) + " degrees Farenheit"+ " and " \
    + condition.lower() + " and feels like " + str(feels_like) + " degrees Farenheit. \n\n This message is sent from Python"

elif response.status_code == 400:
    print("Sorry, no matching location is found.")


sender_email = "weather_email123@gmail.com"
receiver_email = "malachimda101@gmail.com"


port_for_ssl = 465
email_password = "weather_email!23"
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port_for_ssl, context=context) as server:
    server.login("weatheremail123@gmail.com", email_password)
    server.sendmail(sender_email, receiver_email, message)