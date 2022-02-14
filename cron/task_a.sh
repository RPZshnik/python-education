#!/bin/bash

minute=$(date +"%M")
file_name="/cron_task_a.txt"

crontab -l > mycron
touch $HOME$file_name
date '+%d/%m/%y - %T' >> $HOME$file_name

echo $minute$" * * * * date '+\%d/\%m/\%y - \%T' >> "$HOME$file_name >> mycron

crontab mycron
rm mycron
