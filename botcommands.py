import os

from discord.ext import commands
from dotenv import load_dotenv

from dbQueries import insert_in_db, search_in_db
from googleApi import GoogleSearch

load_dotenv()
# To extract DISCORD_TOKEN from .env file which is used to access the discord bot.
discord_bot_token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

# !google keyword functionality
@bot.command(name='google', help='Performs Google Search and returns top 5 links.')
async def google_search_top_five(ctx, *args):
    keyword = ' '.join(args)
    username = str(ctx.author)
    print("#google->", keyword, username)
    gs = GoogleSearch(keyword)
    result = gs.Gsearch()
    insert_in_db(username, keyword)
    if not result:
        await ctx.send("I didn't find any result for " + keyword + ".")
    else:
        await ctx.send(result)


# !recent keyword functionality
@bot.command(name='recent', help='Returns searches performed by a user.')
async def display_recent(ctx, keyword):
    username = str(ctx.author)
    print("#recent->", keyword, username)
    result = search_in_db(username, keyword)
    if not result:
        await ctx.send("I didn't find " + keyword + " in my history.")
    else:
        await ctx.send(result)


# Function to reply hey to your hi. ( Edge case is on line 40)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'hi':
        print("#hi->", message, message.author)
        response = "hey"
        await message.channel.send(response)
    await bot.process_commands(message)


print("Starting bot.")
bot.run(discord_bot_token)
