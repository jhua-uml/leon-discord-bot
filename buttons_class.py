import discord
from discord.ext import commands


class raidButtons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Start Raid",style=discord.ButtonStyle.green)
    async def gray_button(self,interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild.get_role
        # channel = interaction.channel_id
        #await interaction.response.send_message(content='```Raid has started.```')
        #ctx_res = await interaction.original_response()
        await interaction.channel.send(guild(1075346682679656469).mention)
        # await interaction.response.send_message(guild(1075346682679656469).mention)

    @discord.ui.button(label="Cancel Raid",style=discord.ButtonStyle.red)
    async def red_button(self,interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild.get_role
        await interaction.response.send_message(content='```Raid has been cancelled.```')
        ctx_res = await interaction.original_response()
        await ctx_res.channel.send(guild(1075346682679656469).mention)