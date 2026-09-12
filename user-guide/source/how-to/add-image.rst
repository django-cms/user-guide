.. _how-to-add-image:

Adding an image to a page
=========================

.. include:: ../frontend-note.include

This guide shows you how to place an image on a page — either as a standalone element
or embedded in a text. Images come from the :ref:`media library <filer>`, so you
can upload them while adding them to the page, or upload and organise them beforehand
(see :ref:`Managing media files <how-to-media-files>`).

Before you start, make sure you are editing a draft of the page: if the page is
published, click **"New Draft"** in the toolbar first.

Add a standalone image
----------------------

1. Open the **structure board** by clicking the button on the far right side of the
   toolbar.
2. Click the **add button** of the placeholder (or container) where the image should
   appear. A dialog with the available plugins opens.
3. Select the **"Picture / Image"** plugin.

   .. todo::

       **Screenshot needed:** ``how-to/images/add-image-dialog.png`` —
       The "Picture / Image" plugin edit dialog of djangocms-frontend, showing the
       image select field and the alignment options. Quickstart project, light colour
       scheme, browser window ~1200 px wide.

   .. Uncomment once the screenshot exists:
   .. .. image:: images/add-image-dialog.png
   ..     :alt: The Picture / Image plugin dialog

4. Choose the image:

   - Click on the magnifier next to the **"Image"** field to pick an image from the
     media library, or
   - drag and drop a file onto the field, or click its upload icon, to upload a new
     image directly. It will be stored in the media library's "Unsorted uploads"
     folder.

5. Optionally adjust size, alignment and link options — see the notes below.
6. Click **"Save"**. The image appears on the page.
7. Click **"Publish"** in the toolbar to make the change visible to visitors.

Add an image inside a text
--------------------------

You can place images directly inside a text plugin so that they flow with the text:

1. Edit the text plugin (double-click the text on the page, or click the pencil icon
   of the plugin in the structure board).
2. Place the cursor where the image should be inserted.
3. Open the **"CMS Plugins"** menu in the text editor's toolbar and select the image
   plugin.

   .. image:: ../tutorial/images/07-text-enabled-plugins.jpg
       :alt: The CMS Plugins menu in the rich text editor

4. Choose the image as described above and save the plugin dialog.
5. Save the text plugin and publish the page.

Set the alternative text
------------------------

The alternative text ("alt text") is read aloud by screen readers and displayed when
the image cannot be shown. It is essential for accessibility and helps search engines
understand your content.

- In the media library, you can set a default alternative text for each file in its
  **"Alt text"** field (see :ref:`Managing media files <how-to-media-files>`).
- In the image plugin's dialog, you can override it for the specific use of the image
  on this page.

.. tip::

    Write alt text that conveys the purpose of the image in its context, for example
    "Our team at the 2025 company retreat" rather than "photo1.jpg".

Control size and alignment
--------------------------

The image plugin offers options to control how the image is rendered. The exact set of
options depends on your site's design:

- **Width / Height** - scale the image to fixed dimensions. If your site uses a
  responsive design, prefer leaving these empty and letting the design determine the
  size.
- **Alignment** - float the image to the left or right of the surrounding content, or
  centre it.
- **Link** - make the image clickable by linking it to a page, an external URL, or the
  full-size version of the image.

.. note::

    Large image files slow down your pages. The image plugin generates appropriately
    sized thumbnails automatically, but it is still good practice not to upload images
    that are far larger than they will ever be displayed.
