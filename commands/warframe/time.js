const axios = require('axios');

module.exports = {
	name: 'time',
	description: 'Get the world state',
	execute(message, args) {
		try {
			axios.get('https://api.warframestat.us/pc')
				.then((response) => {
					const body = response.data;
					
					const data = [];
					data.push("Here are the worldstates:");
					data.push(`**Earth:** ${body.earthCycle.state} for ${body.earthCycle.timeLeft}`);
					data.push(`**Cetus:** ${body.cetusCycle.state} for ${body.cetusCycle.timeLeft}`);
					data.push(`**Orb Vallis:** ${body.vallisCycle.state} for ${body.vallisCycle.timeLeft}`);

					return message.channel.send(data, {split: true});
				})
				.catch((error) => {
					return message.channel.send(formatError(error));
				});	
		} catch (error) {
			return message.channel.send(formatError(error))
		}
	}
}

function formatError(err) {
	const embed = new Discord.MessageEmbed()
		.setTitle("Error")
		.setDescription (err);

	return embed;
}