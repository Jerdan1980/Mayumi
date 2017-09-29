using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Diagnostics;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using DSharpPlus.Entities;
using DSharpPlus.VoiceNext;

namespace Discord_Bot_2
{
    class voiceConnect
    {
        [Command("join"), Description("Joins VC")]
        public async Task Join(CommandContext ctx)
        {
            //create voice client
            var vNext = ctx.Client.GetVoiceNextClient();
            //check for connections
            var vnc = vNext.GetConnection(ctx.Guild);
            if(vnc != null)
                throw new InvalidOperationException("Already connected in this guild");
            var chn = ctx.Member?.VoiceState?.Channel;
            if(chn == null)
                throw new InvalidOperationException("You need to be in a voice channel");
            //notify
            await ctx.RespondAsync("I'm joined!");

            //pick a hello
            vnc = await vNext.ConnectAsync(chn);
            Random rng = new Random();
            String sound;
            if(rng.Next(2) == 0)
                sound = "..\\resources\\voice_sample_use\\Hello.wav";
            else
                sound = "..\\resources\\voice_sample_use\\Hello 2.wav";
            if(File.Exists(sound))
                throw new FileNotFoundException("File was not found");
            //open ffmpeg
            await vnc.SendSpeakingAsync(true);
            var psi = new ProcessStartInfo {
                FileName = "ffmpeg",
                Arguments = $@"-i ""{sound}"" -ac 2 -f  sl6le -ar 48000 pipe:l",
                RedirectStandardOutput = true,
                UseShellExecute = false
            };
            var ffmpeg = Process.Start(psi);
            var ffout = ffmpeg.StandardOutput.BaseStream;
            //say hello
            var buff = new byte[3840];
            var br = 0;
            while((br = ffout.Read(buff, 0, buff.Length)) > 0)
            {
                if(br < buff.Length) //not a full sample, mute the rest
                    for(var i = br; i < buff.Length; i++)
                        buff[i] = 0;

                await vnc.SendAsync(buff, 20);
            }
            await vnc.SendSpeakingAsync(false);

        }

        [Command("leave"), Description("Leaves VC")]
        public async Task Leave(CommandContext ctx)
        {
            //create voice client
            var vNext = ctx.Client.GetVoiceNextClient();
            var chn = ctx.Member?.VoiceState?.Channel;
            //check connections
            var vnc = vNext.GetConnection(ctx.Guild);
            if(vnc == null)
                throw new InvalidOperationException("Not connected in this guild.");

            //pick a goodbye
            vnc = await vNext.ConnectAsync(chn);
            Random rng = new Random();
            String sound;
            if(rng.Next(2) == 0)
                sound = "..\\resources\\voice_sample_use\\Goodbye.wav";
            else
                sound = "..\\resources\\voice_sample_use\\Goodbye 2.wav";
            if(File.Exists(sound))
                throw new FileNotFoundException("File was not found");
            //open ffmpeg
            await vnc.SendSpeakingAsync(true);
            var psi = new ProcessStartInfo {
                FileName = "ffmpeg",
                Arguments = $@"-i ""{sound}"" -ac 2 -f  sl6le -ar 48000 pipe:l",
                RedirectStandardOutput = true,
                UseShellExecute = false
            };
            var ffmpeg = Process.Start(psi);
            var ffout = ffmpeg.StandardOutput.BaseStream;
            //say goodbye
            var buff = new byte[3840];
            var br = 0;
            while((br = ffout.Read(buff, 0, buff.Length)) > 0)
            {
                if(br < buff.Length) //not a full sample, mute the rest
                    for(var i = br; i < buff.Length; i++)
                        buff[i] = 0;

                await vnc.SendAsync(buff, 20);
            }
            await vnc.SendSpeakingAsync(false);

            //Disconnect
            vnc.Disconnect();
            await ctx.RespondAsync("I've left!");
        }
    }
}
