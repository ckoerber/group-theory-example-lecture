var start = Date.now();
const header = ["s", "h", "v", "f"]
var data = [header];

document.addEventListener('keydown', keyPressed);

function keyPressed(e) {
    if (e.code == "KeyS") {
        start = Date.now()
        data = [header];
    }
    var tmp = Reveal.getIndices();
    var ddata = [(Date.now() - start) / 1000, tmp.h, tmp.v, tmp.f]
    if (e.code == "ArrowRight" | e.code == "ArrowDown") {
        data.push(ddata)
    }
    if (e.code == "KeyD") {
        let csvContent = "data:text/csv;charset=utf-8," + data.map(e => e.join(",")).join("\n");
        var encodedUri = encodeURI(csvContent);
        window.open(encodedUri);
    }
}
