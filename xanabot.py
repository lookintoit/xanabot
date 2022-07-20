from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

class testbee(commands.Bot):
    def __init__(self,bot):
        self.bot = bot
        return

    # set te role of those who can use bot
    #replace "mods" with role that should use bot

    @bot.command()
    @commands.has_role("mods")
    async def announce(ctx, role, message):
        #   grabs roles from context 
        rolesObj = ctx.guild.roles
        #   goes through roles
        for roles in rolesObj:
            #   if role is role set in parameter
            if roles.name == role:
                #   gets members in roles as a list
                memberList = roles.members
                #   goes through list and sends private message
                for member in memberList:
                    await member.send(message)

#   runs bot
def run_bot():
    testbee(bot)
    #   
    #   insert token here
    bot.run("")
    #
if __name__ == '__main__':
    run_bot()