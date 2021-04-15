import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import os
#allows us to cycle through a list
from itertools import cycle
import requests
import json
import random

commandsList = """
Here's a list of the current commands I know:
#cmds
#help
#inspire
#ping
#coinflip
#thank <user>
#encourage <user>
#clear <msg_num>
#kick <user> <reason>
#ban <user> <reason>
#unban <user>
#load
#unload
#reload
#play <youtube music url>
#pause
#resume
#stop
#leave
It's not much atm but hopefully Creator will teach me more!!
"""

async def version_hist():
    with open("versions.json", "r") as f:
        versions = json.load(f)
    return versions


class modFunc(commands.Cog):
    #allows us to connect to the client by passing in client as argument
    def __init__(self, client):
        self.client = client

    
    #The equivalent to @client.event for cogs
    #must pass in self as the first parameter of every function in the class
    #@commands.Cog.listener
    #The equivalent to @client.command() for cogs
    
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await ctx.send("kicked " + member + reason)
        await member.kick(reason = reason)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await ctx.send(f"banned {member} {reason}")
        await member.ban(reason = reason)

    @commands.command()
    async def unban(self, ctx, *, member):
        #list of banned users in the guild
        banned_users = await ctx.guild.bans()
        #splits the member name from the discriminator
        member_name, member_discriminator = member.split('#')

        #cycles through banned entries until it finds a match, then unbans
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.member_discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'My latency is: {round(self.client.latency * 1000)} ms')

    @commands.command()
    async def cmds(self, ctx):
        await ctx.send(commandsList)

    @commands.command()
    @commands.has_permissions(manage_messages = True) #checks if they have manage messages permission. can put mulitple permission check arguments
    async def clear(self, ctx, amount = 20):
        await ctx.channel.purge(limit = amount)

    #Dives into embed function
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def user(self, ctx, member: discord.Member):
        embed = discord.Embed(title = member.name, description = member.mention, color = discord.Color.from_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        #Can add as many fields as I want
        embed.add_field(name = "ID:", value = member.id, inline = True)
        #adds thumbnail to the top right
        #member.avatar_url pulls the url of the user's pfp
        embed.set_thumbnail(url = member.avatar_url)
        #sets footer
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

        await ctx.send(embed= embed)

    #Adding Patch notes
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def version(self, ctx, version, *, description = "light patchwork"):
        #use semantic versioning: MAJOR.MINOR.PATCH
        versions = await version_hist()

        if str(version) in versions:
            await ctx.send("You've already labeled this update!!")
            return
        else:
            versions[str(version)] = {}
            versions[str(version)]["description"] = description

        with open("versions.json", "w") as f:
            json.dump(versions,f)
        
        await ctx.send(f"The {version} update was logged for me, thanks Cozy!!")




#setup function to connect cog to bot, initializes by passing in instance of the class
def setup(client):
    client.add_cog(modFunc(client))
