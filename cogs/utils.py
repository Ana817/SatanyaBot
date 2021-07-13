import discord
from discord.ext import commands
import asyncio
import inspect

class utils(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 3, commands.BucketType.user)}):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  async def say_permissions(self, ctx, member, channel):
        permissions = channel.permissions_for(member)
        e = discord.Embed(colour=member.colour)
        avatar = member.avatar_url_as(static_format='png')
        e.set_author(name=str(member), url=avatar)
        allowed, denied = [], []
        for name, value in permissions:
            name = name.replace('_', ' ').replace('guild', 'server').title()
            if value:
                allowed.append(name)
            else:
                denied.append(name)

        e.add_field(name='Allowed', value='\n'.join(allowed))
        e.add_field(name='Denied', value='\n'.join(denied))
        await ctx.send(embed=e)

  @commands.command()
  async def remind(self, ctx, time, *, task):
    """
    (BETA)Intentaré recordarte cualquier cosa que necesites.
    """
    def convert(time):
      pos = ['s', 'm', 'h', 'd']

      time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

      unit = time[-1]

      if unit not in pos:
        return -1
      try:
        val = int(time[:-1])
      except:
        return -2
      
      return val * time_dict[unit]
    converted_time = convert(time)

    if converted_time == -1:
      await ctx.send("Comando inválido")
      return
    if converted_time == -2:
      await ctx.send("Debes de especificar usando enteros")
      return

    await ctx.send(f"⏱️ {ctx.author.mention}, tu recordatorio para **{task}** fue activado y serás recordado en **{time}**")

    await asyncio.sleep(converted_time)
    await ctx.send(f"⏰ {ctx.author.mention}, tu recordatorio por **{task}** ha terminado.")

  @commands.command(name="commands")
  async def _commands(self, ctx):
    """
    ¿Quieres saber cuántos comandos tengo en mi código?
    """
    value=len([x.name for x in self.bot.commands]) #Variable extraída de AlexFlipnote/discord_bot.py/blob/master/cogs/info.py
    await ctx.send(f"¿Mis comandos? Actualmente tengo **{value}** comandos en mi código fuente. Utiliza `nya>help` para mandarte la lista de comandos que puedes utilizar. (´ ω `♡)")

  @commands.command(name="prefix")
  async def prefix(self, ctx):
    """
    Tengo varios prefijos, prueba a usar el que más te guste.
    """
    await ctx.send("Actualmente mis prefijos son `nya>`, `nya `, `>>` y `@SatanyaBot` ♪└( ＾ω＾ )」")

  @commands.command()
  async def jumbo(self, ctx, emoji: discord.PartialEmoji):
    """
    Deja te paso ese emoji para que lo veas mejor.
    """
    emoji = emoji.url
    await ctx.send(emoji)

  @commands.command()
  async def poll(self, ctx, *args):
    """
    Crea una mini encuesta para lo que gustes
    """
    poll_title = " ".join(args)
    embed = discord.Embed(
        title=f"📊 {poll_title}",
        color=0xfbf9fa,
    )
    embed.set_footer(text=f"Encuesta por: {ctx.message.author} - ¡Reacciona para votar!")
    embed_message = await ctx.send(embed=embed)
    await ctx.message.delete()
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")
    await embed_message.add_reaction("🤷")

  @commands.command() #Extraído de https://github.com/cree-py/RemixBot/blob/master/cogs/utility.py
  async def source(self, ctx, command):
      '''Get the source code for any command.'''
      source = inspect.getsource(self.bot.get_command(command).callback)
      if not source:
        return await ctx.send(f'{command} is not a valid command.')
      try:
        await ctx.send(f'```py\n{source}\n```')
      except:
        await ctx.send("El bloque de código es demasiado largo como para enviarlo. Será mejor que uses `nya>git` para buscar el apartado por tu cuenta. <:doki_hmm:846549184807043133>")

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def botpermissions(self, ctx, *, channel: discord.TextChannel = None):
        """Shows the bot's permissions in a specific channel.
        If no channel is given then it uses the current one.
        This is a good way of checking if the bot has the permissions needed
        to execute the commands it wants to execute.
        To execute this command you must have Manage Roles permission.
        You cannot use this in private messages.
        """
        channel = channel or ctx.channel
        member = ctx.guild.me
        await self.say_permissions(ctx, member, channel)

  @commands.command()
  @commands.guild_only()
  async def permissions(self, ctx, member: discord.Member = None, channel: discord.TextChannel = None):
        """Shows a member's permissions in a specific channel.
        If no channel is given then it uses the current one.
        You cannot use this in private messages. If no member is given then
        the info returned will be yours.
        """
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author

        await self.say_permissions(ctx, member, channel)

def setup(bot: commands.Bot):
    bot.add_cog(utils(bot))