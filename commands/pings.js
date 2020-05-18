module.exports = {
	name: 'pings',
	description: 'Pings multiple times!',
	args: true,
	usage: '<number of pings>',
	cooldown: 60,
	execute(message, args) {
		if(args[0] <= 300) {
			let reply = '';
			for (i = 0; i < args[0]; i++) {
				reply += 'Pong.\n';
			}
			message.channel.send(reply);
		} else {
			message.channel.send("Too many pings. Keep it under 300 inclusive.");
		}
	}
}