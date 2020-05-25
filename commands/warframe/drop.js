const axios = require('axios');
const Discord = require('discord.js');

//sort data
const relics = ['Lith', 'Meso', 'Neo', 'Axi', 'Requiem'];
const missions = new Map([
	['Apollodrius', 'Mercury'],
	["Elion", "Mercury"],
	["Eris", "Xini"],
]);
const standard = ['Assassination', "Capture", "Exterminate", "Hijack", "Mobile Defense", "Rescue", "Sabotage", "Spy"];
const endless = ["Defection", "Defense", "Excavation", "Interception", "Survival"];
	

module.exports = {
	name: 'drop',
	aliases: ['drops'],
	description: 'Gets drop data',
	args: true,
	usage: '<item|location>',
	execute(message, args) {
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
		if(missions.has(args[0])) {
			try {
				axios.get(`https://drops.warframestat.us/data/missionRewards/${missions.get(args[0])}/${args[0]}.json`)
					.then((response) => {
						const body = response.data;
						const data = [];
						
						//split by gamemode
						if(standard.includes(body.gameMode)) {
							data.push(`${missions.get(args[0])} ${args[0]} drops:`);
							body.rewards.forEach(drop => {
								data.push(`**${drop.itemName}** ${drop.chance}%`)
							});
						}
						else {
							data.push('WIP');
						}
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
}

function formatError(err) {
	const embed = new Discord.MessageEmbed()
		.setTitle("Error")
		.setDescription (err);

	return embed;
}