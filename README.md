# One Shot HTML

[![Browse the exam library](https://img.shields.io/badge/Exam_library-Browse_online-A85D49?logo=githubpages&logoColor=white)](https://aryan-astra.github.io/one-shot-html/)
[![GitHub Pages deployment status](https://github.com/aryan-astra/one-shot-html/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/aryan-astra/one-shot-html/actions/workflows/pages.yml)

Student-made question-paper analyses for SRM semester exams and cycle tests. Search the [exam library](https://aryan-astra.github.io/one-shot-html/) by subject, course code, year, or exam type.

[Read Discrete Mathematics (21MAB302T) · SEM 2026](https://aryan-astra.github.io/one-shot-html/sem-2026-21MAB302T-discrete-mathematics.html)

<img src="assets/readme-html-foldout.png" width="640" alt="Two students exploring a foldout HTML file with multiple-choice answers, highlighted questions, and a graph">

## Contribute

Open a pull request with your self-contained `.html` files at the top level of the repo. Use hyphens between words in the course name.

| Exam | Filename |
| --- | --- |
| Semester exam | `sem-YYYY-COURSECODE-course-name.html` |
| Cycle test | `ct-YYYY-COURSECODE-course-name.html` |

For two versions of the same analysis, use the same course-name slug and add `--simplified` and `--detailed` before `.html` to show them on one card. If the filename is already taken by someone else's analysis, use a distinct course-name slug and keep the course code, exam type, and year the same so both cards show the same course title.

Add each filename and the author's GitHub username to the `catalog-files` data in `index.html` to display a credit badge.

The library picks up new and updated analyses when the pull request merges into `main`.
