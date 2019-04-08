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
        [Command("roll"), Description("rolls dice"), Aliases("r")]
        public async Task Roll(CommandContext ctx, [Description("")] string query)
        {
            await ctx.TriggerTypingAsync();

            //initialize variables
            Random rng = new Random();
            int roll = 0;
            string calc = "```"; //starts monotext
            int pick = 0; //temp variable for storing the roll
            int rolls = 0;

            //removes spaces beforehand to prevent them from interfereing
            string[] tempstore = query.Split(' ');
            query = "";
            foreach(string v in tempstore)
                query += v;

            //splits the query into the variables
            string[] tokens = query.Split('d','+','-');
            int number = int.Parse(tokens[0]);
            int sides = int.Parse(tokens[1]);

            //does the calculations
            for(int i = 0; i < number; i++)
            {
                pick = rng.Next(1, sides + 1);
                rolls++;
                roll += pick;
                if(rolls == 1)
                    calc += pick;
                else
                    calc += $" + {pick}";
            }
            //checks to see if there are modifiers
            if(query.Contains("-"))
            {
                pick = int.Parse(tokens[2]);
                roll -= pick;
                calc += " - pick";
            }
            else if(query.Contains("+"))
            {
                pick = int.Parse(tokens[2]);
                roll += pick;
                calc += " + pick";
            }
            calc += "```"; //ends the monotext

            //output
            await ctx.RespondAsync($"{ctx.Member.Username} rolls a {roll}\n{calc}");
        }

        [Command("flip"), Description("flips a coin")]
        public async Task Flip(CommandContext ctx, [Description("The number of coins to flip")] int mult = 1)
        {
            await ctx.TriggerTypingAsync();

            //initialize variables
            Random rng = new Random();
            int heads = 0, tails = 0;
            String output = "";

            //do the calculations
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

            //output
            await ctx.RespondAsync( "```" + output + "```\n" + 
                                    "Heads: " + heads + "\n" +
                                    "Tails: " + tails);
        }

        [Command("randInt"), Description("grabs a random integer")]
        public async Task RandInt(CommandContext ctx, [Description("The lowest value, inclusive")] int lower = int.MinValue, [Description("The highest value, exclusive")] int higher = int.MaxValue, [Description("The number of repitetions")] int rep = 1)
        {
            await ctx.TriggerTypingAsync();
            
            //initialize variables
            Random rng = new Random();
            String output = "";

            //do the calculations
            for(int i = 0; i < rep - 1; i++) //does one less to prevent that extra comma
            {
                output += rng.Next(lower, higher) + ", ";
            }
            output += rng.Next(lower, higher);

            //output
            await ctx.RespondAsync(output);
        }
    }
}
