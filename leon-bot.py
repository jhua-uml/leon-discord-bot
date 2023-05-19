import discord
import os
import random
from discord import app_commands
import datetime as dt
from datetime import timedelta, datetime
from discord.ext import commands, tasks
from asyncio import sleep
from fetch_utils import getMaxDay, getDayIcon

# utc = datetime.timezone.utc

brel_embed_dict = {}

def getAttendees(day_max):
    match day_max:
        case 'mon_cnt':
            client.date_offset = 5
            return "".join(client.mon_atd)
        case 'tue_cnt':
            client.date_offset = 6
            return "".join(client.tue_atd)
        case 'wed_cnt':
            client.date_offset = 0
            return "".join(client.wed_atd)
        case 'thu_cnt':
            client.date_offset = 1
            return "".join(client.thu_atd)
        case 'fri_cnt':
            client.date_offset = 2
            return "".join(client.fri_atd)
        case 'sat_cnt':
            client.date_offset = 3
            return "".join(client.sat_atd)
        case 'sun_cnt':
            client.date_offset = 4
            return "".join(client.sun_atd)

class raidButtons(discord.ui.View):
    def __init__(self)  -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label="Start Raid",style=discord.ButtonStyle.green)
    async def green_button(self,interaction: discord.Interaction, button: discord.ui.Button):
        # guild = interaction.guild.get_role
        # channel = interaction.channel_id
        await interaction.response.send_message(content=f'``{client.raid_name_button}`` has started, please join the lobby')
        # await interaction.response.send_message(content=f'{interaction.user.mention} has started the raid.')
        # await interaction.response.defer(ephemeral=True)
        await interaction.channel.send(f'**Attendees**\n{client.atds}')
        # await interaction.channel.send(interaction.user._roles)
        # await interaction.response.send_message(guild(1075346682679656469).mention)


    @discord.ui.button(label="Cancel Raid",style=discord.ButtonStyle.red)
    async def red_button(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(content=f'{interaction.user.mention} You do not have permission to cancel this raid.', ephemeral=True)


class LeonBot(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
        self.atds = ''
        self.raid_name_button = ''
        self.date_offset = 0

        self.mon_cnt = 0
        self.tue_cnt = 0
        self.wed_cnt = 0
        self.thu_cnt = 0
        self.fri_cnt = 0
        self.sat_cnt = 0
        self.sun_cnt = 0

        self.mon_atd = []
        self.tue_atd = []
        self.wed_atd = []
        self.thu_atd = []
        self.fri_atd = []
        self.sat_atd = []
        self.sun_atd = []

        # self.time = datetime.(hour=0, minute=0, second=5)
        self.end_reg_date = datetime.now() + timedelta(seconds=5)

        self.day_tally = { 'mon_cnt': self.mon_cnt, 'tue_cnt': self.tue_cnt,
                            'wed_cnt': self.wed_cnt, 'thu_cnt': self.thu_cnt,
                            'fri_cnt': self.fri_cnt, 'sat_cnt': self.sat_cnt,
                            'sun_cnt': self.sun_cnt}
        #self.target_message_id = 1040521731363848233

    @tasks.loop(hours=48)
    async def my_task(self, ctx, raid_name, day):
        if self.my_task.current_loop != 0:
            # print(f'{type(getMaxDay(client.day_tally))}') // Debugging

            static_role = discord.utils.get(ctx.guild.roles, id=1002369297756213364)

            now = datetime.now()
            current_time =  now.strftime(("%H:%M:%S"))
            current_month = now.strftime("%B")
            current_day =  now.strftime("%d")

            # day_icon = getDayIcon(getMaxDay(client.day_tally))
            # day_icon = 'getDayIcon(max(client.day_tally, key=lambda key: client.day_tally[key]))'
            day_icon = getDayIcon(max(client.day_tally, key=client.day_tally.get))
            attendees = getAttendees(getMaxDay(client.day_tally))

            timed_embed = discord.Embed(
                title = f"Registration for ``{raid_name}`` has ended",
                description = f'Ended: ``{current_month} {current_day}`` ``{current_time} EST``\n\n' + 
                              f'Raid has been scheduled for:\n {day_icon} {current_month} {day+client.date_offset}``',
                colour = discord.Colour.red()
            )
            timed_embed.add_field(name=f'**Attendees**', value=f'{attendees}' , inline=True)
            self.atds = attendees
            self.raid_name_button = raid_name
            await ctx.channel.send(static_role.mention, embed=timed_embed, view=raidButtons())
            self.my_task.stop()


    @my_task.before_loop
    async def my_task_before(self):
        print('waiting...')
        await client.wait_until_ready()

    @my_task.after_loop
    async def end_raid_reg(self):
        print('task successfully finished')
        for key, value in client.day_tally.items():
            client.day_tally[key] = 0
        print(client.day_tally)

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'I''m online now')
    

    async def on_message(self, message):
        if message.author == client.user:
            return

    async def on_raw_reaction_add(self, payload):

        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        if payload.message_id != brel_embed.id or payload.member.bot:
            return
        
        guild = client.get_guild(payload.guild_id)

        global brel_embed_dict
        # global day_tally
        global day_names

        # Monday
        if payload.emoji.id == 1075213992550731877:
            payload_user = client.get_user(payload.user_id)
            # print(payload) // Debugging
            print(payload_user)
            for field in brel_embed_dict["fields"]:
                if field["name"] == "<:mon:1075213992550731877> **Monday**":
                    field["value"] += f"{payload_user.mention}\n"
            edited_embed = discord.Embed.from_dict(brel_embed_dict)
            await brel_embed.edit(embed=edited_embed)
            client.day_tally['mon_cnt'] += 1
            client.mon_atd.append(f"{payload_user.mention}\n")
            print(client.day_tally['mon_cnt'])
            await sleep(6.0)
        # Tuesday
        elif payload.emoji.id == 1075214017540399214:
            payload_user = client.get_user(payload.user_id)
            for field in brel_embed_dict["fields"]:
                if field["name"] == "<:tue:1075214017540399214> **Tuesday**":
                    field["value"] += f"{payload_user.mention}\n"
            edited_embed = discord.Embed.from_dict(brel_embed_dict)
            await brel_embed.edit(embed=edited_embed)
            client.day_tally['tue_cnt'] += 1
            client.tue_atd.append(f"{payload_user.mention}\n")
            await sleep(6.0)
        # Wednesday
        elif payload.emoji.id == 1075217903546269797:
            payload_user = client.get_user(payload.user_id)
            for field in brel_embed_dict["fields"]:
                if field["name"] == "<:wed:1075217903546269797> **Wednesday**":
                    field["value"] += f"{payload_user.mention}\n"
            edited_embed = discord.Embed.from_dict(brel_embed_dict)
            await brel_embed.edit(embed=edited_embed)
            client.day_tally['wed_cnt'] += 1
            client.wed_atd.append(f"{payload_user.mention}\n")
            await sleep(6.0)
        # Thursday
        elif payload.emoji.id == 1075246801118036020:
            payload_user = client.get_user(payload.user_id)
            for field in brel_embed_dict["fields"]:
                if field["name"] == "<:thu:1075246801118036020> **Thursday**":
                    field["value"] += f"{payload_user.mention}\n"
            edited_embed = discord.Embed.from_dict(brel_embed_dict)
            await brel_embed.edit(embed=edited_embed)
            client.day_tally['thu_cnt'] += 1
            client.thu_atd.append(f"{payload_user.mention}\n")
            await sleep(6.0)
        # Friday
        elif payload.emoji.id == 1075246796357521428:
            payload_user = client.get_user(payload.user_id)
            for field in brel_embed_dict["fields"]:
                if field["name"] == "<:fri:1075246796357521428> **Friday**":
                    field["value"] += f"{payload_user.mention}\n"
            edited_embed = discord.Embed.from_dict(brel_embed_dict)
            await brel_embed.edit(embed=edited_embed)
            client.day_tally['fri_cnt'] += 1
            client.fri_atd.append(f"{payload_user.mention}\n")
            await sleep(6.0)
        # Saturday
        elif payload.emoji.id == 1075246797934563350:
            payload_user = client.get_user(payload.user_id)
            for field in brel_embed_dict["fields"]:
                if field["name"] == "<:sat:1075246797934563350> **Saturday**":
                    field["value"] += f"{payload_user.mention}\n"
            edited_embed = discord.Embed.from_dict(brel_embed_dict)
            await brel_embed.edit(embed=edited_embed)
            client.day_tally['sat_cnt'] += 1
            client.sat_atd.append(f"{payload_user.mention}\n")
            await sleep(6.0)
        # Sunday
        elif payload.emoji.id == 1075246799838773298:
            payload_user = client.get_user(payload.user_id)
            for field in brel_embed_dict["fields"]:
                if field["name"] == "<:sun:1075246799838773298> **Sunday**":
                    field["value"] += f"{payload_user.mention}\n"
            edited_embed = discord.Embed.from_dict(brel_embed_dict)
            await brel_embed.edit(embed=edited_embed)
            client.day_tally['sun_cnt'] += 1
            client.sun_atd.append(f"{payload_user.mention}\n")
            await sleep(6.0)
        else:
            payload.emoji.name == 1029494684973793360
            role = discord.utils.get(guild.roles, name='Clown')
            await payload.member.add_roles(role)

    async def displayembed(self, ctx, name, day, day_delta):

        static_role = discord.utils.get(ctx.guild.roles, id=1002369297756213364)

        now = datetime.now()
        then = datetime.now() + timedelta(seconds=30)

        current_date = now.strftime("%Y-%m-%d")
        current_month = now.strftime("%B")
        current_day =  now.strftime("%d")
        current_time =  now.strftime(("%H:%M:%S"))
        then_time = then.strftime(("%H:%M:%S"))

        embed = discord.Embed(
            title = f"``{name}``",
            description = f'Week of: ``{current_month} {day} - {current_month} {day+day_delta}``\n\nRegistration closes: ``{current_month} {int(current_day)+2}`` at ``{current_time} EST``\n\n',
            colour = discord.Colour.purple()
        )
        embed.add_field(name='<:mon:1075213992550731877> **Monday**', value='', inline=True)
        embed.add_field(name='<:tue:1075214017540399214> **Tuesday**', value='', inline=True)
        embed.add_field(name='<:wed:1075217903546269797> **Wednesday**', value='', inline=True)
        embed.add_field(name='<:thu:1075246801118036020> **Thursday**', value='', inline=True)
        embed.add_field(name='<:fri:1075246796357521428> **Friday**', value='', inline=True)
        embed.add_field(name='<:sat:1075246797934563350> **Saturday**', value='', inline=True)
        embed.add_field(name='<:sun:1075246799838773298> **Sunday**', value='', inline=True)
        global brel_embed_dict
        brel_embed_dict = embed.to_dict()
        # print(brel_embed_dict) // Debugging

        global brel_embed
        brel_embed = await ctx.channel.send(static_role.mention, embed=embed)
        client.my_task.start(brel_embed, name, day)
        await brel_embed.add_reaction('<:mon:1075213992550731877>')
        await brel_embed.add_reaction('<:tue:1075214017540399214>')
        await brel_embed.add_reaction('<:wed:1075217903546269797>')
        await brel_embed.add_reaction('<:thu:1075246801118036020>')
        await brel_embed.add_reaction('<:fri:1075246796357521428>')
        await brel_embed.add_reaction('<:sat:1075246797934563350>')
        await brel_embed.add_reaction('<:sun:1075246799838773298>')
        # print(type(brel_embed)) // Debugging
        # print(brel_embed) // Debugging
    
    async def pingRaid(self, ctx):
        static_role = discord.utils.get(ctx.guild.roles, name='test')
        await ctx.channel.send(static_role.mention)

    async def debugtally(self, variable):

        match variable:
            case 'day_tally':
                msg = f'type: ``{type(client.day_tally)}``\n'
                for x,y in client.day_tally.items():
                    msg += f'{x} : {y}\n'
                return msg
                # return f"type: ``{type(day_tally)}``\n\nmon_cnt: {day_tally[0]}"
            case _:
                return f'Command ``debug`` raised an exception: NameError: name ``{variable}`` is not defined'


  
client = LeonBot()


tree = app_commands.CommandTree(client)

@tree.command(name = "raid", description = "Weekly Raid Scheduler")
@app_commands.checks.has_role('Guild Officer')
async def test(interaction: discord.Interaction, name: str, day: int, day_delta: int):
    await interaction.response.send_message(f"{interaction.user.mention} is scheduling **{name}**", ephemeral=False)
    test_msg = await interaction.original_response()
    interaction.user.guild_permissions
    await LeonBot.displayembed(self, test_msg, name, day, day_delta)
    # print(test_msg) // Debugging


@test.error
async def on_app_command_error(interaction, error):
    await interaction.response.send_message(error)
    # raise error

# @tree.command(name = "testapp", description = "My first application Command")
# async def self(interaction: discord.Interaction, name:str):
#     await interaction.response.send_message("Hello!", ephemeral=True)

@tree.command(name = "debug", description = "Debug what?")
async def self(interaction: discord.Interaction, variable: str):
    # await LeonBot.debugtally(self)
    debug_embed = discord.Embed(
        title = f"",
        description = f'',
        colour = discord.Colour.yellow()
    )
    debug_embed.add_field(name=f'``{variable}`` debug info', value=f'{await LeonBot.debugtally(self, variable)}', inline=True)
    # await interaction.response.send_message(f"{await LeonBot.debugtally(self, variable)}", ephemeral=False)
    await interaction.response.send_message(embed=debug_embed)


client.run(NULL)

print(brel_embed_dict)
