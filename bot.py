import disnake
from disnake.ext import commands
from disnake.ext.commands import CommandSyncFlags

import config

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

sync_flags = CommandSyncFlags.default()

bot = commands.Bot(command_prefix='!', intents=intents, command_sync_flags=sync_flags)

@bot.event
async def on_ready():
    print(f"{bot.user} ")

initial_extensions = [
    "commands.voice",
    "commands.creativity",
    "commands.poster"
]

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f" {extension}: {e}")

bot.run(config.BOT_TOKEN)
