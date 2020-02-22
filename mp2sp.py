# -*- coding: utf-8 -*-

import os, gzip, json, urllib.request as url

player_data_end_offset = 1
playerdat_start_offset = 3

nbt = lambda file: bytearray(gzip.open(file, "r").read())
parse = lambda uuid: json.loads(url.urlopen(url.Request(f"https://api.mojang.com/user/profiles/{uuid}/names")).read())

savesdir = os.getenv("APPDATA") + "/.minecraft/saves/"
saves = [save for save in os.listdir(savesdir) if os.path.exists(savesdir + save + "/level.dat")]

# Print worlds (folders):
for save, i in zip(saves, range(len(saves))):
	print("{:>3}".format(i + 1) + ": " + save)

# Select world:
world = saves[int(input("\nEnter the world number: ")) - 1]

levelpath = savesdir + world
playerpath = levelpath + "/playerdata/"

# Print players found:
players = os.listdir(playerpath)
player_names = [parse(uuid[:-4].replace("-", ""))[-1]["name"] for uuid in players]

print("\nSelected: " + world + "\n\nPlayer data found: ")
for player, i in zip(players, range(len(players))):
	print("{:>3}".format(i + 1) + f": {player_names[i]} ({player})")

# Select player:
n = int(input("\nEnter the player number: ")) - 1
player = players[n]
print(f"\nSelected {player_names[n]} with UUID {players[n][:-4]}.")

# Open .dats
playerdat = nbt(playerpath + player)
#playerdec = open(playerpath + player[:-4] + "_dec.txt", "wb")
#playerdec.write(playerdat)

leveldat = nbt(levelpath + "/level.dat")
#leveldec = open(levelpath + "/level_dec.txt", "wb")
#leveldec.write(leveldat)

# Substitute level.dat section with the player .dat
player_data_start = leveldat.find(bytearray(b"Player")) + 6
player_data_end = leveldat.find(bytearray(b"seenCredits")) + 11 + player_data_end_offset

#print(str(player_data_start) + " - " + str(player_data_end))
new_leveldat = leveldat[:player_data_start] + playerdat[playerdat_start_offset:] + leveldat[player_data_end:]

gzip.open(levelpath + "/level.dat", "w").write(new_leveldat)

print("\nDone!")
