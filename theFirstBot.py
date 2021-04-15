import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import os #allows file manipulation
from itertools import cycle #allows us to cycle through a list
import requests
import json
import random
import mysql.connector
from mysql.connector import Error
import youtube_dl

#connection to discord
client = commands.Bot(command_prefix ='#', intents = discord.Intents.all())
#removes help command to allow for custom
client.remove_command("help")

#cycles in order; status =cycle(['Minecraft', 'Stardew Valley', 'League of Legends', 'Roblox', 'Tiny Royale'])
#CONSTANTS
custEmoji = [
    '<:bearlove:817992135084605450>', 
    '<:cutebear:817992591563685999>',
    '<:flower:817984275332071444>',
    '<:check:817983160323014718>',
    '<:hug:817984488754642944>',
    '<:rupee:817983579849752586>',
    '<:withu:818679987858178058>',
    '<:crescent:818679835835891732>',
    '<:really:818680816552509460>',
    '<:spacebottle:818680206797701131>',
    '<:planet:818680114283675649>',
    '<:cuteghost:818679486576721950>',
    '<:bonk:818680348589555714>',
    '<:cuddle:818679562690494524>',
    '<:chill:818680046847393822>',
    '<:cherryblossom:818679923597377566>',
    '<:cats:818679736125227008>',
    '<:backhug:818679634739986443>',
    ]

random_statements = [
    'I wonder if @Cozy has eaten today...',
    "It was so pretty outside " + random.choice(custEmoji),
    "This game is hard :/",
    "I feel like i'm learning new things everyday and it's greattt " + random.choice(custEmoji),
    "I wonder what @Cozy's doing...",
    "Listening to Lofi makes me feel warm and fuzzy inside " + random.choice(custEmoji),
    ]
acts = [
    discord.Game('Minecraft'), 
    discord.Activity(type=discord.ActivityType.listening, name= 'Spotify'),
    discord.Activity(type=discord.ActivityType.watching, name= "'Attack on Titan' on CrunchyRoll"),
    discord.Game('Stardew valley'),
    discord.Activity(type=discord.ActivityType.listening, name= "'Lofi' on Spotify"),
    discord.Activity(type=discord.ActivityType.watching, name= "'Black Mirror' on Netflix"),
    discord.Game('Genshin Impact'),
    discord.Activity(type=discord.ActivityType.listening, name= "Soundcloud"),
    discord.Activity(type=discord.ActivityType.watching, name= "Disney+"),
    discord.Game('League of Legends'),
    discord.Activity(type=discord.ActivityType.listening, name= "Musi"),
    discord.Activity(type=discord.ActivityType.watching, name= "Hulu"),
    discord.Game('Roblox'),
    discord.Activity(type=discord.ActivityType.watching, name= "Cozy play Minecraft"),
    discord.Activity(type=discord.ActivityType.listening, name= "'Lofi' on Spotify"),
    discord.Game('Tiny Royale'),
    discord.Activity(type=discord.ActivityType.watching, name= "'Jujutsu Kaisen' on CrunchyRoll"),
    ]


#CONNECTS BOT
@client.event
async def on_ready():
    #await client.change_presence(status = discord.Status.idle, activity = discord.Game('Candy Crush'))
    #starts our task loop
    change_task.start()
    random_statement.start()
    print('{0.user} is now online.'.format(client))
    
@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Command Help", description = "A list of everything I know how to do!", color = ctx.author.color)
    em.add_field(name = "Moderation", value = "kick, ban, unban, ping, clear, user, version")
    em.add_field(name = "Social", value = "inspire, thank, coinflip, encourage, pc98, ran")
    em.add_field(name = "Music", value = "connect, disconnect, song, play, pause, stop, current, songlist, catalog")
    em.add_field(name = "Main", value = "l, u, r")

    await ctx.send(embed = em)
#Loading COGS, allows for the creation and inclusion/editing of functions without rerunning main file
#Removes the need for Kaede to go offline when updating functions
#creates load command
@client.command()
async def l(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded!')

#creates unload command
@client.command()
async def u(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded!')

#reload cog command, very useful when updating functions
@client.command()
async def r(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded!')

#loads all extensions in the /cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'Extensions loaded!')


#checks allow only people with certain permissions to use command
#can create a custom check function that can run before command runs, with any type of requirement, so whatever I say goes
#this can be useful if I have level restricted commands
#could also be useful for 'paid' commands

#COMMANDS @client.command()
#TASK LOOPS
#updates every random minute number between 10 and 30
@tasks.loop(minutes = random.randint(10,30))
async def change_task():
    await client.change_presence(activity= random.choice(acts))

#UNDER CONSTRUCTION
@tasks.loop(minutes= random.randint(15,35))
async def random_statement():
    for guild in client.guilds:
        if str(guild) == #guildName:
            for channel in guild.channels:
                if str(channel) == #mainChannelName:
                    await channel.send(random.choice(random_statements))


    
#adding encouraging statements
#Making a leveling system
#if releasing this bot, move this to .env file
client.run(#botToken)