# Music-Randomizer-PC
A mod for the OpenKH Mod Manager that randomizes the KH2 Music along with any other additions.

## How to use:
1. Install the mod using OpenKH Mod Manager
2. Navigate to your OpenKH, folder, then go to `Mods/KH2FM-Mods-Num/Music-Rando-PC`
3. Put the music files into any of the folders below:
  - Field   : Replaces exploration themes and some minigame tracks
  - Battle  : Replaces battle themes, forced fight tracks, and some minigame tracks
  - Cutscene: Replaces cutscene tracks and Dearly Beloved
  - Wild    : Replaces any of the above
4. When in doubt, choose `Wild`. For information on how the zip seed generator classifies the tracks, see [here](https://github.com/tommadness/KH2Randomizer/blob/master/Module/randomBGM.py)
5. Feel free to have subfolders within that folder or to rename the music files, but only the files that end in `.scd` will be considered
6. Run `Randomize.exe`. The program will immediately close and the content of your `mod.yml` will be changed.
7. Apply the mod using OpenKH Mod Manager.
8. Your music is now randomized!

## Advanced Usage:
You can open `musiclist.json` and delete the entry of a track to keep it vanilla.

You can also create more categories by editing the music's type within `musiclist.json`. For example, changing Fields of Honor's type into `lod` will make it use tracks from `lod` or `wild` folders. Names are case-insensitive. Tracks with the `wild` type will only use the music from that folder.

## Extraction Tips:
- Older games can have their files extracted from `.pkg` by `OpenKH`, `build_from_mm` or [`KHPCPatchManager`](https://github.com/AntonioDePau/KHPCPatchManager/releases)
  - KH1 music files can be extracted from `kh1_first.pkg` and `kh1_second.pkg`. They're inside the `amusic` folder. Delete all the folders without `music` in the name.
  - Re:CoM music files can be extracted from `recom.pkg`. They're inside the `STREAM/0001` folder.
  - KH2 music files are inside the `bgm` and `vagstream` folders.
  - BbS music files can be extracted from `bbs_fourth.pkg`. They're inside the `sound/win/bgm` folder.
  - Days and Re:Coded movies music files can be extracted from `mare.pkg`. They're inside the `sound` folder. Delete the `us` and `jp` folder.
  - DDD music files can be extracted from `kh3d_first.pkg` and `kh3d_fourth.pkg`. They're inside the `sound/jp/output/BGM` folder.
- Newer games can have their files extracted from `.pak` by [`Umodel`](https://www.gildor.org/en/projects/umodel) . You will need the extraction key for each game. After that, the .uasset files can be converted using [`VGMToolbox`](https://sourceforge.net/projects/vgmtoolbox/).
  - 0.2 music files are inside `Game/Sound/BGM`. They can be converted to .ogg with VGMToolbox on `Misc. Tools/Extraction Tools/Streams/Xiph.Org OGG Extractor`. The loop points are present within the file but can't be viewed on Foobar.
  - KH3 music files are inside `Game/Sound/BGM`, with remind tracks in `Game/Sound/_DLC/BGM`. They can be converted to .hca with VGMToolbox on `Misc. Tools/Extraction Tools/Streams/CRI HCA Extractor`.
