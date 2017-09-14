using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;

namespace Discord_Bot_2
{
    public class MyCommands
    {
        [Command("hi")]
        public async Task hi(CommandContext ctx)
        {
            await ctx.RespondAsync($"Hello!");
        }
    }
}
