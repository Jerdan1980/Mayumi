using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;
using DSharpPlus.Interactivity;
using CommonBotLibrary;
using CommonBotLibrary.Converters;
using CommonBotLibrary.Exceptions;
using CommonBotLibrary.Extensions;
using CommonBotLibrary.Interfaces;
using CommonBotLibrary.Services;
using CommonBotLibrary.Services.Models;

namespace Discord_Bot
{
    class CBL_connect
    {
        [Command("maths"), Description("does maths")]
        public async Task Maths(CommandContext ctx, [RemainingText] String query)
        {
            ICalculatorService calc = new NCalcService();
            var result = await calc.EvaluateAsync(query);
            await ctx.RespondAsync(result);
        }

        [Command("cirno"), Description("does cirno maths")]
        public async Task Cirno(CommandContext ctx, [RemainingText] String query)
        {
            ICalculatorService calc = new NCalcService();
            string result = await calc.EvaluateAsync(query);
            int final = int.Parse(result);
            await ctx.RespondAsync(final + "");
        }
    }
}
