const Discord = require('discord.js');

module.exports = {
	name: 'avatar',
	description: 'Get the avatar URL of the tagged user(s), or your own avatar.',
	aliases: ['icon', 'pfp'],
	cooldown: 5,
	execute(message) {
		if(!message.mentions.users.size) {
			const embed = new Discord.MessageEmbed()
				.setTitle('Your avatar:')
				.setImage(message.author.displayAvatarURL({ dynamic: true }));
			return message.channel.send(embed);
		}

		const avatarList = message.mentions.users.map(user => {
			return `${user.username}'s avatar: <${user.displayAvatarURL({ dynamic: true })}>`;
		})

		message.channel.send(avatarList);
	}
}