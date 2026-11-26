# One Shot HTML

[![Browse the exam library](https://img.shields.io/badge/Exam_library-Browse_online-A85D49?logo=githubpages&logoColor=white)](https://aryan-astra.github.io/one-shot-html/)
[![GitHub Pages deployment status](https://github.com/aryan-astra/one-shot-html/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/aryan-astra/one-shot-html/actions/workflows/pages.yml)

Student-made question-paper analyses and archives for SRM semester exams and cycle tests. Search the [exam library](https://aryan-astra.github.io/one-shot-html/) by subject, course code, year, or exam type.

<img src="assets/readme-html-foldout.png" width="640" alt="Two students exploring a foldout HTML file with multiple-choice answers, highlighted questions, and a graph">

## Exam analyses

| Course | Exam | Contributor | Views |
| --- | --- | --- | --- |
| Computer Networks (`21CSC302J`) | SEM 2026 | [@aryan-astra](https://github.com/aryan-astra) | [Question archive](https://aryan-astra.github.io/one-shot-html/sem-2026-21CSC302J-computer-networks.html) |
| Discrete Mathematics (`21MAB302T`) | SEM 2026 | [@aryan-astra](https://github.com/aryan-astra) | [Analysis](https://aryan-astra.github.io/one-shot-html/sem-2026-21MAB302T-discrete-mathematics.html) |
| Formal Language and Automata (`21CSC301T`) | SEM 2026 | [@aryan-astra](https://github.com/aryan-astra) | [Simplified](https://aryan-astra.github.io/one-shot-html/sem-2026-21CSC301T-formal-language-and-automata--simplified.html) · [Detailed](https://aryan-astra.github.io/one-shot-html/sem-2026-21CSC301T-formal-language-and-automata--detailed.html) |
| Formal Language and Automata (`21CSC301T`) | SEM 2026 | [@Toib765](https://github.com/Toib765) | [Analysis](https://aryan-astra.github.io/one-shot-html/sem-2026-21CSC301T-formal-language-automata.html) |

Each view opens as a standalone HTML page. In the library, the two versions of an analysis appear side by side, and each contributor has their own course row.

## Contribute

Open a pull request with your self-contained `.html` files at the top level of the repo. Use hyphens between words in the course name.

| Exam | Filename |
| --- | --- |
| Semester exam | `sem-YYYY-COURSECODE-course-name.html` |
| Cycle test | `ct-YYYY-COURSECODE-course-name.html` |

For Simplified and Detailed versions of the same analysis, use the same course-name slug and add `--simplified` and `--detailed` before `.html`. If another contributor has already used the filename, choose a distinct course-name slug and keep the same course code, exam type, and year.

Add each filename and the author's GitHub username to the `catalog-files` data in `index.html` to display a credit badge.

GitHub Pages rebuilds the library when a pull request merges into `main`.
