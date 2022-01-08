import discord
from discord.ext import commands  # extension
import asyncio
import random
from urllib.request import urlopen as uReq  # parse html text using the fn urlopen thats we renamed uReg
from bs4 import BeautifulSoup as soup  # grabs the page it self

client = commands.Bot(command_prefix='.')  # made an instance of the bot and set it to the client variable
client.remove_command('help')  # remove default help command
print("Pika Pika!")  # print in console


#  def is how you start a function
#  an event is a piece of code that runs when a specific activity as happened
#  commands are triggered when ordered to by a user. () are for giving a command an alias or to be hidden

@client.command(pass_context=True)  # new help command
async def help(ctx):
    # formats the help description so is looks nice neat and a bit colorful
    embed = discord.Embed(
        color=discord.Color.gold()  # makes the line on the side gold
    )

    # name is for the title font and value is the description font
    # inline doesnt really do anything as far as I know
    embed.add_field(name='Here\'s what I can do!', value='It\'s not much but I\'m working hard '
                                                         'on some new moves! :zap:', inline=False)
    embed.add_field(name='.fcset', value='Saves the  Friend Code you input (.fcset 4834-8572-7459)', inline=False)
    embed.add_field(name='.fcfind', value='Finds the  Friend Code of the person you mention (.fcfind @Squiglypuff)'
                    , inline=False)
    embed.add_field(name='.fcremove', value='Removes the  Friend Code of the person you mention '
                                            'BUT you have to include the friendcode aswell '
                                            '(.fcremove @Squiglypuff 4834-8572-7459)', inline=False)
    embed.add_field(name='.t2 .t3 .t4', value='Will show all of the pictures in a twitter post depending on the '
                                              'number (if a tweet has 2 pictures use .t2 if it has 3 use .t3 etc.)',
                    inline=False)
    embed.add_field(name='memes', value='.lose .stupid .yessir .nosir .streets .getdown .ahhaha .opinion .yuna .guts .tekken', inline=False)

    await ctx.author.send(embed=embed)  # this will dm you the text above




@client.command()  # set fc
async def fcset(ctx, *, friendcode):
    discordname = ctx.message.author.id
    file = open("friendcodes.txt", "a")  # a is for "appending" aka adding text to the document
    # writes users @ and fc
    file.write(f'<@{discordname}> ')
    file.write(f'{friendcode}\n')
    file.close()  # closes the opened txt file
    await ctx.send(f'<@{discordname}> your Friend Code has been set to {friendcode}')  # this lets the bot speak

#kelly request to show all fc at once
@client.command()  # set fc for names
async def fcall(ctx):
    searchfile = open("friendcodes.txt", "r")
    ayee = searchfile.readlines()
    searchfile.close()
    await ctx.author.send(ayee)

async def fctwo(ctx):
    with open('friendcodes.txt', 'r') as f:
        for line in f:
            await ctx.author.send(line)
            if 'str' in line:
                break


@client.command() #finds friendcodes
async def fcfind(ctx, member):
    searchfile = open("friendcodes.txt", "r")
    member = member.replace('!', '')  # this allows people that have nicknames on discord to be found, by replacing
    # the ! discord puts in your id with nothing thus deleting the ! (thanks alex!)
    print(member)
    for line in searchfile:
        if f'{member}' in line:
            print(member)
            print(line)
            await ctx.send(f"Here you go -> {line}")
    searchfile.close()


# with is an efficient way of opening a file so it can be used,
# setting the open object to a variable (in this case "f"), and closing the file
@client.command()  # remove fc's
async def fcremove(ctx, member, fc):  # discord @ and friend code are required attributes <- right word? idk
    with open("friendcodes.txt", "r") as f:
        lines = f.readlines()  # This method returns a list containing the lines
        # to test if its working
        print(lines)
        print(member)
        print(fc)
    with open("friendcodes.txt", "w") as f:  # opens the text file again to delete text
        for line in lines:
            if line.strip(" \n") != f'{member} {fc}':  # deletes @ if its found and deletes
                f.write(line)  # write all the other fc's
        await ctx.send(f"poof! it's gone!")


@client.command(aliases=['HI'])
async def hi(ctx):
    await ctx.send(f'Pika Pika! <:Snickerchu:514893587549257754>')  # just says pika pika w/ and emote


# memes
@client.command(aliases=['LOSE'])
async def lose(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/480466956869304332/628328001825669180'
                   f'/I_know_what_its_like_to_lose.mp4')


@client.command(aliases=['STUPID'])
async def stupid(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/479126398158766083/628331679701925948'
                   f'/Stupid_im_not_even_gonna_let_you_get_the_chance.mp4')


@client.command(aliases=['YESSIR'])
async def yessir(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/479126398158766083/628331825001005059/Yessir.mp4')


@client.command(aliases=['NOSIR'])
async def nosir(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/479126398158766083/628331878138511391/No_sir_not_me.mp4')


@client.command(aliases=['STREETS'])
async def streets(ctx):
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/607723747264430124/640618945052672050/She_belongs_to_the_streets_Future_meme-EUawJYBttjk.mp4')


@client.command(aliases=['GETDOWN'])
async def getdown(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/479120975468822528/628336591831826452/GET_DOWN_ON_IT.mp4')


@client.command(aliases=['ahaha','AHAHA','AHHAHA'])
async def ahhaha(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/479120975468822528/628340848626630697/ahaha.mp4')


@client.command(aliases=['OPINION'])
async def opinion(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/477579950430617650/638521981746151425/opinion.mp4')


@client.command(aliases=['YUNA'])
async def yuna(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/477579950430617650/638522856019591218/yuna_sin.mp4')

@client.command(aliases=['GUTS'])
async def guts(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/477579950430617650/643121404484517898/guts.mp4')

@client.command(aliases=['TEKKEN'])
async def tekken(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/200791838356013057/650176961741717514/tekken_combo.mp4')

@client.command(aliases=['Padoru'])
async def padoru(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/477579950430617650/659135802491666434/Padoru_Padoru_Original.mp4')

@client.command(aliases=['PADORUPADORU'])
async def PADORU(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/477579950430617650/659135817582903341/padoru_padoru_BOOSTED.mp4')

@client.command(aliases=['ALRIGHT'])
async def alright(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/478432170889838593/661063658201153537/video-1577680126.mp4')

@client.command(aliases=['BET'])
async def bet(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/477579950430617650/661257716823490563/Bet.mp4')

@client.command(aliases=['HEY'])
async def hey(ctx):  # ctx is context and its passed in automatic
    await ctx.send(
        f'https://cdn.discordapp.com/attachments/607723747264430124/678657854520950844/hey.mp4')
#  ^^memes ^^



@client.command()
async def ping(ctx):  # ctx is context and its passed in automatic
    await ctx.send(f'Pika Pika! {round(client.latency * 1000)}ms')  # *1000 to get miliseconds


@client.command(aliases=['t2','T2'])
async def twitter2(ctx, my_url):
    await ctx.send(f'I\'ve got 1 picture on the way!')
    # opening up connection, grabbing the page
    uClient = uReq(my_url)
    # reads whats in the url and saves it to a variable
    page_html = uClient.read()
    # closes client
    uClient.close()
    # html pareses page_html and sets it to page_soup
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "AdaptiveMedia-photoContainer js-adaptive-photo"})
    await ctx.send(containers[1].img["src"])


@client.command(aliases=['t3','T3'])
async def twitter3(ctx, my_url):
    await ctx.send(f'I\'ve got 2 pictures on the way!')
    # opening up connection, grabbing the page
    uClient = uReq(my_url)
    # reads whats in the url and saves it to a variable
    page_html = uClient.read()
    # closes client
    uClient.close()
    # html pareses page_html and sets it to page_soup
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "AdaptiveMedia-photoContainer js-adaptive-photo"})
    await ctx.send(containers[1].img["src"])
    await ctx.send(containers[2].img["src"])


@client.command(aliases=['t4','T4'])
async def twitter4(ctx, my_url):
    await ctx.send(f'I\'ve got 3 more pictures on the way!')
    # opening up connection, grabbing the page
    uClient = uReq(my_url)
    # reads whats in the url and saves it to a variable
    page_html = uClient.read()
    # closes client
    uClient.close()
    # html pareses page_html and sets it to page_soup
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "AdaptiveMedia-photoContainer js-adaptive-photo"})
    await ctx.send(containers[1].img["src"])
    await ctx.send(containers[2].img["src"])
    await ctx.send(containers[3].img["src"])


'''
# aliases is for alt names for the _8ball command
@client.command(aliases=['8ball', 'heypika'])
# you cant have var names start  with a number
async def _8ball(ctx, *, question):  # * allows you to take multiple arguments as one arguments. .i.e a sentence
    #  , help spilt of responses
    responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.',
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
'''

client.run('NjA3NzE0NzI0MTkyMTkwNDY3.XUdosQ.8WHA5NxnXLm_RB35zXwVDrbQj4I')  # this connects your code to your bot
