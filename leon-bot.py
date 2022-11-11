import discord
import os
import random

class LeonBot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1040521731363848233
    async def on_ready(self):
        print('I''m online now')

    async def on_message(self, message):
        if message.author == client.user:
            return
    
        if message.content == '$initialize_test1':
            await message.channel.send('<:static_A:1028917751567372348> Static A: 8 members\n<:static_B:1028917728800669696> Static B: 11 members')

        if 'mum' in message.content:
            messages = ["Stop it.",
                        "Get some new jokes ya goddamn clown.",
                        "It would've taken you zero effort to write that.",
                        "\nNice, a total of 11st/nd/rd mum jokes have been said in this server.",
                        "Last warning."]
            await message.channel.send(message.author.mention + " " + random.choice(messages))

        if message.content == '.displayEmbed':
            embed = discord.Embed(
                title = 'Role Assignment',
                description = 'React below to receive assigned roles.',
                colour = discord.Colour.yellow()
            )
            embed.add_field(name='<:static_A:1028917751567372348> Static A', value='Static Leader: Meatbeater\nRaid times: Unspecified evenings', inline=False)
            embed.add_field(name='<:static_B:1028917728800669696> Static B', value='Static Leader: Morgan/Nagao\nRaid times: Unspecified evenings', inline=False)
            embed.add_field(name = chr(173), value = chr(173))
            embed.add_field(name='<:valtan:980480604606972044> Valtan', value='Get pinged for Valtan Normal/Hard lobbies', inline=False)
            embed.add_field(name='<:vykas:999051969643683901> Vykas', value='Get pinged for Vykas Normal/Hard lobbies', inline=False)
            embed.add_field(name='<:clown_emb:1029494684973793360> Clown', value='Get pinged for Kakul-Saydon lobbies', inline=False)
            await message.channel.send(embed=embed)

    async def on_raw_reaction_add(self, payload):

        if payload.message_id != self.target_message_id:
            return
        
        guild = client.get_guild(payload.guild_id)

        if payload.emoji.id == 980480604606972044:
            role = discord.utils.get(guild.roles, name='Valtan')
            await payload.member.add_roles(role)
        elif payload.emoji.id == 999051969643683901:
            role = discord.utils.get(guild.roles, name='Vykas')
            await payload.member.add_roles(role)
        elif payload.emoji.id == 1028917751567372348:
            role = discord.utils.get(guild.roles, name='Static A')
            await payload.member.add_roles(role)
        elif payload.emoji.id == 1028917728800669696:
            role = discord.utils.get(guild.roles, name='Static B')
            await payload.member.add_roles(role)
        else:
            payload.emoji.name == 1029494684973793360
            role = discord.utils.get(guild.roles, name='Clown')
            await payload.member.add_roles(role)
    
    async def displayembed(self):
        embed = discord.Embed(
            title = 'Role Assignment',
            description = 'React below to receive assigned roles.',
            colour = discord.Colour.red()
        )
        await embed.channel.send(embed)
        
#client = discord.Client(intents=discord.Intents.all())
#@client.event
#async def on_ready():
#    print('Bot is online and ready to interact')
#
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    
#    if message.content == 'ur mum':
#        await message.channel.send('Get some new content ya goddamn clown.')

client = LeonBot(intents=discord.Intents.all())
client.run('MTAyODQ1ODA5MTY0NzM0MDU3NA.Gbcsvu.GwzRn8Wqo3zctvipDjMerMUFSfO8PVcwGutvEE')
