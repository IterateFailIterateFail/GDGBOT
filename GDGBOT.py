import random
import asyncio
from discord.ext.commands import Bot
import discord

BOT_PREFIX = ( "!")
TOKEN = "NDU0OTgzNzUxMjY5ODc1NzI1.Df1Y4g.83TyQMZFb-4rirJFIGlCIkJZy1A"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def tak():
	possible= [
        "https://cdn.discordapp.com/attachments/403729769264447489/425608941993721856/d7d.gif",
        "https://cdn.discordapp.com/attachments/403729769264447489/454970786436874261/thanks.gif",
        "https://cdn.discordapp.com/attachments/403729769264447489/454971073960869906/unknown.png",
        "https://cdn.discordapp.com/attachments/403729769264447489/454972828165472287/2bwxwz.gif",
        "https://cdn.discordapp.com/attachments/403729769264447489/454973186472411166/fruit-tree-branch-repair.png",
		"https://cdn.discordapp.com/attachments/323767712192921602/454969475859611649/TAK-logo.png",
    ]
	await client.say(random.choice(possible))

@client.command()	
async def gdg():
	possible= [
        "https://cdn.discordapp.com/attachments/403729769264447489/425608941993721856/d7d.gif",
        "Welp",
        "...No",
        "Yes",
		"No",
		"*points to left*",
		"You're not wrong",
		"*giggles*",
		"*laughs*",
		"...",
		"https://cdn.discordapp.com/attachments/403729769264447489/425608403193167872/flamer.gif",
		"*grind*",
		"*sigh*",
		"...Yes",
		"https://cdn.discordapp.com/attachments/403729769264447489/425608364580405248/3a6.gif",
		"https://cdn.discordapp.com/attachments/403729769264447489/425608419886628864/070.gif",
		"https://cdn.discordapp.com/attachments/403729769264447489/425608430145765376/544.gif",
		"https://cdn.discordapp.com/attachments/403729769264447489/425608677383471124/exterminatus.gif",
		"https://cdn.discordapp.com/attachments/403729769264447489/425608297974988800/248.gif",
		"chaos?",
		"can we anarchy now?",
		"FOR THE MAN-EMPEROR OF MANKIND!"
    ]
	await client.say(random.choice(possible))

@client.command(pass_context = True)	
async def exterminatus(ctx):
	await client.say("I have arrived, and it is now that I perform my charge. In fealty to the God-Emperor and by the grace of the Golden Throne, I declare Exterminatus upon the server of " + ctx.message.server.name +". I hereby sign the death warrant of an entire server and consign a million souls to oblivion. May Imperial Justice account in all balance. The Emperor Protects.")
	await client.say ("https://cdn.discordapp.com/attachments/403729769264447489/455013422149533706/Exterminatus_of_Matar.gif")
@client.command(pass_context = True)	
async def blam(ctx, user: discord.Member = None):
	special = ["107043526050619392","454983751269875725"] #mien and bot's id
	if user == None:
		await client.say ("WHO DO I SHOOT?!?!?")
	elif user.id in special:
		await client.say("HERSEY! You can't shoot " + user.mention +" a memeber of the Commisariat " + ctx.message.author.mention +"! *BLAM*")
	else:
		await client.say ("On the most serious charge of hersey, I find " + user.mention +" guilty. The sentence shall now be carried out. *BLAM*")
	
@client.command()
async def fire():
	await client.say("https://cdn.discordapp.com/attachments/403729769264447489/455014553261178884/2bx4hf.gif")


@client.command()
async def stop():
	await client.logout()

@client.command()
async def americans():
	await client.say("https://www.youtube.com/watch?v=bBHNsc5EL1Q")

@client.command()
async def english():
	await client.say("https://www.youtube.com/watch?v=a0x6vIAtFcI&feature=youtu.be&t=12s")

@client.command(pass_context = True)	
async def repeat(ctx,msg : discord.message =  None):
	if msg == None:
		await client.say ("No message to repeat")
	else :
		await client.say(ctx.message)
	
	
	
client.run(TOKEN)