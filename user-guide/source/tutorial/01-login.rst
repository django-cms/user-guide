.. _editing:

Logging in
==========

Everything you do in django CMS — writing content, arranging it, publishing it — happens
on your site itself, in your browser, on the page you are looking at. The only thing you
need to get started is a login.

.. note::

    This tutorial assumes you have a django CMS site to work on. If you do not have one
    yet, your developers can set one up for you, or you can create one yourself by
    following the `django CMS installation tutorial
    <https://docs.django-cms.org/en/latest/introduction/01-install.html>`_.

Open the login form
-------------------

Your site may have a login page of its own — if your developers have told you where to
log in, use that. Otherwise add ``?toolbar_on`` to the end of your site's address, for
example ``https://www.example.com/?toolbar_on``. A login form appears at the top of the
page:

.. image:: ./images/01-toolbar-on.jpg
    :alt: django CMS toolbar login

Enter your username and password and log in. If you do not have credentials yet, ask the
developers of your site — they set up the first accounts.

The toolbar appears
-------------------

Once you are logged in, a bar appears at the top of your site: the **django CMS
toolbar**. It follows you to every page of your site, and it is how you will do
everything else in this tutorial — create pages, add content, publish.

Two things are worth knowing before you go on:

- The toolbar is yours alone. Visitors of your site never see it, and the page below it
  looks exactly as it looks to them.
- Nothing you do from here on becomes public by accident. Your changes are kept as
  drafts until you deliberately publish them, and every published version is kept, so
  you can always go back.

In the next lesson you take a tour of the toolbar.
