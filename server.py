import discord
from discord_slash import SlashCommand

client = discord.Client(intents=discord.Intents.all())
# Declares slash commands through the client.
slash = SlashCommand(client, sync_commands=True, auto_delete=True)

guild_ids = [817333076530954261]

@client.event
async def on_ready():
    print("Bot online.")


@slash.slash(name="ping")
async def ping(ctx):  # Defines a new "context" (ctx) command called "ping."
    await ctx.respond()
    await ctx.send(f"Pong! ({client.latency*1000}ms)")


@slash.slash(name="createacc", guild_ids=guild_ids)
async def createacc(ctx):  # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Account creating")

#clear


@slash.slash(name="clear")
@slash.has_permissions(administrator=True)
async def clear(self, ctx, amount):
    try:
        amount = int(amount)
    except:
        print('test')
        amount = 0

    await ctx.channel.purge(limit=amount+1)
    message = await ctx.send(f'***{str(amount)} messages are deleted***')
    await message.delete(delay=2.5)

client.run("ODE3MzMyNzM4OTM5MDI3NDY3.YEH-bg.hf-dGslNc_9_bOWwPp4RB6zhnJo")
