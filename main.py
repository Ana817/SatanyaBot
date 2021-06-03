import discord
from discord.ext import commands
from datetime import datetime
import os
import random
import asyncio
import config
from dotenv import load_dotenv
from psutil import Process
from os import getpid

#Prefijo de comando de discord.ext
bot = commands.Bot(command_prefix="nya>")
bot.launch_time = datetime.utcnow()

@bot.command()
@commands.is_owner()
async def load(cog, extension):
  bot.load_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def unload(cog, extension):
  bot.unload_extension(f"cogs.{extension}")

@bot.command()
@commands.is_owner()
async def reload(cog, extension):
  bot.reload_extension(f"cogs.{extension}")

#Busca todos los cogs y los carga al iniciar
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

@bot.command()
@commands.is_owner()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    uptime = (f"{days}d, {hours}h, {minutes}m, {seconds}s")
    await ctx.send(f"Fuí encencida hace: **{uptime}**")

@bot.command()
@commands.is_owner()
async def memory(ctx):
  await ctx.send(f'Estoy usando **{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB** en mi servidor.')

mention = ["satanya", "satanyabot"]
@bot.event
async def on_message(msg):
  if msg.author.bot:
    return
  if any(word in msg.content.lower() for word in mention):
   nya="<:SatanyaBot:832392370472484875>"
   await msg.add_reaction(nya)
  await bot.process_commands(msg)

#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@bot.event
async def on_ready():
    print('Nos hemos conectado como {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name=f'nya>help | v{config.VERSION} 🔲'))

class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)

bot.help_command = MyNewHelp()
load_dotenv()
bot.run(os.getenv('Token'))
