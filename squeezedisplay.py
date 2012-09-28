#!/usr/bin/env python

from pylms.server import Server
from pylms.player import Player
import subprocess

HOST = '192.168.1.30'
PORT = 9090
SPI_DEV = '/dev/spidev0.1'
SPI_ADR = '00'
BW_TOOLS = '/home/pi/bw_rpi_tools/bw_spi'
PLAYER_ID = '00:04:20:26:97:a0'

sc = Server(hostname=HOST, port=PORT, username="", password="")
sc.connect()

# This is my SqueezeBox ID, just for testing so far.
sq = sc.get_player(PLAYER_ID)

print("Track Title:    " + sq.get_track_title())
print("Artist:         " + sq.get_track_artist())
print("Album :         " + sq.get_track_album())
print("remaining time: " + str(sq.get_time_remaining()))

subprocess.call(['sudo', '/home/pi/bw_rpi_tools/bw_spi/bw_lcd', '-a', SPI_ADR, '-D', SPI_DEV, '-C'])
subprocess.call(['sudo', '/home/pi/bw_rpi_tools/bw_spi/bw_lcd', '-a', SPI_ADR, '-D', SPI_DEV, '-T', '0,0', 'Title:' ])
subprocess.call(['sudo', '/home/pi/bw_rpi_tools/bw_spi/bw_lcd', '-a', SPI_ADR, '-D', SPI_DEV, '-T', '0,1',  sq.get_track_title()])
subprocess.call(['sudo', '/home/pi/bw_rpi_tools/bw_spi/bw_lcd', '-a', SPI_ADR, '-D', SPI_DEV, '-T', '0,2',  'Artist:' ])
subprocess.call(['sudo', '/home/pi/bw_rpi_tools/bw_spi/bw_lcd', '-a', SPI_ADR, '-D', SPI_DEV, '-T', '0,3',  sq.get_track_artist()])
