using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Exceptions;
using DSharpPlus.Entities;
using DSharpPlus.EventArgs;
using DSharpPlus.VoiceNext;
using DSharpPlus.VoiceNext.Codec;

namespace Discord_Bot
{
    class Driver
    {
        //declarations
        static DiscordClient discord;
        static CommandsNextModule commands;
        static VoiceNextClient voice;

        //to run the program
        public static void Main(string[] args)
        {
            var prog = new Driver();
            prog.MayumiAsync().GetAwaiter().GetResult();
        }

        //actual program
        public async Task MayumiAsync()
        {
            //instatiates discord client
            discord = new DiscordClient(new DiscordConfiguration {
                Token = "MzE2MDg0MTU1MTgyMjE5MjY1.DKxCqg.CqhUlPJrPnxFbzb9f9EO_-HdG-c",
                TokenType = TokenType.Bot,
                AutoReconnect = true,
                UseInternalLogHandler = true,
                LogLevel = LogLevel.Debug
            });

            //error checking
            discord.Ready += Client_Ready;
            discord.ClientErrored += Client_Error;

            //enables voice
            var voiceConfig = new VoiceNextConfiguration {
                VoiceApplication = VoiceApplication.Music
            };
            voice = discord.UseVoiceNext(voiceConfig);

            //command string
            commands = discord.UseCommandsNext(new CommandsNextConfiguration {
                StringPrefix = ".",
                EnableMentionPrefix = true
            });

            //errorchecking
            commands.CommandExecuted += Commands_Executed;
            commands.CommandErrored += Commands_Errored;

            //command service
            commands.RegisterCommands<Discord_Bot_2.text>();
            commands.RegisterCommands<Discord_Bot_2.definitions>();
            commands.RegisterCommands<Discord_Bot_2.DnD>();
            commands.RegisterCommands<Discord_Bot_2.voiceConnect>();



            //start program
            await discord.ConnectAsync();
            await Task.Delay(-1);
        }

        private Task Client_Ready(ReadyEventArgs e)
        {
            e.Client.DebugLogger.LogMessage(LogLevel.Info, "Mayumi", "Client is ready to process Events.", DateTime.Now);
            return Task.CompletedTask;
        }

        private Task Client_Error(ClientErrorEventArgs e)
        {
            e.Client.DebugLogger.LogMessage(LogLevel.Error, "Mayumi", $"Exeception Occured: {e.Exception.GetType()}: {e.Exception.Message}", DateTime.Now);
            return Task.CompletedTask;
        }

        private Task Commands_Executed(CommandExecutionEventArgs e)
        {
            e.Context.Client.DebugLogger.LogMessage(LogLevel.Info, "Mayumi", $"{e.Context.User.Username} sucessfully executed '{e.Command.QualifiedName}'", DateTime.Now);
            return Task.CompletedTask;
        }

        private async Task Commands_Errored(CommandErrorEventArgs e)
        {
            e.Context.Client.DebugLogger.LogMessage(LogLevel.Error, "Mayumi", $"{e.Context.User.Username} tried executing '{e.Command?.QualifiedName ?? "<unknown command>"}' but it errored: {e.Exception.GetType()}: {e.Exception.Message ?? "<no message>"}", DateTime.Now);
            
            //check for permissions
            if(e.Exception is ChecksFailedException ex)
            {
                var emoji = DiscordEmoji.FromName(e.Context.Client, ":no_entry:");

                var embed = new DiscordEmbedBuilder {
                    Title = "Access Denied",
                    Description = $"{emoji} You do not have the permissions required to execute this command.",
                    Color = new DiscordColor(0xFF0000)
                };

                await e.Context.RespondAsync("", embed: embed);
            } else
            {
                await e.Context.RespondAsync("Error. Please repeat the question.");
            }
        }

    }
}
