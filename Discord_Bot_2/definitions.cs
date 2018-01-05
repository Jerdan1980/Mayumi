using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;
using HtmlAgilityPack;
using CommonBotLibrary;
using CommonBotLibrary.Converters;
using CommonBotLibrary.Exceptions;
using CommonBotLibrary.Extensions;
using CommonBotLibrary.Interfaces;
using CommonBotLibrary.Services;
using CommonBotLibrary.Services.Models;

namespace Discord_Bot
{
    [Group("define"), Description("Any sort of defining"), Aliases("def"), CanInvokeWithoutSubcommand = true]
    class definitions
    {
        //the default command
        public async Task ExecuteGroupAsync(CommandContext ctx, [RemainingText, Description("The word you're looking for")] string query)
        {
            await ctx.TriggerTypingAsync();

            //creates the url
            string url = "http://www.thefreedictionary.com/";
            string[] terms = query.Split(' '); //splits the query up in case there are spaces
            url += terms[0]; //the first term
            if(terms.Length > 1) //checks if there are multiple terms
            {
                for(int i = 1; i < terms.Length; i++) //if there are, add the connector "+" that goes in place of the " "
                    url += "+" + terms[i];
            }

            //turns the url into an HTML document
            HtmlWeb web = new HtmlWeb();
            HtmlDocument doc = web.Load(url);

            //extracts the wanted text from the HTML document
            string word = doc.DocumentNode.SelectNodes("//*[@id=\"content\"]/div/h1")[0].InnerText;
            string type = doc.DocumentNode.SelectNodes("//*[@id=\"Definition\"]/section[1]/div[1]/i")[0].InnerText;
            string definition = doc.DocumentNode.SelectNodes("//*[@id=\"Definition\"]/section[1]/div[1]/div[1]")[0].InnerText;

            //formats the output
            string output = "__**" + word.ToUpperInvariant() + "**__ _(" + type + ")_\n" + definition;
            await ctx.RespondAsync(output);
        }

        [Command("urban"), Description("Defines something using urban dictionary"), Aliases("urbandictionary", "urbandefine", "u")]
        public async Task UrbanDefine(CommandContext ctx, [RemainingText, Description("The word you're looking for")] string query)
        {
            await ctx.TriggerTypingAsync();

            //uses the UrbanDictionary API
            IDictionaryService uDef = new UrbanDictionaryService();
            var result = (UrbanDictionaryResult) await uDef.GetDefinitionsAsync(query);

            //format the output
            DiscordEmbed embed = new DiscordEmbedBuilder {
                Title = result.Word,
                Description =   $"Definition: {result.Definition}\n" +
                                $"Example: {result.Example}\n" +
                                $"By {result.Author}"
            };
            await ctx.RespondAsync(embed: embed);
        }

        [Command("name"), Description("finds the etymology of a name")]
        public async Task Name(CommandContext ctx, [Description("The name")] string name)
        {
            await ctx.TriggerTypingAsync();
            
            //grabs the url and creates a URL document
            string url = "http://behindthename.com/name/" + name;
            HtmlWeb web = new HtmlWeb();
            HtmlDocument doc = web.Load(url);

            //extracts the wanted text from the HTML document
            string webName = doc.DocumentNode.SelectNodes("//html//body//div[2]//div//div[3]//div[1]//h1")[0].InnerText;
            string gender = doc.DocumentNode.SelectNodes("//html//body//div[2]//div//div[3]//div[2]//div[1]//span[2]//span")[0].InnerText;
            string usage = doc.DocumentNode.SelectNodes("//html//body//div[2]//div//div[3]//div[2]//div[2]")[0].InnerText;
            string meaning = doc.DocumentNode.SelectNodes("//html//body//div[2]//div//div[3]//div[4]")[0].InnerText;

            //formats the output
            DiscordEmbed embed = new DiscordEmbedBuilder {
                Title = webName,
                Color = DiscordColor.Wheat,
                Description =   $"Gender: {gender}\n" +
                                $"Usage: {usage}\n" +
                                $"Meaning: {meaning}\n"
            };
            await ctx.RespondAsync(embed: embed);
        }
    }
}
