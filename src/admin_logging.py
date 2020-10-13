# admin_logging.py
"""
admin_logging is used to log messages that admins are interested in.
"""

from dotenv import load_dotenv
from discord.ext import commands
from discord import utils
import discord


class admin_logging(commands.Cog):
    def __init__(self, bot, logger):
        self.bot = bot
        self.logger = logger
        self.leave_channel_name = 'leave-log'

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = utils.get(
            member.guild.text_channels, name=self.leave_channel_name)
        await channel.send(f"{member.name} has left the server.")


def setup(bot, logger):
    bot.add_cog(admin_logging(bot, logger))
