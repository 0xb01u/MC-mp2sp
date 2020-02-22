# -*- coding: utf-8 -*-

import os, gzip

player_data_end_offset = 5
playerdat_start_offset = 3

savesdir = os.getenv("APPDATA") + "/.minecraft/saves/"
saves = [save for save in os.listdir(savesdir) if not os.path.isfile(savesdir + save) and os.path.exists(savesdir + save + "/level.dat")]

# Print worlds (folders):
for save, i in zip(saves, range(len(saves))):
	print("{:>3}".format(i + 1) + ": " + save)

# Select world:
world = saves[int(input("\nEnter the world number: ")) - 1]
print("\nSelected: " + world + "\n\nPlayer data found: ")

levelpath = savesdir + world
playerpath = levelpath + "/playerdata/"

# Print players found:
players = os.listdir(playerpath)
for player, i in zip(players, range(len(players))):
	print("{:>3}".format(i + 1) + ": " + player)

# Select player:
player = players[int(input("\nEnter the player number: ")) - 1]
print("\nSelected: " + player)

# Open .dats
playerdat = gzip.open(playerpath + player, "r").read()
#playerdec = open(playerpath + player[:-4] + "_dec.txt", "wb")
#playerdec.write(playerdat)

leveldat = bytearray(gzip.open(levelpath + "/level.dat", "r").read())
#leveldec = open(levelpath + "/level_dec.txt", "wb")
#leveldec.write(leveldat)

# Substitute level.dat section with the player .dat
player_data_start = leveldat.find(bytearray(b"Player")) + 6
player_data_end = leveldat.find(bytearray(b"foodTickTimer")) + 13 + player_data_end_offset

#print(str(player_data_start) + " - " + str(player_data_end))
new_leveldat = leveldat[:player_data_start] + playerdat[playerdat_start_offset:] + leveldat[player_data_end:]

gzip.open(levelpath + "/level.dat", "w").write(new_leveldat)

print("\nDone!")
