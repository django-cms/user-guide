.. _how-to-translations:

Translating a page
==================

On a multilingual site, every page can have one content version per language. Each
language is edited, versioned and published independently: publishing the German
translation does not affect the English one. This guide shows how to add and manage
translations.

.. note::

    The available languages are configured by your site's developers. If a language
    you need is missing from the language menu, contact them.

Check which languages a page has
--------------------------------

- The **language menu** in the toolbar shows all languages of the site and lets you
  switch between the translations of the current page.
- In the :ref:`page tree <pagetree>`, the language selector above the tree switches
  the displayed language; a page whose title reads "Empty title" has no version in the
  selected language yet. The coloured status indicators show the publication state per
  language.

Add a translation of a page
---------------------------

1. Navigate to the page you want to translate.
2. Open the **language menu** in the toolbar and select the target language under
   **"Add translation"**.
3. The page settings dialog opens for the new language. Enter the translated **title**
   and check the generated **slug**.
4. Click **"Create"**. An empty draft of the page in the new language opens in edit
   mode.
5. Add the translated content, then **publish** — only this language version is
   published.

Copy content from another language
----------------------------------

Instead of building the translated page from scratch, you can start from the plugins
of an existing translation:

1. Switch to the new translation (which should still be empty) using the language
   menu.
2. Open the **language menu** and select the source language under **"Copy all
   plugins"**.
3. Confirm. All plugins of the source language are copied into the current language.
4. Edit each plugin and replace the texts with their translations, then publish.

.. warning::

    Copying plugins overwrites nothing as long as the target translation is empty, but
    the copies are independent: later changes to the source language are **not**
    synchronised to the translation.

Edit page settings per language
-------------------------------

Title, slug, menu title and the other :ref:`page settings <page-settings>` exist once
per language. To edit them:

1. Open the page menu in the toolbar and select **"Page settings..."**.
2. Use the **language tabs** at the top of the dialog to switch between the
   languages.

   .. image:: ../tutorial/images/02-page-settings.jpg
       :alt: The page settings dialogue with language tabs

3. Save your changes.

Publish and unpublish per language
----------------------------------

Each translation has its own versions and its own publication state. Use the toolbar's
**"Publish"** button while viewing a given language to publish that language, and the
:ref:`version manager <how-to-versions>` to unpublish or revert a single language
version. Visitors only see languages that are published.
