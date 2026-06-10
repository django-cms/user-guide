.. _how-to-pages:

Managing pages
==============

This guide collects the most common page management tasks. Each section is
self-contained: pick the task you want to do and follow its steps. If you are new to
django CMS, work through the :ref:`tutorial <user-tutorial>` first — it introduces the
:ref:`toolbar <toolbar>` and the :ref:`page tree <pagetree>` used throughout this guide.

.. _how-to-create-page:

Create a new page
-----------------

1. Open the page menu in the toolbar and select **"Create page"**. You can choose
   between:

   - **New page** - creates a page at the same level as the page you are currently on
     (a sibling page).
   - **New sub page** - creates a page nested under the page you are currently on
     (a child page).

2. Enter the **title** of the page. The **slug** (the last part of the page's URL) is
   generated automatically from the title; adjust it if needed.
3. Optionally add content to the page directly in the dialog.
4. Click **"Create"**. The new page opens as an unpublished draft in edit mode.
5. Add content to the page (see :ref:`filling in content <plugins>`) and publish it
   with the **"Publish"** button in the toolbar when ready.

.. tip::

    Alternatively, click the **"Create"** button on the right-hand side of the toolbar
    to open the creation wizard, or use the **add button** of a page's row in the
    :ref:`page tree <pagetree>` to create a child page at a specific position.

Duplicate an existing page
--------------------------

1. Navigate to the page you want to duplicate.
2. Open the page menu in the toolbar and select **"Create page"**, then **"Duplicate
   this page"**.
3. Adjust the title and slug of the copy in the dialog and click **"Create"**.
4. The duplicate is created as a draft containing a copy of the original page's
   content. Edit and publish it like any other page.

Copy or move a page in the page tree
------------------------------------

1. Select **"Pages..."** in the page menu of the toolbar to open the page tree.

   .. image:: ../tutorial/images/05-pagetree-form.jpg
       :alt: django CMS page tree

2. To **move** a page, click on the dotted bar on the left of the page's row and drag
   the page to its new position. Drop it onto a page to nest it as a child page, or
   between two pages to make it their sibling.
3. Alternatively, use the **hamburger context menu** at the right end of the page's
   row:

   - Select **"Cut"** (to move) or **"Copy"** (to duplicate the page including its
     sub-pages).
   - Open the hamburger context menu of the destination page and select **"Paste"**.
     The page is inserted as a child of the destination page.

.. note::

    Moving a page changes the URLs of the page and all its sub-pages if the slug
    includes the parent's path. See `Change a page's URL (slug) safely`_ below for how
    to deal with inbound links.

.. _how-to-change-slug:

Change a page's URL (slug) safely
---------------------------------

The slug is the part of the URL that identifies the page. Changing it breaks existing
links to the page — bookmarks, links from other websites and search engine results.
Follow these steps to change it safely:

1. Make sure you are working on a draft: if the page is published, select **"New
   Draft"** in the toolbar first.
2. Open the page menu in the toolbar and select **"Page settings..."**.
3. Change the **"Slug"** field. If the full URL should differ from the slug-based
   default, open the **"URL options"** section and use **"Overwrite URL"**.
4. Click **"Save"**, then publish the change.
5. To preserve visitors and SEO ranking arriving through the old URL, set up a
   redirect from the old URL: see :ref:`Managing redirects <how-to-redirects>`.

.. note::

    Slugs are language-specific. Use the language tabs at the top of the page settings
    dialog to change the slug for each language.

Show or hide a page in the navigation menu
------------------------------------------

1. Navigate to the page.
2. Open the page menu in the toolbar and select **"Hide in navigation"** (or **"Show
   in navigation"** if it is currently hidden).

Alternatively, in the :ref:`page tree <pagetree>`, click the indicator in the
**"Menu"** column of the page's row to toggle its visibility in the navigation menu.

A hidden page remains accessible through its URL — hiding it from the menu does not
unpublish it and does not restrict access.

Set a page as the home page
---------------------------

The home page is the page served at the root URL of your site, marked with a house
icon in the page tree.

1. Select **"Pages..."** in the page menu of the toolbar to open the page tree.
2. Open the **hamburger context menu** at the right end of the row of the page you
   want to make the new home page.
3. Select **"Set as home"**.

.. note::

    The previous home page remains published and becomes reachable under its regular
    slug-based URL.

Delete a page
-------------

.. warning::

    Deleting a page also deletes **all its sub-pages** and all their content versions
    in **all languages**. This cannot be undone. If you only want to take a page
    offline, unpublish it instead (see :ref:`Managing versions <how-to-versions>`) —
    unpublished content can be restored later.

1. Navigate to the page you want to delete.
2. Open the page menu in the toolbar and select **"Delete page..."**.
3. The confirmation dialog lists everything that will be deleted along with the page.
   Review it carefully and confirm.

Alternatively, select **"Delete..."** from the page's hamburger context menu in the
page tree.
