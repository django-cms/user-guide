.. _how-to-copy-content:

Copying content between pages
=============================

The django CMS clipboard copies a plugin, including its nested children, to another
position or page. The pasted copy is independent: changing it later does not change the
original.

Choose copy, alias or page duplication
--------------------------------------

=============================== =======================================================
Goal                            Use
=============================== =======================================================
Reuse a block as a starting     **Copy and paste** the plugin. The two copies can then
point                           be edited independently.
Keep a block identical in       An :ref:`alias <how-to-aliases>`. Publishing the alias
several places                  updates every page that displays it.
Start a new page with all the   :ref:`Duplicate the page <how-to-pages>`.
same content
=============================== =======================================================

Copy one plugin
---------------

1. Open the source page and its **structure board**.
2. Open the settings menu of the plugin you want to copy and select **"Copy"**. The
   plugin and its children replace whatever was previously in your clipboard.
3. Navigate to the destination page, select the correct language and create a draft if
   necessary.
4. Open its structure board. Open the settings menu of the destination placeholder or
   parent plugin and select **"Paste"**.
5. Review the new copy, edit any page-specific text or links, then preview and publish
   the destination page.

The clipboard belongs to your user and remains available when you navigate to another
page. You can inspect it with **"Clipboard..."** in the project menu and empty it with
**"Clear clipboard"**.

Copy all content from a placeholder
-----------------------------------

Open the settings menu in the placeholder's heading and select **"Copy all"**. On the
destination page, open the settings menu of a compatible placeholder and select
**"Paste"**. The copied plugins are added to the destination; review their order before
publishing.

Move rather than copy
---------------------

To move a plugin between pages, work on drafts of both pages and select **"Cut"** on the
source instead of **"Copy"**. Paste it at the destination, preview both pages, and
publish both drafts. Until both are published, visitors may still see the old public
arrangement.

.. warning::

    Cutting removes the plugin from the source draft immediately. If you change your
    mind, paste it back before clearing the clipboard. Discarding the source draft also
    discards any other unpublished changes on that page.

When Paste is unavailable
-------------------------

The destination must accept the copied plugin type. For example, a column may only be
allowed inside a row, and some placeholders only accept a configured set of plugins.
Paste into a compatible parent, or ask the site's administrators about its plugin
restrictions.

