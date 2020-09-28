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

        # get the message
        myMessage = message.content.lower()

        commandDict = {
            "foo": mFoo,
            "bar": mBar,
        }
        for key in commandDict:
            if key in myMessage:
                await commandDict[key](myMessage)
        # then check whether we have to run a command