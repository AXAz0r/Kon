﻿# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2018  Lucia's Cipher
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import inspect

import discord

from kon.core.mechanics.command import SigmaCommand


async def evaluate(cmd: SigmaCommand, message: discord.Message, args: list):
    if not args:
        status = discord.Embed(color=0xBE1931, title='❗ Nothing Inputted To Process')
    else:
        # noinspection PyBroadException
        try:
            execution = " ".join(args)
            output = eval(execution)
            if inspect.isawaitable(output):
                output = await output
            status = discord.Embed(title='✅ Executed', color=0x77B255)
            status.add_field(name='Results', value=f'\n```\n{output}\n```')
        except Exception as e:
            status = discord.Embed(color=0xBE1931, title='❗ Error')
            status.add_field(name='Execution Failed', value=f'{e}')
    await message.channel.send(None, embed=status)
