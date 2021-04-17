import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import requests
import json
import random

#private variables for use, move to .env file if releasing public
tenorKey = #tenor key
tenorLink = #tenor link


def get_gif(self, search):
    apikey = tenorkey
    lmt = 12
    #search
    search_term = f"anime {search}"

    # get the top <lmt> GIFs for the search term
    r = requests.get(tenorLink % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        gifs = json.loads(r.content)
        gif_url = gifs['results'][random.randint(0,lmt - 1)]['url']
        print (gif_url)
        return gif_url
    else:
        gifs = None

class gifFunc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pet(self, ctx, user):
        gif = get_gif(self, "pet")
        #embed attempt
        #em = discord.Embed(color = discord.Color.from_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        #em.set_image(url = f'{gif}')
        await ctx.send(f"{ctx.message.author.mention} pet {user}")
        await ctx.send(gif)

    @commands.command()
    async def stab(self, ctx, user):
        gif = get_gif(self, "stab")
        await ctx.send(f"{ctx.message.author.mention} stabbed {user}")
        await ctx.send(gif)

    @commands.command()
    async def kiss(self, ctx, user):
        gif = get_gif(self, "kiss")
        await ctx.send(f"{ctx.message.author.mention} kissed {user}")
        await ctx.send(gif)

    @commands.command()
    async def hug(self, ctx, user):
        gif = get_gif(self, "hug")
        await ctx.send(f"{ctx.message.author.mention} hugged {user}")
        await ctx.send(gif)

    @commands.command()
    async def cuddle(self, ctx, user):
        gif = get_gif(self, "cuddle")
        await ctx.send(f"{ctx.message.author.mention} cuddled {user}")
        await ctx.send(gif)

    @commands.command()
    async def slap(self, ctx, user):
        gif = get_gif(self, "slap")
        await ctx.send(f"{ctx.message.author.mention} slapped {user}")
        await ctx.send(gif)

    @commands.command()
    async def punch(self, ctx, user):
        gif = get_gif(self, "punch")
        await ctx.send(f"{ctx.message.author.mention} hit {user}")
        await ctx.send(gif)
    
def setup(client):
    client.add_cog(gifFunc(client))