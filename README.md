# Matcha

## What is Matcha?
Matcha is a versatile Discord bot tailored for enhancing interaction and server mangement on Discord platforms. It has features such as music playback, server moderation
and dynamic conversations powered by OpenAI's GPT 4. It is aimed at to make the Discord's community life easier as they not longer need to navigate out of the app to play music or ask a question, everyone can listen, everyone can see!

## Installation

If you'd like, you could invite the Discord bot to your server using this [link](https://discord.com/oauth2/authorize?client_id=1271316963062448254&permissions=3352640&integration_type=0&scope=bot). If not and you would like to add Matcha to your local machine, Please follow the steps below.

### Prerequisites

Before you begin the installation process, ensure you have the following:
- **Python 3.8 or higher**: Install Python from the [official Python website](https://www.python.org/downloads/).
- **git**: Follow the installation instructions on [Git's official site](https://git-scm.com/downloads).
- A **Discord account** and **permissions** to add bots to a server. Create a Discord account at [discord.com](https://discord.com/register) if you don't already have one.

### Step 1: Clone the Repository

Clone the repository using git:

```bash
git clone https://github.com/yourusername/Matcha-Discord-Bot.git
cd Matcha-Discord-Bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install all necessary libraries, such as `discord.py` and `yt-dlp`

### Step 3: Configure Environmental Variables
Create a `.env` file in the root directory of the project. This file will store sensitive information such as your bot's token and OpenAI's API key:

```bash
DISCORD_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

`DISCORD_TOKEN`: Your Discord Bot token can be attained in Discord's [Developer Portal](https://discord.com/developers/applications). Note: Please follow a tutorial if needed as you will need to create your own application and configure it.

`OPENAI_API_KEY`: Your API key from OPENAI can be attained from this [link](https://openai.com/api/). Note: Please follow a tutorial if needed.

### Step 4: Run the bot
To start the bot, run:
```bash
python bot.py
```

If you want to host this bot 24/7, I currently use [Heroku](https://id.heroku.com/login). Cheap/Free 24/7 bot using, $7 dollars a month if you're planning on using it a lot.

### Verify Installation
You can verify the bot installation by using `.hello`, which will send back a message. If replied, that means the bot is installed correctly. 

### Troubleshooting
- Verify that all environmental variables in your `.env` file are correct and respond to valid keys
- Check Python and library versions to ensure compatibility with the bot's requirements

## Usage

### Music Commands
`.play <song>`<br>
`.pause` <br>
`.resume` <br>
`.skip` <br>
`queue` <br>

### General Commands
`.hello` <br>
`.kick @user` <br>
`.ban @user` <br>
`.purge [number]` <br>

### ChatGPT
`.gpt <message>` <br>

## Acknowledgements
- Thanks to OpenAI for the GPT-4 API
- Thanks to Discord.py team for maintaining a useful library and having a support team whenever needed

## Please read
I am currently updating this bot whenever possible. This is honestly a fun personal project that I wanted to do as I've always wondered how to make a Discord bot. There may be many bugs so please let me know if possible. I am currently in the process of adding it to top.gg so that more people can use it and add it to their servers!