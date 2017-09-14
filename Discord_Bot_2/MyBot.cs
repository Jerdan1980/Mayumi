using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;

namespace Discord_Bot
{
    class MyBot
    {
        //declarations
        static DiscordClient discord;
        static CommandsNextModule commands;

        static void Main(string[] args)
        {
            MainAsync(args).ConfigureAwait(false).GetAwaiter().GetResult();
        }

        static async Task MainAsync(string[] args)
        {
            //instatiates discord client
            discord = new DiscordClient(new DiscordConfiguration {
                Token = "",
                TokenType = TokenType.Bot,
                UseInternalLogHandler = true,
                LogLevel = LogLevel.Debug
            });

            //command string
            commands = discord.UseCommandsNext(new CommandsNextConfiguration {
                StringPrefix = ";;",
                EnableMentionPrefix = true
            });

            commands.RegisterCommands<MyBot>();

            await discord.ConnectAsync();
            await Task.Delay(-1);
        }
    }
}
