# Group Theory in Nuclear and Particle Physics Slide

## How to port from Keynote

1. Copy each div from Keynote into pages
2. Export to word
3. Import on ubuntu and export to html
4. run `scripts/clean_html.py` over exported html
5. Copy into proper reveal.js shape.

## Resize windows (ubuntu)

```bash
wmctrl -l
wmctrl -r Firefox -e 0,100,100,1485,1150
wmctrl -r UxPlay@ckoerber-2020 -e 0,1585,100,835,1112
```
## Install
You need `npm` installed to build the dependencies
```bash
npm install .
```
And `sass` to compile the `scss` file to a `css` file
```bash
make css
```

Download and extract the [RUB corporate fonts](https://serviceportal.ruhr-uni-bochum.de/Begriffesammlung/Documents/RUB-Corporate-Design-Fonts.zip) into `static/fonts`

## Run

The presentation can be viewed in any browser (`index.html`).

Ideally, you can run it on a localhost (this allows including slides), by running
```bash
python3 -m http.server
```
and visiting http://0.0.0.0:8000/ or (your ip) instead.

Additionally, versions of Chrome browsers can be used [to export it to `pdf`](https://revealjs.com/pdf-export/): [index.html?print-pdf](index.html?print-pdf).
