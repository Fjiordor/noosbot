import discord


class NoosClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to discord')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hello {member.name}, welcome to the Noosphere\n'
            f'praise the Omnissiah'
        )

    async def on_message(self, message):
        # avoiding loops
        if message.author == self.user:
            return

        # define command functions here

        async def mFoo(myMessage):
            print(f'mFoo got triggered by {myMessage}')
            await message.channel.send('bar')

        async def mBar(myMessage):
            print(f'mBar got triggered by {myMessage}')
            await message.channel.send('foo')

        # map the functions to command strings
        commandDict = {
            "foo": mFoo,
            "bar": mBar,
        }

        # get the message
        myMessage = message.content.lower()

        # check message for defined commands and execute them.
        for key in commandDict:
            if key in myMessage:
                await commandDict[key](myMessage)

    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = payload.member.guild#discord.utils.find(lambda g: g.id == guild_id, self.guilds)

        #funkctions for emotes

        async def addRoleBasic():

            await payload.member.add_roles(discord.utils.get(guild.roles, name='Servitor'))

        async def defaultFun():
            print(f'emote payload not parsed :\n{payload}')

        async def addRoleProg():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='CODING'))

        async def addRoleMV():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='MINECRAFT'))

        async def addRoleMM():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='MODDED MINECRAFT'))

        async def addRoleFactorio():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='FACTORIO'))

        async def addRoleDRG():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='DEEP ROCK GALACTIC'))

        async def addRoleAU():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='AMONG US'))

        async def addRoleDotA2():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='DOTA'))

        async def addRoleLeague():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='LEAGUE'))

        async def addRoleStellaris():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='STELLARIS'))

        async def addRoleBorderlands():
            await payload.member.add_roles(discord.utils.get(guild.roles, name='BORDERLANDS'))

        emoteDictBasic = {
        '☑️': addRoleBasic
        }

        emoteDictChannelRoles = {
            'Bash': addRoleProg,
            'Minecraft': addRoleMV,
            'Forge': addRoleMM,
            'Factorio': addRoleFactorio,
            'DeepRock': addRoleDRG,
            'Amongus': addRoleAU,
            'Dota2': addRoleDotA2,
            'League': addRoleLeague,
            'Stellaris': addRoleStellaris,
            'Borderlands': addRoleBorderlands,
        }

        messageDict = { #match message ids to emote dicts
            760367376046096394: emoteDictBasic,
            762377842423627798: emoteDictChannelRoles,
        }
        defaultDict = {

        }


        await messageDict.get(message_id, defaultDict).get(payload.emoji.name, defaultFun)()




    async def on_raw_reaction_remove(self, payload):
        pass
