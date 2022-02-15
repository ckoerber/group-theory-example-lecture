# Group Theory in Nuclear and Particle Physics Example Lecture

This repository contains slides which were presented in the weekly *"Group Theory in Nuclear and Particle Physics"* lecture (the 10th lecture) at Ruhr-University Bochum during the winter semester of 21/22.
The lecture is a master's level course for physicists and mathematicians.
This repository demonstrates how this framework was used.

You can access the slides under this link: [ckoerber.github.io/group-theory-example-lecture](https://ckoerber.github.io/group-theory-example-lecture/)

## Features
These slides contain dynamic elements such as
* a voice-over (recorded during the digital "live" lecture),
* [animated figures](https://ckoerber.github.io/group-theory-example-lecture/#/4/2),
* [white-board like derivations in the form of videos](https://ckoerber.github.io/group-theory-example-lecture/#/3/2)

The slides are based on the [reveal.js framework](https://revealjs.com/), were created using open-source tools only, and are under version control (this repository stores the entire presentation).

More details can be found in the [documentation](https://ckoerber.github.io/group-theory-example-lecture/docs/).

## Run

The presentation can be directly viewed in any browser (`index.html`) after cloning the repository.
I.e., all needed static files are included, and no additional `npm install` is needed (you may want to adjust this if you want to use this as a base for different projects).

Because of the current architecture (slides are separated into several files and included by `index.html`),
you have to launch a local webserver to generate the content.
This is done, i.e., by
```bash
python3 -m http.server
# or
npx  http-server
```
and visiting [http://{ip-address}:8000/](http://0.0.0.0:8000/) (where the IP-address is usually `127.0.0.1`, `localhost`, or `0.0.0.0`; the above command tells you where to look).
