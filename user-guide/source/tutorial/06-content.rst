.. _content:

Creating a page
===============

Content needs somewhere to live. Usually that is a page, though your site may hold other
kinds of content too — blog posts, or :ref:`aliases <explanation-aliases>`, chunks of
content that are reused in several places. In this lesson you create a page.

Create your page
----------------

1. Click the **"Create"** button on the right-hand side of the toolbar. The creation
   wizard opens and asks what you would like to create.

   .. image:: ./images/06-wizard-1.jpg
       :alt: Step 1 of the wizard dialog: choosing what to create

2. Choose **"New page"** — it creates a page next to the page you are currently on — and
   click **"Next"**.
3. Give your page a **title**. Leave the **slug** empty: django CMS derives it from the
   title, and it becomes the last part of the page's address. Leave the content field
   empty as well; you will fill the page in the next lesson.

   .. image:: ./images/06-wizard-2.jpg
       :alt: Step 2 of the wizard dialog: title, slug and content

4. Click **"Create"**.

Your new page opens in edit mode, and the version menu in the toolbar shows it as a
draft. The page is empty — and it is yours alone until you publish it in :ref:`lesson 8
<publishing>`.

Notice what you did *not* have to decide: colours, fonts, spacing, where the navigation
goes. All of that comes from the page's **template**, built by your site's designers and
shared with every other page. You supply the content; the design takes care of
presenting it consistently.

.. tip::

    There are other ways to create a page. The page menu's **"Create page"** entry opens
    a fuller dialog that contains all page settings at once, and the add button of a row
    in the page tree creates a child page exactly where you want it.

    .. image:: ./images/06-create-page.jpg
        :alt: Create page dialog with page settings

    All routes are described in :ref:`Create a new page <how-to-create-page>`.

.. _page-settings:

Change page settings
--------------------

Every page has a set of settings — its title, the slug that forms its URL, how it
appears in the navigation, and more. They are the same fields you saw in the page
dialog. To review them, select **"Page settings..."** in the page menu, or click the
settings icon of the page's row in the page tree.

The two fields you will always fill in are:

- **Title** — the title of the page. It is displayed by your site's template, used in
  the browser tab and by search engines, and reused in the navigation menu unless you
  set a separate menu title.
- **Slug** — the part of the URL that identifies the page. It is generated
  automatically from the title; keep it short and meaningful.

.. tip::

    Use a title that tells readers what the page contains. Keep the slug short,
    recognisable and appropriate for the page's language.

Close the dialog again — we will fill the page with content in the next lesson. All
other fields, including the URL options and the advanced settings, are described in the
:ref:`page settings reference <ref-page-settings>`.
