# remindbot
This project is a GroupMe bot which would respond to a message containing the time slot by taking info from a Google Sheet (used to sign up for various shifts for my organizations recruitment) with the corresponding people signed up.

The code was linked to Heroku (a web app hosting services) and the app link was set as the callback URL for the GroupMe bot.

## History

I began by hard-coding my computer to type the schedule in proper time intervals via Java's Robot class. This was extremely inefficient as it took 30 minutes every night and was very difficult to update and had potential to stop working if the mouse was moved at all. I then hard-coded the schedule every night into this bot, which was more efficient, but certainly not as good as it could be. Finally, I took the time to figure out how to fetch data from a Google Sheet which yielded what is now in the code. A side note, I made these changes and many of my friends did not understand why I needed to update the bot as it worked perfectly before. They did not understand the tedious work of hard-coding the schedule.

## Limitations/Future

The bot was successful at keeping people accountable and reminding them of their shifts. However, I was pushed for time on development (as this was a last minute idea) and I was unable to figure out how to hide the credentials for the bot account used to grab the information from the Google Sheet. To mitigate this, the credentials were reconfigured frequently (at least twice a day) and given very limited access. In the future, I believe the best way to get around this issue would be to add environment variables to Heroku (which are hidden from all other users) for a temporary account created specifically for this project.
