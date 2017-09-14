using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;
using HtmlAgilityPack;

namespace Discord_Bot_2
{
    class definitions
    {
        [Command("urbandefine"), Description("defines something using urban dictionary")]
        public async Task UrbanDefine(CommandContext ctx, string query)
        {
            string url = "http://www.thefreedictionary.com/" + query;
            HtmlWeb web = new HtmlWeb();
            HtmlDocument doc = web.Load(url);
            string word = doc.DocumentNode.SelectNodes("//*[@id=\"content\"]/div/h1")[0].InnerText;
            string type = doc.DocumentNode.SelectNodes("//*[@id=\"Definition\"]/section[1]/div[1]/i")[0].InnerText;
            string definition = doc.DocumentNode.SelectNodes("//*[@id=\"Definition\"]/section[1]/div[1]/div[1]")[0].InnerText;
            string output = "__**" + word.ToUpperInvariant() + "**__ _(" + type + ")_\n" + definition;
            await ctx.RespondAsync(output);
        }

        [Command("name"), Description("finds the etymology of a name")]
        public async Task Name(CommandContext ctx, string query)
        {
            string url = "http://behindthename.com/name/" + query;
            HtmlWeb web = new HtmlWeb();
            HtmlDocument doc = web.Load(url);
        }
    }
}
