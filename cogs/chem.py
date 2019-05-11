#discord imports
import asyncio, discord
from discord.ext import commands
#rdkit imports
from  rdkit import Chem
from rdkit.Chem import Draw

class chem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #chemdraw command
    @commands.command()
    async def chemdraw(self, ctx, smiles : str):
        #attempt generating mol
        mol = Chem.MolFromSmiles(smiles)

        #send file
        if(mol is None):
            await ctx.send("Invalid SMILES.")
        else:
            Draw.MolToFile(mol, 'images/chemdraw.png')
            await ctx.send(file=discord.File("images/chemdraw.png"))

def setup(bot):
    bot.add_cog(chem(bot))