import discord
from discord.ext import commands
import os
import random
import asyncio
import config

#keep_alive: formato para mantener al bot activo 24/7 mediante un ping generado cada 5 min
from keep_alive import keep_alive

#Prefijo de comando de discord.ext
bot = commands.Bot(command_prefix="nya>")


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


#on_ready: Cuando el bot esté activo y funcional mandará un mensaje confirmando que está corriendo.
@bot.event
async def on_ready():
    print('Nos hemos conectado como {0.user}'.format(bot))

#Busca todos los cogs y los carga al iniciar
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

#Creación de un estado que cambia cada 10 segundos
@bot.event
async def random_pr():
    await bot.wait_until_ready()
    statuses = [f'nya>help | v{config.VERSION}', f'moderar en {len(bot.guilds)} servidores', 'Discord.py']
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity = discord.Game(name=status))
        await asyncio.sleep(10)
bot.loop.create_task(random_pr())

hola = ["hola", "buenas", "wenas", "hello"]
adios = ["adiós", "adios", "bye", "chao"]
#@bot.event
async def on_message(msg):
  if any(word in msg.content.lower() for word in hola):
   await msg.add_reaction("👋")
  if any(word in msg.content.lower() for word in adios):
    await msg.add_reaction("🖐️")
  await bot.process_commands(msg)

#Sección de mantenimiento 24/7 encendido e iniciado del bot
keep_alive()
bot.run(os.getenv('Token'))
