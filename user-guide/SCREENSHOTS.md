# Regenerating screenshots

The screenshots in this guide can be generated from a prepared django CMS test site
with Playwright. The recipe is kept in `screenshots.yml`; credentials stay in
environment variables and must not be committed.

## First-time setup

From the `user-guide` directory, create the documentation environment and install the
browser tooling:

```console
make install
make screenshots-install
```

Prepare a representative django CMS site with stable content, an English interface,
and a staff user. Then run:

```console
export DJANGOCMS_BASE_URL=http://localhost:8000
export DJANGOCMS_USERNAME=admin
export DJANGOCMS_PASSWORD='...'
make screenshots
```

For a completely disposable local fixture, one command creates and seeds a django CMS
project, starts its development server, captures the screenshots, and removes the
project again:

```console
make screenshots-temporary
```

This uses the `djangocms` command from the virtual environment and its official project
template. It therefore requires network access the first time. The temporary account
uses `admin` / `djangocms-screenshots`; override either value with
`DJANGOCMS_USERNAME` and `DJANGOCMS_PASSWORD` if desired.

The fixture enables versioning and aliases and provides stable data for the complete
guide, not only the toolbar overview:

| Area | Seeded fixture |
|---|---|
| Pages | Welcome, About us, Services, Consulting, Training, and Contact, including a nested Services branch and mixed publication/navigation states |
| Languages | Published English and German content on the Welcome page |
| Plugins | A titled container with nested text, image, standalone Link / Button, inline file link, and alias plugins |
| Media | A `Tutorial` folder containing a generated PNG with alt text and a sample PDF |
| Aliases | A `Shared sections` category and versioned `Contact callout` alias |
| Versions | Four English Welcome versions: one unpublished, one published, one archived, and one current draft with content differences suitable for comparison |

The main fixture is available at `/en/welcome/`. Its version history and draft make
the toolbar publish controls, version menu, manage-versions list, version comparison,
and all four version-state indicators available to screenshot recipes.

## Capture inventory

The repository audit found 36 browser-generated images referenced by the guide. Every
one has an enabled recipe in `screenshots.yml`. The page-tree illustration
(`tutorial/images/05-pagetree.jpg`) and version-state diagram
(`tutorial/images/08-version-states.png`) are explanatory artwork and deliberately stay
outside the Playwright recipe. Older, unreferenced images are not regenerated.

Run `python scripts/capture_screenshots.py --list` to print the machine-readable
inventory. The test suite also compares the YAML outputs with image directives and
“Screenshot needed” markers in all RST files, so adding a documentation screenshot
without adding its recipe fails the tests. It also rejects a “Screenshot needed” marker
when the requested image already exists.

Existing image files are replaced only after their new capture succeeds. Run against
a disposable or backed-up site: actions such as clicking a Publish button can change
CMS content.

To test another django CMS version, start that version's prepared site and either
change `DJANGOCMS_BASE_URL` or use the command-line override:

```console
python scripts/capture_screenshots.py --base-url http://cms-5-1.test:8000
```

Useful development commands are:

```console
# Validate the recipe and display its output files without opening a browser.
python scripts/capture_screenshots.py --dry-run

# Develop or debug a single recipe in a visible browser.
python scripts/capture_screenshots.py --headed --only 'project-menu'

# Capture a group selected by id or output path.
python scripts/capture_screenshots.py --only 'toolbar-*' --only '*/08-*'
```

## Recipe format

Paths in `output_dir` are relative to `screenshots.yml`. Each screenshot needs a
unique `id` and an `output` path. `url` is relative to `base_url`; absolute URLs also
work. Screenshots run in file order in one authenticated browser context.

```yaml
screenshots:
  - id: page-menu
    url: /en/?toolbar_on
    output: tutorial/images/02-page-menu.jpg
    actions:
      - click: '[aria-label="Page menu"]'
      - wait_for:
          selector: '.cms-dropdown-menu[aria-expanded="true"]'
          state: visible
    labels:
      - selector: '.cms-logo'
        text: Logo
        position: top-left
      - selector: '.cms-dropdown-menu[aria-expanded="true"]'
        text: Page menu
        position: outside-right
        color: '#005a9c'
    capture:
      selector: '.cms-dropdown-menu[aria-expanded="true"]'
      padding: 8
      quality: 90
      hide:
        - '.timestamp'
      mask:
        - '.private-customer-name'
```

Use `enabled: false` to retain a work-in-progress recipe without running it. The
global `setup` actions run once; `before_each` runs before every selected screenshot;
an entry's `actions` run immediately before its capture.

Supported actions are:

- `goto`, `reload`, `click`, `double_click`, `fill`, `press`, `hover`, `check`,
  `uncheck`, `select_option`, and `scroll_into_view`
- `wait_for`, `wait_for_timeout`, and `wait_for_load_state`
- `evaluate` for small browser-side setup that cannot be expressed by another action;
  it accepts `frame` when the expression must run inside a modal or sideframe

Most element actions accept either a selector string or a mapping. A mapping can also
contain Playwright options such as `timeout` or `force`. Use `frame` alongside
`selector` when an element is inside an iframe:

```yaml
- fill:
    frame: 'iframe[title="Edit plugin"]'
    selector: 'input[name="name"]'
    value: Example
```

With no capture option, the current viewport is saved. Set `full_page: true` to save
the whole page, or set `selector` to save one element. Element captures also support
`frame` and `padding`. Add an `include` list of CSS selectors to expand the crop to
other visible elements in the same document—for example, to include the toolbar
entry that opened a dropdown. Common screenshot options include `quality` (JPEG
only), `omit_background`, `animations`, `caret`, `scale`, `hide`, `mask`, and
`mask_color`.

Use `labels` to identify important elements in the resulting image. Each label draws
a temporary coloured outline around the matching element and places its text inside
one corner. `selector` and `text` are required. `position` can be `top-left` (the
default), `top-right`, `bottom-left`, or `bottom-right`. To place the badge next to
the element instead, use `outside-top`, `outside-right`, `outside-bottom`, or
`outside-left`. Bottom labels are centred by default; use `outside-bottom-left` or
`outside-bottom-right` to align them with the corresponding edge of the element.
Element captures automatically expand to include outside badges; `color` defaults to
django CMS magenta (`#d40055`). A label can also use `frame` when its element is
inside an iframe. Selectors must resolve to one visible element. Labels affect only
the screenshot and are removed from the page immediately after capture.

Any string value can refer to an environment variable as `${NAME}`. A default can be
provided as `${NAME:-default}`. Missing variables without a default stop the run before
the browser is opened. `DJANGOCMS_PAGE_PATH` can point recipes at a fixture page other
than `/`; temporary-site mode sets it to `/en/welcome/?toolbar_on` automatically.

When upgrading django CMS, keep the image ids and output paths stable, point the recipe
at the new test instance, and adjust only URLs or selectors that changed. Run one
recipe headed while updating selectors, then run the complete set headlessly and
review the image diff before committing it.
