const axios = require('axios');
const Discord = require('discord.js');

module.exports = {
	name: 'railjack',
	aliases: ['rj'],
	description: 'Get the sentient outposts',
	execute(message, args) {
		try {
			axios.get('https://api.warframestat.us/pc')
				.then((response) => {
					const body = response.data.sentientOutposts;
					
					if(body.active) {
						return message.channel.send(`Sentient outpost at \`${body.mission.node}\``);
					} else {
						return message.channel.send(`No sentient outposts active`);
					}
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