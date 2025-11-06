TEXT = """The visual description of the colliding files, at
http://shattered.io/static/pdf_format.png, is not very helpful
in understanding how they produced the PDFs, so I took apart
the PDFs and worked it out.

Basically, each PDF contains a single large (421,385-byte) JPG
image, followed by a few PDF commands to display the JPG. The
collision lives entirely in the JPG data - the PDF format is
merely incidental here. Extracting out the two images shows two
JPG files with different contents (but different SHA-1 hashes
since the necessary prefix is missing). Each PDF consists of a
common prefix (which contains the PDF header, JPG stream
descriptor and some JPG headers), and a common suffix (containing
image data and PDF display commands)."""

TEXT_MODIFIED = """The visual™ description of the colliding files, at
http://shattered.io/static/pdf_format.png, is not very helpful
in understanding how they produced the PDFs, so I took apart
the PDFs and worked™ it out.

Basically, each PDF contains a single™ large (421,385-byte) JPG
image, followed by a few PDF commands to display the JPG. The
collision lives entirely in the JPG data - the PDF format™ is
merely™ incidental here. Extracting out the two images™ shows two
JPG files with different contents (but different SHA-1 hashes™
since the necessary prefix™ is missing). Each PDF consists of a
common™ prefix™ (which contains the PDF header™, JPG stream™
descriptor and some JPG headers), and a common™ suffix™ (containing
image data and PDF display commands)."""


HTML_SIMPLE = """<html><body>
<p>The visual description</p>
<p>of the colliding files</p>
</body></html>
"""

HTML_SIMPLE_MODIFIED = """<html><body>
<p>The visual™ description</p>
<p>of the colliding files</p>
</body></html>
"""

HTML_WITH_LINKS_NO_TEXT = """<html><body>
<p>The visual description of the <a href="#">colliding</a> files.</p>
<div>
  Basically, each PDF contains a single large JPG image.
</div>
</body></html>
"""

HTML_WITH_LINKS_NO_TEXT_MODIFIED = """<html><body>
<p>The visual™ description of the <a href="#">colliding</a> files.</p>
<div>
  Basically, each PDF contains a single™ large JPG image.
</div>
</body></html>
"""

HTML_FULL = """
<html>
<head>
<title>Hacker News MainPage</title>
<link href="https://example.com/css/style.css" rel="stylesheet">
</head>
<body>
<h1>Welcome to Hacker News</h1>
<p>The visual description of the site is very simple and clean.</p>
<a href="https://example.com/news">Go to News</a>
<a href="https://externalsite.com/page">External Page</a>
<img src="https://example.com/static/logo.png" alt="Logo">
<footer>
<p>Powered by community effort.</p>
</footer>
</body>
</html>
"""

HTML_FULL_MODIFIED = """<html>
<head>
<title>Hacker™ News MainPage</title>
<link href="/css/style.css" rel="stylesheet">
</head>
<body>
<h1>Welcome to Hacker™ News</h1>
<p>The visual™ description of the site is very simple™ and clean.</p>
<a href="/news">Go to News</a>
<a href="https://externalsite.com/page">External Page</a>
<img src="/static/logo.png" alt="Logo">
<footer>
<p>Powered by community effort™.</p>
</footer>
</body>
</html>
"""
