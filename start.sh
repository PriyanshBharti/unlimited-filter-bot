echo "Cloning Repo...."
git clone https://github.com/ZauteKm/TG-Filter-Bot.git /TG-Filter-Bot
cd /TG-Filter-Bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
