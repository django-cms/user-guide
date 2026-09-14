.. _how-to-rearrange-content:

Rearranging content on a page
=============================

Use the structure board to change the order and nesting of plugins without recreating
their content. These changes affect the draft you are editing and remain private until
you publish it.

Prepare the page
----------------

1. Open the page in the correct language.
2. If it is published, click **"New Draft"**. Otherwise, click **"Edit"**.
3. Open the **structure board** with the toggle at the far right of the toolbar.

   .. image:: ../tutorial/images/07-nested-plugins.jpg
       :alt: Structure board showing plugins nested inside a page placeholder

Find the plugin you want to move. Each entry shows its type and a short description. On
a computer with a keyboard, hold **Shift** while pointing at an entry to highlight its
content on the page.

Move a plugin
-------------

1. Take hold of the dotted drag handle on the left of the plugin's entry.
2. Drag it until the insertion marker appears at the intended position.
3. Release it and check that it appears at the expected level in the tree.

You can move a plugin to another position in the same container or placeholder. You can
also drag it into a plugin that accepts child plugins, such as a container or column.
To move it back out, drag it to a position aligned with the intended parent level.

.. note::

    The template and plugin configuration control which plugin types are allowed at
    each position. If django CMS refuses a drop, choose a compatible placeholder or
    parent plugin. Site administrators or developers can change these restrictions.

Move content to another page
----------------------------

Dragging only rearranges the current structure board. To move a plugin to another page,
use **"Cut"** and **"Paste"** as described in :ref:`Copying content between pages
<how-to-copy-content>`. Both source and destination pages need drafts, and both must be
published for the complete move to become public.

Check or undo the move
----------------------

Open **"Preview"** and check the page at both wide and narrow browser widths. If the
plugin is in the wrong place, return to **"Edit"** and drag it back.

Some sites provide **Undo** and **Redo** buttons in the toolbar while you edit. **Undo**
reverses the most recent supported content action, such as moving a plugin; **Redo**
applies an action again after you undo it. The buttons are disabled when there is no
corresponding action in the current editing history.

Undo and Redo are optional and separate from page versions. If the buttons are not
present—or the change is no longer in their editing history—move the plugin back
manually or use a retained page version.

As a last resort, you can discard the draft and start again from the published version,
but that also removes every other unpublished change in the draft. See :ref:`Managing
versions <how-to-versions>` before discarding work.
