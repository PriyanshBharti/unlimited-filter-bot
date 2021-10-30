echo "Cloning Repo...."
git clone https://github.com/ZauteKm/unlimited-filter-bot.git /unlimited-filter-bot
cd /unlimited-filter-bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
