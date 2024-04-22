from telegram import Bot
import asyncio

class Telegram_Module:
    '''
    Steps to create Bot

    1. Import the Bot class from telegram module.
    2. create an instance of the Telegram bot by passing to the 
       Bot constructor method the API ID which you have created in telegram.
    3. Using this BOT instance call the send_test_message function and invoke it
       with the Telegram Group chat ID. The group has already been created by you.
    '''
    def __init__(self, api_token, group_chat_id):
        self.bot_token = api_token
        self.group_chat_id = group_chat_id

    async def send_test_message(self, message):
        # Create an instance of the Telegram Bot class
        bot = Bot(token=self.bot_token)
        await bot.send_message(chat_id=self.group_chat_id, text=message)

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_TOKEN' with your actual API token
    api_token = '7163302206:AAFAREbTltSUyita-qMkSctBOHCWhnoWmDw'

    # Replace 'YOUR_GROUP_CHAT_ID' with the ID of your Telegram group chat
    group_chat_id = '5031516354'

    # Create an instance of the Telegram_Module class
    telegram = Telegram_Module(api_token, group_chat_id)

    # Replace 'Your test message' with the message you want to send
    test_message = "Your test message"

    # Send the test message
    asyncio.run(telegram.send_test_message(test_message))
