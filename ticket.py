import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ticket(ctx):
    guild = ctx.guild
    ticket_name = f"ticket-{ctx.author.name}"
    existing_channel = discord.utils.get(guild.channels, name=ticket_name)

    if not existing_channel:
        # Create a new channel with the ticket_name
        category = discord.utils.get(guild.categories, name='Tickets')
        if not category:
            category = await guild.create_category(name='Tickets')
        await guild.create_text_channel(ticket_name, category=category)

        # Get the newly created channel
        new_channel = discord.utils.get(guild.channels, name=ticket_name)

        # Add permissions to the channel
        await new_channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
        await new_channel.set_permissions(guild.default_role, read_messages=False)
        await new_channel.set_permissions(client.user, read_messages=True, send_messages=True)

        # Send a message to the new channel
        await new_channel.send(f"{ctx.author.mention}, thank you for contacting support. A staff member will be with you shortly.")

    else:
        await ctx.send(f"{ctx.author.mention}, you already have a ticket open.")

client.run('YOUR_BOT_TOKEN')
