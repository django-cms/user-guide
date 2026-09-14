.. _publishing:

Publishing content
==================

.. include:: ../versioning-note.include

The page you created is still a draft. Editors can see it, but visitors cannot. In this
lesson you preview it, publish it, and confirm which version is live.

Preview the draft once more. When it is ready, return to edit mode and click the
highlighted **"Publish"** button in the toolbar. If the toolbar shows **"Edit"** instead,
click that first.

.. image:: ./images/08-publish-button.jpg
    :alt: The highlighted Publish button in the django CMS toolbar

After publishing, your site opens either the page or the Manage versions view. From the
version list, use the view button in the newest row to return to the page. The version
menu in the toolbar now shows **"Published"**.

.. image:: ./images/08-version-menu.jpg
    :alt: Version menu showing the Published state

Version states
--------------

Pages and other publishable content can have more than the two states Draft and
Published.

The version you just published is in the **Published** state — it is the one your
visitors see, and it can no longer be changed. To make further changes you create a new
**Draft** from it with **"New Draft"**. When you publish that draft, the version you
published today becomes **Unpublished** and remains in the history. A draft you want to
set aside without publishing can be **Archived**.

All four states, and the actions each of them allows, are listed in the :ref:`version
states reference <ref-version-states>`.

Looking back at what changed
----------------------------

Published and archived versions remain in the version history, so you can compare them
or restore their content. Drafts that you discard or delete cannot be recovered. Open
the version menu in the toolbar and select **"Manage versions..."** to see the retained
history of the page you just published:

.. image:: ./images/08-manage-versions.jpg
    :alt: Manage versions dialog

Working with that history — comparing, reverting and discarding versions — is covered
step by step in :ref:`Managing versions <how-to-versions>`.

Before you finish, open the page in a private browser window and check what visitors
receive. :ref:`Previewing and verifying changes <how-to-preview-verify>` provides a
short checklist for future updates.

That completes the tutorial: you have logged in, found your way around the toolbar and
the page tree, uploaded an image, created a page, filled it with content and published
it. From here, the :ref:`how-to guides <user-how-to>` cover the everyday tasks, and the
:ref:`concepts <user-explanation>` explain why django CMS works the way it does.
