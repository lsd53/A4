#! /bin/bash 
day=$(date +%a)
awk -v d=$day ' $1==d {print $0}' myweekly_act.txt | awk 'BEGIN {FS=":"} {print $2}' | mail -s "Reminder: Tasks for Today"  lsd53@cornell.edu

