# Music-Randomizer-PC
A mod for the OpenKH Mod Manager that randomizes the KH2 Music along with any other additions.

## How to use:
1. Install the mod using OpenKH Mod Manager
2. Navigate to your OpenKH, folder, then go to `Mods/KH2FM-Mods-Num/Music-Rando-PC`
3. Put the music files into any of the folders below (you'll have to create them yourself):
  - Field : Replaces exploration themes and some minigame tracks
  - Fight : Replaces battle themes, forced fight tracks, and some minigame tracks
  - Cutscene : Replaces cutscene tracks and Dearly Beloved
  - Wild : Replaces any of the above
4. When in doubt, choose `Wild`. For information on how the zip seed generator classifies the tracks, see [here](https://github.com/tommadness/KH2Randomizer/blob/master/Module/randomBGM.py)
5. Run `Randomize.exe`. The program will immediately close and the content of your `mod.yml` will be changed.
6. Apply the mod using OpenKH Mod Manager.
7. Your music is now randomized!

##Intermediate Usage:
You can have subfiles within any of the default folders, with all files ending in `.scd` being included in the randomization pool. For example, `field/new/mytrack.scd` will be included as a field theme. Don't use any of the default folder names as subfolder names in order to avoid any unintended consequences.

You can also have any of the default folders inside as subfiles. For example, `new/fight/mytrack.scd` will be included as a fight theme.

When combined, the deepest subfile will be the music's final type. For example, `field/new/fight/mytrack.scd` will be included as a fight theme instead of a field theme. This can lead to unintended consequences, so please be careful.

## Advanced Usage:
By editing the `MusicData.yml`, you can greatly customize how the randomization is done.
- Deleting an entry of a track will keep it vanilla.
- The mod will includes files in `Replacement Music Location`, so this can be used if you want to keep the music files elsewhere. When it is empty (written as `''`), the mod will include files in its location.
- You can create more categories by editing the music's type. For example, changing Fields of Honor's type into `[LoD,Battle,Wild]` will make it use tracks from `lod`, `battle`, or `wild` folders. Names are case-insensitive and duplicates can be used to influence weighting. The caveat from Intermediate Usage also applies with any custom types.

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
