#!/usr/bin/env python3
import os
import os.path
import requests
from urllib.parse import urlparse
import time

def parse_markdown_http_links(markdown_file: os.PathLike) -> list[str]:
    ret = []
    with open(markdown_file, "r") as f:
        for line in f.readlines():
            if "http" not in line:
                continue
            link = extract_wiki_link_from(line)
            if link:
                ret.append(link)
    return ret


def download_http_link(link, filename) -> None:
    response = requests.get(link)
    with open(filename, 'wb') as file:
        file.write(response.content)

def get_page_name_from(url_link: str) -> str:
    parsed_url = urlparse(url_link)
    page_name = os.path.basename(parsed_url.path)
    return page_name

def extract_wiki_link_from(line: str) -> str:
    start_index = line.find('https://')
    if start_index == -1:
        start_index = line.find('http://')
    end_index = line.find(' "')
    return line[start_index:end_index]

def mkdir_p(folder: str) -> None:
    if not os.path.exists(folder):
        os.makedirs(folder)


if __name__ == "__main__":
    # Prefix
    # folder = "data/html/prefix"
    # mkdir_p(folder)
    # for link in parse_markdown_http_links("data/prefix_enchants.md"):
    #     page_name = get_page_name_from(link)
    #     html_file = os.path.join(folder, page_name + ".html")
    #     download_http_link(link, html_file)
    #     print(f"Downloaded {html_file}")

    # Suffix
    folder = "data/html/suffix"
    mkdir_p(folder)
    for link in parse_markdown_http_links("data/suffix_enchants.md"):
        page_name = get_page_name_from(link)
        html_file = os.path.join(folder, page_name + ".html")
        download_http_link(link, html_file)
        print(f"Downloaded {html_file}")
        time.sleep(3)