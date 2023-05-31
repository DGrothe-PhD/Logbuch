# Logbuch
just a short script to log events with a timestamp

checks.py is the part to generate events. daylogs.txt is the log of your checks.

## How it works
`python checks.py`
Add new event(s), or type `q` for quitting if prompted to do so.

## Usecases
Hackalife's usecase:
I want to log events like meals, takeing medicine and so on.

Other usecases:
- Log when opening and closing a window in your room.
- Log the temperature in your room while the windows are open
- Guess the artists of songs while listening to the radio and later compare your results to the playlist.
- Quickly jot down parts of work you start and finish, to fill timesheets for projects
- &hellip;

Solution:
Running checks.py, it shows the last logged event [yyyy,mm,dd,hh,mm,ss] name.
adding a new event by typing its name.
it adds  the new event to the top of daychecks.txt, so you can look it up later.
