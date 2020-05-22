const fs = require('fs');
//const axios = require('axios');
const Discord = require('discord.js');

const commands = new Discord.Collection();

//grab subcommands
const commandFiles = fs.readdirSync('./commands/warframe').filter(file => file.endsWith('.js'));
for (const file of commandFiles) {
	const command = require(`./warframe/${file}`);
	//set a new item in the Collection
	//with the key as the command name and the value as the exported modlue
	commands.set(command.name, command);
}

module.exports = {
	name: 'warframe',
	aliases: ['wf'],
	description: 'All the stuff about warframe!',
	args: true,
	usage: `<sub-command>`,
	cooldown: 10,
	execute(message, args) {
		//check if command exists
		const command = commands.get(args[0]) || 
			commands.find(cmd => cmd.aliases && cmd.aliases.includes(args[0]));
		if (!command) {
			return message.reply('Command does not exist!');
		}

		//if so, remove the wf argument
		args.shift();

		//check if guild only command
		if (command.guildOnly && message.channel.type !== 'text') {
			return message.reply('I can\'t execute that command inside DMs!');
		}

		//check for correct number of arguments
		if (command.args && !args.length) {
			let reply = `You didn't provide any arguments, ${message.author}!`;
			//add usage for good UX
			if (command.usage) {
				reply += `\nThe proper usage would be: \`${prefix}${command.name} ${command.usage}\``;
			}
			return message.channel.send(reply)
		}

		//actually run the command
		try {
			command.execute(message, args);
		} catch (error) {
			console.error(error);
			message.reply('there was an error trying to execute that command!');
		}
	}
}

function formatError(err) {
	const embed = new Discord.MessageEmbed()
		.setTitle("Error")
		.setDescription (err);

	return embed;
}