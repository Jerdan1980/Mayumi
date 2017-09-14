﻿using System;
using System.IO;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;

namespace Discord_Bot_2
{
    //misc stuff
    public class Greetings
    {
        [Command("hi"), Description("Says hello"), Aliases("hello", "hullo", "Hi", "Hello", "Hullo")]
        public async Task Hi(CommandContext ctx)
        {
            Random rng = new Random();
            string[] data = File.ReadAllLines(@"..\\resources\\textSpeech\\hello.txt");
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
            string[] data = File.ReadAllLines(@"..\\resources\\textSpeech\\goodbye.txt");
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
            string[] data = File.ReadAllLines(@"..\\resources\\textSpeech\\goodnight.txt");
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
            string[] data = File.ReadAllLines(@"..\\resources\\textSpeech\\laugh.txt");
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
            string[] data = File.ReadAllLines(@"..\\resources\\textSpeech\\rip.txt");
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
        [Command("echo"), Description("repeats"), Aliases("say")]
        public async Task Echo(CommandContext ctx, string output) => await ctx.RespondAsync(output);
    }
}
