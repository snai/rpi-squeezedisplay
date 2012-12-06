#!/usr/bin/env python

# rpi-squeezedisplay: A small Tool to display Information on a display 
# attached to the Raspberry Pi
# Copyright (C) 2012 Martin Grohmann
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Creative Commomns - Share Alike License.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Creative Commons - Share Alike License for more details.
# 
# You should have received a copy of the License along with this program. 
# If not, see <https://creativecommons.org/licenses/by-sa/3.0/>

from pylms.server import Server
from pylms.player import Player
import subprocess

HOST = '192.168.1.30'
PORT = 9090
USER = ''
PW = ''
SPI_DEV = '/dev/spidev0.1'
SPI_ADR = '00'
BW_TOOLS = '/home/pi/bw_rpi_tools/bw_spi/bw_lcd'
PLAYER_ID = '00:04:20:26:97:a0'

sc = Server(hostname=HOST, port=PORT, username=USER, password=PW)
sc.connect()

sq = sc.get_player(PLAYER_ID)

title = sq.get_track_title()[0:20]
artist = sq.get_track_artist()[0:20]

def write_lcd(pos, content):
    subprocess.call(['sudo', BW_TOOLS, '-a', SPI_ADR, '-D', SPI_DEV, '-T', pos, content])

def clear_lcd():
    subprocess.call(['sudo', BW_TOOLS, '-a', SPI_ADR, '-D', SPI_DEV, '-C'])

clear_lcd()
write_lcd('0,0', 'Title: ')
write_lcd('0,1', title) 
write_lcd('0,2', 'Artist:')
write_lcd('0,3', artist)

