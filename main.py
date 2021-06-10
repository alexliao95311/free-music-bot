import discord
from discord.ext import commands
from keep_alive import keep_alive
import os
client = commands.Bot(command_prefix = "$")
client.remove_command('help')

p = '' #prefix
owner = '' #owner (you)
name = '' #name of bot

my_secret = os.environ['token']


@client.event
async def on_ready():
    print('bot online')
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = f'some jazzy tunes! | {p}help'))
    client.load_extension('cogs.music')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('I don\'t have permissions to do that. Please make sure you use the correct invite link and give me the required permissions')
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        await ctx.send(f'Something went wrong. Please have the owner of this bot ({owner}) DM the bot maker')
        await ctx.send(f"|| {error} ||")

@client.command()
async def help(ctx):
    embed = discord.Embed(title = f"{name} Help", description = f'My prefix is `{p}`', color = 0x0000FF)
    embed.add_field(name='Jazzy Commands', value=f'`{p}help` - shows this page\n\n`{p}play <song>` - plays music\n\n`{p}stop` - stops the music\n\n`{p}pause` - pauses the music\n\n`{p}resume` - resumes the music\n\n`{p}join` - joins the VC\n\n`{p}leave` - leaves the VC')
    embed.set_footer(text=f'Made by {owner}')
    await ctx.send(embed=embed)

keep_alive()
client.run(my_secret)


