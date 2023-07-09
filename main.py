#!/usr/bin/env python3
# ------------------------------------------------
#
#                REQUEST BOT
#               (c) Pau Gasull
#                 09/07/2023
#
# ------------------------------------------------

# --INCLUDES-- #
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import os


# --CONSTANTS-- #
BOT_TOKEN = 'ODUzMzUxODIxNTA5Nzg3NjU4.G8BiIC.U7SqT-AX0lz1rZuynaVgk3ZjJPOy7AlPm8NVGo'
intents = discord.Intents.default()
intents.message_content = True
BOT = discord.Bot(intents=intents)


# -- COMMANDS -- #
@BOT.slash_command(name = "request", description = "create a new request")
async def request(ctx, req: Option(str, "Your request")):
    if ctx.author == BOT.user:
        return

    embed = discord.Embed(
        title=req,
        description="requested by: " + ctx.author.display_name,
        color=0x008000)
    await ctx.respond(embed=embed)

    channel = BOT.get_channel(int(ctx.channel.id))
    message = await channel.fetch_message(
        channel.last_message_id)

    for reaction in ["<:RCB_reaction_upvote:853547686665125898>", "<:RCB_reaction_downvote:853547768001462272>"]:
        await message.add_reaction(emoji=reaction)


# --MAIN -- #
@BOT.event
async def on_ready():
    print(f"{BOT.user} is ready and online!")


BOT.run(BOT_TOKEN)
