# Coin Counter

This is a small web app I made to help my family efficiently count a massive jar of coins.

To make it useful and allow multiple people to count at once, use the command `ifconfig |grep inet` to get your local machine's IP address. Replace line 78 in app.py with `app.run(host="XXX.X.X.XXX")`  and replace line 2 in script.js with `const URL = 'http://XXX.X.X.XXX:5000/';`, where `XXX.X.X.XXX` is your IP adddress. That will make it visible and allow other devides to access the site and share the same counts.
