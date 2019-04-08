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
        [Command("calc"), Description("Computes the equation"), Aliases("maths", "math", "calculate", "compute")]
        public async Task Maths(CommandContext ctx, [RemainingText, Description("The equation to compute")] string equation)
        {
            await ctx.TriggerTypingAsync();

            //uses CBL's calculator API
            ICalculatorService calc = new NCalcService();
            var result = await calc.EvaluateAsync(equation);
            await ctx.RespondAsync(result);
        }

        [Command("cirno"), Description("If cirno did math")] //cirno is thought to do math in base 9.
        public async Task Cirno(CommandContext ctx, [RemainingText, Description("THe equation to compute")] String equation)
        {
            await ctx.TriggerTypingAsync();

            //uses CBL's calculator api
            ICalculatorService calc = new NCalcService();
            string result = await calc.EvaluateAsync(equation);

            //convert to base 9
            int number;
            if(int.TryParse(result, out number)) //the method currently only works with integers
            {
                await ctx.RespondAsync(custClass.changeBase(number, 9));
            } else
                await ctx.RespondAsync("Difficult");
        }
    }
}
