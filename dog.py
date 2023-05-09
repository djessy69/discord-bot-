import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

# Command to respond with a random joke
@client.command()
async def joke(ctx):
    jokes = ['Why did the tomato turn red? Because it saw the salad dressing!',
             'Why did the scarecrow win an award? Because he was outstanding in his field!',
             'Why don’t scientists trust atoms? Because they make up everything!']
    await ctx.send(f'{ctx.author.mention}, {random.choice(jokes)}')

# Command to roll a dice
@client.command()
async def roll(ctx):
    number = random.randint(1, 6)
    await ctx.send(f'{ctx.author.mention}, you rolled a {number}!')

# Command to send a random cat picture
@client.command()
async def cat(ctx):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_url = response.json()[0]['url']
    await ctx.send(f'{ctx.author.mention}, here\'s your cat picture!')
    await ctx.send(cat_url)

# Command to send a random dog picture
@client.command()
async def dog(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_url = response.json()['message']
    await ctx.send(f'{ctx.author.mention}, here\'s your dog picture!')
    await ctx.send(dog_url)

# Command to respond with a random dad joke
@client.command()
async def dadjoke(ctx):
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke = response.json()['joke']
    await ctx.send(f'{ctx.author.mention}, {joke}')

client.run('YOUR_BOT_TOKEN')
