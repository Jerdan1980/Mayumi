const axios = require('axios');

module.exports = {
	name: 'nightwave',
	description: 'Check nightwave status',
	execute(message, args) {
		try {
			axios.get('https://api.warframestat.us/pc')
				.then((response) => {
					const body = response.data.nightwave;

					if(body.active) {
						const embed = new Discord.MessageEmbed()
							.setTitle("Today's nightwave")
							.addFields (
								body.activeChallenges.map((challenge) => {
									return {
										name: `**${challenge.title}**: ${challenge.isDaily ? 'Daily' : 'Weekly'}, ${challenge.reputation}`,
										value: challenge.desc
									}
								})
							);

						return message.channel.send(embed);
					} else {
						return message.channel.send("Nightwave is not active currently.");
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