.. _explanation-plugins:

Plugins
=======

In django CMS, content is not one big block of formatted text. It is a **tree of
plugins**: typed components — a text, an image, a row of columns, a video — each with
its own editing form, nested inside each other and inside
:ref:`placeholders <explanation-placeholders>`. This page explains why content is
structured this way.

Why structured content beats one big text field
-----------------------------------------------

Many simpler systems give editors a single rich-text area per page and leave the rest
to copy-and-paste. django CMS deliberately splits content into typed components,
because the structure pays off in several ways:

- **The design stays in charge of presentation.** An image plugin knows it is an
  image, so the site's design decides how images are rendered — sized, cropped,
  responsive — consistently across the whole site. In a free-form text field, every
  editor's manual formatting choices accumulate into inconsistency.
- **Content can be rendered anywhere.** Because the structure is machine-readable,
  the same content can be rendered for desktop and mobile, reused in another context
  (see :ref:`aliases <explanation-aliases>`), or restyled wholesale when the site is
  redesigned — without anyone editing the content itself.
- **Complex elements stay editable by everyone.** A carousel or a multi-column layout
  is a form with a few fields, not a chunk of fragile markup. Editors without HTML
  knowledge can build pages that would otherwise require a developer.
- **Each piece is manageable on its own.** Plugins can be moved by drag & drop,
  copied between pages and languages, and edited individually — the rest of the page
  is untouched.

When to use a plugin instead of text formatting
-----------------------------------------------

The text plugin's rich-text editor can do a lot — and for paragraphs, lists and
emphasis it is the right tool. As a rule of thumb, switch to a dedicated plugin when
the element has *meaning or behaviour* beyond formatted text: images, buttons, links
to other pages of the site, videos, structured layouts. You get the design's styling
for free, and the element remains intact if the text around it changes.

Some plugins can even live *inside* a text, through the editor's "CMS Plugins" menu —
combining the flow of text with the robustness of typed components. A link to another
page inserted this way keeps working even when that page's URL changes.

Which plugins do I have?
------------------------

The set of available plugins is specific to each site: it depends on the installed
packages (the quickstart project ships the set described in the :ref:`plugin reference
<ref-plugins>`) and may include custom plugins built for your site's particular needs.
Custom plugins are outside the scope of this guide — but the way you interact with
them (add, edit, nest, drag) is always the same, which is what the
:ref:`tutorial <plugins>` teaches.
