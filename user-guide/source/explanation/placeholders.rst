.. _explanation-placeholders:

Placeholders
============

Placeholders are the regions of a page where you, as an editor, can put content. They
are defined in the page's **template** by the site's designers, and they appear in the
structure board when you edit a page. This page explains why django CMS divides pages
this way, and why that division is a feature rather than a limitation.

Separating design from content
------------------------------

A django CMS page is the product of two independent things:

- a **template**, written by designers and developers, that determines the look of the
  page: the header, the navigation, the fonts and colours, and *where* content can
  appear;
- the **content** — the tree of plugins you create — that fills the template's
  placeholders.

The template defines one placeholder for each region that should be editable: perhaps
one for the main content area, one for a sidebar, one for a banner. Everything outside
the placeholders is fixed by the template.

Why you cannot put content "anywhere"
-------------------------------------

It might seem restrictive that content can only go into predefined regions. This
restriction is deliberate, and it is what keeps a large site consistent:

- **Consistency without effort.** Every page using the same template automatically
  has the same layout. Editors cannot accidentally break the design, place text over
  the navigation, or produce a page that looks out of place.
- **Freedom within the regions.** Inside a placeholder you are free: any available
  plugin, in any order, nested as deeply as the plugins allow.
- **Redesigns without content migration.** Because content lives in placeholders
  rather than in fixed page markup, the site's design can be replaced by switching
  templates — the content stays where it is and is rendered in the new design. The
  same content can even be rendered differently per device.

How templates, placeholders and plugins relate
----------------------------------------------

Think of it as a hierarchy::

    Template            (the design — fixed)
    └── Placeholder     (an editable region — defined by the template)
        └── Plugins     (your content — text, images, layout elements, ...)
            └── ...     (plugins can contain other plugins)

A page can offer different templates to choose from (via the page menu's "Templates"
entry); each may provide different placeholders. Which plugins a placeholder accepts
can also be configured — for example, a narrow sidebar placeholder might not accept
wide layout plugins.

If you need an additional editable region on a page, that is a change to the template,
and a conversation to have with your site's developers.
