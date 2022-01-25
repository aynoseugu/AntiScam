from discord.ext import commands
from AntiScam import AntiScam
whitelist = [758089372976545854] 
logs_channel = 935625148525051917
bot = commands.Bot(command_prefix='d;')
bot.remove_command('help') 
@bot.listen()
async def on_message(buenas):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='935640727776534608', verified_role='935640653432516719', logs_channel=935625148525051917) 
bot.run('OTM1NjMwODIyNTQxNzcwODAy.YfBcGw.Y9vBWCk_Qovtbcs79Qdw6qF0NOM')
