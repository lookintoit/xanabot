from discord.ext import commands
import discord
import io
import aiohttp

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
        if(len(ctx.message.attachments) == 0):
            await ctx.invoke(bot.get_command('botAnnounce'), role=role, message=message)
            print("sending message")
        elif(len(ctx.message.attachments) > 0):
            await ctx.invoke(bot.get_command('botFileAnnounce'), role=role, message=message)
            print('sending message and data')
            
            
            
    @bot.command()
    @commands.has_role("bot")
    async def botAnnounce(ctx, role, message):
        rolesObj = ctx.guild.roles
        for roles in rolesObj:
            #   if role is role set in parameter
            if roles.name == role:
                #   gets members in roles as a list
                memberList = roles.members
                #   goes through list and sends private message
                for member in memberList:
                    try:
                        await member.send(message)
                    except: pass
                    
    @bot.command()
    @commands.has_role("bot")
    async def botFileAnnounce(ctx, role, message):
        filesList = []
        rolesObj = ctx.guild.roles
        #   grabs the files and sends them to a list as binary
        for i in range(0, len(ctx.message.attachments)):
            async with aiohttp.ClientSession() as session:
                async with session.get(ctx.message.attachments[i].url) as resp:
                    if resp.status != 200:
                        print("can't download")
                    else:
                        data = io.BytesIO(await resp.read())
                        #   turns the data into a discord file object
                        discData = discord.File(fp = data, filename=ctx.message.attachments[i].filename)
                        #   adds discord file object into a list
                        filesList.append(discData)
        #   sends the files to users
        for roles in rolesObj:
            #   if role is role set in parameter
            if roles.name == role:
                #   gets members in roles as a list
                memberList = roles.members
                #   goes through list and sends private message
                for member in memberList:
                    try:
                        #   sends discord file object
                        await member.send(files = filesList)
                    except: pass
                    

#   runs bot
def run_bot():
    testbee(bot)
    #   
    #   insert token here
    bot.run("")
    #
if __name__ == '__main__':
    run_bot()
