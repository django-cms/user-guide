.. _how-to-aliases:

Reusing content with aliases
============================

.. include:: ../alias-note.include

An alias is a piece of content that is maintained in one place and displayed on as
many pages as you like. When you change the alias content, every page showing it is
updated at once. Typical uses are footers, contact blocks, banners and announcements.
For the background, see :ref:`the explanation of aliases <explanation-aliases>`.

Create an alias
---------------

1. Open the project menu in the toolbar (it shows the name of your site) and select
   **"Aliases..."**. The alias overview opens in the sidebar.
2. If you want to group aliases, create a **category** first; otherwise use an
   existing one.
3. Click **"Add Alias"**, give the alias a descriptive name, and save.

   .. todo::

       **Screenshot needed:** ``how-to/images/aliases-changelist.png`` —
       The Aliases overview in the sidebar with at least one category and one alias
       visible, the "Add Alias" button visible. Quickstart project, light colour
       scheme, browser window ~1200 px wide.

   .. Uncomment once the screenshot exists:
   .. .. image:: images/aliases-changelist.png
   ..     :alt: The Aliases overview in the sidebar

4. Open the alias to edit its content. An alias has a placeholder which you fill with
   plugins exactly like a page: open the structure board, add plugins, and arrange
   them (see :ref:`filling in content <plugins>`).
5. Publish the alias using the toolbar, just like a page.

Turn existing content into an alias
-----------------------------------

If content that should be reused already exists on a page:

1. Open the **structure board** on that page (working on a draft).
2. Open the **context menu** of the plugin you want to reuse (the hamburger menu on
   the right of the plugin's entry) and select **"Create Alias"**.
3. Choose a name and category for the new alias and save.

The selected plugin and its nested plugins are copied into the new alias. You can now
replace the original content with the alias plugin so future edits happen in one
place only.

Insert an alias on a page
-------------------------

1. On the target page (working on a draft), open the **structure board** and click the
   **add button** of the placeholder where the alias content should appear.
2. Select the **"Alias"** plugin.
3. Choose the alias in the dialog and save.
4. Publish the page.

The page now displays the alias content at that position.

Edit alias content
------------------

1. Open the project menu and select **"Aliases..."**, then open the alias — or click
   on the alias content on any page that shows it and follow the edit link.
2. Create a new draft if the alias is published, make your changes, and publish.

All pages displaying the alias show the updated content as soon as the alias is
published. You do not need to touch, or republish, the pages themselves.

.. note::

    Aliases are versioned like pages: drafts of an alias are not publicly visible
    until published, and you can revert to earlier versions through its version
    history (see :ref:`Managing versions <how-to-versions>`).
