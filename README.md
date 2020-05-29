# Mayumi
A multipurpose discord bot
[Add Mayumi to your server](https://discordapp.com/api/oauth2/authorize?client_id=316084155182219265&permissions=67492864&scope=bot)

# Hosting Mayumi
## Requirements
 - Python 3.8.0+
Highly recommended to use virtual environments like ven

## Installation
1. Clone the github repo
2. Install packages in [requirements.txt](requirements.txt). I will be using venv here  
  a. Open terminal  
	b. Run `python3 -m venv ./`  
	c. Activate it  
	- Windows: `cd ./Scripts` then `activate`
	- Unix: `source ./bin/activate`
	d. Run `pip install -r requirements.txt` on the main directory
3. Create your own [config.json](./sampleconfig.json)
## Running the code
1. Activate the venv (steps 2c and 2d in Installation)
2. Open terminal and run `python3 bot.py` on the main directory

# FAQ
## How can I help?
* **I found a bug!** _If there are problems, submit an issue to this repo._
* **I want something implemented!** _Submit an issue to this repo and I'll see what i can do._
* **Mayumi is offline! What do I do?** _This is normal, please do not worry._
* **I want to contribute!** _Thank you! Feel free to contact Jerdan1980 or submit new/fixed code as an issue._

## Whats with the versions?
- Mayumi v1 is my first crack at making a discord bot. It used C# and while functional could only run on windows machines. I didn't have a suitable computer to run it 24/7 and quit after getting tired of boot up and install times.
- I created Mayumi v2 and Aria as v1's python counterpart. I got too busy with irl stuff so I couldn't continue working on it.
- Mayumi v3 is centered around supporting a chemistry server. Aria is used as a tester bot as to avoid disturbing servers. I gave up because anaconda was a pain to work with.
- Mayumi v4 uses javascript for easier installation and hosting as npm greatly speeds up package management.
- Mayumi v5 is more or less a rewrite of v3, as it uses python. Javascript has a great lack in chemistry packages and AJAX/AJAJ was too much work for a discord bot like this. This time im using venv which is more or less native, more intuitive (imo), and doesnt have a ton of extra apps that you dont need to use on it.