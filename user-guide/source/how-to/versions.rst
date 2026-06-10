.. _how-to-versions:

Managing versions
=================

.. include:: ../versioning-note.include

django CMS keeps track of page revisions, allowing you to revert to previous versions if
needed. Here's a step-by-step guide on how to manage versions:

1. **Accessing the "manage versions" view:**

   Either

   - Select "Pages..." in the page menu of the toolbar and look for the page the
     versions of which you want to manage.
   - Click on the status indicator to open the dropdown menu
   - Select "Manage versions..."

   or

   - Preview or edit the page the versions of which you want to manage.
   - Click on the version menu and chose "Manage versions..."

     .. image:: ../tutorial/images/08-version-menu-open.jpg
         :scale: 50

2. **Inspecting all versions:**

   .. image:: ./images/versions-changelist.jpg
       :alt: Versions of a page content

   - Created and modified dates
   - Title and language
   - Username of the author
   - Status: Draft, Published, Unpublished, and Archived
   - Action buttons

3. **Acting upon versions:** Actions differ by status of the version. They include

   - Edit (pencil): Edit this version (draft) or create a new draft from this version
     (published)
   - Archive: Mark this draft as archived for later usage
   - Revert: Create new draft from this archived or unpublished version
   - Publish: Publish this draft
   - Unpublish: Make this published version unavailable
   - Delete: Delete this draft version
   - View: Preview this version

4. **Comparing two versions:**

   - Select exactly two versions to compare by checking the box on their left side
   - From the pull-down menu marked ``-------`` select "Compare versions"
   - Click "Go"

     .. image:: ../tutorial/images/08-comparing-versions.jpg
         :alt: Comparing two versions

.. note::

    Only draft versions can be deleted. Outdated versions are kept on purpose.

Managing versions in django CMS allows to understand the history of content.
Drafts can be archived for later reuse. All versions currently public or once public are
marked "published" or "unpublished", respectively. The content of versions can be
compared with each other.

.. _how-to-revert:

Revert to a previous version
----------------------------

If a published change turns out to be wrong, you can restore an earlier version:

1. Open the **"manage versions"** view of the page (see above) and make sure you are
   looking at the right language.
2. Find the version you want to restore. If you are unsure, compare it to the current
   version first (see "Comparing two versions" above).
3. Click the **"Revert"** action button of that unpublished or archived version. A new
   draft with the content of that version is created.

   .. note::

       If a draft already exists, django CMS asks you whether to discard it — a page
       can only have one draft per language at a time.

4. Review the new draft and click **"Publish"** in the toolbar to make it live.

Reverting never deletes history: the previously published version is marked
"unpublished" and remains available in the version list.

Discard a draft
---------------

To throw away unpublished changes:

1. Open the page in preview or edit mode.
2. Open the **version menu** in the toolbar and select **"Discard Changes"**, then
   confirm.

Alternatively, delete the draft from the "manage versions" view using its **delete**
action button. In both cases the published version stays untouched and remains live;
only the unpublished draft is removed. Discarding a draft cannot be undone — if you
might need the changes later, **archive** the draft instead.
