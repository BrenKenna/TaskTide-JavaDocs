from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree

BASE_URL = "https://api.docs.tasktide.org"

root = Element(
    "urlset",
    {"xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
)

for path in sorted(Path("javadoc").rglob("*.html")):
    relative = path.relative_to("javadoc").as_posix()

    url = SubElement(root, "url")
    loc = SubElement(url, "loc")
    loc.text = f"{BASE_URL}/{relative}"

ElementTree(root).write(
    "javadoc/sitemap.xml",
    encoding="utf-8",
    xml_declaration=True
)