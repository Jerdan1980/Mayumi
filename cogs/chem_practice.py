#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random

#class holding questions
class chem_practice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #molar solubility
    @commands.command()
    async def molsol(self, ctx):
        #list of ksp
        Ksp_list = []
        Ksp_list.append (Ksp('PbBr2', 6.6e-6, 1, 2))
        Ksp_list.append (Ksp('CuBr', 6.3e-9, 1, 1))
        Ksp_list.append (Ksp('AgBr', 5.4e-13, 1, 1))
        Ksp_list.append (Ksp('Hg2Br2', 6.4e-23, 1, 2))
        Ksp_list.append (Ksp('PbCl2', 1.2e-5, 1, 2))
        Ksp_list.append (Ksp('CuCl', 1.7e-7, 1, 1))
        Ksp_list.append (Ksp('AgCl', 1.8e-10, 1, 1))
        Ksp_list.append (Ksp('Hg2Cl2', 1.4e-18, 1, 2))
        Ksp_list.append (Ksp('BaF2', 1.8e-7, 1, 2))
        Ksp_list.append (Ksp('MgF2', 7.4e-11, 1, 2))
        Ksp_list.append (Ksp('SrF2', 2.5e-9, 1, 2))
        Ksp_list.append (Ksp('CaF2', 1.5e-10, 1, 2))
        Ksp_list.append (Ksp('PbI2', 8.5e-9, 1, 2))
        Ksp_list.append (Ksp('CuI', 1.1e-12, 1, 1))
        Ksp_list.append (Ksp('AgI', 8.5e-17,1, 1))
        Ksp_list.append (Ksp('Hg2I2', 4.5e-29, 1, 2))
        Ksp_list.append (Ksp('CaSO4', 7.1e-5, 1, 1))
        Ksp_list.append (Ksp('Ag2SO4', 1.2e-5, 2, 1))
        Ksp_list.append (Ksp('Hg2SO4', 6.8e-7, 1, 1))
        Ksp_list.append (Ksp('SrSO4', 3.5e-7, 1, 1))
        Ksp_list.append (Ksp('PbSO4', 1.8e-8, 1, 1))
        Ksp_list.append (Ksp('BaSO4', 1.1e-10, 1, 1))
        Ksp_list.append (Ksp('Ag(CH3COO)', 4.4e-3, 1, 1))
        Ksp_list.append (Ksp('Hg2(CH3COO)2', 4.0e-10, 1, 2))
        Ksp_list.append (Ksp('MgCO3', 6.8e-6, 1, 1))
        Ksp_list.append (Ksp('NiCO3', 1.3e-7, 1, 1))
        Ksp_list.append (Ksp('CaCO3', 5.0e-9, 1, 1))
        Ksp_list.append (Ksp('SrCo3', 5.6e-10, 1, 1))
        Ksp_list.append (Ksp('MnCo3', 2.2e-11, 1, 1))
        Ksp_list.append (Ksp('CuCO3', 2.5e-10, 1, 1))
        Ksp_list.append (Ksp('CoCO3', 1.0e-10, 1, 1))
        Ksp_list.append (Ksp('FeCO3', 2.1e-11, 1, 1))
        Ksp_list.append (Ksp('ZnCO3', 1.2e-10, 1, 1))
        Ksp_list.append (Ksp('Ag2CO3', 8.1e-12, 2, 1))
        Ksp_list.append (Ksp('CdCO3', 6.2e-12, 1, 1))
        Ksp_list.append (Ksp('PbCO3', 7.4e-14, 1, 1))
        Ksp_list.append (Ksp('Ba(OH)2', 5.0e-3, 1, 2))
        Ksp_list.append (Ksp('Sr(OH)2', 6.4e-3, 1, 2))
        Ksp_list.append (Ksp('Ca(OH)2', 4.7e-6, 1, 2))
	    Ksp_list.append (Ksp('Mg(OH)2', 5.6e-12, 1, 2))
        Ksp_list.append (Ksp('Mn(OH)2', 2.1e-13, 1, 2))
        Ksp_list.append (Ksp('Cd(OH)2', 5.3e-15, 1, 2))
        Ksp_list.append (Ksp('Pb(OH)2', 1.2e-15, 1, 2))
        Ksp_list.append (Ksp('Fe(OH)2', 4.9e-15, 1, 2))
        Ksp_list.append (Ksp('Ni(OH)2', 5.5e-16, 1, 2))
        Ksp_list.append (Ksp('Co(OH)2', 1.1e-15, 1, 2))
        Ksp_list.append (Ksp('Zn(OH)2', 4.1e-17, 1, 2))
        Ksp_list.append (Ksp('Cu(OH)2', 1.6e-19, 1, 2))
        Ksp_list.append (Ksp('Hg(OH)2', 3.1e-26, 1, 2))
        Ksp_list.append (Ksp('Sn(OH)2', 5.4e-27, 1, 2))
        Ksp_list.append (Ksp('Cr(OH)3', 6.7e-31, 1, 3))
	    Ksp_list.append (Ksp('Al(OH)3', 1.9e-33, 1, 3))
        Ksp_list.append (Ksp('Fe(OH)3', 2.6e-39, 1, 3))
        Ksp_list.append (Ksp('MgC2O4', 4.8e-6, 1, 1))
        Ksp_list.append (Ksp('FeC2O4', 2.0e-7, 1, 1))
        Ksp_list.append (Ksp('NiC2O4', 1.0e-7, 1, 1))
        Ksp_list.append (Ksp('SrC2O4', 5.0e-8, 1, 1))
        Ksp_list.append (Ksp('CuC2O4', 3.0e-8, 1, 1))
        Ksp_list.append (Ksp('BaC2O4', 1.6e-7, 1, 1))
        Ksp_list.append (Ksp('CdC2O4', 1.4e-8, 1, 1))
        Ksp_list.append (Ksp('ZnC2O4', 1.4e-9, 1, 1))
        Ksp_list.append (Ksp('CaC2O4', 2.3e-9, 1, 1))
        Ksp_list.append (Ksp('Ag2C2O4', 3.5e-11, 2, 1))
        Ksp_list.append (Ksp('PbC2O4', 4.8e-12, 1, 1))
        Ksp_list.append (Ksp('Hg2C2O4', 1.8e-13, 1, 1))
        Ksp_list.append (Ksp('MnC2O4', 1.0e-15, 1, 1))
        Ksp_list.append (Ksp('Ag3PO4', 8.9e-17, 3, 1))
        Ksp_list.append (Ksp('AlPO4', 9.8e-21, 1, 1))
        Ksp_list.append (Ksp('Mn3(PO4)2', 1.0e-22, 3, 2))
        Ksp_list.append (Ksp('Ba3(PO4)2', 3.0e-23, 3, 2))
        Ksp_list.append (Ksp('BiPO4', 1.3e-23, 1, 1))
        Ksp_list.append (Ksp('Sr3(PO4)2', 4.0e-28, 3, 2))
        Ksp_list.append (Ksp('Pb3(PO4)2', 7.9e-43, 3, 2))
        Ksp_list.append (Ksp('CaCrO4', 7.1e-4, 1, 1))
        Ksp_list.append (Ksp('SrCrO4', 2.2e-5, 1, 1))
        Ksp_list.append (Ksp('Hg2CrO4', 2.0e-9, 1, 1))
        Ksp_list.append (Ksp('BaCrO4', 1.2e-10, 1, 1))
        Ksp_list.append (Ksp('Ag2CrO4', 2.0e-12, 2, 1))
        Ksp_list.append (Ksp('PbCrO4', 2.8e-13, 1, 1))

        #shuffle the dict to get a random Ksp
        salt = random.shuffle(Ksp_list)[0]
        
        #ask the question
        await ctx.send('You have {salt.name} with Ksp {salt.Ksp}. What is the molar solubility?')
        await ctx.send('Reply in format `submit <answer>`. Do not include units. Ex: `submit 3`. You have a 2% tolerance') 

        #checker method
        def check(msg, user):
            return msg.content.startswith('submit') and user == ctx.author:

        #grab input and check for correctness
        try:
            msg = await ctx.wait_for('message', Timeout=120.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'Out of time! the correct answer is ||{salt.S}||')
        else:
            answer = msg.content.split()[1]
            if (abs(answer-salt.S) / salt.S * 100) <= 2:
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1) 


def setup(bot):
    bot.add_cog(chem_practice(bot))


#class for Ksp
class Ksp():
    def __init__(self, name_of_salt, Ksp_val, x, y):
        self.name = name
        self.Ksp = Ksp_val
        self.x = x
        self.y = y
        self.S = pow(Ka/(pow(y,y) * pow(x,x)),1/(x+y))


