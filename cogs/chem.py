#discord imports
import asyncio, discord
from discord.ext import commands
#rdkit imports
from  rdkit import Chem
from rdkit.Chem import Draw
#standard imports
import os

class chem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #chemdraw command
    @commands.command()
    async def chemdraw(self, ctx, smiles : str):
        #attempt generating mol
        try:
            mol = Chem.MolFromSmiles(smiles)
        except Exception as e:
            await ctx.send(e.message)

        #send file
        if(mol is None):
            await ctx.send("Invalid SMILES.")
        else:
            Draw.MolToFile(mol, f'images/{ctx.author.id}.png')
            await ctx.send(file=discord.File(f"images/{ctx.author.id}.png"))
            os.remove(f"images/{ctx.author.id}.png")

def setup(bot):
    bot.add_cog(chem(bot))