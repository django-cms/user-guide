.. raw:: html

    <style>
        .row {
           clear: both;
        }

        .column img {border: 1px solid gray;}

        @media only screen and (min-width: 1000px),
               only screen and (min-width: 500px) and (max-width: 768px){

            .column {
                padding-left: 5px;
                padding-right: 5px;
                float: left;
            }

            .column3  {
                width: calc(33.3% - 10px);
            }

            .column2  {
                width: calc(50% - 11px);
                position: relative;
            }
            .column2:before {
                padding-top: 61.8%;
                content: "";
                display: block;
                float: left;
            }
            .top-left {
                border-right: 1px solid var(--color-background-border);
                border-bottom: 1px solid var(--color-background-border);
            }
            .top-right {
                border-bottom: 1px solid var(--color-background-border);
            }
            .bottom-left {
                border-right: 1px solid var(--color-background-border);
            }
        }
    </style>

.. _user-manual:

Using django CMS
================

django CMS lets you edit your website on the website itself. You log in, and your pages
gain a toolbar: double-click a heading to rewrite it, drag a section into a new place,
drop in an image where you need one — on the page, in context, seeing what your visitors
will see.

Nothing goes public by accident. Your changes stay drafts until you publish them, and
every version that was ever live is kept — so you can always look back, compare, and
restore.

This guide is for the people who fill a django CMS site with content: editors, authors
and site administrators. It assumes no knowledge of Django, HTML or programming.

Start here
----------

.. rst-class:: clearfix row

.. rst-class:: column column2 top-left

:ref:`Tutorial <user-tutorial>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**New to django CMS? Start here.** From your first login to a published page, in about
half an hour.

.. rst-class:: column column2 top-right

:ref:`How-to guides <user-how-to>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Recipes for everyday tasks**: add an image, reuse a footer on every page, translate a
page, undo a change that went wrong.

.. rst-class:: column column2 bottom-left

:ref:`Concepts <user-explanation>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Why django CMS works the way it does.** Placeholders, plugins, drafts and versions,
reusable content.

.. rst-class:: column column2 bottom-right

:ref:`Reference <user-reference>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Look things up**: the toolbar menus, the page tree, the page settings, the version
states, and the plugins installed on your site.

.. rst-class:: clearfix row

What you can do
---------------

- :ref:`Build and organise your site's pages <how-to-pages>` — create them, nest them,
  rename their URLs, decide what appears in the navigation.
- :ref:`Put images on a page <how-to-add-image>`, on their own or inside a text, from a
  media library shared by the whole site.
- :ref:`Add links and buttons <how-to-links>` that keep working even when the page they
  point at moves.
- :ref:`Maintain a footer, a banner or a contact block in one place <how-to-aliases>`
  and show it on as many pages as you like.
- :ref:`Publish a page in several languages <how-to-translations>`, each one edited and
  published independently.
- :ref:`Compare, restore or discard versions <how-to-versions>` — every state your site
  has been in is kept.
- :ref:`Organise the files of your site <how-to-media-files>` in the media library.
- :ref:`Redirect an old address <how-to-redirects>` so visitors and search engines still
  find the content.

About this guide
----------------

django CMS sites are highly customisable and vary a great deal. The examples here follow
the `quickstart project from GitHub
<https://github.com/django-cms/django-cms-quickstart>`_, which provides a typical set of
features — all of them optional for your own site. Where a section only applies to a
particular package, it says so at the top.

The origin of this document is a guide provided by `Kapt.mobi
<https://support.kapt.mobi/index.php/docs/kapt-doc/>`_. It has been translated from the
native French and extended.

.. note::

    This guide is a priority for the django CMS project, and it is never finished. If
    you would like to contribute — a correction, a missing how-to, a screenshot — we
    would love to hear from you: join us on `our friendly Discord channel
    <https://discord-docs-channel.django-cms.org/>`_.

.. only:: not odtsource

    .. admonition:: Take the whole guide with you
        :class: tip

        This guide is also available as one document you can read offline,
        print, improve, or hand to a new colleague: `download the user guide (ODT)
        <django-cms-user-guide.odt>`_. It opens in LibreOffice, Word, Pages and Google
        Docs. The file is rebuilt with the rest of the guide, so it is never out of date.

.. toctree::
    :maxdepth: 1
    :hidden:

    tutorial/index
    how-to/index
    explanation/index
    reference/index
