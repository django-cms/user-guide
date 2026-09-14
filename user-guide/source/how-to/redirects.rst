.. _how-to-redirects:

Redirecting an old page
=======================

A redirect sends visitors from one page to another. Use one when an old address must
continue to work after its content has moved. Redirects are language-specific, so check
and publish each required language separately.

Redirect a page
---------------

1. Open the **project menu** and select **"Pages..."**.
2. Find the page whose current address should redirect visitors.

   .. image:: ../tutorial/images/05-pagetree-form.jpg
       :alt: Page tree with page-management controls

3. If the page is published, open its publication status menu and select **"New
   Draft"**.
4. Open the page settings with the sliders button in its row.
5. Expand **"URL options"** and choose the destination in **"Redirect"**.

   .. image:: ./images/redirect-settings.jpg
       :alt: Redirect field in the URL options of the page settings

6. Save the settings and publish the draft.
7. Open the source address in a private browser window and confirm that it reaches the
   intended destination.

The redirect only works while the source page still exists at the old address. If you
already changed its slug or moved it to a different parent, create a page at the old
location and configure that page to redirect to the new one.

.. warning::

    Do not redirect a page to itself, and do not create a chain that eventually leads
    back to it. A loop such as A → B → A prevents visitors from reaching either page.

Redirect each language
----------------------

Page settings belong to one language at a time. Use the language tabs in the settings
dialog to select the source language, then set and publish its redirect. Repeat for the
other languages that need one; their destinations may differ.

Remove a redirect
-----------------

1. Create a draft of the redirecting page.
2. Open **"Page settings..."**, expand **"URL options"**, and clear **"Redirect"**.
3. Save and publish the draft.
4. Visit the page while logged out and confirm that its own content appears again.

Hiding the source page from navigation is optional. A hidden page still responds at its
URL, so its redirect continues to work.
