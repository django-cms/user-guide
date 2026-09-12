.. _ref-plugins:

Standard plugins
================

Each site has its own set of installed plugins. This reference is based on the plugins
installed with django CMS quickstart. For how to work with plugins in general, see
:ref:`filling in content <plugins>` in the tutorial.

django CMS groups its plugins into categories. We list the plugins by category.

Generic
-------

**Text**
    The text plugin is a simple yet versatile plugin used for adding and editing text
    content. It allows you to directly insert formatted text, such as paragraphs,
    headings, lists, and links.

    :Fields: The rich text itself, edited in the editor that opens when the plugin is
             added or changed.
    :Note: Other plugins (images, links, ...) can be embedded into the text through
           the "CMS Plugins" menu of the editor. See :ref:`how-to-internal-links` and
           :ref:`how-to-add-image`.

**Alias**
    The Alias plugin is a powerful tool that enables content editors to display certain
    content on many pages without duplicating it. The Alias plugin let predefined
    content blocks appear at its position by linking them. If the alias content is
    updated, the linked content also changes.

    :Fields: Alias — the alias whose content is displayed at this position.
    :Note: See :ref:`Reusing content with aliases <how-to-aliases>`.

Frontend
--------

.. include:: ../frontend-note.include

The frontend plugins are part of the djangocms-frontend package, which might (or might
not) be installed on your site. Its purpose is to provide web site components like
sliders, accordions, etc. for content editors. Those components in most cases are
implemented by the designer of the web site. Content editors can use the component
at any place on the site.

**Accordion**
    Use the Accordion plugin to build vertically collapsing accordions.

**Alert**
    Provide contextual feedback messages for typical user actions for a handful of
    contexts: success, warning, danger, info, ....

**Badge**
    Provide small counters or pieces of information for a handful of contexts: success,
    warning, danger, info, ....

**Blockquote**
    Quote blocks of content from another source. Optionally provide a source.

**Card**
    Structure content with a flexible and extensible container with multiple variants
    and options

    :Fields: Background context (colour), text alignment, card components (header,
             body, footer, image overlay) added as nested plugins.
    :Note: Use "Card layout" to arrange several cards in a grid or deck.

**Card layout**
    Organise several cards into one layout

**Carousel**
    Cycle through elements, images or slides of text, like a carousel.

    :Fields: Transition style, interval, controls and indicator options; the slides
             are added as nested "Carousel slide" plugins, each with an image,
             optional caption and link.

**Code**
    Present (computer) code blocks

**Collapse**
    Toggle the visibility of content

**Container**
    Contain, pad, and align your content within a given device or viewport for
    responsive designs

    :Fields: Container type (fixed, fluid or breakpoint-specific), spacing and
             background options. All fields are optional.
    :Tip: The title field is shown in the plugin tree — name your containers after the
          page sections they hold to keep large plugin trees navigable.

**Editor note**
    Mark contents visible to editors only

**Figure**
    Display related images and text

**Heading**
    Add headline with optional anchor.

    :Fields: Heading text, heading level (H1–H6), optional anchor identifier that can
             be used as a link target and by the "Table of contents" plugin.

**Icon**
    Give visual clues by adding icons

**Jumbotron (deprecated)**
    Showcase your hero unit

**Link / Button**
    Reference and link other contents

    :Fields: Link text; destination (internal page, external URL, file, phone number
             or email address); link type (text link or button) and button context
             (colour); size and target options.
    :Note: See :ref:`Creating links and buttons <how-to-links>`.

**List group**
    Displaying a series of content flexibly. Modify and extend them to support just
    about any content within.

**Media**
    Construct highly repetitive components like blog comments, tweets, and the like

**Picture / Image**
    Show images from the media library

    :Fields: Image (chosen from the media library or uploaded directly); optional
             external image URL; width, height and alignment; optional link (internal
             page or external URL); responsive and thumbnail options.
    :Note: See :ref:`Adding an image to a page <how-to-add-image>`.

**Row** and **Column**
    Build responsive layouts of all shapes and sizes thanks to a twelve column system,
    six default responsive tiers

    :Fields: Row: vertical/horizontal alignment and gutter options; the option to
             create several columns at once. Column: column width (1–12) per
             breakpoint, alignment and offset options.
    :Note: Columns only live inside rows. Content plugins are nested inside the
           columns.

**Spacing**
    Add horizontal spaces around the child content

**Table of contents**
    Create a table of contents for all sections starting with the "Heading" plugin.

**Tabs**
    Create a tabbed interface for content that is only shown when the corresponding tab
    is activated.
