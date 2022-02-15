"""This script was inspired by

https://github.com/james-bird/layer-to-svg/blob/master/layer2svg.py

Adds fragment stack.
"""
import xml.etree.ElementTree as ET
import os
import copy
import click

TEMPLATE = """
<div class="r-stack">
{img_html}
</div>
"""

IMG_HTML = """  <img class="fragment" data-fragment-index="{n}" src="{src}">"""


@click.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("-n", default=0, show_default=True, type=int)
def main(file: str, n: int = 0):
    """Create new layer svg and print reveal include html."""
    folder = os.path.splitext(file)[0]
    print(f"Reading {file}")
    tree = ET.parse(file)
    root = tree.getroot()

    if not os.path.exists(folder):
        print(f"Creating folder {folder}")
        os.makedirs(folder)

    out_svgs = []
    for g in root.findall("{http://www.w3.org/2000/svg}g"):
        label = g.get("{http://www.inkscape.org/namespaces/inkscape}label")

        if label == "background":
            continue

        temp_tree = copy.deepcopy(tree)
        temp_root = temp_tree.getroot()

        # remove other layers
        for g in temp_root.findall("{http://www.w3.org/2000/svg}g"):
            label_other = g.get("{http://www.inkscape.org/namespaces/inkscape}label")
            if label_other != label:
                temp_root.remove(g)
            else:
                style = g.get("style")
                if isinstance(style, str):
                    style = style.replace("display:none", "display:inline")
                    g.set("style", style)

        f_name = os.path.join(folder, label + ".svg")
        temp_tree.write(f_name)
        out_svgs.append(f_name)

    print(
        TEMPLATE.format(
            img_html="\n".join(
                [IMG_HTML.format(n=i + n, src=src) for i, src in enumerate(out_svgs)]
            )
        )
    )


if __name__ == "__main__":
    main()
