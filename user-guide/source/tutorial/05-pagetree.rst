.. _pagetree:

The page tree structure
=======================

The tree structure of your site allows you to access all your pages. Many features and
information are present in this part of your site. To better understand them, we suggest
you look at how to access your tree structure, and understand the principles that are
linked to it and its features.

See the page tree
-----------------

To access the tree structure of your site, go to the project menu (which has the name of
your site, or "example.com" on the screenshots here), and choose "Pages...". The side
bar opens and shows the complete tree structure of your site. That is to say, all the
pages that make up your site: visible and non-visible, pages and sub-pages, published or
not.

Alternatively, you can reach the page tree by clicking "Page contents" in the admin
sidebar, which you find in the "django CMS" section.

Principles of the parent, child and sibling pages
-------------------------------------------------

This section is intended to give you a better understanding of what is meant by page
inheritance and the names given to it.

The page tree structure is divided into different sections: these are the pages at
different levels. Each page can be nested in another one, i.e. a page can contain
several sub-pages. This page is then called the "parent page" and its sub-pages are its
"child pages". A child page can also have its own child pages. The idea is to organise
your site in several different levels so that it is clearer for the user.

To better understand, let us take the image of a tree as a metaphor:

- Your **home page** is the trunk, it presents all the thematic pages of your site.
- The **top-level pages** are the branches of your tree and have other small branches.
  We call these top-level pages "parent pages".
- The small branches correspond to the **child pages** of your top-level pages (the
  "parents"). Each parent page may or may not have child pages, just as the branch of a
  tree may or may not have smaller branches.
- The leaves of your tree represent the content of your pages or the sub-pages of your
  child pages, which do not have any child pages of their own.

.. figure:: images/05-pagetree.jpg
    :alt: The page tree structure of django CMS

    The page tree structure: Related pages, child and sibling pages. A small branch is
    composed of pages 3, 4 and 5. The leaves are in this example are pages 2, 4 and 5.

Each page is thus nested in the others when they have a common point: all your blog
posts correspond to the parent page "Blog" for example. All your pages having the same
the same central goal can be grouped together in a group and form the set of child pages
of a parent page bearing the name of this topic. Thus, your parent page allows access to
the content of your daughter pages and helps the user to better find his way around your
site in relation to what he is looking for and wants to do.

As for a sibling page, it is simply a page at the same level as those around it in the
tree. In a group of child pages, all pages are siblings. The same applies to parent
pages.

Managing the page tree
----------------------

The page tree is more than a list of your pages: each row tells you the state of a page
and gives you the actions you can perform on it.

.. image:: ./images/05-pagetree-form.jpg
    :alt: The django CMS page tree form

Take a moment to look at the row of one of your pages. Next to its **title** you see

- the **status indicator**, whose colour tells you whether the page is published in the
  selected language, has unpublished changes, or does not exist in that language yet,
- the **"Menu"** column, which tells you whether the page is part of your site's
  navigation,
- and, at the right end of the row, the buttons to open the page's **settings**, to add
  a **child page**, and a context menu with further actions.

Above the tree, the language menu decides which language version of the tree you are
looking at; the dotted bar on the left of each row lets you **move pages by drag &
drop**.

.. tip::

    Every symbol used in the tree is listed in the legend, which you open with the
    information icon at the bottom right:

    .. image:: ./images/05-pagetree-legend.jpg
        :scale: 50
        :alt: Legend for the page tree

You do not need to memorise the tree's controls now — they are all described in the
:ref:`page tree reference <ref-page-tree>`, and the everyday tasks (moving a page,
hiding it from the navigation, setting the home page, deleting it) are covered in
:ref:`Managing pages <how-to-pages>`.
