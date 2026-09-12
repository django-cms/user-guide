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

Open the media library
----------------------

1. Open the **project menu** in the toolbar and select **"Administration..."**.
2. In the **Filer** section, click **"Folders"**.

.. image:: ../tutorial/images/04-filer-section.jpg
    :alt: The filer section of the admin sidebar contains the media library

You see the folders of your library. The greyed-out **"Unsorted uploads"** folder
collects every file that was uploaded directly from a plugin dialog and never assigned
to a folder.

Create folders
--------------

Folders work like the ones on your computer, and they are the only thing standing
between you and a library of several hundred unsorted files.

1. Click **"New Folder"** at the top right of the folder list.
2. Give the folder a name and save.

To create a folder inside another one, open the parent folder first and then click
**"New Folder"** there.

.. tip::

    Organise folders the way your team looks for files — by section of the site, by
    campaign or by year — rather than by file type. "Press photos 2025" is easier to
    search than "JPEGs".

Upload files
------------

1. Open the folder the files should go into.
2. Drag the files from your computer onto the browser window, or click the **upload
   button** at the top right and select them. Several files at a time are fine.

The files appear in the folder as soon as the upload finishes.

Describe a file
---------------

Click a file's name to open its details. The fields worth filling in are:

- **Name** — what you and your colleagues will search for.
- **Alt text** — a short description of what an image shows. Screen readers read it
  aloud and browsers display it when the image cannot be loaded, which makes it the
  single most valuable field for the accessibility of your site. It is used as the
  default whenever the image is placed on a page.
- **Caption** — text that some plugins display alongside the image.

Save when you are done.

Find, move and rename files
---------------------------

- **Find** a file with the search field above the file list.
- **Move** files by selecting them with the checkboxes on the left and choosing the move
  action from the menu above the list; then pick the destination folder. You can also
  drag a file onto a folder.
- **Rename** a file by opening its details and changing its name. The file keeps working
  on every page that uses it — pages refer to the file itself, not to its name.

Replacing a file is the fastest way to update an image that appears in many places: the
pages showing it keep their reference, so they all display the new version at once. If
your installation offers no replace action, upload the new file and edit the plugins
that should use it.

Delete files safely
-------------------

.. warning::

    Deleting a file removes it from every page that uses it. An image deleted here
    disappears from the articles and pages it was placed on, and those pages will not
    warn you.

Before deleting a file or a folder, check whether its contents are still in use. If you
are unsure, move the file to an "Archive" folder instead of deleting it: nothing breaks,
and it is out of the way.
