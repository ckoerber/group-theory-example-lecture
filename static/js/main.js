Reveal.initialize({
    width: 1782, // 1460
    height: 1260, // 1050
    margin: 0.04,
    minScale: 0.2,
    maxScale: 2.0,
    center: true,
    slideNumber: true,
    history: true,
    pdfSeparateFragments: false,
    fragments: true,
    fragmentInURL: true,
    plugins: [
        RevealMarkdown,
        RevealMath.KaTeX,
        // RevealAudioSlideshow, // command this line if you want to exclude the audio slideshow
        RevealSearch
    ],
    katex: {
        version: 'latest',
        delimiters: [{
                left: '$$',
                right: '$$',
                display: true
            },
            {
                left: '$',
                right: '$',
                display: false
            },
            {
                left: '\\(',
                right: '\\)',
                display: false
            },
            {
                left: '\\[',
                right: '\\]',
                display: true
            }
        ],
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre']
    },
    // audio: {
    //     autoplay: false,
    //     playerStyle: 'position: fixed; bottom: 10px; left: 25%; width: 50%; height:75px; z-index: 33;',
    //     defaultAudios: true,
    //     prefix: 'media/audio/main/',
    //     suffix: ".mp3",
    //     defaultDuration: 600
    // }
})

window.addEventListener("load", function() {
    revealDiv = document.querySelector("body div.reveal")
    footer = document.getElementById("footer");
    revealDiv.appendChild(footer);
});
