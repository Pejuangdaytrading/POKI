import os
import datetime

# Domain kamu
BASE_URL = "https://dailyfunhub.site"

# Folder artikel
ARTICLES_DIR = "articles"

# Output file
SITEMAP_FILE = "sitemap.xml"

def generate_sitemap():
    urls = []

    # homepage
    urls.append({
        "loc": f"{BASE_URL}/",
        "lastmod": datetime.date.today().isoformat(),
        "priority": "1.0"
    })

    # scan folder articles
    for file in os.listdir(ARTICLES_DIR):
        if file.endswith(".html"):
            urls.append({
                "loc": f"{BASE_URL}/{ARTICLES_DIR}/{file}",
                "lastmod": datetime.date.today().isoformat(),
                "priority": "0.8"
            })

    # build xml
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url in urls:
        xml += "  <url>\n"
        xml += f"    <loc>{url['loc']}</loc>\n"
        xml += f"    <lastmod>{url['lastmod']}</lastmod>\n"
        xml += f"    <priority>{url['priority']}</priority>\n"
        xml += "  </url>\n"

    xml += "</urlset>\n"

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"Sitemap generated: {SITEMAP_FILE}")

if __name__ == "__main__":
    generate_sitemap()
