import discord
from discord.ext import commands

token = "PUT YOUR TOKEN HERE"

bot = commands.Bot(command_prefix = "!")

print('What would you like to stream?')
status = input(' > ')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://discord.gg/oklm'
    )
    print('Streaming: ' + status)
    await bot.change_presence(activity=stream)

bot.run(token, bot=False)    
