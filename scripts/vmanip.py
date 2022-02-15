"""Simple script which generates ffmpeg command to crop and speed up movie."""
import os

from PIL import Image  # Pillow 8.0.1
import cv2  # opencv-python 4.4.0.46

import streamlit as st  # streamlit 0.71.0
from streamlit_cropper import st_cropper, _resize_img  # streamlit-cropper   0.1.3


CWD = os.getcwd()


@st.cache
def get_frames(movie_file: str):
    """Capture images as array from movie."""
    if not os.path.exists(movie_file):
        files_in_dir = os.listdir(os.path.dirname(movie_file))
        raise ValueError(f"Could not locate movie (files in dir {files_in_dir})")
    _, extension = os.path.splitext(movie_file)
    if extension not in [".mov", ".mp4"]:
        raise ValueError("Format not supported")

    capture = cv2.VideoCapture(movie_file)

    images = []

    success, count = True, 0
    while success:
        capture.set(cv2.CAP_PROP_POS_MSEC, (count * 5000))
        success, image = capture.read()
        if success:
            images.append(image)
        count += 1

    return images


def get_command(filename, box, speedup=1.0, extension="mp4"):
    """Creates ffmpeg command which crops and speeds up movie (if desired)."""
    outfile = filename.split(".")
    outfile = ".".join(outfile[:-1] + ["cropped", extension])
    w, h, l, t = (box[key] for key in ["width", "height", "left", "top"])

    return (
        " ".join(
            [
                "ffmpeg",
                "-i",
                filename,
                "-filter_complex",
                f'"[0]setpts={1/speedup:1.2f}*PTS[b];'
                f"[b] crop = {w}:{h}:{l}:{t}[c];"
                f'[0]atempo={speedup:1.2f}[a]"'
                f' -map "[c]" -map "[a]" {outfile}',
            ]
        )
        if abs(speedup - 1.0) > 0.009
        else f'ffmpeg -i {filename} -filter:v "crop={w}:{h}:{l}:{t}" {outfile}'
    )


def main():
    """Run script."""
    st.header("Movie cropper")
    st.text("Tool to obtain ffmpeg command for cropping and speeding up movies.")
    st.text(f"Workdir: {CWD}")
    movie_file = st.text_input(label="Specify a movie")

    if movie_file:
        images = get_frames(movie_file)
        index = st.slider(
            "Select a movie frame",
            min_value=1,
            max_value=len(images) - 1,
            value=len(images) - 1,
            step=max(int(len(images) / 20), 1),
        )
        img = Image.fromarray(images[index])

        box = st_cropper(
            img,
            realtime_update=True,
            box_color="#0000FF",
            aspect_ratio=None,
            return_type="box",
        )

        # st_cropper rescales the image, this repeats the resizing to present preview...
        img_resized = _resize_img(img)
        cropped_img = img_resized.crop(
            (
                box["left"],
                box["top"],
                box["width"] + box["left"],
                box["height"] + box["top"],
            )
        )
        st.text("Preview")
        st.image(cropped_img)

        # ... and to invert the rescaling to get the box for the movie
        ratio = img.size[0] / img_resized.size[0]
        actual_box = {key: int(val * ratio) for key, val in box.items()}
        st.json(actual_box)

        speedup = st.slider(
            "Speed up movie?", min_value=0.5, max_value=2.0, value=1.1, step=0.05,
        )
        extension = st.text_input("Output extension?", value="mp4")
        command = get_command(
            movie_file, actual_box, speedup=speedup, extension=extension
        )
        st.code(command)


if __name__ == "__main__":
    main()
