.. _ref-plugins:

Standard plugins
================

The plugins available to you depend on the site's configuration and on the placeholder
or parent plugin you are using. This page describes the plugins included in a typical
django CMS quickstart project. Your site may add, remove, rename or restrict them.

For the actions common to every plugin, see :ref:`Filling in content <plugins>`,
:ref:`Rearranging content <how-to-rearrange-content>` and :ref:`Copying content
<how-to-copy-content>`.

Generic
-------

**Text**
    Adds formatted text, including paragraphs, headings, lists and links.

    :Fields: Rich text edited in the editor that opens when you add or change the
             plugin.
    :Note: The editor's **"CMS Plugins"** menu can embed images, links and other
           supported plugins inside the text. See :ref:`Creating links and buttons
           <how-to-links>` and :ref:`Adding an image <how-to-add-image>`.

**Alias**
    Displays a reusable content block maintained separately from the page. Publishing
    a change to the alias updates every place that displays it.

    :Fields: The alias to display.
    :Note: See :ref:`Reusing content with aliases <how-to-aliases>`.

Frontend
--------

.. include:: ../frontend-note.include

These plugins provide common layout and interface components. Their appearance and
available options depend on the site's design, so the result may differ from the
examples described here.

**Accordion**
    Groups content into sections that expand and collapse vertically.

**Alert**
    Displays a prominent status or feedback message, such as information, success,
    warning or danger.

**Badge**
    Displays a small label, status or count.

**Blockquote**
    Marks a quotation and can identify its source.

**Card**
    Groups related content in a bordered or styled panel.

    :Fields: Background style, text alignment and nested card components such as a
             header, body, footer or image overlay.
    :Note: Use **Card layout** to arrange several cards together.

**Card layout**
    Arranges multiple Card plugins in a grid or deck.

**Carousel**
    Presents a sequence of slides containing images or other content.

    :Fields: Transition, interval, controls and indicators. Add each slide as a nested
             **Carousel slide** plugin with an optional image, caption and link.

**Code**
    Displays a block of computer code with suitable formatting.

**Collapse**
    Lets visitors show and hide nested content.

**Container**
    Groups, aligns and constrains other plugins as one page section.

    :Fields: Fixed, fluid or breakpoint-specific width; spacing; background options.
    :Tip: Give the container a descriptive title such as "Team" or "Contact". The title
          appears in the structure board and makes long pages easier to navigate.

**Editor note**
    Adds a note that editors can see but visitors cannot.

**Figure**
    Groups an image or other media with related text, such as a caption.

**Heading**
    Adds a heading with an optional link target.

    :Fields: Heading text, level (H1–H6), and an optional anchor used by links and the
             **Table of contents** plugin.

**Icon**
    Displays an icon from the icon set configured for the site.

**Jumbotron (deprecated)**
    Displays a large highlighted section. Use the layout components recommended by
    your site's designers for new content.

**Link / Button**
    Links to another page, an external URL, a file, a telephone number or an email
    address. It can appear as a text link or a styled button.

    :Fields: Link text, destination, link type, visual context, size and target.
    :Note: See :ref:`Creating links and buttons <how-to-links>`.

**List group**
    Presents a series of related items as a vertical list.

**Media**
    Places media beside nested content, for example an image beside a short text.

**Picture / Image**
    Displays an image from the media library or an external image URL.

    :Fields: Image, dimensions, alignment, optional link, responsive behaviour and
             thumbnail options.
    :Note: See :ref:`Adding an image to a page <how-to-add-image>`.

**Row** and **Column**
    Build responsive multi-column layouts. Columns live inside rows; content plugins
    live inside columns.

    :Fields: Row alignment and gutters; Column width, alignment and offset at each
             configured responsive breakpoint.

**Spacing**
    Adds configurable space around nested content.

**Table of contents**
    Builds a linked list from Heading plugins rendered before it on the page.

**Tabs**
    Groups content into labelled panels and displays one panel at a time.
