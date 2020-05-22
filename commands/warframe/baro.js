const axios = require('axios');

module.exports = {
	name: 'baro',
	description: 'Check for baro',
	execute(message, args) {
		try {
			axios.get('https://api.warframestat.us/pc')
				.then((response) => {
					const body = response.data.voidTrader;
					
					if(!body.active) {
						return message.channel.send(`Baro arriving in ${body.startString}`);
					} else {
						const data = []
						data.push("**Baro's inventory:**");
						body.inventory.map((item) => {
							data.push(`__${item.item}__ ${item.ducats} ducats and ${item.credits / 1000}k credits`);
						});
						data.push(`_Leaving in ${body.endString}~_`);

						return message.channel.send(data);
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