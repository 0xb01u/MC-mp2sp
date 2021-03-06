# MC-mp2sp - Minecraft multiplayer to singleplayer world porter
mp2sp is a Python script which transforms the multiplayer player data of a specified player in a Minecraft world into singleplayer player data for the same world.

## Why is this useful?
By default, Minecraft doesn't load singleplayer player data the same way it does for multiplayer player data, which means that if you want to play a multiplayer world in singleplayer, you will lose all your player data (inventory, experience, ender chest, position in the world, etc).

Moreover, despite not being able of loading multiplayer player data as singleplayer player data, Minecraft **will overwrite** the multiplayer player data for a player with its singleplayer player data if the latter gets modified. This means that, not only you will lose all your player data in singleplayer, **you won't be able of recovering it** by loading the world in multiplayer again.

mp2sp overcomes this issue by copying the multiplayer player data of a player to the singleplayer player data of that same world. **For mp2sp to work, the world must have not been played in singleplayer** after being played in multiplayer for the last time.

# Using mp2sp
Copy the script and run it with Python. It will display all your Minecraft worlds on your saves folder. Enter the number of the world you want to edit (the one shown before its name). A list of all the players that have played the world on multiplayer will be shown. Enter the number of your player. Profit.

### It is possible to cheat with this, isn't it?
Yeah, it's pretty obvious you can duplicate items (specifically inventories) very easily using this. I'm not going to say how, however.

But you do you, man.

Isn't it easier to open creative mode or use MCEdit?

# Technical explanation
The data for Minecraft worlds is stored in a format called *NBT*.

The multiplayer player data for all players who have played on a world is stored in the _playerdata_ folder of that world.

The singleplayer player data for the last singleplayer of a world, alongside the rest of the data for that world, is stored in the _level.dat_ file of that world.

This script simply reads the NBT data for a multiplayer player, decompresses it (since the NBT file format is _usually_ compressed), and pastes it in its corresponding place in the level.dat file. Then it recompresses the level.dat file and saves it, overwriting the previous one.

# TODO
 - This pretty much needs a GUI.
 -- When the GUI is done, add multiple input methods (drag and drop, select manually...)
 - Add an automatic offline mode: if the program can't reach the Internet to request the player names, just print their uuids instead of crashing.
 - Automatically backup the world.