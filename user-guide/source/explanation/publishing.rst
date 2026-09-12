.. _explanation-publishing:

Publishing
==========

.. include:: ../versioning-note.include

In django CMS, publishing and versioning are crucial aspects for editors managing
content. Here's a breakdown of how they work:

Publishing
----------

Publishing refers to making content available to website visitors. In django CMS, you
typically create or edit content using a **draft**, which means the unfinished content
or changes are not immediately visible to the public. Editors can work on content
privately until it's ready for publication.

This is the typical workflow:

1. **Create Draft:** Editors create or modify content only in a draft version within the
   CMS admin interface.
2. **Preview:** They can preview how the content will appear on the live site before
   publishing.
3. **Publish:** When ready, editors can publish the changes to make them visible on the
   live website for visitors to see.

Published content cannot be changed any more. To make additional changes, start the
process over and create a new draft based on the published version.

Why published versions cannot be edited
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Making published versions immutable may feel inconvenient at first, but it is a
deliberate design decision:

- **A reliable history.** Every state your site has ever been in is preserved
  exactly. You can always answer "what did this page say last month?" and prove it.
- **Safe rollback.** Because old versions are never altered, reverting to one of them
  restores precisely what was once live — not an approximation.
- **No accidental publishing.** Visitors can never see a half-finished edit, because
  edits only ever happen in drafts that you publish as a deliberate step.

Versions as a history
---------------------

Because every draft and every version that was ever published is kept, your content
carries its own history. You can see what a page looked like at any point in time,
compare two versions to find out exactly what changed between them, and restore an
earlier version if a change turns out to be wrong. Nothing an editor does is
irreversible, which is what makes it safe to work directly on a live site.

The four states a version can be in, and the actions each state allows, are listed in
the :ref:`version states reference <ref-version-states>`. The steps for comparing,
reverting and discarding versions are in :ref:`Managing versions <how-to-versions>`.

Locked versions
---------------

.. note::

    This feature is not enabled in all installations of django CMS. See `django CMS
    Versioning documentation
    <https://djangocms-versioning.readthedocs.io/en/latest/settings.html#DJANGOCMS_VERSIONING_LOCK_VERSIONS>`_
    for more information.

Version locking in django CMS is a feature that automatically locks each draft version
of a content item to prevent unintended modifications or edits. A locked draft can only
be changed by the person who created the draft. This functionality is particularly
useful when you want to ensure that not two editors make changes to a specific content,
ensuring changes do not interfere with each other.
