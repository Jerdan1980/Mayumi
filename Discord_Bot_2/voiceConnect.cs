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

namespace Discord_Bot
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
            {
                await ctx.RespondAsync("I'm already connected in this channel!");
                return;
            }
            var chn = ctx.Member?.VoiceState?.Channel;
            if(chn == null)
            {
                await ctx.RespondAsync("You need to be in a voice channel -_-");
                return;
            }
            //notify
            await ctx.RespondAsync("I have joined!");
            vnc = await vNext.ConnectAsync(chn);
        }

        [Command("greet"), Description("says hello in VC")]
        public async Task Greet(CommandContext ctx)
        {
            var vNext = ctx.Client.GetVoiceNextClient();
            if(vNext == null)
            {
                await ctx.RespondAsync("VNext is not enabled or configured.");
                return;
            }
            // check whether we aren't already connected
            var vnc = vNext.GetConnection(ctx.Guild);
            if(vnc == null)
            {
                // already connected
                await ctx.RespondAsync("Not connected in this guild.");
                return;
            }
            //pick a hello
            Random rng = new Random();
            String sound;
            if(rng.Next(2) == 0)
                sound = "..\\resources\\voice_sample_use\\Hello.wav";
            else
                sound = "..\\resources\\voice_sample_use\\Hello 2.wav";
            if(!File.Exists(sound))
                throw new FileNotFoundException("File was not found");
            //says hello
            await vnc.SendSpeakingAsync(true);
            Exception exc = null;
            try
            {
                var ffmpeg_inf = new ProcessStartInfo {
                    FileName = "ffmpeg",
                    Arguments = $"-i \"{sound}\" -ac 2 -f s16le -ar 48000 pipe:1",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true
                };
                var ffmpeg = Process.Start(ffmpeg_inf);
                var ffout = ffmpeg.StandardOutput.BaseStream;
                //buffers ffmpeg output
                using(var ms = new MemoryStream())
                {
                    await ffout.CopyToAsync(ms);
                    ms.Position = 0;

                    var buff = new byte[3840]; // buffer to hold the PCM data
                    var br = 0;
                    while((br = ms.Read(buff, 0, buff.Length)) > 0)
                    {
                        if(br < buff.Length) // it's possible we got less than expected, let's null the remaining part of the buffer
                            for(var i = br; i < buff.Length; i++)
                                buff[i] = 0;

                        await vnc.SendAsync(buff, 20); // we're sending 20ms of data
                    }
                }
            }
            catch (Exception e) { exc = e; }
            finally
            {
                await vnc.SendSpeakingAsync(false);
            }
            if(exc != null)
                await ctx.RespondAsync($"An exception occured during playback: `{exc.GetType()}: {exc.Message}`");
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
            if(!File.Exists(sound))
                throw new FileNotFoundException("File was not found");
            //open ffmpeg
            await vnc.SendSpeakingAsync(true);
            var psi = new ProcessStartInfo {
                FileName = "ffmpeg",
                Arguments = $@"-i ""{sound}"" -ac 2 -f  s16le -ar 48000 pipe:1",
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
