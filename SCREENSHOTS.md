# Screenshots needed

This is the checklist of screenshots that are referenced by the documentation but
have not been captured yet. Capture them from the
[django CMS quickstart project](https://github.com/django-cms/django-cms-quickstart)
(light colour scheme, browser window ~1200 px wide unless stated otherwise), add
the image file at the listed path under `user-guide/source/`, and uncomment the
prepared `.. image::` directive in the source page.

See [CONTRIBUTING.md](CONTRIBUTING.md#screenshot-placeholders) for the placeholder
convention. Audit this list against the sources with:

```bash
grep -rn "Screenshot needed" user-guide/source --include="*.rst"
```

| Image file | Source page | What to capture | Status |
|---|---|---|---|
| `tutorial/images/04-filer-new-folder.png` | `tutorial/04-filer.rst` | The filer folder list with the "New Folder" button highlighted and the new "Tutorial" folder dialog open. | needed |
| `tutorial/images/04-filer-upload.png` | `tutorial/04-filer.rst` | The inside of a filer folder with one uploaded image visible and the upload button at the top right highlighted. | needed |
| `tutorial/images/07-add-image.png` | `tutorial/07-plugins.rst` | The "Picture / Image" plugin dialog with an image selected from the media library's "Tutorial" folder. | needed |
| `how-to/images/add-image-dialog.png` | `how-to/add-image.rst` | The "Picture / Image" plugin edit dialog of djangocms-frontend, showing the image select field and the alignment options. | needed |
| `how-to/images/links-button-dialog.png` | `how-to/links.rst` | The "Link / Button" plugin edit dialog of djangocms-frontend, showing the internal/external link fields and the "Link type" / context (colour) options. | needed |
| `how-to/images/aliases-changelist.png` | `how-to/aliases.rst` | The Aliases overview in the sidebar with at least one category and one alias visible, the "Add Alias" button visible. | needed |
