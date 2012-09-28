#!/usr/bin/env python

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

