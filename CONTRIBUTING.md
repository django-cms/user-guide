# Contributing to the django CMS User Guide

Thank you for helping to improve the django CMS user guide! Contributions of all
sizes are welcome — from fixing a typo to writing a new how-to guide or capturing
screenshots. If you have questions, join us on
[our friendly Discord channel](https://discord-docs-channel.django-cms.org/).

## Building the documentation locally

The documentation is built with [Sphinx](https://www.sphinx-doc.org/) from
reStructuredText sources in `user-guide/source/`.

```bash
cd user-guide
make install   # create a virtualenv and install dependencies
make run       # live-reload server at http://localhost:8001
```

One-off builds:

```bash
cd user-guide
make html      # build to user-guide/build/html
```

CI builds the docs with the `dirhtml` builder in *nit-picky* mode, which treats
broken cross-references as warnings you should fix:

```bash
cd user-guide
. env/bin/activate
sphinx-build -b dirhtml -n -d build/doctrees source build/dirhtml
```

Other useful checks (also run by CI or Read the Docs):

```bash
codespell user-guide/source   # common-typo check (CI runs this)
cd user-guide
make spelling                 # en_GB spell check; add valid terms to user-guide/spelling_wordlist
make linkcheck                # verify external links
```

## How the guide is organized: Diátaxis

The guide follows the [Diátaxis framework](https://diataxis.fr/), which divides
documentation into four quadrants with distinct purposes. Before writing, decide
which quadrant your content belongs to:

| Section (folder) | Diátaxis quadrant | Purpose |
|---|---|---|
| Tutorial (`tutorial/`) | Tutorial | A *lesson*: takes a newcomer by the hand through a series of steps. Minimal explanation, the learner does something at every step. |
| How-to guides (`how-to/`) | How-to guides | A *recipe*: numbered steps to achieve **one specific goal**, for a user who already knows the basics. Link to concepts instead of explaining them inline. |
| Concepts (`explanation/`) | Explanation | *Understanding*: explains why django CMS works the way it does. No step-by-step instructions. |
| Reference (`reference/`) | Reference | *Information*: austere, structured description of the editing interface (menus, fields, states, plugins). No instruction, no persuasion. |

Note: the section visible to readers is titled **"Concepts"** (friendlier for
content editors), but it corresponds to Diátaxis "Explanation" and lives in the
`explanation/` folder.

## Conventions

- **Do not rename or move existing `.rst` files.** The published documentation
  uses one URL per file (`dirhtml` builder); renaming a file breaks published
  URLs. Rewrite files in place. If a move is unavoidable, a redirect must be set
  up in the Read the Docs dashboard.
- **Brand spelling:** always *django CMS* (lowercase "django"), even at the start
  of a sentence.
- **Section markers:** `=` for the page title, `-` for sections, `~` for
  subsections.
- **Labels:** pages and sections that are cross-referenced get a label such as
  `.. _how-to-add-image:` on the line above the heading; link with
  ``:ref:`how-to-add-image` ``.
- **Shared notes:** reusable admonitions live in `user-guide/source/*.include`
  (`versioning-note`, `frontend-note`, `alias-note`, `contribute-note`). Include
  them with `.. include:: ../versioning-note.include` instead of duplicating the
  text.
- **Images** live in an `images/` directory next to the page that uses them.
  Tutorial images are prefixed with the lesson number (`05-pagetree.jpg`); other
  sections use kebab-case names starting with the page stem
  (`redirect-settings.jpg`). Pages may reuse images from other sections via
  relative paths such as `../tutorial/images/02-toolbar.jpg`.
- **Spelling** is British English (en_GB), checked with
  `sphinxcontrib-spelling`. Add legitimate new terms to
  `user-guide/spelling_wordlist`.

## Screenshot placeholders

Screenshots are captured from the
[django CMS quickstart project](https://github.com/django-cms/django-cms-quickstart).
If you write content but cannot capture a screenshot, add a placeholder where the
image will eventually go, using exactly this pattern:

```rst
.. todo::

    **Screenshot needed:** ``how-to/images/add-image-dialog.png`` —
    Image plugin edit dialog with the media library picker open. Quickstart
    project, light colour scheme, browser window ~1200 px wide.

.. Uncomment once the screenshot exists:
.. .. image:: images/add-image-dialog.png
..     :alt: The Image plugin dialog with the media library picker open
```

Rules:

- The `todo` body starts with the literal marker `**Screenshot needed:**`,
  followed by the path of the future image (relative to `user-guide/source/`),
  an em dash, and a one-sentence description of what to capture (subject, state
  of the UI, anything that must be visible).
- Immediately below, include the final `.. image::` directive **commented out**
  (each line prefixed with `.. `), with the filename and `:alt:` text already
  written, so enabling the image is a simple uncomment once it is captured.
- Add a matching row to [`SCREENSHOTS.md`](SCREENSHOTS.md).

Placeholders render as visible "Todo" admonitions in the built documentation
(`todo_include_todos = True`), inviting readers to contribute the missing
capture.

All currently needed captures are listed in [`SCREENSHOTS.md`](SCREENSHOTS.md).
You can audit the list against the sources with:

```bash
grep -rn "Screenshot needed" user-guide/source --include="*.rst"
```

Capturing screenshots is one of the easiest ways to contribute: set up the
quickstart project, follow the capture description, and open a pull request that
adds the image and uncomments the prepared `.. image::` directive.
