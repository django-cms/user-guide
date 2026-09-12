.. _publishing:

Publishing content
==================

.. include:: ../versioning-note.include

Once you have finished filling in your newly created page (or blog post), it is saved as
a draft. It will not be published until you decide to do so. As an editor, you can view
drafts, but any site visitors will only see published pages.

To publish a page, click on the highlighted "Publish" button in the toolbar. This button
is visible in the page's edit mode. (If there is a highlighted "Edit" button instead,
click it first to get to edit mode.)

.. image:: ./images/08-publish-button.jpg
    :scale: 50
    :alt: The version menu showing "published" state.

When published you will be taken to the published page or the "manage versions" dialog,
depending on the setup of your site. If you're taken to the manage versions dialog,
click on the eye button of the top listed version to get back to the page you just
published.

You will see in the toolbar that the version menu now shows that the content is
"published".

.. image:: ./images/08-version-menu.jpg
    :scale: 50
    :alt: The version menu showing "published" state.

Version states
--------------

Since django CMS 4, pages and other publishable content can have more than the two
states "draft" and "published".

.. note::

    Versioning is managed by an optional package like django CMS Versioning. Your
    installation might manage versions differently. This guide assumes that django CMS
    Versioning is installed.

The version you just published is in the **"published" state** — it is the one your
visitors see, and it can no longer be changed. To make further changes you create a new
**draft** from it with the "New Draft" button; when you publish that draft, the version
you published today becomes **"unpublished"** and is kept as a record. A draft you want
to set aside without publishing can be **archived**.

All four states, and the actions each of them allows, are listed in the :ref:`version
states reference <ref-version-states>`.

Looking back at what changed
----------------------------

Every version of the page is kept, so you can always find out what a page looked like
at an earlier point, compare two versions, or restore one. Open the version menu in the
toolbar and select **"Manage versions..."** to see the full history of the page you
just published:

.. image:: ./images/08-manage-versions.jpg
    :alt: Manage versions dialog

Working with that history — comparing, reverting and discarding versions — is covered
step by step in :ref:`Managing versions <how-to-versions>`.

That completes the tutorial: you have logged in, found your way around the toolbar and
the page tree, uploaded an image, created a page, filled it with content and published
it. From here, the :ref:`how-to guides <user-how-to>` cover the everyday tasks, and the
:ref:`concepts <user-explanation>` explain why django CMS works the way it does.
