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
        [Command("urbandict"), Description("fetches a definition from ubrandictionary")]
        public async Task Urbandict(CommandContext ctx, [RemainingText] String query)
        {
            UrbanDictionaryService uDict = new UrbanDictionaryService();
            IEnumerable<UrbanDictionaryResult> temp = await uDict.GetDefinitionsAsync(query);
            UrbanDictionaryResult answer = temp.GetEnumerator().Current;

            DiscordEmbed embed = new DiscordEmbedBuilder {
                Title = $" ~ {answer.Word} ~ ",
                Color = DiscordColor.Grayple,
                Description =   answer.Definition +
                                "/nEx: " + answer.Example +
                                "/nBy: " + answer.Author
            };
            await ctx.RespondAsync(embed: embed);
        }

        [Command("maths"), Description("does maths")]
        public async Task Maths(CommandContext ctx, [RemainingText] String query)
        {
            NCalcService nCalc = new NCalcService();
            String answer = await nCalc.EvaluateAsync(query);
        }
    }
}
