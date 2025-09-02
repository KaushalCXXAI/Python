
import requests
from bs4 import BeautifulSoup

class WebPageSummarizer:
    def __init__(self, url):
        self.url = url
        self.html = None
        self.soup = None
        self.summary = {}
        self.summary['url'] = url

    def fetch_html(self):
        response = requests.get(self.url)
        response.raise_for_status()
        self.html = response.text

    def parse_html(self):
        if not self.html:
            self.fetch_html()
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def extract_title(self):
        title_tag = self.soup.find('title')
        self.summary['title'] = title_tag.get_text(strip=True) if title_tag else ''

    def extract_meta_description(self):
        meta_desc = self.soup.find('meta', attrs={'name': 'description'})
        if not meta_desc:
            meta_desc = self.soup.find('meta', attrs={'property': 'og:description'})
        self.summary['meta_description'] = meta_desc['content'].strip() if meta_desc and 'content' in meta_desc.attrs else ''

    def extract_headings(self):
        self.summary['headings'] = {}
        for level in range(1, 7):
            heading_tags = self.soup.find_all(f'h{level}')
            # Ensure headings are always present as a list, even if empty
            self.summary['headings'][f'h{level}'] = [tag.get_text(strip=True) for tag in heading_tags] if heading_tags else []

    def extract_links(self):
        links = []
        for a in self.soup.find_all('a', href=True):
            link_text = a.get_text(strip=True)
            href = a['href']
            links.append({'text': link_text, 'href': href})
        self.summary['links'] = links if links else []

    def extract_bold_text(self):
        bold_tags = self.soup.find_all(['b', 'strong'])
        self.summary['bold_text'] = [b.get_text(strip=True) for b in bold_tags] if bold_tags else []

    def extract_italic_text(self):
        italic_tags = self.soup.find_all(['i', 'em'])
        self.summary['italic_text'] = [i.get_text(strip=True) for i in italic_tags] if italic_tags else []

    def extract_code_blocks(self):
        code_blocks = []
        for code in self.soup.find_all(['pre', 'code']):
            code_blocks.append(code.get_text('\n', strip=True))
        self.summary['code_blocks'] = code_blocks if code_blocks else []

    def extract_key_description(self):
        main_desc = ''
        main_tag = self.soup.find('main')
        if main_tag:
            first_p = main_tag.find('p')
            if first_p:
                main_desc = first_p.get_text(strip=True)
        if not main_desc:
            for p in self.soup.find_all('p'):
                text = p.get_text(strip=True)
                if text:
                    main_desc = text
                    break
        self.summary['key_description'] = main_desc

    def extract_short_summary(self):
        headings = self.summary.get('headings', {})
        h1s = headings.get('h1', [])
        self.summary['short_summary'] = (
            self.summary.get('meta_description')
            or self.summary.get('key_description')
            or (h1s[0] if h1s else self.summary.get('title', ''))
        )

    def summarize(self):
        self.parse_html()
        self.extract_title()
        self.extract_meta_description()
        self.extract_headings()
        self.extract_links()
        self.extract_bold_text()
        self.extract_italic_text()
        self.extract_code_blocks()
        self.extract_key_description()
        self.extract_short_summary()
        return self.summary

if __name__ == '__main__':
    import sys, json
    if len(sys.argv) != 2:
        print("Usage: python webpage_summarizer.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    summarizer = WebPageSummarizer(url)
    summary = summarizer.summarize()
    title = summary["title"].split(" ")
    name = " ".join(title[:2])
    data = json.dumps(summary, indent=2, ensure_ascii=False) 
    # print(data.title.split(" "))
    file = open(name + ".txt" , 'w')
    file.write(data)
    file.close()