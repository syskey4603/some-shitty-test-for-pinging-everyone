import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(pass_context=True)
async def devtest(ctx):
	for user in ctx.guild.members:
		await ctx.send("<@" + str(user.id) + ">")

bot.run("OTMxODk2MDQxNTg5MDQ3MzU2.YeLF0g.jb72Cz7l1k0zJ836R2OfttG50RY")