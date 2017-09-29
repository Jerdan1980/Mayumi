using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;

namespace Discord_Bot_2
{
    class DnD
    {
        [Command("roll"), Description("rolls dice")]
        public async Task Roll(CommandContext ctx, string query)
        {
            Random rng = new Random();
            string[] tokens = query.Split('d',' ','+','-');
            int number = int.Parse(tokens[0]);
            int sides = int.Parse(tokens[1]);
            int roll = 0;
            for(int i = 0; i < number; i++)
            {
                roll += rng.Next(1, sides + 1);
            }
            if(query.Contains("-"))
                roll -= int.Parse(tokens[2]);
            else
                roll += int.Parse(tokens[2]);
            await ctx.RespondAsync($"{ctx.Member.Username} rolls a {roll}");
        }
    }
}
