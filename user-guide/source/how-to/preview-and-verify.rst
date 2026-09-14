.. _how-to-preview-verify:

Previewing and verifying changes
================================

Preview a draft before publishing it, then check the published page as a visitor. This
separates two useful questions: "Is this draft ready?" and "Is the right version now
live?"

Preview the draft
-----------------

1. Make sure the toolbar shows the intended page and language.
2. Save any plugin dialog that is still open. Closing a dialog without saving discards
   the changes made in that dialog.
3. Click **"Preview"** on the right-hand side of the toolbar.

   .. image:: ../tutorial/images/02-toolbar.jpg
       :alt: django CMS toolbar with its context-dependent action buttons

Preview mode hides the editing controls on the page and renders the current draft
without making it public. To make another change, click **"Edit"**.

.. note::

    Preview shows the draft to a logged-in editor. Permissions, caching and other
    site-specific behaviour can still make a visitor's view differ.

Check the page before publishing
--------------------------------

In Preview mode, check at least the following:

- headings, text, images and spacing are in the intended order;
- links and buttons open the correct destinations;
- images have suitable alternative text and are not unexpectedly cropped;
- the page is the correct language and its title and URL are correct; and
- the layout remains usable in a narrower browser window.

If the page contains shared alias content, remember that the alias has its own draft and
publication state. Previewing a page does not publish a draft of an alias.

Publish and verify the live page
--------------------------------

1. Return to **"Edit"** mode if necessary and click **"Publish"**.
2. Click **"View published"** in the toolbar. This opens the version visitors should
   receive rather than your next draft.
3. Open the page in a private browser window, or log out and open it again. Check the
   page, language, URL, navigation entry, links and media once more.

If the logged-out result does not match **"View published"**, first check that you
published the correct language. If it still differs, see :ref:`When you cannot edit or
publish <how-to-editing-troubleshooting>`.
