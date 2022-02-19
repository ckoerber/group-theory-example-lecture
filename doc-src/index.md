# Lecture based on reveal.js

This repository contains slides presented in the weekly *"Group Theory in Nuclear and Particle Physics"* lecture (the 10th lecture) at Ruhr-University Bochum during the winter semester of 21/22.
The lecture is a master's level course for physicists and mathematicians.

In this documentation, you can find

* details and brief instructions about the used packages,
* the concept behind the slides and customizations made to match the weekly lecture schedule

## Modifications

These slides are based on [reveal.js](https://revealjs.com/).
The repository is already configured to load dependencies and style files automatically.
This configuration is implemented by the `index.html` file, which loads the content of the slides via the `<section data-markdown="slides/lecture-10/*.html">` tags.
The source code for individual slides can be found in the `slides/lecture-10/*.html` files.
If you want to update the slides, adjust the respective slide HTML.
If you want to add or remove slides, adjust or add corresponding section tags in the `index.html` file.
It is also possible to load [markdown files](https://revealjs.com/markdown/) instead of HTML files.
Both the markdown and HTML versions can render latex (wrapped with a single `$`for inline latex and a double `$$` for equation environments).

In the language of reveal.js, individual slides are called `<sections>` (html tags) and animated objects within slides are called [`class="fragment"`](https://revealjs.com/fragments/) (html attributes).
Contents like headings, paragraphs, lists, and images follow the standard HTML or markdown syntax.


## Run it
The slides can be viewed on a local machine without installing dependencies; they are already included in the static folder (no additional `npm install` is needed).
I.e., the presentation can be directly viewed in any browser (`index.html`) after cloning the repository.

Because of the current file layout (slides are separated into several files and included by `index.html`),
to properly access files, you have to launch a local HTTP server with
```bash
python3 -m http.server
# or
npx http-server
```
and visiting [http://{ip-address}:8000/](http://0.0.0.0:8000/) (where the IP-address is usually `127.0.0.1`, `localhost`, or `0.0.0.0`; the above command tells you where to look).

This server dependence can be circumvented by removing the `data-markdown="slides/lecture-10/0-about.html"` attributes in `index.html` and, instead, placing the file's content inside the `<section>` tags.

## Components


!!! note
    It was the design choice to place external dependencies rather on the creators' side so that the users (clients) only need to load a minimal set of dependencies&mdash;improving stability.
    The scripts and ideas explained in the following sections were used on macOS and Ubuntu systems.
    Some of the helper scripts used Python3.8.
    They are not thoroughly tested and should be viewed as an example for accomplishing the goal.
    I am happy to receive feedback and PRs which improve these steps.


* [Creating audio files and the voice-over](components/audio/)
* [Recording and embedding videos](components/video/)
* [Animating vector graphics](components/figures/)
* [Custom CSS and visual improvements](components/custom-css/)
* [Embedding slides into other frameworks (like Moodle)](components/embedding/)
