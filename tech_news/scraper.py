import time
import requests
from parsel import Selector

# Requisito 1


def fetch(url):
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()

        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = [new for new in selector.css(".entry-title a::attr(href)").getall()]

    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next::attr(href)").get()

    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    info_new = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a.url::text").get(),
        "comments_count": len(selector.css(".comment-list li").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) ::text").getall()
        ).strip(),
        "tags": selector.css("a[rel='tag']::text").getall(),
        "category": selector.css(".category-style span.label::text").get(),
    }

    return info_new


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
