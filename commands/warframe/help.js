module.exports = {
	name: 'help',
	description: 'help',
	execute(message, args) {
		message.channel.send('Commands include baro, nightwave, ralijack, sortie and time.');
	}
}
