# BMS-Preview-Audio-GUI

## About

I wanted a way for people to more easily use the BMS Audio Preview Generator than just using the command line.

## Instructions to Run the Application

1. Download the latest release of the BMS-Preview-Audio-GUI.
2. Download the latest release of the [BMSPreviewAudioGenerator](https://github.com/MikiraSora/BmsPreviewAudioGenerator/releases). (Tested using release 0.8.7)
3. Drag the gui.exe file into the BMSPreviewAudioGenerator folder.
4. Run gui.exe.

**NOTE**: BMSAudioPreviewGenerator does need .NET Core 3.1. Please install if the error "missing hostfxr.dll" occurs.

## Instructions to Use the Application

1. \**OPTIONAL*\* Change the start time and end time of where you want the previews to begin and end for the songs.
2. Click on **Choose Folder** to specify where your BMS songs folder is.
3. Click on **Generate Previews** to begin generating the audio previews in the specified folder.

## TODO

Making more of the command line arguments available on the GUI.

1. Fade in/Fade out.
2. Fast clip (on/off).
3. Process buffer size.
4. Check valid.
5. No skip.