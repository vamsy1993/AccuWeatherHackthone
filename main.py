import argparse
import weatherfeature
import productfeature


class MainClass:
    def __init__(self):
        self.cities = []

    def run(self):
        while True:
            # Get user input for the city
            city = input("Enter a city name (or 'exit' to quit): ")

            if city.lower() == "exit":
                break

            # Add the city to the list
            self.cities.append(city)

            try:
                # Fetch weather for the city
                weather = weatherfeature.WeatherFeature(city)
                weather.fetch_weather()
                
                # Fetch forecast for the city
                forecast = productfeature.ProductFeature().fetch_result_forecast(city)
                print(forecast)
                
            except Exception as e:
                print("An error occurred while fetching data for", city)
                print("Error:", e)

        # Process the collected cities
        if self.cities:
            # Print the collected cities
            print("Collected cities:")
            for city in self.cities:
                print(city)
        else:
            print("No cities collected.")


if __name__ == "__main__":
    # Create an instance of the main class
    main_instance = MainClass()

    # Call the run method of the main instance
    main_instance.run()
