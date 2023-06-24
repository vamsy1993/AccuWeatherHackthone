#This file contains the main class WeatherFeature which is used to fetch the weather data for a given city.
import requests
import sys
import datetime


class WeatherFeature:
    API_KEY = "0qFugncSNESeK5KSPutHZhOi0g3XXuFy"

    def __init__(self, City):
        # Constructor for the main class
        self.City = City

    def fetch_locationID(self):
        # Function to fetch the location ID for the city
        BASE_URL = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey="
        URL = BASE_URL + self.API_KEY + "&q=" + self.City + "&language=en-us&details=false"

        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            location_id = data[0]["Key"]
            return location_id
        except requests.exceptions.RequestException as e:
            print("Error occurred while fetching location ID:", e)
            sys.exit(1)
        except (KeyError, IndexError) as e:
            print("Invalid response received while fetching location ID:", e)
            sys.exit(1)

    def fetch_weather(self):
        # Function to fetch the current weather for the city
        location_id = self.fetch_locationID()
        BASE_URL = "http://dataservice.accuweather.com/currentconditions/v1/"
        URL = BASE_URL + location_id + "?apikey=" + self.API_KEY + "&language=en-us&details=false"

        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            weather_text = data[0]["WeatherText"]
            weather_icon = data[0]["WeatherIcon"]
            temp = data[0]["Temperature"]["Metric"]["Value"]
            temp_unit = data[0]["Temperature"]["Metric"]["Unit"]
            print("Location: " + self.City)
            print("Weather Text: " + weather_text)
            print("Weather Icon: " + str(weather_icon))
            print("Temperature: " + str(temp) + " " + temp_unit)
            print("Local Time: " + str(datetime.datetime.now().strftime("%H:%M:%S")))
            print("Local Date: " + str(datetime.datetime.now().strftime("%Y-%m-%d")))
        except requests.exceptions.RequestException as e:
            print("Error occurred while fetching weather data:", e)
            sys.exit(1)
        except (KeyError, IndexError) as e:
            print("Invalid response received while fetching weather data:", e)
            sys.exit(1)

    def fetch_forecast(self):
        # Function to fetch the 5-day forecast for the city
        location_id = self.fetch_locationID()
        BASE_URL = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"
        URL = BASE_URL + location_id + "?apikey=" + self.API_KEY + "&language=en-us&details=false&metric=true"

        try:
            response = requests.get(URL)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error occurred while fetching forecast data:", e)
            sys.exit(1)
        except (KeyError, IndexError) as e:
            print("Invalid response received while fetching forecast data:", e)
            sys.exit(1)

