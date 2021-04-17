import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import os
#allows us to cycle through a list
from itertools import cycle
import requests
import json
import random

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
objEmoji = [
    '<:flower:817984275332071444>',
    '<:crescent:818679835835891732>',
    '<:spacebottle:818680206797701131>',
    '<:planet:818680114283675649>',
    '<:cherryblossom:818679923597377566>'
    ]
actEmoji = [
    '<:backhug:818679634739986443>',
    '<:cats:818679736125227008>',
    '<:chill:818680046847393822>',
    '<:cuddle:818679562690494524>',
    '<:withu:818679987858178058>',
    '<:hug:817984488754642944>',
    '<:cutebear:817992591563685999>',
    '<:bearlove:817992135084605450>'
    ]
#neural network will replace most of this hardcode

#private variables for use, move to .env if making code public
zenquotes_apiLink = #zenquotes api link
botName = #bot name
 

item_images = [
    "https://i.postimg.cc/J07ysb3Q/cityalley.png",
    "https://i.postimg.cc/nrsJSrnJ/classroom.png",
    "https://i.postimg.cc/9fWj5Jc1/croissant.png",
    "https://i.postimg.cc/Jn0Vt0Dk/itachi.png",
    "https://i.postimg.cc/85Y8vGMn/magicalsky.png",
    "https://i.postimg.cc/TYgwTNXX/mcdonalds.png",
    "https://i.postimg.cc/667qm5jq/mountainroad.png",
    "https://i.postimg.cc/T15zqsc2/mysticalsky.png",
    "https://i.postimg.cc/LhdryVyt/nap.png",
    "https://i.postimg.cc/pLvdrQ25/nightcity.png",
    "https://i.postimg.cc/WpQzLLCn/nightisland.png",
    "https://i.postimg.cc/mgSgHcDX/nightpyramids.png",
    "https://i.postimg.cc/d0ttmqZq/overgrowncity.png",
    "https://i.postimg.cc/CKPMcWbb/pinksky.png",
    "https://i.postimg.cc/Kz1GwJ5w/redsky.png",
    "https://i.postimg.cc/435smjWr/relax.png",
    "https://i.postimg.cc/bwfhLqM7/shower.png",
    "https://i.postimg.cc/RVHmcWP1/siblings.png",
    "https://i.postimg.cc/0QyxmZ3r/templenight.png",
    "https://i.postimg.cc/5yZMhJtF/tokyosubs.png",
    "https://i.postimg.cc/G3Nr8Fjh/waterfall.png",
    "https://i.postimg.cc/85XGbMQ4/windowclassroom.png"
    ]

agrees = ["me too"]
thank_statements = [
    "Thanksss" + random.choice(actEmoji), 
    "Thank you! uwu", 
    "Thank u sm"  + random.choice(actEmoji)
    ]
coin = [
    "Heads <:cutebear:817992591563685999>", 
    "Tails <:cutebear:817992591563685999>"
    ]
starter_encouragements = [
    "It's okay :/",
    "You're a great person!" + random.choice(actEmoji),
    "Keep pushing through!",
    "It's okay, you're strong, you can make it through" + random.choice(actEmoji),
    "Don't worry... i'm sure things will get better" + random.choice(actEmoji),
    "I beleive in you" + random.choice(actEmoji)
    ]
sleep = ["goodnight, Kaede", "Goodnight, Kaede", "goodnightt, Kaede"]
sleepBot = ["goodnight" + random.choice(actEmoji), "Goodnight" + random.choice(actEmoji), "goodnightt"]
greets = [
    "Hey!" + random.choice(actEmoji), 
    "Hello!", 
    "Hiii", 
    "Heyy" + random.choice(actEmoji), 
    "Hai!" + random.choice(actEmoji)
    ]
sad_words = ["i'm sad", "i'm depressed", "i'm unhappy", "i'm angry", "i'm miserable", "i'm upset"]
userGreets = ["#hello", "#hey", "#hi"]

def get_quote(self):
        response = requests.get(zenquotes_apiLink)
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return(quote)


class socFunc(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def inspire(self, ctx):
        quote = get_quote(self)
        await ctx.send("<:flower:817984275332071444> Here's some inspiration <:flower:817984275332071444>")
        await ctx.send(quote)
    
    @commands.command()
    async def thank(self, ctx, user):
        await ctx.send(f'{random.choice(thank_statements)} {user}')

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send("The coinflip is:\n" + random.choice(coin))

    @commands.command()
    async def encourage(self, ctx, user = ''):
        await ctx.send(f'{random.choice(starter_encouragements)} {user}')

    @commands.command()
    async def pc98(self, ctx):
        embed = discord.Embed(color = discord.Color.blue())
        #Sends an embedded image, using the url
        embed.set_image(url = random.choice(item_images))
        await ctx.send(embed = embed)


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        msg = message.content.lower()

        if msg.startswith(botName):
            await message.channel.send("Yes??")


        if any(word in msg for word in userGreets):
            if message.author.id == 407943427616145409:
                await message.channel.send('Creator <:flower:817984275332071444> ' + random.choice(greets))
            else:
                await message.channel.send(random.choice(greets))

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(starter_encouragements))
        
        if any(word in msg for word in agrees):
            await message.channel.send("ikr")

        if any(word in msg for word in sleep):
            await message.channel.send(random.choice(sleepBot) + self.ctx.author.mention)

        if botName in message.content.lower():
            await message.add_reaction(random.choice(objEmoji))

        #overwriting on_message stops commands from being processes, this line fixes that
        #await self.client.process_commands(message)


#setup function to connect cog to bot, initializes by passing in instance of the class
def setup(client):
    client.add_cog(socFunc(client))
