import pandas as pd
import numpy as np
import click
from datetime import timedelta, datetime


def hvf2label(row):
    d = row.to_dict()
    f = row["f"]
    d["h"] = int(d["h"])
    v = str(int(d["v"]))
    out = "{h}".format(**d)
    if not np.isnan(f):
        f = int(f)
        f = f".{f}" if f >= 0 else ""
    else:
        f = ""
    return out + f".{v}" + f


def row2label(row):
    d = row.to_dict()
    return "{s0:7.3f}\t{s:7.3f}\t".format(**d) + hvf2label(row)


@click.command()
@click.argument("inp", type=click.Path(exists=True))
@click.option("--start", "-s", type=str)
@click.option("--length", "-l", type=str)
@click.option("--coord", "-c", type=str)
def main(inp, start=None, length=None, coord=None):
    try:
        df = pd.read_csv(inp, sep=r"\s+", dtype={"h": int, "v": int})
        assert list(df.columns) == ["s", "h", "v", "f"]
    except AssertionError:
        df = pd.read_csv(inp, sep=r",", dtype={"h": int, "v": int})
        assert list(df.columns) == ["s", "h", "v", "f"]

    df["label"] = df.apply(hvf2label, axis=1)

    if coord:
        timestamp, fragment = coord.split("->")
        timestamp = datetime.strptime(timestamp, "%H:%M:%S")
        seconds = timedelta(
            hours=timestamp.hour, minutes=timestamp.minute, seconds=timestamp.second
        ).total_seconds()
        idx = df.index[df["label"] == fragment][0]
        print(idx)
        assert idx > 0
        csv_seconds = df.loc[idx - 1, "s"]
        df["s"] += -csv_seconds + seconds

    if length:
        length = datetime.strptime(length, "%H:%M:%S")
        seconds = timedelta(
            hours=length.hour, minutes=length.minute, seconds=length.second
        ).total_seconds()
        offset = df["s"].max() - seconds
        df["s"] -= offset

    elif start:
        start = datetime.strptime(start, "%H:%M:%S")
        offset = timedelta(hours=start.hour, minutes=start.minute, seconds=start.second)
        df["s"] -= offset.total_seconds()

    print(df)
    df["s0"] = np.roll(list(df["s"]) + [0], 1)[:-1]
    s = "\n".join(df.apply(row2label, axis=1).values)

    print(s)
    with open(inp + ".auda.txt", "w") as out:
        out.write(s)


if __name__ == "__main__":
    main()
