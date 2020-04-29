---
title: Add instruments
---
In order to add a SFZ instrument sample library to the site list, the following
steps are required:

- Create a new page under `/software/instruments`, inside a proper category
	subdirectory, e.g.: `/software/instruments/pianos/some_piano.md`.
	The category must match with the `page` information in the YAML DB (see below).

- Add the instrument information in the `_data/sfz/instruments.yml` DB.

- If an audio demo is available for the instrument, it must be made in mp3 format,
	placed in the `/assets/audio` directory with the same name and category as
	the page, so for the example described above it will be at
	`/assets/audio/pianos/some_piano.mp3`. A demo player will be added in the
	resulting HTML page.

## Category index page

If the instrument will take part of a new category, an index page must be created
with a related page name. For example in `/software/instrument/basses/`:

```
---
title:  "Basses"
layout: "no_title"
---
{% raw %}{% include sfz/instruments_table.html %}{% endraw %}
```

the `title` value can be arbitrary, it's just what will be displayed
on the browser window title.

## Instrument page

For example, a `/software/instruments/pianos/some_piano.md` will be:

```
---
title:  "Some Piano"
layout: "sfz/instrument"
---
<here will be inserted automatically the instrument brief description in the DB>

Here goes only an optional, detailed instrument description content,
that will be appended to the brief description above. The empty line will be
added automatically as separator, no need to add one manually.
```

## The DB entry

Both instruments and related categories are added manually in alphabetic order.
As example:

```yaml
categories:
- name: ...

- name: "Pianos"
  page: "pianos"
  instruments:
  - name:    "Some piano" # page title, may be different from the one used in the browser title bar
    page:    "some_piano" # page file name without extension
    version: "1.2"        # if any version specified, optional
    author:  "Some Author"
    license: "CC-BY-3.0"  # if any license specified, optional
    url:     "https://some_author.com/some_piano"
    download_size: "6 GB" # total download size to display in the pianos list
    short_description:
      "A great piano sample library in SFZ format."
    use_details_page: true # used when having an instrument page, not used to link to the instrument website directly
    downloads:
    - label: "Instrument"
      url: "https://some_author.com/some_piano.zip"
      format: "wav"
      samplerate: "44.1"
      size: "5 GB"
      short_description: "Zipped file"

    - label: "Manual"
      url:   "https://some_author.com/some_piano_en.zip"
      size:  "1 GB"
      short_description: "English manual."
...
```
When specified, licenses must be in [SPDX License ID] format.

[SPDX License ID]: https://spdx.org/licenses/
