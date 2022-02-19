# Animating vector graphics

This section explains a possible way how you can build up vector graphics like on [Slide 4/2 in the example lecture](https://ckoerber.github.io/group-theory-example-lecture/#/4/2).
It assumes you already have created or have access to a vector graphic (i.e., a PDF or SVG).

## Used Tools

* [Inkscape](https://inkscape.org/) (but any other tool to form SVG layers should work as well)
* [`scripts/layer2svg.py`](https://github.com/ckoerber/group-theory-example-lecture/blob/main/scripts/layer2svg.py) (i.e., Python3)


## Concept

To me, the most stable solution for animating figures is to include figure elements as individual fragments. This solution does not require additional client-side dependencies and allows a stable PDF export.

## Steps

The essential steps to animate the graphics are:

1. Import the vector graphic to Inkscape.
2. Move animation steps to individual layers.
3. Export the layered figure to `SVG`.
4. Run `scripts/layer2svg.py` to create individual `SVG` files for each layer.
5. Include and adjust the corresponding HTML inside your slides.


### Move animation steps to individual layers in Inkscape

Once a file was imported to Inkscape (`File > Open`), the steps are:

1. Open the Layers tab via `Layer > Layers`.
2. Create a new layer for the next animation step, `Layer > Add layer`.
3. Select all objects you do not want on the first animation step and move them to the new layer (`Layer> Move Selection to Layer Above`). Depending on the input, it might not directly be possible to select some objects alone; you may have to ungroup them first `Object > Ungroup` (or you may want to group them for easier handling `Object > Group`).
4. Repeat this procedure until you have separated all objects onto their respective animation layer
5. Export to SVG by `File > Save as` and select the SVG format

### Create individual SVG files for each layer

For convenience, I have provided a script (inspired by [github.com/james-bird/layer-to-svg/](https://github.com/james-bird/layer-to-svg/blob/master/layer2svg.py)) which exports the newly created layers into their own `SVG`.

I.e., running
```bash
python3 scripts/layer2svg.py [-n 0] media/imgs/figure.svg
```
will create the separated SVG files in
```bash
media/imgs/figure/layer1.svg
media/imgs/figure/layer2.svg
...
```
and also prints the corresponding reveal.js HTML
```html
<div class="r-stack">
  <img class="fragment" data-fragment-index="0" src="media/imgs/layer1.svg">
  <img class="fragment" data-fragment-index="1" src="media/imgs/layer1.svg">
  ...
</div>
```
which can be directly included in the slides.

The `-n` option allows specifying the starting `data-fragment-index`.
The `data-fragment-index` can be omitted but may make it easier to coordinate text and graphic appearance orders in the slides.
