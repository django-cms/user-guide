.. _ref-version-states:

Version states reference
========================

.. include:: ../versioning-note.include

Every editable content item — a page content in a given language, an alias, a blog
post — has a series of numbered versions. Each version is in exactly one of four
states.

.. figure:: ../tutorial/images/08-version-states.png
    :alt: Version states and the editing process

    The possible states and the actions which change the state of a version.

The four states
---------------

================ =======================================================================
State            Meaning
================ =======================================================================
**Draft**        The version an editor can change. At most one draft exists per content
                 item and language at any time. Drafts are only visible to editors.
**Published**    The version visitors currently see. At most one published version
                 exists per content item and language. Published versions cannot be
                 edited.
**Unpublished**  A version that was published at some point and is not any more —
                 either unpublished manually or replaced by publishing another
                 version. Kept as a permanent record.
**Archived**     A draft that was set aside for later use. Not visible to visitors and
                 not editable until reverted into a new draft.
================ =======================================================================

Actions per state
-----------------

The actions available in the :ref:`manage versions view <how-to-versions>` and the
toolbar depend on the state of the version:

==================== ======= =========== ============= ==========
Action               Draft   Published   Unpublished   Archived
==================== ======= =========== ============= ==========
Edit                 ✓       —           —             —
Publish              ✓       —           —             —
Archive              ✓       —           —             —
Discard / Delete     ✓       —           —             —
Unpublish            —       ✓           —             —
Revert (new draft)   —       —           ✓             ✓
Compare              ✓       ✓           ✓             ✓
View / Preview       ✓       ✓           ✓             ✓
==================== ======= =========== ============= ==========

Notes:

- Only drafts can be deleted. Published and unpublished versions are kept on purpose
  as a permanent history.
- Publishing a draft automatically moves the previously published version to
  "unpublished".
- "Edit" on a published version in the version manager creates a new draft based on
  it (same as the "New Draft" toolbar button).
- Reverting an unpublished or archived version creates a **new** draft with that
  version's content; the old version itself is preserved. If a draft already exists,
  you are asked whether to discard it first.

Version locking
---------------

If version locking is enabled on your site, a draft can only be edited by the user who
created it until the lock is removed or the draft is published. See the
:ref:`publishing explanation <user-explanation>` and the `djangocms-versioning
documentation
<https://djangocms-versioning.readthedocs.io/en/latest/settings.html#DJANGOCMS_VERSIONING_LOCK_VERSIONS>`_.
