#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
class Script(object):

    START_MSG = """<b>Hi {},
Im a simple bot which is designed and built for adding filters in any group.

<b>Hits <i>/help</i> for commands and more Information.</b>
"""


    HELP_MSG = """
<b>What is a filter bot?</b>
A bot were group admins can set replies for a particular keyword and the bot will automatically send preset replies whenever that keyword enountered in the chat.

<b><u>Usual Commands:</u></b>
/start - Check if I'm alive!
/help - Command help
/about - Something about me!

<b>© Developed by ❤️ @ZauteKm</b>
"""

    FILTER_MSG = """
<b><u>Filters:</u></b>
Filter is the feature were users can set automated replies for a particular keyword and the bot will respond whenever a keyword is found the message.

<b>NOTE:</b>
1. bot should have admin privillage in order to reply filters in a chat.
2. only admins can add filters in a chat.
3. filters does support all the telegram markdowns, medias and buttons.
4. alert buttons are also supported with a limit of 64 characters.
5. there are some easter eggs, try to find it out.

<b>Commands and Usage:</b>
/add <name reply>: Add filter for name.
/view: List all filters in chat.
/del <name>: delete a specific filter (separate keywords with spaces for deleting multiple filters at a time).
/delall: Delete entire filters (Group Owner Only!).
"""

    CONNECTION_MSG = """
<b><u>Connections:</u></b>
Used to connect bot to PM which let will you to execute both normal filter related commands and some other sensitive commands right from the PM that will
reflect in the group which helps you to keep the filter additions and other stuffs private and helps to prevent flooding.

<b>NOTE:</b>
1. Only admins can add a connection.
2. In a chat you can simply use the /connect for starting a connection and in PM you must specify chat id right after the command.

<b>Commands and Usage:</b>
/connect <chat id>: Connect your group to my PM. You can also simply use.
/connect: Only in groups.
/disconnect <chat id>: Disconnect from a chat.
/connections: List all your connections.
"""

    EXTRAS_MSG = """
<b><u>Extras:</u></b>

/id: Get the chat id of a user or the current chat.
/info: <user id> or <reply to any message>: whois info of a user.
"""

    BUTTONS_MSG = """
<b><u>Buttons:</u></b>

Filter supports both url and alert inline buttons, now lets see how to implement it.

<b>NB:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly formatted as below or else result will be malformed.

<b>URL buttons:</b>
<code>[Button 1](buttonurl:https://example.com)</code>
<code>[Button 2](buttonurl:https://example.com:same)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:Ahoy, this is an alert!)</code>

* Bot does support buttonurl and buttonalert alias
"""

    ABOUT_MSG = """🤖<b>My Name: Filter Bot</b>

👨‍💻<b>Creator:</b> @ZauteKm    

♻️<b>Language:</b> <code>Python3</code>

📜<b>Library:</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""
