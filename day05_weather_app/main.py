# Entry point of the program.
# Handles user input and displays weather data repeatedly.

from weather import get_weather  # Import function from weather.py


def main():
    print("=== Weather App ===")

    while True:  # infinite loop until user chooses to exit
        city = input("\nEnter city name (or type 'exit' to quit): ")

        # If user wants to exit
        if city.lower() == "exit":
            print("👋 Thanks for using Weather App. Goodbye!")
            break

        # Fetch weather info
        result = get_weather(city)

        if "error" in result:
            print(f"❌ {result['error']}")
        else:
            print(f"\n🌍 City: {result['city']}")
            print(f"🌡️ Temperature: {result['temperature']}°C")
            print(f"💧 Humidity: {result['humidity']}%")
            print(f"☁️ Condition: {result['condition']}")


# Run main() only if file is executed directly
if __name__ == "__main__":
    main()
