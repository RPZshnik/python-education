

API=c69f0a95e61933c96d35b77c4e4dd666
crontab -l > mycron

echo "0 7 * * * curl -o ~/weather_$(date +\%d_\%m_\%y).json 'http://api.openweathermap.org/data/2.5/weather?q=Kharkiv&APPID=$API&units=metric'" >> mycron

crontab mycron
rm mycron
