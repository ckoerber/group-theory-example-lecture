# About

Because of the COVID-19 Pandemic, it was not feasible to have in-person (university) lectures during the entire year of 2021.
Remote lectures were Zoom meetings.
On first thought, the two most common options for presenting theoretical knowledge are

* white-board like lectures where the majority of the meeting uses handwritten visuals, and
* the presentation of slides.

Depending on the content, both have down- and upsides. So, why shouldn't one use both?

Having the demands that:

* The lectures should be reasonably standalone. I.e., accessibly both in "live" events and "asynchronously" on learning platforms (like Moodle).
* The asynchronous part should be interactive and searchable.
* The lectures should contain dynamic elements (videos, intractable graphs, quizzes, ...).
* The lectures should be under version control and editable by the Teaching Assistants (i.e., platform-independent and uses open-source stacks; with a strong emphasis here)

While LaTeX/Beamer fulfills most of the points (though I find it relatively hard to obtain "visual beauty"), it does not allow dynamic components; so one would have to develop and deploy further resources.

While Keynote and PowerPoint fulfill the first points, they are unfortunately not open-source, and it is not useful to place related files under version control (plus they have a relatively large memory footprint).

This eventually brought me to `reveal.js`&mdash; combining all of the above aspects; I would describe it as the dynamic web-equivalent of beamer.

Arguably, creating such material is a lot of work in the first place.
However, I believe that if properly developed over multiple iterations, such material ensures a better education for future students and may even save preparation time in the long run.
