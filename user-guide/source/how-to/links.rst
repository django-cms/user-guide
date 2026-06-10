.. _how-to-links:

Creating links and buttons
==========================

.. include:: ../frontend-note.include

This guide shows the different ways to create links: inside a text, as a standalone
link or styled button, to other pages of your site, to external websites, to files,
and to email addresses.

Before you start, make sure you are editing a draft of the page: if the page is
published, click **"New Draft"** in the toolbar first.

Link text inside the rich text editor
-------------------------------------

To link a word or phrase to an **external website**:

1. Edit the text plugin (double-click the text on the page, or click the pencil icon
   of the plugin in the structure board).
2. Select the text that should become a link.
3. Click the **link button** in the editor's toolbar and enter the URL, including
   ``https://``.
4. Confirm, save the text plugin, and publish the page.

.. _how-to-internal-links:

Link to another page of your site
---------------------------------

For links to other pages of your own site, do not paste the page's URL as an external
link. Use a **dynamic link** instead — it stays correct even if the destination page's
URL changes later:

1. Edit the text plugin and place the cursor where the link should appear (or select
   the text to be linked).
2. Open the **"CMS Plugins"** menu in the text editor's toolbar and select the
   **"Link / Button"** plugin.

   .. image:: ../tutorial/images/07-text-enabled-plugins.jpg
       :alt: The CMS Plugins menu in the rich text editor

3. In the dialog, enter the link text (if you did not select text before) and choose
   the destination page in the **"Internal link"** field. Start typing to search the
   page tree.
4. Save the plugin dialog, save the text plugin, and publish the page.

.. note::

    Why this matters: if the destination page's slug changes or the page is moved, a
    pasted URL breaks, while a dynamic link is updated automatically. See
    :ref:`Change a page's URL (slug) safely <how-to-change-slug>`.

Add a standalone link or button
-------------------------------

Use the **"Link / Button"** plugin of djangocms-frontend to place a link outside of a
text, for example a call-to-action button:

1. Open the **structure board** and click the **add button** of the placeholder or
   container where the link should appear.
2. Select the **"Link / Button"** plugin.

   .. todo::

       **Screenshot needed:** ``how-to/images/links-button-dialog.png`` —
       The "Link / Button" plugin edit dialog of djangocms-frontend, showing the
       internal/external link fields and the "Link type" / context (colour) options.
       Quickstart project, light colour scheme, browser window ~1200 px wide.

   .. Uncomment once the screenshot exists:
   .. .. image:: images/links-button-dialog.png
   ..     :alt: The Link / Button plugin dialog

3. Enter the **link text** and the destination: an internal page, an external URL, a
   file from the media library, a phone number, or an email address.
4. To render the link as a button, set the **"Link type"** option to "Button" and pick
   a style (context) that fits its purpose, e.g. "Primary" for the main action of the
   page.
5. Click **"Save"** and publish the page.

Link to a file from the media library
-------------------------------------

To let visitors download or open a file (for example a PDF):

1. Upload the file to the media library if it is not there yet (see :ref:`Managing
   media files <how-to-media-files>`).
2. Add a **"Link / Button"** plugin — standalone (see above) or inside a text via the
   **"CMS Plugins"** menu.
3. In the dialog, choose the file in the **"File link"** field.
4. Save and publish the page.

Link to an email address
------------------------

In the **"Link / Button"** plugin dialog, fill in the **"Email address"** field
instead of a page or URL. Clicking the link will open the visitor's email program with
a new message to that address.
