from nextcord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()


bot = commands.Bot(command_prefix='!')


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))
