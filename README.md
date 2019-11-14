# MC-mp2sp - Minecraft multiplayer to singleplayer world porter
mp2sp is a Python script which transforms the multiplayer player data of a specified player in a Minecraft world into singleplayer player data for the same world.
## Why is this useful?
By default, Minecraft doesn't load singleplayer player data the same way it does for multiplayer player data, which means that if you want to play a multiplayer world in singleplayer, you will lose all your player data (inventory, experience, ender chest, position in the world, etc).
Moreover, despite not being able of loading multiplayer player data as singleplayer player data, Minecraft **will overwrite** the multiplayer player data for a player with its singleplayer player data if the latter gets modified. This means that, not only you will lose all your player data in singleplayer, **you won't be able of recovering it** by loading the world in multiplayer again.
mp2sp overcomes this issue by copying the multiplayer player data of a player to the singleplayer player data of that same world. **For mp2sp to work, the world must have not been played in singleplayer** after being played in multiplayer for the last time.
# Using mp2sp
_TODO_
# Technical explanation
_TODO_