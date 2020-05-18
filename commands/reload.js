const {authors} = require('../config.json');

module.exports = {
	name: 'reload',
	description: 'Reloads a command',
	args: true,
	execute(message, args) {
		const commandName = args[0].toLowerCase();
		const command = message.client.commands.get(commandName) || 
			message.client.commands.find(cmd => cmd.aliases && cmd.aliases.includes(commandName));
		
		if(!authors.includes(message.author.id.toString())) {
			return message.channel.send(`${message.author}, you do not have permission to use the reload command!`);
		}

		if(!command) {
			return message.channel.send(`There is no command with name or alias\`${commandName}\`, ${message.author}!`);
		}

		delete require.cache[require.resolve(`./${command.name}.js`)];

		try {
			const newCommand = require(`./${command.name}.js`);
			message.client.commands.set(newCommand.name, newCommand);
			message.channel.send(`Command \`${command.name}\` was reloaded!`);
		} catch (error) {
			console.log(error);
			message.channel.send(`There was an error while reloading a command \`${command.name}\`:\n\`${error.message}\``);
		}
	}
}