.. _explanation-aliases:

Aliases
=======

.. include:: ../alias-note.include

In django CMS, the Alias plugin is a powerful tool that enables content editors to
display in as many places as they like without duplicating it. Essentially, it creates a
reference or link to content that resides in a separate place - called an "Alias".

Key aspects of the Alias plugin include:

1. **Content Replication:** Rather than copying content, the alias content is referenced
   either in a page template or by using the Alias plugin.
2. **Cross-Page Content Sharing:** It facilitates sharing content across different pages
   within the site. For instance, if there's a section that needs to appear in multiple
   places but should have consistent content, the aliases can be employed to achieve
   this.
3. **Maintaining Consistency:** Using aliases ensures consistency in content across
   various parts of the website. If the original content gets updated, all aliases
   referencing it will reflect those changes instantly.
4. **Saves Effort and Reduces Errors:** Instead of manually replicating content across
   multiple pages (which could lead to discrepancies or errors), the Alias plugin
   streamlines the process and reduces the chance of inconsistencies.
5. **Ease of Management:** Content editors can manage content in one place while
   displaying it in multiple locations, making it easier to maintain and update
   information without having to navigate through numerous pages.

In essence, aliases in django CMS serves as a smart reference system, allowing content
editors to reuse existing content across the site while maintaining consistency and
efficiency in content management.

When to use an alias — and when to copy
---------------------------------------

Use an **alias** when the content must stay identical everywhere it appears, and a
future change should take effect everywhere at once: footers, contact blocks, legal
notices, campaign banners. One edit, published once, updates every page.

**Copy** the content instead when the places are meant to evolve independently: a
page that starts from the same building blocks but will be adapted to its context.
A copy gives each page its own content; an alias would couple pages together that
should not be coupled — an edit intended for one page would silently change all the
others.

A useful test: *"If I change this next month, should every page change?"* If yes, use
an alias (see :ref:`Reusing content with aliases <how-to-aliases>`); if no, copy.
