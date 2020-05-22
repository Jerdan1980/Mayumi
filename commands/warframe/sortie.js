const axios = require('axios');

module.exports = {
	name: 'railjack',
	description: 'Get today\'s sortie',
	execute(message, args) {
		try {
			axios.get('https://api.warframestat.us/pc')
				.then((response) => {
					const body = response.data.sortie.variants;

					if(args[1] && args[1].toLowerCase() === 'full') {
						const embed = new Discord.MessageEmbed()
							.setTitle("Today's sortie")
							.addFields (
								{name: `Mission 1: **${body[0].missionType}**`, value: `${body[0].node}, ${body[0].modifier}`},
								{name: `Mission 2: **${body[1].missionType}**`, value: `${body[1].node}, ${body[1].modifier}`},
								{name: `Mission 3: **${body[2].missionType}**`, value: `${body[2].node}, ${body[2].modifier}`},
							);

						return message.channel.send(embed);
					} else {
						return message.channel.send(`Today's sortie: ${body[0].missionType}, ${body[1].missionType}, ${body[2].missionType}`);
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