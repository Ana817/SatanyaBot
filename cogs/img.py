from discord.ext import commands
import discord
from asyncdagpi import Client, ImageFeatures
import os
from dotenv import load_dotenv
load_dotenv()

dagpi = Client(os.getenv('Dagpi'))

class img(commands.Cog, command_attrs={'cooldown': commands.Cooldown(1, 10, commands.BucketType.user)}):
  """Modificadores de imágenes"""
  
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(aliases=["av"])
  async def avatar(self, ctx, member: discord.Member=None):
    """
    Checa el perfil de un usuario.
    """
    if member is None:
      member = ctx.author
    avatar= str(member.avatar_url_as(static_format="png", size=1024))
    embed = discord.Embed(
      title= f"Foto de perfil de {member}",
    )
    embed.set_image(url=avatar)
    await ctx.reply(embed=embed)

  @commands.command()
  async def pixel(self, ctx, member: discord.Member=None):
    """
    Censura el perfil de otro, porque sí.
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_pxl = str(member.avatar_url_as(static_format="png", size=1024))
      img_pxl = await dagpi.image_process(ImageFeatures.pixel(), url_pxl)
      file_pxl = discord.File(fp=img_pxl.image,filename=f"pixel.{img_pxl.format}")
      await ctx.send(file=file_pxl)

  @commands.command()
  async def pet(self, ctx, member: discord.Member=None):
    """
    Hazle un patpat a un miembro.
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_ptpt = str(member.avatar_url_as(static_format="png", size=1024))
      img_ptpt = await dagpi.image_process(ImageFeatures.petpet(), url_ptpt)
      file_ptpt = discord.File(fp=img_ptpt.image,filename=f"pet.{img_ptpt.format}")
      await ctx.send(file=file_ptpt)
  
  @commands.command(aliases=["trigger"])
  async def triggered(self, ctx, member: discord.Member=None):
    """
    T R I G G E R E D
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_trgg = str(member.avatar_url_as(static_format="png", size=1024))
      img_trgg = await dagpi.image_process(ImageFeatures.triggered(), url_trgg)
      file_trgg = discord.File(fp=img_trgg.image,filename=f"triggered.{img_trgg.format}")
      await ctx.send(file=file_trgg)

  # @commands.command()
  # async def ussr(self, ctx, member: discord.Member):
  #   """
  #   USSR
  #   """
  #   async with ctx.typing():
  #     url_ussr = str(member.avatar_url_as(static_format="png", size=1024))
  #     img_ussr = await dagpi.image_process(ImageFeatures.communism(), url_ussr)
  #     file_ussr = discord.File(fp=img_ussr.image,filename=f"ussr.{img_ussr.format}")
  #     await ctx.send(file=file_ussr)

  @commands.command()
  async def colors(self, ctx, member: discord.Member=None):
    """
    Analiza los colores de la foto de perfil de alguien.
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_clrs = str(member.avatar_url_as(static_format="png", size=1024))
      img_clrs = await dagpi.image_process(ImageFeatures.colors(), url_clrs)
      file_clrs = discord.File(fp=img_clrs.image,filename=f"colors.{img_clrs.format}")
      await ctx.send(file=file_clrs)

  @commands.command()
  async def gay(self, ctx, member: discord.Member=None):
    """
    #Pride
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_gy = str(member.avatar_url_as(static_format="png", size=1024))
      img_gy = await dagpi.image_process(ImageFeatures.gay(), url_gy)
      file_gy = discord.File(fp=img_gy.image,filename=f"gay.{img_gy.format}")
      await ctx.send(file=file_gy)

  @commands.command()
  async def fedora(self, ctx, member: discord.Member=None):
    """
    Ma'lady
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_fdr = str(member.avatar_url_as(static_format="png", size=1024))
      img_fdr = await dagpi.image_process(ImageFeatures.fedora(), url_fdr)
      file_fdr = discord.File(fp=img_fdr.image,filename=f"fedora.{img_fdr.format}")
      await ctx.send(file=file_fdr)

  @commands.command()
  async def jail(self, ctx, member: discord.Member=None):
    """
    Para mandar a cualquiera a la carcel
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_jl = str(member.avatar_url_as(static_format="png", size=1024))
      img_jl = await dagpi.image_process(ImageFeatures.jail(), url_jl)
      file_jl = discord.File(fp=img_jl.image,filename=f"jail.{img_jl.format}")
      await ctx.send(file=file_jl)

  @commands.command()
  async def bonk(self, ctx, member: discord.Member=None):
    """
    ¿Alguien anda horny?
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_bnk= str(member.avatar_url_as(static_format="png", size=1024))
      img_bnk = await dagpi.image_process(ImageFeatures.bonk(), url_bnk)
      file_bnk = discord.File(fp=img_bnk.image,filename=f"bonk.{img_bnk.format}")
      await ctx.send(file=file_bnk)

  @commands.command()
  async def delete(self, ctx, member: discord.Member=None):
    """
    Borra a alguien de la existencia
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_dlt= str(member.avatar_url_as(static_format="png", size=1024))
      img_dlt = await dagpi.image_process(ImageFeatures.delete(), url_dlt)
      file_dlt = discord.File(fp=img_dlt.image,filename=f"delete.{img_dlt.format}")
      await ctx.send(file=file_dlt)

  @commands.command()
  async def kaboom(self, ctx, member: discord.Member=None):
    """
    KABOOM!
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_bmb= str(member.avatar_url_as(static_format="png", size=1024))
      img_bmb = await dagpi.image_process(ImageFeatures.bomb(), url_bmb)
      file_bmb = discord.File(fp=img_bmb.image,filename=f"bomb.{img_bmb.format}")
      await ctx.send(file=file_bmb)

  @commands.command()
  async def neon(self, ctx, member: discord.Member=None):
    """
    Porque todo es más bonito con el neón
    """
    if member is None:
      member = ctx.author
    async with ctx.typing():
      url_nn= str(member.avatar_url_as(static_format="png", size=1024))
      img_nn = await dagpi.image_process(ImageFeatures.neon(), url_nn)
      file_nn = discord.File(fp=img_nn.image,filename=f"neon.{img_nn.format}")
      await ctx.send(file=file_nn)

def setup(bot: commands.Bot):
    bot.add_cog(img(bot))
