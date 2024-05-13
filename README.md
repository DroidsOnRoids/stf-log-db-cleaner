# stf-log-db-cleaner

Removes outdated entries from STF database

Configuration environment variables: 
* `MAX_AGE_MILLIS` - Unix timestamp of the oldest entries to keep 
* `HOST` - STF host 
* `PORT` - STF port

Sample systemd service and timer in `systemd` folder.
