#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import sys, traceback
import json
import sqlite3
import itertools

#cleans strings
def scrub(table_name):
    return ''.join( chr for chr in table_name if chr.isalnum() )

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('profiles.db', detect_types=sqlite3.PARSE_DECLTYPES)

    #update database
    async def update(self):
        self.conn.commit()

    #adder
    async def add_pts(self, author: int, guild: str, pts: int):
        #creates guild tabel if not exists
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS guild_{scrub(str(guild))} (user_id INTEGER, earned_pts INTEGER, UNIQUE(user_id))")
        
        #create user if they dont already exist
        self.conn.execute("INSERT OR IGNORE INTO users VALUES (?, 0, 0)", (author,))
        self.conn.execute(f"INSERT OR IGNORE INTO guild_{scrub(str(guild))} VALUES (?, 0)", (author,))

        #add points
        self.conn.execute("UPDATE users SET available_pts = available_pts + ?, lifetime_pts = lifetime_pts + ? WHERE user_id = ?", (pts, pts, author))
        self.conn.execute(f"UPDATE guild_{scrub(str(guild))} SET earned_pts = earned_pts + ? WHERE user_id = ?;", (pts, author))
        
        #save
        await self.update()

    #subtracter
    #returns true if is able to subtract
    async def sub_pts(self, author: int, pts: int):
        #create user if they don't already exist
        self.conn.execute("INSERT OR IGNORE INTO users VALUES (?, 0, 0)", (author,))

        #subtract points if they have more than 0
        avail = self.conn.execute("SELECT available_pts FROM users WHERE user_id = ?", (author,)).fetchone()[0]
        if avail >= pts:
            self.conn.execute("UPDATE users SET available_pts = available_pts - ? WHERE user_id = ?", (pts, author))
            await self.update()
            return True
        else:
            return False

    #profile command
    @commands.command()
    async def profile(self, ctx, query: str = ""):
        if query == "":
            #create user if they dont already exist
            self.conn.execute("INSERT OR IGNORE INTO users VALUES (?, 0, 0)", (ctx.author.id,))
            
            #output their data
            row = self.conn.execute("SELECT * FROM users WHERE user_id = ?", (ctx.author.id,))
            await ctx.send(tuple(row))
        else:
            await ctx.send("WIP")

    #ranking command
    @commands.command()
    async def top(self, ctx, query: int = 0):
        leaderboard = self.conn.execute(f"SELECT * FROM guild_{scrub(str(guild))} ORDER BY points DESC").fetchall()[query * 10: query * 10 + 9]
        #format output
        output = "**Leaderboard:**\n"
        for row in leaderboard:
            output += f"{i+1}: {ctx.guild.get_user_info(int(row[0])).display_name()}\n"
        await ctx.send(output)

def setup(bot):
    bot.add_cog(profile(bot))