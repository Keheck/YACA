# Yet Another Chess AI

This is just a little pet-project of making an AI that plays chess. It's programmed in python and uses pygame, so make sure both of those are installed before you run it. The entrypoint for the program should be `/src/main.py`. Assuming you're in the root folder of this respository on your machine, type `python ./src/main.py` (replace `python` with `py` if you're on Windows, otherwise it may open the MS Store page for Python).

The game is portable, which means that no matter where on your filesystem the game lies, as long as python can reach it and its subdirectories, it is runnable. It also does not depend on any OS specific configurations like environment variables.

The `./data/settings.json` file contains information about what state to launch the game in. There you can tell the game if you want to play against the AI or a real opponent, change the AI strength, activate the eval-bar and many more settings. View the settings.json's wikipage to know more.

## Licenses

[Chess Pieces Sprite.svg](https://commons.wikimedia.org/wiki/File:Chess_Pieces_Sprite.svg) uploaded by jurgenwesterhof and licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en) (Split up and converted to individual .png files)
