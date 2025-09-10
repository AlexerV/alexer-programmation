# Discord.py

## Installation
Installer la bibliothèque :
```bash
pip install discord.py
```

Vérifier :
```bash
pip show discord.py
```

---

## Exemple minimal de bot
```python
import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot connecté en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "ping":
        await message.channel.send("pong 🏓")

client.run("TON_TOKEN_ICI")
```

---

## Les événements principaux
Les événements principaux
- `on_ready` : quand le bot est prêt
- `on_message` : quand un message est envoyé
- `on_member_join` : quand un membre rejoint
- `on_member_remove` : quand un membre quitte

---

## Commandes avec commands.Bot
Il est recommandé d’utiliser le système de commandes intégré :
```python
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot prêt : {bot.user}")

@bot.command()
async def salut(ctx):
    await ctx.send("Salut 👋 !")

bot.run("TON_TOKEN_ICI")
```

---

## Embeds (messages stylisés)
```python
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Infos Bot", description="Un bot fait avec discord.py", color=0x00ff00)
    embed.add_field(name="Auteur", value="Alexer", inline=True)
    await ctx.send(embed=embed)
```

---

## Gestion des erreurs
```python
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Erreur : {str(error)}")
```

---

## Résumé
Avec discord.py, tu peux :
- Répondre à des messages
- Créer des commandes personnalisées
- Gérer des événements Discord
- Utiliser des embeds pour rendre les messages plus jolis
