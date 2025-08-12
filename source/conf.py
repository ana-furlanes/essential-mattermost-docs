# General information about the project.
project = "Essential Mattermost Docs"
copyright = "2015-2025 Mattermost"
author = "Ana Furlanes"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/letter-m.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# A list of CSS files. The entry must be a filename string or a tuple containing the filename string and the attributes
# dictionary. The filename must be relative to the html_static_path, or a full URI with scheme like
# https://example.org/style.css. The attributes is used for attributes of <link> tag. It defaults to an empty list.
html_css_files = [
    "css/mattermost-global.css",
    "css/homepage-v1.css",
    "css/compass-icons.css",
    "css/version-filter.css",
    "css/changelog-filter.css",
]

# A list of JavaScript filenames. The entry must be a filename string or a tuple containing the filename string and the
# attributes dictionary. The filename must be relative to the html_static_path, or a full URI with scheme like
# https://example.org/script.js. The attributes is used for attributes of <script> tag. It defaults to an empty list.
html_js_files = [
    "js/jquery.js",
    "js/thermometer.js",
    "js/myscript-v1.js",
    "js/version-filter.js",
    "js/changelog-filter.js",
]

# The name of an image file, relative to the configuration directory, to use as favicon of the docs. This file should
# be a Windows icon file (.ico) being 16x16 or 32x32 pixels in size.
html_favicon = "_static/my-favicon.ico"