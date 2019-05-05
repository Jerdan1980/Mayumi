require 'discordrb'
require 'json'

print "token json filepath: "
filepath = gets
tokens = JSON.parse(File.read(filepath.chomp))

bot = Discordrb::Commands::CommandBot.new token: tokens['discord'], prefix: tokens['prefix']

#end this man's whole career
bot.command(:stop, help_available: false) do |event|
    break unless event.user.id == tokens['author ID']
    bot.send_message(event.channel.id, "Bot is shutting down!")
    exit
end

#taken from discordrb examples
bot.command(:ping) do |event|
    m = event.respond('Pong!')
    m.edit "Pong! Time taken: #{Time.now - event.timestamp} seconds."
end

#dice roll command, modified from discordrb examples
bot.command(:roll, description: 'rolls dice', usage: 'roll NdS', min_args: 1) do |event, dnd_roll|
    #parse input using regex
    number, sides, modifier = dnd_roll.split(/[d\+\-]/)
    
    #check input
    next 'Invalid syntax. Try: `roll 1d6`' unless number && sides
    begin
        number = Integer(number)
        sides = Integer(sides)
    rescue ArgumentError
        next 'You must pass two **numbers**. Try: `roll 1d6`'
    end

    #roll dice
    rolls = Array.new(number) { rand(1..sides) }
    sum = rolls.reduce(:+)

    if modifier
        #check input
        begin
            modifier = Integer(modifier)
        rescue ArgumentError
            next 'You must pass three **numbers**. Try: `roll 1d6+4`'
        end

        #check sign of modifier
        if dnd_roll.include? "-"
            modifier *= -1
        end

        #output
        event << "You rolled: `#{rolls} + (#{modifier})`"
        event << "Total: **#{sum + modifier}**"
    else
        #output
        event << "You rolled: `#{rolls}`"
        event << "Total: **#{sum}**"
    end
end

bot.command(:pfp) do |event|
    bot.send_file(event.channel.id, File.open("Mayumi pfp.png", 'r'), caption: "HELLO WORLD")
end

bot.command(:draw) do |event|
	"WIP"
end


bot.run
