# Life Aims Reminder

Keeping your aims in mind (and up to date) makes it more likely you'll achieve them!

---

Automatically open a blank "life aims" document with pre-scheduled time frames
every Thursday morning and Sunday evening (adapt for different days/times).

The `blank.txt` file looks like so (and can obviously also be edited):

```
LOG YOUR GOALS
---------------

today:
-
-
-

tomorrow:
-
-
-

one week:
-
-
-

[...]

six months:
-
-
-

[...]

five years:
-
-
-
```

## Installation

Using `.plist` files on MacOS allows to schedule tasks that run **also later**, e.g.
in case the computer was asleep or switched off at the scheduled time.

The `.plist` files need to be loaded in order to work, and the **working directory**
needs to be adapted for your specific path. Change the `<string>` part of this:

```
    <key>WorkingDirectory</key>
        <string>/Users/martin/Documents/projects/aims/</string>
```

to the path where you clone this repository to.
(Also the `<string>` in `<key>StandardErrorPath</key>` needs to be set to the
    same directory to receive error logs)

For easiest use of the `.plist` job, I would suggest to move the `.plist` file
into your `/Users/<yourUserName>/Library/LaunchAgents/` folder (create it if it doesn't
    yet exist). All `.plist`s in this folder get automatically loaded during system startup.

## Alternate: `cron` job

Running `aims.py` registers a CRON job on your system. It is straightforward to set up
(aka just run the file (Python 3!)) but only works if your computer is switched on during
the time of task execution.

---

## Resources

- http://stackabuse.com/scheduling-jobs-with-python-crontab/
- http://www.launchd.info/
- https://apple.stackexchange.com/questions/249446/launchd-plist-format-for-running-a-command-at-a-specific-time-on-a-weekday
