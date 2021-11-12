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

I'm an advanced filter bot with many capabilities!</b>
There is no practical limits for my filtering capacity :)

<b>See <i>/help</i> for commands and more details.</b>
"""


    HELP_MSG = """
<b>Commands Help</b>

Add me as admin in your group and start filtering :)

<b><u>Basic Commands:</u></b>

/start - Check if I'm alive!
/help - Command help
/about - Something about me!

<b>© Developed by ❤️ @ZauteKm</b>
"""

    FILTER_MSG = """
<b><u>Filter Commands:</u></b>

/add <code>name reply</code>: Add filter for name.
/del <code>name</code>: Delete filter.
/delall: Delete entire filters (Group Owner Only!).
/viewfilters: List all filters in chat.
"""

    CONNECTION_MSG = """
<b><u>Connection Commands:</u></b>

/connect <code>groupid</code>: Connect your group to my PM. You can also simply use.
/connect: Only in groups.
/connections: Manage your connections.
"""

    EXTRAS_MSG = """
<b><u>Extras:</u></b>

/status: Shows current status of your bot (Auth User Only).
/id: Shows ID information.
/info: Shows User Information. Use <code>/info</code> as reply to some message for their details!
"""

    BUTTONS_MSG = """
<b><u>Buttons:</u></b>

Filter supports both url and alert inline buttons, now lets see how to implement it.

<b>NB:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly formatted as below or else result will be malformed.

<b>URL buttons:</b>
<code>[Button Text](buttonurl://t.me/example.com)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:Ahoy, this is an alert!)</code>

* Bot does support buttonurl and buttonalert alias
"""

    ABOUT_MSG = """🤖<b>My Name: Filter Bot</b>

👨‍💻<b>Creator:</b> @ZauteKm    

♻️<b>Language:</b> <code>Python3</code>

📜<b>Library:</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""
