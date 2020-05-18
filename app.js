const Discord = require('discord.js');
const client = new Discord.Client();

const fs = require('fs');

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('pong');
  }
});

fs.readFile('config.json', 'utf8', (err, data) => {
	if (err) throw err;
	let config = JSON.parse(data);
	console.log(config);
	client.login(config['discord']);
})