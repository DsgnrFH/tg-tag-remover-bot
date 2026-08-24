
# Telegram tag messages remover

This bot will detect and delete every text message containing the tag you provide at the top of `main.py`

# Setup

You will need the library `requests`: `pip install requests`

Inside of `main.py` you can find the following:
- `TOKEN` - You will have to take that from BotFather after creating a bot
- `API` - You can ignore or adjust this if Telegram decides to change it
- `TAG` - The bot will react to any message containing this string
- `IGNORE HUMANS` - Makes the bot ignore any human input. Helpful for only reacting to bots' messages or if you are a sane person nowadays
- `REACT_TO_MESSAGE` - Makes the bot react to the human messages containing the `TAG`. Only works when `IGNORE_HUMANS` is set to `True`.

You can also adjust the emoji reaction. In my case, it is the eyes.

Feel free to contribute or to steal this code.

