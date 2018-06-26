# /usr/local/bin/python3
import os
from crontab import CronTab


# getting absolute path of user's files
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
blank_file_name = 'blank.txt'

# initiate crontab object
cron = CronTab(user=True)  # user=True uses current user profile
# gather and define new file name each time the cron job runs
get_date = os.popen("date '+%Y_%m_%d'").read().rstrip()
date_file_name = 'aims_' + get_date + '.txt'
# create new file with current date
copy_file = 'cp {0} {1};'.format(dir_path + blank_file_name, dir_path + date_file_name)
# open file for user to input aims
open_file = 'open {0};'.format(dir_path + date_file_name)
command = copy_file + open_file

# create and register CRON job
job = cron.new(command=command, comment='open new blank file for recording aims')
job.dow.on('THU', 'SUN')  # change for different frequencies
cron.write()
