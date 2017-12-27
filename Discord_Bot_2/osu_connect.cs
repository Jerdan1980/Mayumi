﻿using System;
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
    class osu_connect
    {
        public static OsuClient osu = new OsuClient(Driver.OSU_key);

        [Command("userfull"), Description("all stats, all games")]
        public async Task Userfull(CommandContext ctx, string query)
        {
            OsuUser user = osu.GetUser(query)[0];
            OsuUserBest[] best = osu.GetUserBest(query);
            OsuUserRecent[] recent = osu.GetUserRecent(query);

            String output = $"~ {user.username} (lvl {user.level}) ~\n" +
                            $"Rank: {user.pp_rank} ({user.pp_country_rank} in {user.country})\n" +
                            $"PP: {user.pp_raw}\n" +
                            $"Score: {user.ranked_score} weighted, {user.total_score} unweighted\n" +
                            $"Accuracy: {user.accuracy}\n" +
                            $"{user.playcount} plays ({user.count_rank_ss} SSs, {user.count_rank_s} Ss, {user.count_rank_a} As)";
            await ctx.RespondAsync(output);
        }

        
        [Command("user"), Description("Basic stats")]
        public async Task User(CommandContext ctx, string query)
        {
            OsuUser user = osu.GetUser(query)[0];
            //OsuUserBest best = osu.GetUserBest(query)[0];
            //OsuBeatmap best_song = osu.GetBeatmap((int) long.Parse(best.beatmap_id))[0];
            //OsuUserRecent recent = osu.GetUserRecent(query)[0];
            //OsuBeatmap recent_song = osu.GetBeatmap((int) long.Parse(recent.beatmap_id))[0];

            DiscordEmbed embed = new DiscordEmbedBuilder {
                Title = $"{user.username} (lvl {user.level})",
                ThumbnailUrl = user.image,
                Color = DiscordColor.HotPink,
                Description =   $"Rank: {user.pp_rank} ({user.pp_country_rank} in {user.country})\n" +
                                $"PP: {user.pp_raw}\tAccuracy: {user.accuracy}\n" +
                                $"Score: {user.ranked_score}\tPlays: {user.playcount}\n" //+
                                //$"Recently Played: "/*{recent_song.title} [{recent_song.version}] by {recent_song.artist} -*/ +$"{recent.accuracy}% {recent.rank}\n" +
                                //$"Best Played: "/*{best_song.title} [{best_song.version}] by {best_song.artist} -*/ +$"{best.accuracy}% {best.rank}";
            };            
            await ctx.RespondAsync(embed: embed);
        }
    }
}
