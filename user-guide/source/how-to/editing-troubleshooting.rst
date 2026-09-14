.. _how-to-editing-troubleshooting:

When you cannot edit or publish
===============================

Start with the symptom below. The controls you see depend on the current page, language,
version state, installed packages and your permissions. Save any open plugin dialog
before refreshing the page or navigating away.

The toolbar is missing
----------------------

1. Check whether you are logged in to the correct site and account.
2. Add ``?toolbar_on`` to a URL without a query string, or ``&toolbar_on`` if the URL
   already contains ``?``, then reload it.
3. If the login form appears, log in. If the page reloads without a toolbar, your
   account may not have permission to use it on that site.

The Edit or New Draft button is missing
---------------------------------------

- Confirm that you are viewing a django CMS page rather than an external application
  or an administration screen.
- Switch to the intended language. That language may not have page content yet; use
  **"Add translation"** in the language menu if necessary.
- If **"New Draft"** is shown, the page is published and needs a draft before it can be
  edited. If **"Edit"** is shown, a draft already exists.
- If neither action is available, another user may own a locked draft, or your account
  may lack change permission.

The Publish button is missing or disabled
-----------------------------------------

1. Save and close any open plugin dialog.
2. Confirm that the toolbar's version menu says **"Draft"** and that you are in Edit or
   Preview mode.
3. Confirm the language: each translation has its own draft and publication state.
4. Look for a lock or another editor's name in the version information. If version
   locking is enabled, ask that editor to finish or ask an authorised administrator to
   release the lock.
5. If no lock is shown, your account may be allowed to edit but not publish. Ask a site
   administrator to check your permissions and workflow.

A plugin is missing, or Paste is disabled
------------------------------------------

Plugin availability is configured per site, placeholder and parent plugin. Open the add
menu of the intended placeholder rather than another parent. If the plugin still is not
listed, it is not installed or not allowed there.

Paste is disabled when the clipboard is empty, the destination cannot contain children,
or that plugin type is restricted. See :ref:`Copying content between pages
<how-to-copy-content>`.

Published changes are not visible
---------------------------------

1. Use **"Preview"** to confirm the draft contains the change.
2. Check that you published the same page and language you are now viewing.
3. Use **"View published"**, then open the page in a private window to check the visitor
   view.
4. If shared alias content is involved, publish the alias draft as well.
5. Reload the visitor page. If the correct published version appears in the CMS but not
   to visitors, give the page URL and publication time to the site's developers so they
   can check caching and deployment.

A sidebar or dialog is stuck
-----------------------------

Save the form if possible, close the sidebar or dialog, and open it again from the
toolbar. If it remains stuck, reload the main browser window after confirming that no
unsaved form is open. A wider browser window can also help with sidebars and the
structure board.

What to include when asking for help
------------------------------------

Send the administrator the page URL, selected language, action you expected, version
state shown in the toolbar, and the exact message displayed. A screenshot of the full
toolbar and relevant dialog is usually more useful than a tightly cropped error.
