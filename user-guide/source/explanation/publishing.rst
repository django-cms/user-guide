.. _explanation-publishing:

Publishing
==========

.. include:: ../versioning-note.include

In django CMS, nothing you write goes live by accident. Content exists as a series of
**versions**, and exactly one of them — the published version — is the one visitors see.
This page explains what that division buys you.

Drafts and published versions
-----------------------------

You never edit a live page. You edit a **draft**: your own working copy, visible to you
and your colleagues in the CMS and to nobody else. You can take as long over it as you
need, preview it exactly as visitors will see it, and leave it half-finished overnight
without anyone noticing.

**Publishing** is the deliberate step that puts your draft in place of what was live
before. The draft becomes the published version, and the version it replaces is kept as
a record. To change the page again, you start a new draft from the published version —
which is why the toolbar offers you "New Draft" rather than letting you type straight
into a live page.

Why published versions cannot be edited
---------------------------------------

Making published versions immutable may feel inconvenient at first, but it is a
deliberate design decision:

- **A reliable history.** Retained published and archived versions show what the page
  said at earlier points in time.
- **Safe rollback.** Because retained versions are not altered, reverting to one of
  them restores precisely what it contained — not an approximation.
- **No accidental publishing.** Visitors can never see a half-finished edit, because
  edits only ever happen in drafts that you publish as a deliberate step.

Versions as a history
---------------------

Published versions and drafts you choose to archive build a history of your content.
You can compare retained versions to see what changed and restore an earlier version if
a published change turns out to be wrong. Discarding or deleting a draft is different:
it cannot be undone. Deleting a page or media file can also be irreversible.

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

Where several people edit the same site, two of them can start work on the same page
without noticing — and whoever saves last silently overwrites the other's work. Version
locking prevents that: a draft belongs to the editor who created it, and only that
editor can change it until the draft is published or the lock is released. Editing
becomes a queue rather than a race.
