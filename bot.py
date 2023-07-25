import discord
import responses
import constants
import QuoteBot    

quoteBot = QuoteBot.QuoteBot()
# Send messages
async def send_message(user, message, user_message, is_private):
    try:
        # response = responses.handle_response(user_message)
        # await message.author.send(response) if is_private else await message.channel.send(response)
        response = quoteBot.handle_message(user, user_message)
        await message.channel.send(response) 

    except Exception as e:
        print(e)

def run_discord_bot():
    intents = discord.Intents.all()
    intents.message_content = True
    TOKEN = constants.TOKEN
    # client = discord.Client(intents=discord.Intents.default())
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        user = username
        await send_message(user, message, user_message, is_private=False)

    client.run(TOKEN)