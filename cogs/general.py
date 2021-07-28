import discord, platform
import config
from discord.ext import commands
from datetime import datetime
from psutil import Process
from os import getpid
import pkg_resources
import time

def lines_of_code():
    """
    I did not write this code.
    This code was taken off of a tag in discord.gg/dpy owned by Dutchy#6127
    I don't know if this is licensed
    but alas
    :return:
    """
    import pathlib
    p = pathlib.Path('./')
    cm = cr = fn = cl = ls = fc = 0
    for f in p.rglob('*.py'):
        if str(f).startswith("venv"):
            continue
        fc += 1
        with f.open() as of:
            for l in of.readlines():
                l = l.strip()
                if l.startswith('class'):
                    cl += 1
                if l.startswith('def'):
                    fn += 1
                if l.startswith('async def'):
                    cr += 1
                if '#' in l:
                    cm += 1
                ls += 1
    return {
        "comments": cm,
        "coroutine": cr,
        "functions": fn,
        "classes": cl,
        "lines": ls,
        "files": fc
    }

lines = lines_of_code()

class general(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 10, commands.BucketType.user)}):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  #Comando de test/ping
  @commands.command(name="ping")
  async def ping(self, ctx: commands.Context):
        """
        ¡Pong!
        """
        pings = []
        #number = 0
        typings = time.monotonic()
        await ctx.trigger_typing()
        typinge = time.monotonic()
        typingms = round((typinge - typings) * 1000)
        pings.append(typingms)
        latencyms = round(self.bot.latency * 1000)
        pings.append(latencyms)
        # discords = time.monotonic()
        # url = "https://discordapp.com/"
        # async with self.bot.session.get(url) as resp:
        #     if resp.status is 200:
        #         discorde = time.monotonic()
        #         discordms = round((discorde-discords)*1000)
        #         pings.append(discordms)
        #         discordms = f"{discordms}ms"
        #     else:
        #         discordms = "Failed"
        # for ms in pings:
        #     number += ms
        # average = round(number / len(pings))
        await ctx.send(f"__**Ping Times:**__\nTyping: `{typingms}ms`  |  Latency: `{latencyms}ms`")
        # embed = discord.Embed(
        #   title="🏓 Pong",
        #     description=(f'<a:dscrd_typing:862837114240237599> Escribiendo: **{typingms}ms**\n <a:dscrd_loading:866731675547336721> Ping: **{latencyms}ms**\n <a:clyde:846625894395412480> Discord: **{discordms}ms**\n Promedio: {average}'),
        #     color=0xfbf9fa
        #     #timestamp=datetime.utcnow()
        # )
        # embed.set_thumbnail(url="https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png?width=465&height=473")
        # await ctx.send(embed=embed)
  
  @commands.command(name="git")
  async def git(self, ctx: commands.Context):
        """
        Código fuente de SatanyaBot
        """
        await ctx.send("Puedes revisar mi código fuente en https://github.com/KuroCat56/SatanyaBot")
  
  @commands.command(name="invite")
  async def invite(self, ctx: commands.Context):
      """
      Links de invitación de SatanyaBot y al server
      """
      embed = discord.Embed(
          title="¿Quieres agregarme a tu servidor o unirte al mío?",
          description="Enlaces útiles de invitación",
          color=0xfbf9fa,
      )
      embed.add_field(
          name="<:join:847940361937879051> Link de server",
          value="[「SatanyaBot」](https://discord.gg/bqcdKxuW3X)",
          inline=True
      )
      embed.add_field(
          name="<:join:847940361937879051> Link SatanyaBot",
          value="[Invítame](https://discord.com/oauth2/authorize?client_id=805589802484760577&scope=bot&permissions=641723511)",
          inline=True
      )
      embed.add_field(
          name="<a:cutestars:846625824538886214> Donaciones",
          value="[Ko-fi](https://ko-fi.com/kurocat56)",
          inline=False
      )
      embed.add_field(
          name="<:wumpus_star:846611108784504872> Califícame en top.gg",
          value="[Próximamente](https://top.gg/)",
          inline=False
      )
      embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png?width=1024&height=290"
      )
      await ctx.send("Te he enviado mis enlaces de invitación <:SatanyaBot:858480664143331338>")
      await ctx.author.send(embed=embed)
  
  @commands.command(name="info", aliases=["botinfo", "about"])
  async def info(self, context):
        """
        Información útil (y no tan útil) del bot.
        """
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime = (f"{days}d, {hours}h, {minutes}m, {seconds}s")
        
        embed = discord.Embed(
        title="¡Hola, soy SatanyaBot!",
        description="Gracias por dejarme estar en tu servidor. Soy la primer bot de Discord *opensource* en español desarrollada en Python. Recuerda que si quieres ver mis comandos usa **nya>help**",
        color=0xfbf9fa,
        timestamp=datetime.utcnow()
        )
        embed.set_author(
        name=f"SatanyaBot | v{config.VERSION}",
        icon_url = "https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png?width=465&height=473")
        
        embed.add_field(
        name="Creador y Colaboradores:",
        value="[KuroCat#4816](https://linktr.ee/KuroCat56)",
        inline=False
        )
        embed.add_field(
        name="Mi versión de Python:",
        value=f"{platform.python_version()}",
        inline=True
        )
        embed.add_field(
        name="Encendida desde hace:",
        value=f"{uptime}",
        inline=True
        )
        embed.add_field(
        name="Uso de memoria actual:",
        value=f"{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB",
        inline=True
        )
        embed.add_field(
        name="Prefijo:",
        value=f"{config.PREFIX}",
        inline=True
        )
        embed.add_field(
        name= "# Comandos:",
        value=f"{len([x.name for x in self.bot.commands])}",
        inline=True
        )
        embed.add_field(
        name= "# Líneas:",
        value=f"{lines.get('lines'):,}",
        inline=True
        )
        embed.add_field(
        name= "# Servers:",
        value=f"{len(self.bot.guilds)}",
        inline=True
        )
        # statistics - Extraído de https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/stats.py#L216-L263
        total_members = 0
        #total_unique = len(self.bot.users)

        text = 0
        voice = 0
        guilds = 0
        for guild in self.bot.guilds:
            guilds += 1
            if guild.unavailable:
                continue

            total_members += guild.member_count
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    text += 1
                elif isinstance(channel, discord.VoiceChannel):
                    voice += 1

        embed.add_field(name='# Miembros', value=f'{total_members} totales', inline=True)
        embed.add_field(name='# Canales', value=f'{text + voice} totales', inline=True)
        embed.add_field(
        name= "Cumpleaños 🍰",
        value="31/01/2021 | 09:50 AM",
        inline=False
        )
        embed.add_field(
        name= "Donaciones <a:cutestars:846625824538886214>",
        value="[Ko-fi](https://ko-fi.com/kurocat56)",
        inline=True
        ) 
        embed.add_field(
        name= "Top.gg <:wumpus_star:846611108784504872>",
        value="[Próximamente](https://top.gg/)",
        inline=True
        )
        embed.add_field(
        name="Enlaces",
        value="[Github](https://github.com/KuroCat56/SatanyaBot) **|** [Servidor de Soporte](https://discord.gg/bqcdKxuW3X) **|** [Invítame](https://discord.com/oauth2/authorize?client_id=805589802484760577&scope=bot&permissions=641723511)",
        inline=False
        )
        version = pkg_resources.get_distribution('discord.py').version
        embed.set_footer(
        text=f"Desarrollada en discord.py v{version}",
        icon_url='http://i.imgur.com/5BFecvA.png'
        )
        embed.set_image(url="https://media.discordapp.net/attachments/829223734559637545/859608410537459752/bannerSatanyaBot_Logotipo4x.png?width=1024&height=290"
        )
        await context.send(embed=embed)

  @commands.command(aliases=['si', 'server']) #Extraído de https://github.com/cree-py/RemixBot/blob/master/cogs/info.py
  async def serverinfo(self, ctx):
        '''Información básica del servidor.'''
        guild = ctx.guild
        guild_age = (ctx.message.created_at - guild.created_at).days
        created_at = f"Servidor creado {guild.created_at.strftime('%b %d %Y │ %H:%M')}.\n¡Eso fue hace {guild_age} días!"

        em = discord.Embed(description=created_at, color=0xfbf9fa)
        em.add_field(name='Owner', value=guild.owner, inline=False)
        em.add_field(name='Miembros', value=len(guild.members), inline=False)
        em.add_field(name='Roles', value=len(guild.roles))
        em.add_field(name='<:dscrd_channel:851449868722896936> Canales de texto', value=len(guild.text_channels))
        em.add_field(name='<:dscrd_voice:862873567204212776> Canales de voz', value=len(guild.voice_channels))


        em.set_thumbnail(url=None or guild.icon_url)
        em.set_author(name=guild.name, icon_url=None or guild.icon_url)
        await ctx.send(embed=em)

  @commands.command(name="opensource", aliases=["open"])
  async def opensource(self, ctx):
    embed = discord.Embed(
        title="SatanyaBot apoya el open source y tú también deberías",
        description="Soy una bot open source así que todo mi desarrollo está sostenido gracias al apoyo de otros desarrolladores y demás proyectos open source.",
        color=0xfbf9fa,
        timestamp=datetime.utcnow()
      )
    embed.set_author(
        name=f"SatanyaBot | v{config.VERSION}",
        icon_url = "https://media.discordapp.net/attachments/829223734559637545/859941157944557588/headAsset_214x-8.png?width=465&height=473",
      )
    embed.add_field(
        name="Enlaces",
        value="[Github](https://github.com/KuroCat56/SatanyaBot) **|** [Servidor de Soporte](https://discord.gg/bqcdKxuW3X) **|** [Invítame](https://discord.com/oauth2/authorize?client_id=805589802484760577&scope=bot&permissions=641723511)",
        inline=False
        )
    embed.set_footer(
        text=f"Solicitado por {ctx.message.author}"
        )
    await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(general(bot))