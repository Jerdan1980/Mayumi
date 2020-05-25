const fs = require('fs');
const Discord = require('discord.js');
const {discord, prefix} = require('./config.json')

const client = new Discord.Client();
client.commands = new Discord.Collection();

//grab all the commands
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	//set a new item in the Collection
	//with the key as the command name and the value as the exported modlue
	client.commands.set(command.name, command);
}
//that one command
const wfItems = require('./commands/warframe/items.js');

const cooldowns = new Discord.Collection();
let wfRegexp = /\|[\w\s]+\|(?!\|)/gim; //regex for wf-items

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', message => {
	//make sure its not a bot first!
	if(message.author.bot) return;

	//check for wf item
	if(wfRegexp.test(message.content)) {
		message.content.match(wfRegexp).forEach(item => {
			try {
				wfItems.execute(message, item);
			} catch (error) {
				console.error(error);
				message.reply('there was an error trying to execute that command!');
			}
		});
		return
	}

	//parse messages for commands
	if (!message.content.startsWith(prefix)) return;
	const args = message.content.slice(prefix.length).split(/ +/);
	const commandName = args.shift().toLowerCase();

	//checks if command exists
	const command = client.commands.get(commandName) || 
		client.commands.find(cmd => cmd.aliases && cmd.aliases.includes(commandName));
	if (!command) {
		return message.reply('Command does not exist!');
	}

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

	//handle cooldowns
	if (!cooldowns.has(command.name)) {
		cooldowns.set(command.name, new Discord.Collection());
	}
	const now = Date.now();
	const timestamps = cooldowns.get(command.name);
	const cooldownAmount = (command.cooldown || 1) * 1000;
	if (timestamps.has(message.author.id)) {
		const expirationTime = timestamps.get(message.author.id) + cooldownAmount;

		if (now < expirationTime) {
			const timeLeft = (expirationTime - now) / 1000;
			return message.reply(`please wait ${timeLeft.toFixed(1)} more second(s) before reusing the \`${command.name}\` command.`);
		}
	}
	timestamps.set(message.author.id, now);
	setTimeout(() => timestamps.delete(message.author.id), cooldownAmount);

	//actually run the command
	try {
		command.execute(message, args);
	} catch (error) {
		console.error(error);
		message.reply('there was an error trying to execute that command!');
	}
});

client.login(discord);