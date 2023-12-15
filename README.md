# SFZ Instruments website

Originally integrated into the [SFZ Format website], now as standalone,
listing various sfz instruments published around the web, including the ones in
this Github organization.

Feel free to join our [Discord] chat and, if you want to contribute, you can also
check the [Wiki] to see how to add new instruments to the description list.

## Dependencies

The website is built using the following software and technologies:

- [AnchorJS] anchors headings, MIT license
- [Bootstrap] UI toolkit, code under MIT license, docs under [Creative Commons]
- [Favicon Generator] for favicons
- [Font Awesome] for icons, [SIL OFL 1.1] license
- [highlight.js] for syntax highlighting, BSD 3-Clause license
- [Markdown] markup language
- [MKDocs] static website generator, BSD-2-Clause license
- [SASS] for stylesheets, MIT license

## Local Build Quick-start Guide

Install [poetry] and run:

```bash
$ poetry install
$ poetry run mkdocs serve
```

Use the automatic setup via `mkdocs.sh`

The local website should be available at <http://localhost:8000/>

## Creating posts

This can be done either manually by creating a new .md file
in the `mkdocs/docs/news/posts` directory, paying attention for a correct filename,
date and [front-matter], or by running the following command:

```bash
$ ./new_post.sh "New post title" "<author_name>"
```

## License

The source code of this website is released under the [CC0-1.0] License.
See [LICENSE] file for details.


[AnchorJS]:           https://www.bryanbraun.com/anchorjs/
[Bootstrap]:          https://getbootstrap.com/
[CC0-1.0]:            https://creativecommons.org/publicdomain/zero/1.0/
[Creative Commons]:   https://creativecommons.org/licenses/by/3.0/
[Discord]:            https://discord.gg/t7nrZ6d
[Favicon Generator]:  https://realfavicongenerator.net/
[Font Awesome]:       https://fontawesome.io/
[front-matter]:       https://www.mkdocs.org/user-guide/writing-your-docs/#meta-data
[highlight.js]:       https://highlightjs.org/
[LICENSE]:            LICENSE
[Markdown]:           https://daringfireball.net/projects/markdown/
[MKDocs]:             https://www.mkdocs.org/
[poetry]:             https://python-poetry.org/
[SASS]:               https://sass-lang.com/
[SIL OFL 1.1]:        https://scripts.sil.org/cms/scripts/page.php?item_id=OFL
[SFZ Format website]: https://sfzformat.com/
[Wiki]:               https://github.com/sfzinstruments/sfzinstruments.github.io/wiki/Add-Instruments
