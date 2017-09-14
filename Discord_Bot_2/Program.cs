using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;

namespace Discord_Bot
{
    class Program
    {
        //declares discord client
        static DiscordClient discord;

        static void Main(string[] args)
        {
            MainAsync(args).ConfigureAwait(false).GetAwaiter().GetResult();
        }

        static async Task MainAsync(string[] args)
        {
            //instatiates discord client
            discord = new DiscordClient(new DiscordConfiguration {
                Token = "",
                TokenType = TokenType.Bot
            });

            discord.MessageCreated += async e => {
                if(e.Message.Content.ToLower().StartsWith("ping"))
                    await e.Message.RespondAsync("pong");
            };

            await discord.ConnectAsync();
            await Task.Delay(-1);
        }
    }
}
