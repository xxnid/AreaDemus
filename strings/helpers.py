# Copyright (C) 2021-2023 TeamUltroid.
# Ultroid - UserBot.
# UltroidUser - xexenId.
#
# This file is a part of https-//github.com/teamultroid/ultroid.
# Please read the GNU affero general license.
# https-//www.github.com/teamultroid/ultroid/blob/main/license.


HELP_1 = """<b>Admin Commands</b>.

✅ Just add in the starting of the commands to use them for channels.
1️⃣ /pause - pause the current playing stream.
2️⃣ /resume - resume the paused stream.
3️⃣ /skip - skip the current playing stream and start streaming the next track in queue.
4️⃣ /end or /stop - clears the queue and end the current playing stream.
5️⃣ /player - get a interactive player panel.
6️⃣ /queue - shows the queued tracks list."""

HELP_2 = """<b>Auth Users</b>.

✅ Auth users can use admin rights in the bot without admin rights in the chat.
1️⃣ /auth (usn/id) - add a user to auth list of the bot.
2️⃣ /unauth (usn/id) - remove a auth users from the auth users list.
3️⃣ /authusers - shows the list of auth users of the group."""

HELP_3 = """<b>Broadcast</b>.

✅ <b>Broadcasting Mode</b>.
1️⃣ /broadcast - broadcast a message to served chats of the bot.
2️⃣ /broadcast - (example) /broadcast -user -assistant -pin, your text.

◉ -pin - pins your broadcasted messages in served chats.
◉ -pinloud - pin your broadcasted message in served chats and send notification to the members.
◉ -user - broadcasts the message to the users who have started your bot.
◉ -assistant - broadcast your message from the assitant account of the bot.
◉ -nobot - forces the bot to not broadcast the message."""

HELP_4 = """<b>Chat Blacklist</b>.

✅ Restrict shit chats to use our precious bot.
1️⃣ /blacklistchat - blacklist a chat from using the bot.
2️⃣ /whitelistchat - whitelist the blacklisted chat.
3️⃣ /blacklistedchat - shows the list of blacklisted chats."""

HELP_5 = """<b>Block User</b>

✅ Starts ignoring the blacklisted user, so that he can't use bot commands.
1️⃣ /block (usn or reply to a user) - block the user from our bot.
2️⃣ /unblock (usn or reply to a user) - unblocks the blocked user
3️⃣ /blockedusers - shows the list of blocked users."""

HELP_6 = """<b>Channelplay</b>.

✅ You can stream audio/video in channel.
1️⃣ /cplay - starts streaming the requested audio track on channel's videochat.
2️⃣ /cvplay - starts streaming the requested video track on channel's videochat.
3️⃣ /cplayforce or /cvplayforce - stops the ongoing stream and starts streaming the requested track.
4️⃣ /channelplay - (chat username or id or disable) connect channel to a group and starts streaming tracks by the help of commands sent in group."""

HELP_7 = """<b>GlobalBan Feature</b>.

1️⃣ /gban - (usn or reply to a user) globally bans the chutiya from all the served chats and blacklist him from using the bot.
2️⃣ /ungban - (usn or reply to a user) globally unbans the globally banned user.
3️⃣ /gbannedusers - shows the list of globally banned users."""

HELP_8 = """<b>Loop Stream</b>.

✅ Starts streaming the ongoing stream in loop.
1️⃣ /loop - (enable/disable) enable or disable loop for the ongoing stream
2️⃣ /loop - (1, 2, 3, ...) enable the loop for the given value."""

HELP_9 = """<b>Maintenance Mode</b>.

1️⃣ /logs - get logs of the bot.
2️⃣ /logger - (enable/disable) bot will start logging the activities happen on bot.
3️⃣ /maintenance - (enable/disable) enable or disable the maintenance mode of your bot."""

HELP_10 = """<b>Ping & Stats</b>.

1️⃣ /start - starts the music bot.
2️⃣ /help - get help menu with explanation of commands.
3️⃣ /ping - shows the ping and system stats of the bot.
4️⃣ /stats - shows the overall stats of the bot."""

HELP_11 = """<b>lay Commands</b>.

1️⃣ v - stands for video play.
2️⃣ force - stands for force play.
3️⃣ /play or /vplay - starts streaming the requested track on videochat.
4️⃣ /playforce or /vplayforce - stops the ongoing stream and starts streaming the requested track."""

HELP_12 = """<b>Shuffle Queque</b>.

1️⃣ /shuffle - shuffle's the queque.
2️⃣ /queque - shows the shuffled queque."""

HELP_13 = """<b>Seek Stream</b>.

1️⃣ /seek (duration in seconds) - seek the stream to the given duration.
2️⃣ /seekback (duration in seconds) - backward seek the stream to the the given duration."""

HELP_14 = """<b>Song Downloads</b>.

1️⃣ /song - (song name, youtube url) download any track from youtube in Mp3, Mp4 formats."""

HELP_15 = """<b>SpeedTest Commands</b>.

✅ You can control the playback speed of the ongoing stream.
1️⃣ /speed or /playback - for adjusting the audio playback speed in group.
2️⃣ /cspeed or /cplayback - for adjusting the audio playback speed in channel."""
