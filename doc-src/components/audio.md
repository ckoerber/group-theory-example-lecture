
# Adding an audio voice-over

This section explains how to add an audio voice-over to the slides (or how to disable it).

## Used tools

* [Audacity](https://www.audacityteam.org/)
* [`scripts/label.py`](https://github.com/ckoerber/group-theory-example-lecture/blob/main/scripts/label.py)
* *(Already included in the presentation by default)* [reveal.js-plugins/audio-slideshow](https://github.com/rajgoel/reveal.js-plugins/tree/master/audio-slideshow) and [`static/js/timer.js`](https://github.com/ckoerber/group-theory-example-lecture/blob/main/static/js/timer.js)

## Concept

When recording the lecture, either using Audacity or Zoom, I create a single `mp3` file for the entire recording.
The custom JavaScript `static/js/timer.js` logs whenever I advance a slide (right and down).
This log can be imported into Audacity to identify reveal.js slides/fragments with sections of the recording (i.e., labeling the sound track).
The individually labeled track can be exported to multiple `mp3` files, which are automatically detected by the presentation.
This modularity allows replacing or modifying individual parts at a later point.

*(In principle, `reveal.js-plugins/audio-slideshow` adds a custom recorder to the browser with similar functionality.)*


## Steps

Creating and linking the audio files to the presentation works in two steps.
First, you have to create a presentation without the audio. Second, you have to record the audio and slide transitions ("Live").
Third, you have to combine the information regarding slide transitions with the recorded audio file ("Post-Processing").

### Live

1. Start a recording of the presentation.
2. Open the slides and press the `s` key to reset the timer.
3. Finish the presentation.
4. Press the `d` key to download the log
    (**it essential you download the log before closing the browser/tab or pressing the `s` key again**).

### Post-processing

5. Parse the downloaded CSV file into the Audacity readable format by running
```bash
python scripts/label.py [--coord "{timestamp}->{slide}"] log.csv
```
This script creates the file `log.csv.auda.txt`, which can be imported into Audacity.
The optional `--coord` flag allows associating a given timestamp with a given slide/fragment position.
I.e., `--coord "00:01:30->2.0"` specifies that the 1min 30s mark should correspond to slide transition `2.0`.
The slide positions and fragments can be read of the browser URL, but note that they are offset by one.
Once the `*.auda.txt` label file was created, you can manually adjust entries; i.e., remove unwanted transitions and adjust individual timings by editing the `txt` file (for example, in case of some transitions, in the beginning, should not be present).

2. Import the audio file `File > Import > Audio` and label file `File > Import > Labels` into Audacity.
3. Once you are happy with the label positions, export the individual files with `File > Export > Export Multiple...`. It is important to select:
    * "Split files based on Labels"
    * "Name files using Labels/Track Name"
    * and select the folder `media/audio/main` (can be changed)

The created audio files now correspond to the proper slide positions and are automatically detected by `audio-slideshow`.

## Configuration

The configuration of the auto-slideshow is handled in  [`static/js/main-w-audio.js`](https://github.com/ckoerber/group-theory-example-lecture/blob/main/static/js/main-w-audio.js).
See also [reveal.js-plugins/audio-slideshow](https://github.com/rajgoel/reveal.js-plugins/tree/master/audio-slideshow) for more options.
