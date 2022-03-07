import discord
import random
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('My prefix is .'))
    print("bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("hi")

@client.command()
async def modbeg(ctx):
    await ctx.send("Stop begging for mod chris!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)} ms')

#moderation
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member: discord.Member, *, reason= "no reason provided"):
    await ctx.send(member.name +" has been kicked: " +reason)
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member: discord.Member, *, reason= "no reason provided"):
    await ctx.send(member.name +" has been banned: " +reason)
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member:discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False, speak=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f"{member.mention} was muted.")
        await member.send(f"You have been muted from {guild.name}")
    else:
        await member.add_roles(role)
        await ctx.send(f"{member.mention} was muted.")
        await member.send(f"You have been muted from {guild.name}")

@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name= "Muted")
    await member.remove_roles(mutedRole)
    await ctx.send(f"{member.mention} was unmuted")

#fun
@client.command(aliases=['cf'])
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command(aliases=['rn'])
async def randomnumber(ctx):
    choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", '11', "12", "13", "14", "15", '16', '17', '18', '19', '20', '21', '22', '23', '24', '25','26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
    rannum = random.choice(choices)
    await ctx.send(rannum)

@client.command(aliases=['td'])
async def truthordare(ctx):
        rantord =["Truth: Do you hate Trump?",
                "Dare: Give chris mod.", 
                "Dare: Do a face revel.", 
                "Truth: Do you like this server?", 
                "Truth: What is your favorite song?",
                "Dare: Apply for mod in the server.",
                "Truth: Are you planning on marrying your partner?",
                "Dare: Send the 6th to last photo in your camera roll.",
                "Truth: Would you marry your partner that you are currently dating?",
                "Dare: Get a pet snake.",
                "Truth: What's your favorite color?",
                "Dare: Ask your 1st @ on a date.",
                "Truth: Whats your dream job?",
                "Dare: Subscribe to NWW116 on YouTube :)",
                "Truth: Favorite server you are a member of?",
                "Dare: Ask your 2nd @ out on a date."]
        rantd = random.choice(rantord)
        await ctx.send(rantd)

client.run("TOKEN")
