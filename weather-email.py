"""
This program calls on weather API to access data, formats the data, and then sends the data to a list of email when the program is run
Malachi Ashley
4/2/2021
"""
import requests , json #imports requests and JSON modules
import smtplib , ssl #imports smtplib and ssl modules

api_key = "" #api key from weatherapi.com, removed for privacy

#full url to make calls from, q=06459 is for the city of Middletown,CT, API key removed
url = "http://api.weatherapi.com/v1/forecast.json?key=&q=06459&days=1&aqi=no&alerts=no"

#request data from the API using the requests module
response = requests.get(url)

#format the data in JSON format to access
data = response.json()
name = data['location']['name']
state = data['location']['region']
current_temp = data['current']["temp_f"]
condition = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
max_temp = data["forecast"]["forecastday"][0]["day"]["maxtemp_f"]
min_temp = data["forecast"]["forecastday"][0]["day"]["mintemp_f"]
chance_of_rain = data["forecast"]["forecastday"][0]["day"]["daily_will_it_rain"]

#the base weather message with all the requested information
weather_message = "Subject: Weather for Today" \
            +"\n\n Good Morning Gentlemen! \n\n The current weather for today in " + name + ", " + state + " is " + str(current_temp) + " degrees Farenheit"+ " with a high of "\
            + str(max_temp) + " and a low of " + str(min_temp) + ". We have " + condition.lower() + " skies above with a "  + str(chance_of_rain) + " percent chance of rain."

def compose_message():
    """
    returns a string with the base weather message and a specific message based off of the tempature and chance of rain
    """
    if max_temp<=40:
        return weather_message + " Sounds like its gonna be a cold one gents. Bundle up, put on your best layers and pray for warmer days ahead." \
            + "\n\n This message is sent from Python(and Malachi)"
    elif max_temp>=57 and max_temp<70 and chance_of_rain<30:
        return weather_message + " You smell that guys? That right there is a gorgeous day. Get on outside and lets go catch some yish." \
            + "\n\n This message is sent from Python(and Malachi)"
    elif max_temp>=70 and chance_of_rain<30:
         return weather_message + " Wow, if this isn't the best day ever. What beautiful weather we have in store for us!" \
            + " If you're not already at the beach, what are you doing with yourself? Like really think, cause you should be outside. Also we're yossin in like 0.2 seconds so get up." \
            + "\n\n This message is sent from Python(and Malachi)"
    else:
        return weather_message + " Unfortunatley not the best weather ahead of us today. One of those 'meh' days. " \
            + "\n\n This message is sent from Python(and Malachi)"

#throwaway email for sending the weather information
sender_email = "weather_email123@gmail.com"

#email list for people who want to receive a daily email with the weather information, empty for privacy
receiver_email_list = []

#necessary port for ssl
port_for_ssl = 465

email_password = "" #empty for privacy

#Creates a secure ssl context
context = ssl.create_default_context()

#login to emaiil server and then iterate over recipients in email list and send them the message
with smtplib.SMTP_SSL("smtp.gmail.com", port_for_ssl, context=context) as server:
    server.login("weatheremail123@gmail.com", email_password)
    for email in receiver_email_list:
        server.sendmail(sender_email, email, compose_message())