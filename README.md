# stuartsdesk
Code for powering a raspberry pi display I have on my desk, which has its own Twitter account. In `desk-flask/` is the code for a Flask server that listens for a direct message on Slack from my account to the dedicated bot account to set the status. Then in `replybot/` is a second python program that listens to the direct messages from everyone else on Slack and replies with the last status.

I learned flask from [this tutorial](https://github.com/miguelgrinberg/microblog) and this code is a heavily modified fork of the code from that, which is copyright (c) 2012, Miguel Grinberg. Released under an MIT-compatible license.
