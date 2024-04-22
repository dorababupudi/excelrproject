# Import necessary modules
import random  # for generating random sensor readings
import asyncio  # for asynchronous operations
from rules import rules  # import sensor rules
from telegram_bot_class import Telegram_Module  # import Telegram bot class
from global_variables import api_token, group_chat_id  # import API token and group chat ID
import sys

# Create an instance of Telegram_Module with API token and group chat ID
telegram = Telegram_Module(api_token, group_chat_id)

# Function to check if CO2 level violates rules
def is_co2_violated(co2):
    # CO2 rules definition
    co2_ll = rules['co2']['LL']  # CO2 Lower Limit
    co2_ul = rules['co2']['UL']  # CO2 Upper Limit
    # Check if CO2 reading is outside the defined rule limits
    return co2 < co2_ll or co2 > co2_ul

# Function to check if temperature level violates rules
def is_temp_violated(temp):
    # Temperature rules definition
    temp_ll = rules['temp']['LL']  # Temperature Lower Limit
    temp_ul = rules['temp']['UL']  # Temperature Upper Limit
    # Check if temperature reading is outside the defined rule limits
    return temp < temp_ll or temp > temp_ul

# Function to check if humidity level violates rules
def is_humidity_violated(humidity):
    # Humidity rules definition
    hum_ll = rules['humdty']['LL']  # Humidity Lower Limit
    hum_ul = rules['humdty']['UL']  # Humidity Upper Limit
    # Check if humidity reading is outside the defined rule limits
    return humidity < hum_ll or humidity > hum_ul

# Asynchronous function to continuously monitor sensor readings
async def monitor_sensors():
    while True:
        # Simulate sensor readings
        co2 = round(random.uniform(0, 5000), 2)  # CO2 reading in PPM
        temp = round(random.uniform(15, 50), 2)  # Temperature reading in °C
        humidity = round(random.uniform(60, 100), 2)  # Humidity reading in %
        
        # Print sensor readings to console
        print(f'CO2: {co2} PPM, Temp: {temp} °C, Humidity: {humidity}%')
        
        # Check if any sensor values violate rules and send alerts if necessary
        if is_co2_violated(co2):
            message = f'CO2 Alert! CO2 value is {co2} PPM'
            await telegram.send_test_message(message)
        
        if is_temp_violated(temp):
            message = f'Temperature Alert! Temperature is {temp} °C'
            await telegram.send_test_message(message)
        
        if is_humidity_violated(humidity):
            message = f'Humidity Alert! Humidity is {humidity}%'
            await telegram.send_test_message(message)
        
        # Prompt user to continue or exit monitoring
        break_yes = input('Please select Y or N(Y/N)>')
        
        if break_yes == 'Y':
            print("Thank you")
        break


# Main entry point of the program
if __name__ == '__main__':
    asyncio.run(monitor_sensors())  # Run the monitor_sensors function asynchronously
