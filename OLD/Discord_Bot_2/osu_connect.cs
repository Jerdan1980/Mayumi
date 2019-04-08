using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;
using DSharpPlus.Interactivity;
using System.Net;
using System.IO;
using CSharpOsu;
using CSharpOsu.Module;
using CSharpOsu.Util;

namespace Discord_Bot
{
    [Group("osu"), Description("Pertaining to osu!")]
    class osu_connect
    {
        public static OsuClient osu = new OsuClient(Driver.OSU_key); //the osu client for the api

        [Command("userfull"), Description("Grabs all stats, all games of a player")]
        public async Task Userfull(CommandContext ctx, [Description("The name of the player")] string username)
        {
            await ctx.TriggerTypingAsync(); //say that the bot is typing
            
            //initialize variables
            //the first user in the array is usually the one they want
            OsuUser user = osu.GetUser(username)[0];
            OsuUserBest[] best = osu.GetUserBest(username);
            OsuUserRecent[] recent = osu.GetUserRecent(username);

            //format the output of the text
            String output = $"Rank: {user.pp_rank} ({user.pp_country_rank} in {user.country})\n" +
                            $"PP: {user.pp_raw}\n" +
                            $"Score: {user.ranked_score} weighted, {user.total_score} unweighted\n" +
                            $"Accuracy: {user.accuracy}\n" +
                            $"{user.playcount} plays ({user.count_rank_ss} SSs, {user.count_rank_s} Ss, {user.count_rank_a} As)";

            //create a discord embed to hold the output
            DiscordEmbed embed = new DiscordEmbedBuilder {
                Title = $"~ {user.username} (lvl {user.level}) ~\n",
                ThumbnailUrl = user.image,
                Color = DiscordColor.HotPink,
                Description = output
            };

            await ctx.RespondAsync(embed: embed); //send the message
        }

        [Command("profile"), Description("Basic stats")]
        public async Task User(CommandContext ctx, string query)
        {
            await ctx.TriggerTypingAsync(); //say that the bot is typing

            OsuUser user = osu.GetUser(query)[0]; //get user stats

            //create a discord embed to hold the output
            DiscordEmbed embed = new DiscordEmbedBuilder {
                Title = $"{user.username} (lvl {user.level})",
                ThumbnailUrl = user.image,
                Color = DiscordColor.HotPink,
                Description =   $"Rank: {user.pp_rank} ({user.pp_country_rank} in {user.country})\n" +
                                $"PP: {user.pp_raw}\tAccuracy: {user.accuracy}\n" +
                                $"Score: {user.ranked_score}\tPlays: {user.playcount}\n"
            };            
            await ctx.RespondAsync(embed: embed);
        }
    }
}
