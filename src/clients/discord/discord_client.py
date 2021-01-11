import discord


class DiscordClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(activity = discord.Game('🍵'))

    async def on_message(self, message):
        # bot won't respond to itself
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
