.. _touch:

Using touch-screen devices with django CMS
==========================================

.. important::

    These notes apply to the **django CMS administration and editing interfaces**.
    The visitor-facing site is designed separately and may have different device
    requirements.

Touch support depends on the browser, screen size, installed plugins and the site's
frontend code. A tablet-sized screen generally gives the toolbar, sidebars and editing
dialogs more room than a phone. For longer editing sessions, a keyboard and pointing
device may still be more comfortable.

Touch interactions
------------------

django CMS uses interactions that were originally designed for a mouse, including
double-clicking, hovering and dragging. On a touch screen:

- A tap may open an editing control or select an item, depending on the context.
- Some content can be opened for editing by tapping it, while other content is easier
  to reach through its pencil button in the structure board.
- Use the dotted drag handle when moving pages or plugins. Starting a gesture elsewhere
  may scroll the view instead.
- Controls that normally appear on hover may be less obvious. The page tree, structure
  board and context menus provide explicit buttons for many of the same actions.

If a gesture is difficult to perform reliably, use the corresponding menu or action
button where one is available.

.. _device-support:

Screen size and orientation
---------------------------

The toolbar, structure board and administration sidebar all take up space beside the
page being edited. On a narrow screen, controls may be crowded or the editable page may
become too small to assess accurately. Switching to landscape orientation or a larger
screen can help.

Always check the result in **Preview** mode. Responsive pages can look different at
different viewport sizes, and the editing interface itself changes the space available
to the page.

Rich-text editing
-----------------

Rich-text editors and on-screen keyboards vary between browsers and devices. The
keyboard can cover part of a dialog, and selecting text or embedded plugins precisely
may be difficult. Saving frequently and using a hardware keyboard can make substantial
text editing easier.

The rich-text editor is supplied by an installed package, so its controls and touch
behaviour may differ from those shown in this guide.

Site-specific limitations
-------------------------

A site's CSS and markup can affect frontend editing. Small links, overlapping elements
or content with little space around it may be hard to select by touch even when the CMS
interface itself works correctly. If a particular page or plugin cannot be edited
reliably on a touch device, report the page, browser and device to the team responsible
for the site. They can determine whether the problem belongs to django CMS, an installed
plugin or the site's frontend.
