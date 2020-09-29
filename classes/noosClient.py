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

        async def mFoo(myMessageStr):
            print(f'mFoo got triggered by {myMessageStr}')
            await message.channel.send('bar')

        async def mBar(myMessageStr):
            print(f'mBar got triggered by {myMessageStr}')
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
        pass

    async def on_raw_reaction_remove(self, payload):
        pass
