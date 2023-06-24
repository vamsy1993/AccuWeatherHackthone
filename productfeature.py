# Description: This file contains the ProductFeature class which is used to fetch the 5-day forecast for a city and filter the results to include only cloudy forecasts.
import weatherfeature
import pandas as pd

class ProductFeature:

    # Create a function for converting JSON to a dataframe
    @staticmethod
    def json_to_dataframe(json_data):
        # Convert JSON to dataframe
        try:
            df = pd.DataFrame(json_data)
            return df
        except Exception as e:
            print("Error converting JSON to dataframe:", str(e))
            return None

    

    @staticmethod
    def fetch_result_forecast(city):
        # Fetch the 5-day forecast for the city
        try:
            forecast_data = weatherfeature.WeatherFeature(city).fetch_forecast()

            forecast_list = []
            for i in range(5):
                date = forecast_data["DailyForecasts"][i]["Date"]
                min_temp = forecast_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
                max_temp = forecast_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
                day = forecast_data["DailyForecasts"][i]["Day"]["IconPhrase"]
                night = forecast_data["DailyForecasts"][i]["Night"]["IconPhrase"]

                forecast_list.append({
                    "Date": date,
                    "Minimum Temperature": min_temp,
                    "Maximum Temperature": max_temp,
                    "Day": day,
                    "Night": night
                })

            df = ProductFeature.json_to_dataframe(forecast_list)

            if df is not None:
                # Filter the dataframe to include only cloudy forecasts
                cloudy_df = df[df["Day"].str.contains("cloudy", case=False) | df["Night"].str.contains("cloudy", case=False)]

                if not cloudy_df.empty:
                    return cloudy_df
                else:
                    print("No cloudy weather forecast found.")
            else:
                print("Error fetching forecast data.")

        except Exception as e:
            print("An error occurred:", str(e))

        return None


