.. _how-to-media-files:

Managing media files
====================

The media library holds the files of your site — images, documents, videos — in folders,
independently of the pages that use them. A file is uploaded once and can then be placed
on as many pages as you like. This guide covers the tasks you do in the library itself;
for putting an image on a page see :ref:`Adding an image to a page <how-to-add-image>`.

.. note::

    The media library is provided by the django-filer package, which is part of
    installations such as the django CMS quickstart project. If your site manages files
    differently, ask your developers.

On this page
------------

- :ref:`Open the media library <how-to-open-media-library>`
- :ref:`Create folders <how-to-media-folders>`
- :ref:`Upload files <how-to-upload-media>`
- :ref:`Describe a file <how-to-describe-media>`
- :ref:`Find, move or rename files <how-to-organise-media>`
- :ref:`Delete files safely <how-to-delete-media>`

.. _how-to-open-media-library:

Open the media library
----------------------

1. Open the **project menu** in the toolbar and select **"Administration..."**.
2. In the **Filer** section, click **"Folders"**.

.. image:: ../tutorial/images/04-filer-section.jpg
    :alt: The filer section of the admin sidebar contains the media library

You see the folders of your library. The greyed-out **"Unsorted uploads"** folder
collects every file that was uploaded directly from a plugin dialog and never assigned
to a folder.

.. _how-to-media-folders:

Create folders
--------------

Folders work like the ones on your computer. A simple, shared naming scheme keeps a
large library usable for everyone.

1. Click **"New Folder"** at the top right of the folder list.
2. Give the folder a name and save.

To create a folder inside another one, open the parent folder first and then click
**"New Folder"** there.

.. tip::

    Organise folders the way your team looks for files — by section of the site, by
    campaign or by year — rather than by file type. "Press photos 2025" is easier to
    search than "JPEG images".

.. _how-to-upload-media:

Upload files
------------

1. Open the folder the files should go into.
2. Drag the files from your computer onto the browser window, or click the **upload
   button** at the top right and select them. Several files at a time are fine.

The files appear in the folder as soon as the upload finishes.

.. _how-to-describe-media:

Describe a file
---------------

Click a file's name to open its details. The fields worth filling in are:

- **Name** — what you and your colleagues will search for.
- **Alt text** — the default text alternative used when the image is placed on a page.
  Describe the image's purpose rather than its filename. See :ref:`Set the alternative
  text <how-to-add-image>` for context-specific guidance.
- **Caption** — text that some plugins display alongside the image.

Save when you are done.

.. _how-to-organise-media:

Find, move and rename files
---------------------------

- **Find** a file with the search field above the file list.
- **Move** files by selecting them with the checkboxes on the left and choosing the move
  action from the menu above the list; then pick the destination folder. You can also
  drag a file onto a folder.
- **Rename** a file by opening its details and changing its name. The file keeps working
  on every page that uses it — pages refer to the file itself, not to its name.

To update every reference while keeping the same media record, follow :ref:`Replacing
an existing media file <how-to-replace-media>`. Upload a separate file instead when
some pages must continue to use the old content.

.. _how-to-delete-media:

Delete files safely
-------------------

.. warning::

    Deleting a file affects every page that refers to it. Images disappear and file
    links stop working; the affected pages do not warn you.

Before deleting a file or a folder, check whether its contents are still in use. If you
are unsure, move the file to an "Archive" folder instead of deleting it: nothing breaks,
and it is out of the way.
