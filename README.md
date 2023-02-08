# [SFZ Instruments] website

[![CC0 Badge]][CC0-1.0]

Originally part of [SFZ Format website], available here also as standalone,
listing instruments published in this organization and other external sites.

Check the [Wiki] to see how to add new instruments to the description list.

## Dependencies

The website is built using [Jekyll]. [Node.js] to compile
all static assets including the [Bootstrap] library and built on
along with the [SASS] stylesheets. Most of the content on the website is
written using [Markdown].
Icons are provided by [Font Awesome], favicons by [Favicon Generator].
Anchors headings are provided by [jekyll-anchor-headings] by [Alleyo],
licensed under the MIT license.

## Local Build Quick-start Guide

- Install the required dependencies: `ruby` and `yarn`
- Use the automatic setup via `setup.sh`

or manually:

```bash
$ gem update
$ gem install bundler
$ yarn --no-bin-links
$ yarn dist
$ bundle exec jekyll serve --watch --host 0.0.0.0
```

The local website should be available at <http://localhost:4000/>

## Creating posts

This can be done either manually by creating a new .md file
in the [_posts] directory, paying attention for a correct filename, date and
[front-matter], or by running the following command:

```bash
$ ./new_post.sh "New post title" "<author_name>"
```

## License

The source code of this website is released under the [CC0-1.0] License.
See [LICENSE] file for details.

[Alleyo]:                 https://pure-liquid.allejo.org/
[Bootstrap]:              http://getbootstrap.com/
[Favicon Generator]:      https://realfavicongenerator.net/
[Font Awesome]:           http://fontawesome.io/
[front-matter]:           https://jekyllrb.com/docs/front-matter/
[Jekyll]:                 http://jekyllrb.com/
[jekyll-anchor-headings]: https://github.com/allejo/jekyll-anchor-headings/
[Markdown]:               https://daringfireball.net/projects/markdown/
[Node.js]:                http://nodejs.org/
[_posts]:                 https://github.com/sfzinstruments/sfzinstruments.github.io/tree/source/_posts/
[SASS]:                   https://sass-lang.com/
[SFZ Format website]      https://sfzformat.com/
[SFZ Instruments]:        https://sfzinstruments.github.io/
[Wiki]:                   https://github.com/sfzinstruments/sfzinstruments.github.io/wiki/Add-Instruments

[LICENSE]:   LICENSE
[CC0 Badge]: https://badgen.net/badge/license/CC0/orange
[CC0-1.0]:   https://creativecommons.org/publicdomain/zero/1.0/
