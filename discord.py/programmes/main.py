# bot.py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # important pour lire le contenu des messages
bot = commands.Bot(command_prefix="!", intents=intents)

# Quand le bot démarre
@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")

# Commande simple
@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Commande avec argument
@bot.command()
async def dire(ctx, *, message):
    await ctx.send(f"Tu as dit : {message}")

# Embed
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Infos Bot", description="Bot d'exemple avec discord.py", color=0x3498db)
    embed.add_field(name="Auteur", value="Alexer", inline=True)
    embed.set_footer(text="Cours discord.py")
    await ctx.send(embed=embed)

bot.run("TON_TOKEN_ICI")  # ⚠️ Remplace par ton vrai token
