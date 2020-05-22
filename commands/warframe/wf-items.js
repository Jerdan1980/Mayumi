module.exports = {
	name: 'item',
	aliases: ['items'],
	description: 'Grabs an item',
	args: true,
	execute(message, args) {
		let itemName = Array.isArray(args) ? args.join(' ') : args;
		itemName = itemName.split('|').join('').trim();
		message.channel.send(`Item: \`${itemName}\``);
	}
}