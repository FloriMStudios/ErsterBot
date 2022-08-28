import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
         print("ich bin jetzt online")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("test"):
        await message.channel.send("Bestanden")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1011317225904410655)
    embed = discord.Embed(title=":wave: | Willkommen auf diesem Server.", description= f"Herzlich willkommen, {member.mention}.")
    embed.add_field(name="Wir freuen uns, dich zu sehen.", value=f"Wir sind jetzt {len(set(bot.users))}")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1010253273959256186/1010678361028317264/unknown.png")
    await channel.send(embed=embed)


bot.run("MTAxMDk2NzQ3MTEzNTY1ODA2Nw.GvlFaZ.EnDXQg69KYKjMDDfT7_brPTayV-6dJQbBgASlc")
