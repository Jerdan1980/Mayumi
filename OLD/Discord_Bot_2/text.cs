using System;
using System.IO;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;

namespace Discord_Bot
{
    //misc stuff
    public class text
    {
        [Command("hi"), Description("Says hello"), Aliases("hello", "hullo", "Hi", "Hello", "Hullo", "waddup")]
        public async Task Hi(CommandContext ctx)
        {
            Random rng = new Random();
            string[] data = File.ReadAllLines(@"..\\Discord_Bot_2\\Resources\\textSpeech\\hello.txt");
            var choice = rng.Next(data.Length + 1);
            if(choice == data.Length + 1)
            {
                var emoji = DiscordEmoji.FromName(ctx.Client, ":wave:");
                await ctx.RespondAsync($"{emoji} Hello~");
            } else
                await ctx.RespondAsync(data[choice]);
        }

        [Command("goodbye"), Description("Says goodbye"), Aliases("cya", "bye")]
        public async Task Goodbye(CommandContext ctx)
        {
            Random rng = new Random();
            string[] data = File.ReadAllLines(@"..\\Discord_Bot_2\\Resources\\textSpeech\\goodbye.txt");
            var choice = rng.Next(data.Length + 1);
            if(choice == data.Length + 1)
            {
                var emoji = DiscordEmoji.FromName(ctx.Client, ":wave:");
                await ctx.RespondAsync($"{emoji} Goodbye~");
            } else
                await ctx.RespondAsync(data[choice]);
        }

        [Command("goodnight"), Description("Says goodnight"), Aliases("night")]
        public async Task Goodnight(CommandContext ctx)
        {
            Random rng = new Random();
            string[] data = File.ReadAllLines(@"..\\Discord_Bot_2\\Resources\\textSpeech\\goodnight.txt");
            var choice = rng.Next(data.Length + 1);
            if(choice == data.Length + 1)
            {
                var emoji = DiscordEmoji.FromName(ctx.Client, ":zzz:");
                await ctx.RespondAsync($"{emoji} Sweet Dreams~");
            } else
                await ctx.RespondAsync(data[choice]);
        }

        [Command("laugh"), Description("Laughs"), Aliases("haha", "lol", "kek")]
        public async Task Laugh(CommandContext ctx)
        {
            Random rng = new Random();
            string[] data = File.ReadAllLines(@"..\\Discord_Bot_2\\Resources\\textSpeech\\laugh.txt");
            var choice = rng.Next(data.Length + 2);
            if(choice == data.Length + 1)
            {
                var emoji = DiscordEmoji.FromName(ctx.Client, ":wave:");
                await ctx.RespondAsync($"{emoji}");
            } else if(choice == data.Length + 2)
            {
                var emoji = DiscordEmoji.FromName(ctx.Client, ":laughing:");
                await ctx.RespondAsync($"{emoji}");
            } else 
                await ctx.RespondAsync(data[choice]);
        }

        [Command("rip"), Description("rips"), Aliases("RIP")]
        public async Task RIP(CommandContext ctx)
        {
            Random rng = new Random();
            string[] data = File.ReadAllLines(@"..\\Discord_Bot_2\\Resources\\textSpeech\\rip.txt");
            var choice = rng.Next(data.Length + 2);
            if(choice == data.Length + 1)
            {
                var emoji = DiscordEmoji.FromName(ctx.Client, ":coffin:");
                await ctx.RespondAsync($"{emoji}");
            } else if(choice == data.Length + 2)
            {
                var emoji = DiscordEmoji.FromName(ctx.Client, ":skull_crossbones:");
                await ctx.RespondAsync($"{emoji}");
            } else
                await ctx.RespondAsync(data[choice]);
        }
        [Command("say"), Description("repeats"), Aliases("echo", "repeat")]
        public async Task Echo(CommandContext ctx, string output) => await ctx.RespondAsync(output);

        [Command("time"), Description("tells time")]
        public async Task Time(CommandContext ctx) => await ctx.RespondAsync("learn it yourself");

        [Command("fortune"), Description("gives a fortune cookie")]
        public async Task Fortune(CommandContext ctx)
        {
            Cookie[] cookies = Cookie.fileToArray();
            Random rng = new Random();
            int pick = rng.Next(cookies.Length);
            Cookie fortune = cookies[pick];

            string output = $"_{fortune.Fortune}_\n" +
                            $"Your lucky numbers: {fortune.Numbers}";
            if(fortune.Learn == true)
            {
                output += "\n";
                output += $"**Learn Chinese:** _{fortune.English}_ is {fortune.Chinese}";
            }

            DiscordEmbed embed = new DiscordEmbedBuilder {
                Title = $"{ctx.Member.Nickname}'s fortune",
                Color = DiscordColor.Wheat,
                Description = output
            };

            await ctx.RespondAsync(embed: embed);
        }

        [Command("pun"), Description("A pun for you!")]
        public async Task Pun(CommandContext ctx, [Description("The topic of the pun")] string keyword)
        {
            Random rng = new Random();
            string[] puns = custClass.getPuns(keyword);
            int choice = rng.Next(puns.Length);
            await ctx.RespondAsync(puns[choice]);
        }
    }
}
