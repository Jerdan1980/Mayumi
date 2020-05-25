const axios = require('axios');
const Discord = require('discord.js');

//sort data
const relics = ['Lith', 'Meso', 'Neo', 'Axi', 'Requiem'];
const frames = ['Systems', 'Chassis', 'Neuroptics', 'Blueprint'];
	

module.exports = {
	name: 'items',
	aliases: ['item', 'drop', 'drops'],
	description: 'Gets drop data',
	args: true,
	usage: '<item|location>',
	execute(message, args) {
		//clean up inputs to a single query
		let itemName = Array.isArray(args) ? args.join(' ') : args;
		itemName = itemName.split('|').join('').trim();
		//modify args for relics to be easier
		//may seem backwards but ensures everything works
		args = itemName.split(' ');

		//check if relic. should be ["Type", "Name"]
		if(relics.includes(args[0])) {
			try {
				axios.get(`https://drops.warframestat.us/data/relics/${args[0]}/${args[1]}.json`)
					.then((response) => {
						const body = response.data.rewards.Intact;
						
						const data = [];
						data.push(`Relic ${args[0]} ${args[1]}`);
						data.push(`**Common:** ${body.filter(drop => drop.chance === 25.33).map(drop => drop.itemName).join()}`);
						data.push(`**Uncommon:** ${body.filter(drop => drop.chance === 11).map(drop => drop.itemName).join()}`);
						data.push(`**Rare:** ${body.filter(drop => drop.chance === 2).map(drop => drop.itemName).join()}`);
	
						return message.channel.send(data, {split: true});
					})
					.catch((error) => {
						return message.channel.send(formatError(error));
					});	
			} catch (error) {
				return message.channel.send(formatError(error))
			}
		}

		//has to be an item. check if mod or frame
		//check for primes, which doesnt work
		else if(itemName.includes('Prime')) {
			return message.channel.send(`${itemName} is **prime**, so it does not drop.`);
		} else if(frameCheck(itemName)) {
			try {
				axios.get(`https://drops.warframestat.us/data/blueprintLocations.json`)
					.then((response) => {
						const body = response.data.blueprintLocations.find(bp => bp.blueprintName === itemName);
						const embed = new Discord.MessageEmbed();
						
						if(!body) {
							//not found
							const embed = new Discord.MessageEmbed()
								.setTitle(`${itemName} was not found!`)
								.setDescription(`Check for typos and capitalization.`);
							return message.channel.send(embed);
						} else {
							const embed = new Discord.MessageEmbed()
								.setTitle(`${itemName}`)
								.addFields(
									body.enemies.map(enemy => {
										return {
											name: `${enemy.enemyName}`,
											value: `${enemy.rarity}: ${enemy.chance}%`,
											inline: true
										}
									})
								);
							return message.channel.send(embed);
						}
					})
					.catch((error) => {
						return message.channel.send(formatError(error));
					});	
			} catch (error) {
				return message.channel.send(formatError(error))
			}
		}
		else {
			try {
				axios.get(`https://drops.warframestat.us/data/modLocations.json`)
					.then((response) => {
						const body = response.data.modLocations.find(mod => mod.modName === itemName);					
						
						if(!body) {
							//not found
							const embed = new Discord.MessageEmbed()
								.setTitle(`${itemName} was not found!`)
								.setDescription(`Check for typos and capitalization.`);
							return message.channel.send(embed);
						} else {
							const embed = new Discord.MessageEmbed()
								.setTitle(`${itemName}`)
								.addFields(
									body.enemies.map(enemy => {
										return {
											name: `${enemy.enemyName}`,
											value: `${enemy.rarity}: ${enemy.chance}%`,
											inline: true
										}
									})
								);
							return message.channel.send(embed);
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
}

function formatError(err) {
	const embed = new Discord.MessageEmbed()
		.setTitle("Error")
		.setDescription (err);

	return embed;
}

function frameCheck(str) {
	let found = false;
	frames.forEach(f => {if(str.includes(f)) found = true});
	return found;
}