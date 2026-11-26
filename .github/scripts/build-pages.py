from argparse import ArgumentParser
from html import escape
import json
from pathlib import Path
import re
from shutil import copyfile


ROOT = Path(__file__).resolve().parents[2]
QUESTION_ARCHIVE = 'CN_Question_Archive.html'
SITE_ASSETS = (
    'readme-html-foldout.png',
    'favicon.png',
    'srm-exam-library-share.png',
    'srm-exam-library-share.jpg',
)
CATALOG_TAG = '<script type="application/json" id="catalog-files">'
VERSION_LABELS = {'simplified': 'Simplified', 'detailed': 'Detailed'}
PAPER_NAME = re.compile(
    r'(sem|ct)-(\d{4})-([a-z0-9]+)-([a-z0-9]+(?:-[a-z0-9]+)*)(?:--(simplified|detailed))?\.html',
    re.IGNORECASE | re.ASCII,
)


def replace_contents(document, opening, closing, contents):
    start = document.index(opening) + len(opening)
    end = document.index(closing, start)
    return document[:start] + contents + document[end:]


def build(output):
    index = (ROOT / 'index.html').read_text(encoding='utf-8')
    credits = json.loads(index.split(CATALOG_TAG, 1)[1].split('</script>', 1)[0])
    papers = []
    courses = {}
    for path in sorted(ROOT.iterdir()):
        match = PAPER_NAME.fullmatch(path.name)
        if not match or not path.is_file() or path.is_symlink():
            continue
        exam, year, code, slug, version = match.groups()
        key = (exam.upper(), year, code.upper())
        title = slug.replace('-', ' ').title().replace(' And ', ' and ')
        _, files = courses.setdefault(key, (title, []))
        files.append((path.name, slug.lower(), version.lower() if version else None))
        papers.append(path)

    def credit_text(author):
        return f' · @{escape(author)}' if author else ''

    def fallback_link(filename, label):
        return f'<a href="{escape(filename)}">{escape(label)}</a>'

    fallback_links = []
    for (exam, year, code), (title, files) in courses.items():
        label = f'{title} ({code}) · {exam} {year}'
        version_groups = {}
        standalone = []
        for filename, slug, version in files:
            author = credits.get(filename)
            if version:
                version_groups.setdefault((slug, author), {})[version] = filename
            else:
                standalone.append(f'<li>{fallback_link(filename, label)}{credit_text(author)}</li>')
        for (_, author), versions in version_groups.items():
            links = ''.join(
                f'<li>{fallback_link(versions[version], version_label)}</li>'
                for version, version_label in VERSION_LABELS.items() if version in versions
            )
            fallback_links.append(f'<li>{escape(label)}{credit_text(author)}<ul>{links}</ul></li>')
        fallback_links.extend(standalone)

    catalog = json.dumps({path.name: credits.get(path.name) for path in papers}, indent=2)
    index = replace_contents(index, CATALOG_TAG, '</script>', f'\n{catalog}\n  ')
    fallback = f'<ul>{"".join(fallback_links)}</ul>' if papers else '<p>No analyses published yet.</p>'
    index = replace_contents(index, '<noscript>', '</noscript>', fallback)

    output.mkdir(parents=True)
    (output / 'assets').mkdir()
    for name in SITE_ASSETS:
        copyfile(ROOT / 'assets' / name, output / 'assets' / name)
    for paper in papers:
        copyfile(paper, output / paper.name)
    copyfile(ROOT / QUESTION_ARCHIVE, output / QUESTION_ARCHIVE)
    (output / 'index.html').write_text(index, encoding='utf-8')
    print(f'Prepared {len(papers)} analysis file(s) for GitHub Pages.')


if __name__ == '__main__':
    parser = ArgumentParser(description='Build the static SRM Exam Library.')
    parser.add_argument('output', type=Path, help='New directory for the generated site')
    build(parser.parse_args().output)
