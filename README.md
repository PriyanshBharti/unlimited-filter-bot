# Telegram Filter Bot
An advanced Filter Bot with nearly unlimitted filters!

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg">

  </a>
</p>
<p align="center">
  <a href="https://github.com/ZauteKm/unlimited-filter-bot/stargazers">
    <img src="https://img.shields.io/github/stars/ZauteKm/unlimited-filter-bot?style=social">

  </a>
  
  <a href="https://github.com/ZauteKm/unlimited-filter-bot/fork">
    <img src="https://img.shields.io/github/forks/ZauteKm/unlimited-filter-bot?label=Fork&style=social">

  </a>  
</p>

---

### Features
* Nearly unlimited filters
* Supports all type of filters(Including Alert Button Filter).
* Can save button filters directly (Rose Bot Feature)
* Supports multiple PM connections
* And all other features of a Filter Bot :D

---

#### Deploy the bot and start adding your filters :)


## How to use the bot
* Add bot to your group with admin rights.

* Add your filters :)


## Bot Commands

(You need to be an admin or Auth User in order to use these commands)

> Filter Commands
* `/add <filtername> <filtercontent>`  -  To add your filter. You can also reply to your content with /add command.

* `/del <filtername>`  -  Delete your filter.

* `/delall`  -  Delete all filters from group. (Group Owner Only!)

* `/viewfilters`  -  List all filters in chat.

> Connection Commands
* `/connect groupid`  -  Connects your group to PM. You can also simply use, `/connect` in groups.

* `/connections`  -  Manage your connections. (only in PM)

> Extras
* `/status`  -  Shows current status of your bot (Auth User Only)

* `/id`  -  Shows ID information

* `/info <userid>`  -  Shows User Information. Also use `/info` as reply to some message for their details!

---

## Variables

1. `TG_BOT_TOKEN`  - Get bot token from @BotFather
2. `API_ID`        - From my.telegram.org
3. `API_HASH`      - From my.telegram.org
4. `AUTH_USERS`  - ID of users that can use the bot commands. Get from [UseTGidBot](https://telegram.dog/UseTGidBot) by using /id command
5. `DATABASE_URI`  - Mongo Database URL from https://cloud.mongodb.com/
6. `DATABASE_NAME`  - Your database name from mongoDB. Default will be 'Cluster0'
7. `SAVE_USER`  -  Give yes or no . Usefull for getting userinfo and total user counts. May reduce filter capacity :( .
8. `HEROKU_API_KEY`  -  To check dyno status. Go to https://dashboard.heroku.com/account , scroll down and press Reveal API


### Optional - To set alternate Bot Commmands!
( *Add required field as heroku var and give desired command as value. You can edit it in sample_config.py also!*)

* `ADD_FILTER_CMD`  -  default will be 'add'
* `DELETE_FILTER_CMD`  -  default will be 'del'
* `DELETE_ALL_CMD`  -  default will be 'delall'
* `CONNECT_COMMAND`  -  default will be 'connect'
* `DISCONNECT_COMMAND`  -  default will be 'disconnect'

EG;  
![Vars Eg](https://telegra.ph/file/1f956f3491f2f20a9c1ec.jpg)


## Installation

<details><summary>Deploy to Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/ZauteKm/unlimited-filter-bot/tree/master">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details>
  <summary><b>Deploy in your VPS</b></summary>
<br/>

```sh
git clone https://github.com/ZauteKm/unlimited-filter-bot
cd unlimited-filter-bot
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```

</details>

---

## Credits

<p align="left">
  <a href="https://github.com/pyrogram/pyrogram">
    <img alt="Pyrogram" src ="https://i.imgur.com/BOgY9ai.png" width="104.75" height="32"/>
  </a>
</p>

<p align="left">
  <a href="https://docs.mongodb.com">
    <img alt="MongoDB" src ="https://img.shields.io/badge/MongoDB-%234ea94b.svg?&style=for-the-badge&logo=mongodb&logoColor=white"/>
  </a>
</p>
