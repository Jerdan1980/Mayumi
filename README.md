# Mayumi
A multipurpose discord bot
[Add Mayumi to your server](https://discordapp.com/api/oauth2/authorize?client_id=316084155182219265&permissions=67492864&scope=bot)

# Hosting Mayumi
## Requirements
Mayumi requires Anaconda (python 3.6.8), rdkit, and discord.py.
1. Install [Anaconda](https://www.anaconda.com/distribution/#download-section)
2. Open terminal and run
```
conda create -c rdkit my-env-name rdkit
conda activate my-env-name
conda install pip
```
3. Use `which pip` to ensure that the current pip is located at the current virtual environment, then run `pip install discord.py`
4. Create your own [tokens.json](./sampletoken.json) file somewhere in your system
## Running the code
1. Open terminal and run `driver3.py` on the environment
```
conda activate my-env-name
python driver3.py
```
2. It will ask for the tokens filepath. Type in the filepath to your `tokens.json` file. The terminal will then say `Loaded!`

# FAQ
## How can I help?
* **I found a bug!** _If there are problems, submit an issue to this repo._
* **I want something implemented!** _Submit an issue to this repo and I'll see what i can do._
* **Mayumi is offline! What do I do?** _This is normal, please do not worry._
* **I want to contribute!** _Thank you! Feel free to contact Jerdan1980 or submit new/fixed code as an issue._

## Whats with the versions?
Mayumi v1 is my first crack at making a discord bot. It used C# and while functional could only run on windows machines. I didn't have a suitable computer to run it 24/7 and quit after getting tired of boot up and install times.
I created Mayumi v2 and Aria as v1's python counterpart. I got too busy with irl stuff so I couldn't continue working on it.
Mayumi v3 still uses and is centered around supporting a chemistry server. Aria is used as a tester bot as to avoid disturbing servers.
