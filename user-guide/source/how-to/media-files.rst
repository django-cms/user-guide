.. _how-to-media-files:

Managing media files
====================

In django CMS, managing media files such as images, videos, documents, etc., is often
handled using a popular Django package called "django-filer." This package integrates
seamlessly with django CMS to handle file management efficiently. Here's a step-by-step
guide on managing media files in django CMS using django-filer:

1. **Accessing Filer in django CMS Admin:** Once installed, you can access the
   django-filer functionalities through the django CMS admin interface.
2. **Uploading Files:** Content editors can navigate to the Filer section within the CMS
   admin to upload new files (images, documents, videos, etc.). They can create folders,
   upload files, and organise them within the file manager provided by django-filer.
3. **Inserting Files into Content:** When editing content in django CMS, content editors
   can easily insert files (images, documents) stored in django-filer using plugins or
   specific placeholders designed to handle media elements. For instance, they might use
   a "File" or "Image" plugin that allows them to select files from the django-filer
   library and place them within the content area.
4. **File Management:** Django-filer provides features for renaming, deleting, moving,
   and organising files and folders within the file manager interface, ensuring a
   well-structured and manageable collection of media files.

By using django-filer, content editors can easily manage media files directly within the
CMS interface, simplifying the process of adding and organising various types of content
elements throughout the website.
