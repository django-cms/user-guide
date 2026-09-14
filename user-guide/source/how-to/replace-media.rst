.. _how-to-replace-media:

Replacing an existing media file
================================

.. note::

    This guide describes the django-filer media library used by the django CMS
    quickstart project. Your site may use a different media system.

Replace a file when every page that refers to it should display or download the new
content. Upload a separate file instead when the old and new versions must remain
available independently.

Before replacing the file
-------------------------

- Keep a local copy of the current file. The media library does not provide version
  history for file contents.
- Check that every existing use should change. Replacement preserves the media record,
  so all plugins and links that refer to it continue to use that record.
- For an image, compare its dimensions, aspect ratio and subject position with the old
  one. Existing crops and layouts may render it differently.

Replace it in the media library
-------------------------------

1. Open the project menu and select **"Administration..."**.
2. In the **Filer** section, open **"Folders"** and find the file.
3. Click its name to open its details.
4. Expand **"Advanced"** and choose the replacement in the **"File"** field.
5. Review the name, alternative text, caption and other metadata. Update them if the
   replacement has a different purpose or subject.
6. Save.

If the File field is absent or read-only, your account cannot replace the file or the
site has disabled that operation. Ask a site administrator rather than deleting the
existing file.

Verify every important use
--------------------------

Open the pages where the file is most important and check both Preview and the
published visitor view. For images, check narrow and wide layouts because existing
thumbnail and cropping settings still apply. For documents, follow the public download
link and confirm its contents.

Generated thumbnails or site caches may take a short time to update. If the old file
continues to appear after reloading the published page, report the file and page URLs to
the site's developers.

.. warning::

    Replacing a file cannot be undone through django CMS version history. Page versions
    retain a reference to the same media record, not a private copy of the old file.

