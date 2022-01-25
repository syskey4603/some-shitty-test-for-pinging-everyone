import discord
from discord.ext import commands

spammessage = ""
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(pass_context=True)
async def devtest(ctx):
	while True:
		global spammessage
		for user in ctx.guild.members:
			spammessage = spammessage + "<@" + str(user.id) + ">"
		await ctx.send(spammessage)
		spammessage = ""


@bot.command()
async def imbored(ctx):
	await ctx.send(ctx.message.author.name + ", did i ask")

bot.run(ez)
