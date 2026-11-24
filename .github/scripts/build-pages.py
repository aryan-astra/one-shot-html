from argparse import ArgumentParser
from html import escape
import json
from pathlib import Path
import re
from shutil import copyfile


ROOT = Path(__file__).resolve().parents[2]
COVER = Path('assets/readme-html-foldout.png')
PAPER_NAME = re.compile(
    r'(sem|ct)-(\d{4})-([a-z0-9]+)-([a-z0-9]+(?:-[a-z0-9]+)*)\.html',
    re.IGNORECASE | re.ASCII,
)


def replace_contents(document, opening, closing, contents):
    start = document.index(opening) + len(opening)
    end = document.index(closing, start)
    return document[:start] + contents + document[end:]


def build(output):
    papers = []
    fallback_links = []
    for path in sorted(ROOT.iterdir()):
        match = PAPER_NAME.fullmatch(path.name)
        if not match or not path.is_file() or path.is_symlink():
            continue
        exam, year, code, slug = match.groups()
        title = slug.replace('-', ' ').title()
        label = escape(f'{title} ({code.upper()}) · {exam.upper()} {year}')
        papers.append(path)
        fallback_links.append(f'<li><a href="{escape(path.name)}">{label}</a></li>')

    catalog = json.dumps([path.name for path in papers], indent=2)
    index = (ROOT / 'index.html').read_text(encoding='utf-8')
    index = replace_contents(
        index, '<script type="application/json" id="catalog-files">', '</script>',
        f'\n{catalog}\n  ',
    )
    fallback = f'<ul>{"".join(fallback_links)}</ul>' if papers else '<p>No analyses published yet.</p>'
    index = replace_contents(index, '<noscript>', '</noscript>', fallback)

    output.mkdir(parents=True)
    (output / COVER.parent).mkdir()
    copyfile(ROOT / COVER, output / COVER)
    for paper in papers:
        copyfile(paper, output / paper.name)
    (output / 'index.html').write_text(index, encoding='utf-8')
    print(f'Prepared {len(papers)} analysis file(s) for GitHub Pages.')


if __name__ == '__main__':
    parser = ArgumentParser(description='Build the static SRM Exam Library.')
    parser.add_argument('output', type=Path, help='New directory for the generated site')
    build(parser.parse_args().output)
