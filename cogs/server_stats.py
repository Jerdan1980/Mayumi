#discord imports
import asyncio, discord
from discord.ext import commands

class server_stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #roles
    @commands.group(pass_context=True, aliases=['r'])
    async def role(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No subcommand passed")

    #role counter
    @role.command(aliases=['count'])
    async def c(self, ctx, query: str = ""):
        if query == "":
            await ctx.send("No role selected!")
        else:
            try:
                role = ctx.message.role_mentions[0]
                counter = 0
                for m in ctx.channel.guild.members:
                    if role in m.roles:
                        counter += 1
                await ctx.send(f'{counter} users have `{role.name}` role.')

            except Exception:
                    found = False
                    for r in ctx.channel.guild.roles:
                        if not found and (query.lower() in r.name.lower()):
                            found = True
                            role = r
                    
                    if found:
                        counter = 0
                        for m in ctx.channel.guild.members:
                            if role in m.roles:
                                counter += 1
                        await ctx.send(f'{counter} users have `{role.name}` role.')
                    else:
                        await ctx.send('Role not found!')

    #lists who has the role
    @role.command(aliases=['list'])
    async def l(self, ctx, query: str = ""):
        if query == "":
            await ctx.send("No role selected!")
        else:
            try:
                role = ctx.message.role_mentions[0]
                memlist = []
                for m in ctx.channel.guild.members:
                    if role in m.roles:
                        memlist.append(m.display_name)
                output = f'{len(memlist)} users have `{role.name}` role:\n`'
                output += "`, `".join(memlist)
                output += '`'
                await ctx.send(output)

            except Exception:
                    found = False
                    for r in ctx.channel.guild.roles:
                        if not found and (query.lower() in r.name.lower()):
                            found = True
                            role = r
                    
                    if found:
                        memlist = []
                        for m in ctx.channel.guild.members:
                            if role in m.roles:
                                memlist.append(m.name)
                        output = f'{len(memlist)} users have `{role.name}` role:\n`'
                        output += "`, `".join(memlist)
                        output += '`'
                        await ctx.send(output)
                    else:
                        await ctx.send('Role not found!')

def setup(bot):
    bot.add_cog(server_stats(bot))