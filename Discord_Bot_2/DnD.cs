using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;

namespace Discord_Bot
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

        [Command("flip"), Description("flips a coin")]
        public async Task Flip(CommandContext ctx, int mult = 1)
        {
            Random rng = new Random();
            int heads = 0, tails = 0;
            String output = "";
            for(int i = 0; i < mult; i++)
            {
                int coin = rng.Next(2);
                if(coin == 1)
                {
                    heads++;
                    output += "H";
                }else if(coin == 0)
                {
                    tails++;
                    output += "T";
                }
            }
            await ctx.RespondAsync( "```" + output + "```\n" + 
                                    "Heads: " + heads + "\n" +
                                    "Tails: " + tails);
        }

        [Command("randInt"), Description("grabs a random integer")]
        public async Task RandInt(CommandContext ctx, int lower = int.MinValue, int higher = int.MaxValue, int rep = 1)
        {
            Random rng = new Random();
            String output = "";
            for(int i = 0; i < rep - 1; i++)
            {
                output += rng.Next(lower, higher) + ", ";
            }
            output += rng.Next(lower, higher);
            await ctx.RespondAsync(output);
        }
    }
}
