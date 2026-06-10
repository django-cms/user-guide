.. _plugins:

Filling in content
==================

Now that you have created a place where your content can live, you can start filling in
actual content. Like the page tree, content is structured in so called "plugins" which
live in plugin trees inside placeholders.

Structure board
---------------

Your page will have one or more placeholders to fill with content. They are displayed in
the **structure board**.

To add plugins to your page (or alias, or blog), you need go to open the structure board
by clicking the button on the far right side of the menu bar.

.. image:: ./images/07-structure-toggle.jpg
    :alt: Toggle button for the structure board
    :scale: 50

There are different types of plugins for adding content, each with a specific purpose.
The ones you will mainly need are the "classic" rich text, image, video, link and button
plugins.

.. note::

    Which plugins are available on your site strongly depends on the installation. Take
    this guide as a blueprint on how to interact with plugins. Even if you have
    different plugin options installed the editing process is always the same.

Once you have clicked on the structure board button, the structure board will open on
the right side of your browser window. It will show one or more placeholders.

.. image:: ./images/07-structure-board.jpg
    :alt: django CMS structure board
    :scale: 50

Adding plugins
--------------

To add content to a page, click on the button . A dialog box will open, showing you the
list of content you can add. Make your choice, a new dialog box opens.

.. image:: ./images/07-add-plugin.jpg
    :scale: 50
    :alt: Select a plugin to add

Fill in the fields (in the container example below you do not have to fill any fields -
all are optional), and save. The new content is displayed on your page.

.. image:: ./images/07-add-container.jpg
    :scale: 50
    :alt: Add container dialog box

.. note::

    The exact content of the add or edit plugin depends on the plugin itself. The
    container plugin in the example is one of many plugins provided by the django CMS
    Frontend package which are designed to structure your page.

    Those plugins do have a set of tabs (coloured in blue) at the top of the dialog and
    offer a wide set of design options, most of which are optional.

Repeat the operation as many times as you want and for as much content as you want.

If you want to move content to arrange their layout, for example to move an image before
or after text, use the "drag & drop" function of the CMS via the notch on the left of
the content type.

You can also add content to change your layout; some of this content is nestable (you
can put text in columns, which are themselves inserted in a section).

If this element allows the addition of nestable content, the add plugin button will be
available at the same level as the module title. The triangle icon will appear next to
the dotted line of the drag and drop button to show or hide the nested content:

.. image:: ./images/07-nested-plugins.jpg
    :scale: 50
    :alt: Nested plugins in a placeholder

.. tip::

    If you **hover** over the structure menu items while pressing the **SHIFT** key, the
    content displayed on the CMS page will be highlighted, so you can see what each
    plugin corresponds to.

Editing plugins
---------------

You can change existing plugins by either

- **double clicking** on the content in the page (when in edit mode)
- **clicking the pencil icon** of the plugin in the structure board.

Editing works exactly like creating a plugin

Integrating content
-------------------

When you add content to your page, you may want to integrate text, a video, clickable
buttons or links into your text.

Text
~~~~

django CMS includes a rich text editor. Its interface is particularly simple, since it
only consists of the text you want to enter:

.. image:: ./images/07-ckeditor.jpg
    :alt: django CMS' integrated rich text editor

.. tip::

    If your installation has inline editing enabled, you can even edit text right on the
    web page if the pencil button in the toolbar is activated:

    .. image:: ./images/07-inline-editing.jpg
        :alt: django CMS text inline editing

.. tip::

    All plugins show a few words of summary in the plugin tree. Those plugin trees can
    get huge, though. To keep an overview, use a feature of the Container plugin:

    The title field is a text field to briefly describe the container content. It will
    be displayed in the plugin tree. It is a good practice to use separate containers
    for different sections of your page and fill the title for quick navigation in the
    plugin tree.

Some plugins can even be added directly to a text plugin using the "CMS Plugins" menu
within the text editor. This is useful for adding dynamic links to your text. Dynamic
links are links to other pages of your site which - should the destination change its
URL - will be automatically kept up-to-date.

.. image:: ./images/07-text-enabled-plugins.jpg
    :alt: The CMS Plugins menu in the rich text editor

.. tip::

    To remove "CMS Plugins" menu within the text editor, click on the editor and hit
    the backspace or delete key to remove it.

    If for some reason the content of the plugin is empty, try positioning the cursor behind it empty object and use backspace.

Images
~~~~~~

Let's place the image you uploaded to the media library in :ref:`lesson 4 <filer>` on
your page:

1. Open the **structure board** and click the **add button** of your placeholder (or
   of the container you created earlier).
2. Select the **"Picture / Image"** plugin from the list.
3. Click the magnifier next to the **"Image"** field, navigate to your "Tutorial"
   folder and pick your image.
4. Save the dialog. Your image appears on the page.

.. todo::

    **Screenshot needed:** ``tutorial/images/07-add-image.png`` —
    The "Picture / Image" plugin dialog with an image selected from the media
    library's "Tutorial" folder. Quickstart project, light colour scheme, browser
    window ~1200 px wide.

.. Uncomment once the screenshot exists:
.. .. image:: ./images/07-add-image.png
..     :alt: Adding an image with the Picture / Image plugin

Links
~~~~~

Now make a piece of your text link to another page of your site:

1. Edit your text plugin and place the cursor where the link should appear.
2. Open the **"CMS Plugins"** menu in the editor's toolbar and select the
   **"Link / Button"** plugin.
3. Enter the link text, choose a page of your site in the **"Internal link"** field,
   and save.
4. Save the text plugin. The link is now part of your text — and because it is a
   dynamic link, it keeps working even if the destination page's URL changes later.

Where to go from here
---------------------

You now know the editing workflow: open the structure board, add plugins, arrange and
edit them. The how-to guides cover the everyday tasks in more depth — for example
:ref:`adding images <how-to-add-image>`, :ref:`creating links and buttons
<how-to-links>` and :ref:`reusing content with aliases <how-to-aliases>` — and the
:ref:`plugin reference <ref-plugins>` lists all plugins that ship with the quickstart
project. Next, in the final lesson, you publish your work.
