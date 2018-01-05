using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;
using Steam;
using SteamWebAPI2.Exceptions;
using SteamWebAPI2.Interfaces;
using SteamWebAPI2.Models;
using SteamWebAPI2.Utilities;

namespace Discord_Bot
{
    [Group("steam"), Description("connects to steam")]
    class steam_connect
    {
        [Command("player"), Description("user stats")]
        public async Task player(CommandContext ctx, [Description("The steam player ID")] ulong playerID)
        {
            await ctx.TriggerTypingAsync();

            //grab the information using the steam API
            var steamInterface = new SteamUser(Driver.steam_key);
            var playerSummaryResponse = await steamInterface.GetPlayerSummaryAsync(playerID);
            var playerSummaryData = playerSummaryResponse.Data;
            var friendsListResponse = await steamInterface.GetFriendsListAsync(playerID);
            var friendsListData = friendsListResponse.Data;

            //format the output
            var embed = new DiscordEmbedBuilder {
                Title = playerSummaryData.Nickname,
                ThumbnailUrl = playerSummaryData.AvatarUrl,
                Color = DiscordColor.Blurple,
                Description = "Number of friends: " + friendsListData.Count
            };
            await ctx.RespondAsync(embed: embed);
        }
    }
}
