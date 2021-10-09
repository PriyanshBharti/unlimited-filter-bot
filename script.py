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

I'm an advanced filter bot with many capabilities!
There is no practical limits for my filtering capacity :)

See <i>/help</i> for commands and more details.</b>
"""


    HELP_MSG = """
<i>Add me as admin in your group and start filtering :)</i>


<b>Basic Commands;</b>

/start - Check if I'm alive!
/help - Command help
/about - Something about me!


<b>Filter Commands;</b>

<code>/add name reply</code>  -  Add filter for name

<code>/del name</code>  -  Delete filter

<code>/delall</code>  -  Delete entire filters (Group Owner Only!)

<code>/viewfilters</code>  -  List all filters in chat


<b>Connection Commands;</b>

<code>/connect groupid</code>  -  Connect your group to my PM. You can also simply use,
<code>/connect</code> in groups.

<code>/connections</code>  -  Manage your connections.


<b>Extras;</b>

/status  -  Shows current status of your bot (Auth User Only)

/id  -  Shows ID information

<code>/info userid</code>  -  Shows User Information. Use <code>/info</code> as reply to some message for their details!


<b>© @ZauteKm</b>
"""


    ABOUT_MSG = """🤖<b>My Name : Telegram Filter Bot</b>

👨‍💻<b>Creater :</b> @ZauteKm    

♻️<b>Language :</b> <code>Python3</code>

📜<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 

"""
