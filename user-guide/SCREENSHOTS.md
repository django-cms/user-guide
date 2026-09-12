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

For a completely disposable local fixture, one command creates a django CMS project,
adds an `admin` superuser, creates a `/en/welcome/` page, nests a text plugin inside a
Frontend container plugin, starts the development server, captures the screenshots,
and removes the project again:

```console
make screenshots-temporary
```

This uses the `djangocms` command from the virtual environment and its official project
template. It therefore requires network access the first time. The temporary account
uses `admin` / `djangocms-screenshots`; override either value with
`DJANGOCMS_USERNAME` and `DJANGOCMS_PASSWORD` if desired.

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
- `evaluate` for small browser-side setup that cannot be expressed by another action

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
`frame` and `padding`. Common screenshot options include `quality` (JPEG only),
`omit_background`, `animations`, `caret`, `scale`, `hide`, `mask`, and `mask_color`.

Any string value can refer to an environment variable as `${NAME}`. A default can be
provided as `${NAME:-default}`. Missing variables without a default stop the run before
the browser is opened. `DJANGOCMS_PAGE_PATH` can point recipes at a fixture page other
than `/`; temporary-site mode sets it to `/en/welcome/?toolbar_on` automatically.

When upgrading django CMS, keep the image ids and output paths stable, point the recipe
at the new test instance, and adjust only URLs or selectors that changed. Run one
recipe headed while updating selectors, then run the complete set headlessly and
review the image diff before committing it.
