const axios = require('axios');
const Discord = require('discord.js');

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

							return message.channel.send(data, {split: true});
						})
						.catch((error) => {
							return message.channel.send(`Error: \`${error}\``);
						});	
				} catch (error) {
					return message.channel.send(`Error: \`${error}\``)
				}
				break;
			case 'railjack':
			case 'rj':
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
							return message.channel.send(`Error: \`${error}\``);
						});	
				} catch (error) {
					return message.channel.send(`Error: \`${error}\``)
				}
				break;
			case 'sortie':
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
							return message.channel.send(`Error: \`${error}\``);
						});	
				} catch (error) {
					return message.channel.send(`Error: \`${error}\``)
				}
				break;
			case 'baro':
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
									data.push(`__${item.ItemType}__ ${item.PrimePrice} ducats and ${item.RegularPrice} credits`);
								});
								data.push(`_Leaving in ${body.endString}~_`);

								return message.channel.send(embed);
							}
						})
						.catch((error) => {
							return message.channel.send(`Error: \`${error}\``);
						});	
				} catch (error) {
					return message.channel.send(`Error: \`${error}\``)
				}
				break;
			break;
			default:
				message.channel.send('Incorrect arguments. please try again.');
		}
	}
}