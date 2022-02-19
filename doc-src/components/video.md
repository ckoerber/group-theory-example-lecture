# Adding video recordings to slides

This section explains how the "derivation videos" were created and added to the slides.

## Used tools
* Writing hardware. I.e., a graphics tablet or similar (I used an IPad + Apple Pen with [Notability](https://notability.com))
* A screen recorder (i.e., QuickTime on macOS, [screencast](https://help.ubuntu.com/stable/ubuntu-help/screen-shot-record.html) on Ubuntu or Zoom)
* A way to connect the writer with the recorder (I used [UxPlay](https://github.com/antimof/UxPlay) to duplicate the IPad screen on Ubuntu)
* *(Optional)* [`ffmpeg`](https://www.ffmpeg.org/) or other tools to edit the video.
* *(Optional)* [`scripts/vmanip.py`](ttps://github.com/ckoerber/group-theory-example-lecture/blob/main/scripts/vmanip.py) (Python) to generate `ffmpeg` commands for cropping the created video.

## Steps

Setup the hardware and recoding software and record the video :)

## Cropping the video

The script [`scripts/vmanip.py`](ttps://github.com/ckoerber/group-theory-example-lecture/blob/main/scripts/vmanip.py) allows generating `ffmpeg` commands which can be used to optimize and crop the video.
To continue, you first need to install `ffmpeg` and `pip install -r requirements.txt`.

The command
```bash
streamlit run scripts/vmanip.py
```
will create a GUI which can be accessed in your browser (see the printed URL).
When following the URL, you can specify a movie, drag-and-drop the boundaries to crop the file, specify a factor to speed up the recording, and eventually copy the corresponding `ffmpeg` command.

![Example for the `scripts/vmanip.py` GUI](imgs/cropper.png)

For example, for a crop to the box `width:height:x:y` and a speedup of `x1.05`
```
ffmpeg -i media/videos/lecture-10/su2-example.mp4 -filter_complex "[0]setpts=0.95*PTS[b];[b] crop = 3385:2109:37:28[c];[0]atempo=1.05[a]" -map "[c]" -map "[a]" media/videos/lecture-10/su2-example.cropped.mp4
```
This command needs to be run outside the GUI to create the modified file.
