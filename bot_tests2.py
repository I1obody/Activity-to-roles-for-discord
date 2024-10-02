import discord
import discord.member
import discord.guild
from discord import Activity
from discord import Member
from discord.ext import tasks
from discord.app_commands import checks
from discord import Role
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get

intents = discord.Intents.all()
intents.presences = True
intents.message_content = True
global ID
global activ

class LoopForActivity(discord.Client):
    @tasks.loop(seconds = 3)
    async def activity_roles(self, ctx):
            global activ
            i = 0
            id_list=[]
            for i in range(len(ctx.guild.members)):
                id_list.append(ctx.guild.members[i])
                members = id_list[i]
                member = ctx.guild.get_member_named(str(members))
                try:                            
                    global activ
                    activ = member.activity.name
                    role = member.roles
                    if member.bot == False:                    
                        if member.status == discord.Status.online:
                            
                            if activ != None:
                                a = get(role, name = activ)
                                print (a)
                                try:
                                    if get(role, name = activ) == None:              
                                        await ctx.guild.create_role(name = str(activ), hoist = True, mentionable = True)                                                                                                                                  
                                        ID = get ( ctx.guild.roles, name = str(activ) )
                                        await ctx.role.edit(position = 1)
                                        await member.add_roles(ID)
                                    elif get(role, name = activ) != None:
                                        await member.add_roles(get(role, name = activ))
                                        await ctx.role.edit(position = 1)
                                except AttributeError:
                                    LoopForActivity
                except AttributeError:
                    LoopForActivity
                
    @activity_roles.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()
        

    async def on_message(self, message):
        if message.content.startswith('!me'):
            self.activity_roles.start(message)
    
    
    

client = LoopForActivity(intents = discord.Intents.all())
client.run('YOURS_BOT_TOKEN_HERE')            