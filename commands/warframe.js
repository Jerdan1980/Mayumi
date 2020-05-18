const axios = require('axios');

module.exports = {
	name: 'warframe',
	description: 'All the stuff about warframe!',
	args: true,
	aliases: ['wf'],
	cooldown: 10,
	execute(message, args) {
		switch(args[0].toLowerCase()) {
			case 'time':
				try {
					axios.get('https://api.warframestat.us/pc')
						.then((response) => {
							const body = response.data;
							
							const data = [];
							data.push("Here are the worldstates:");
							data.push(`**Earth:** ${body.earthCycle.state} for ${body.earthCycle.timeLeft}`);
							data.push(`**Cetus:** ${body.cetusCycle.state} for ${body.cetusCycle.timeLeft}`);
							data.push(`**Orb Vallis:** ${body.vallisCycle.state} for ${body.vallisCycle.timeLeft}`);

							message.channel.send(data, {split: true});
						})
						.catch((error) => {
							message.channel.send(`Error: \`${error}\``);
						});	
				} catch (error) {
					message.channel.send(`Error: \`${error}\``)
				}
				break;
			default:
				message.channel.send('Incorrect arguments. please try again.');
		}
	}
}