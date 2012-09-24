#!/usr/bin/env python

from pylms.server import Server
from pylms.player import Player

sc = Server(hostname="192.168.1.30", port=9090, username="", password="")
sc.connect()

# This is my SqueezeBox ID, just for testing so far.
sq = sc.get_player("00:04:20:26:97:a0")

print("Track Title:    " + sq.get_track_title())
print("Artist:         " + sq.get_track_artist())
print("Album :         " + sq.get_track_album())
print("remaining time: " + str(sq.get_time_remaining()))
