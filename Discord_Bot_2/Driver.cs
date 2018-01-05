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
using DSharpPlus.Interactivity;
//using System.Windows.Forms;

namespace Discord_Bot
{
    class Driver
    {
        //declarations
        static DiscordClient discord;
        static CommandsNextModule commands;
        static VoiceNextClient voice;
        //other keys
        public static String OSU_key;
        public static String steam_key;

        //to run the program
        [STAThread]
        public static void Main(string[] args)
        {
            //grabs the token file
            string token = "", okey = "", devkey = "";

            while(true)
            {
            Console.Out.Write(": ");
            string fileName = Console.In.ReadLine();
                if(File.Exists(@fileName))
                {
                    token = File.ReadAllLines(@fileName)[0];
                    okey = File.ReadAllLines(@fileName)[1];
                    devkey = File.ReadAllLines(@fileName)[2];
                    break;
                } else
                    Console.Out.WriteLine("Enter valid file.");
            }

            var prog = new Driver();
            prog.MayumiAsync(token, okey, devkey).GetAwaiter().GetResult();
        }

        //actual program
        public async Task MayumiAsync(string sToken, string o_key, string s_key)
        {
            //instatiates discord client
            discord = new DiscordClient(new DiscordConfiguration {
                Token = sToken,
                TokenType = TokenType.Bot,
                AutoReconnect = true,
                UseInternalLogHandler = true,
                LogLevel = LogLevel.Info
            });

            //enables voice
            //disabled until voice works on linux.
            /*var voiceConfig = new VoiceNextConfiguration {
                VoiceApplication = VoiceApplication.Music
            };
            voice = discord.UseVoiceNext(voiceConfig);*/

            //command string
            commands = discord.UseCommandsNext(new CommandsNextConfiguration {
                StringPrefix = ">",
                EnableMentionPrefix = true
            });

            //errorchecking
            discord.Ready += Client_Ready;
            discord.ClientErrored += Client_Error;
            commands.CommandExecuted += Commands_Executed;
            commands.CommandErrored += Commands_Errored;

            //command service
            commands.RegisterCommands<Discord_Bot.text>();
            commands.RegisterCommands<Discord_Bot.definitions>();
            commands.RegisterCommands<Discord_Bot.DnD>();
            //commands.RegisterCommands<Discord_Bot.voiceConnect>();
            OSU_key = o_key; //osu key
            commands.RegisterCommands<Discord_Bot.osu_connect>();
            steam_key = s_key; //steam key
            commands.RegisterCommands<Discord_Bot.steam_connect>();
            commands.RegisterCommands<Discord_Bot.CBL_connect>();

            //triggers
            discord.MessageCreated += Eight_Ball;

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
        
       private async Task Eight_Ball(MessageCreateEventArgs e)
       {
            if(e.Message.Content.Contains("8ball") || (e.Message.Content.Contains("should") && e.Message.Content.Contains("?")))
            {
                Random rng = new Random();
                string[] data = File.ReadAllLines(@"MayumiYesNo.txt");
                var choice = rng.Next(data.Length);
                await e.Message.RespondAsync(data[choice]);
            }
        }
    }
}
