#!/usr/bin/env python3

import os
import requests
import shutil
import tempfile
from urllib.parse import urlparse

versions = {
  "anchor":          "4.3.1",
  "bootstrap":       "5.3.0",
  "bootstrap-table": "1.22.1",
  "hljs":            "11.8.0",
  "jquery":          "3.6.0",
  "popper":          "2.11.8"
}

def download_helper(url, path, check=True):
  filename = path
  if os.path.isdir(filename):
    filename += '/' + os.path.basename(urlparse(url).path)

  if check and os.path.isfile(filename):
    return

  print("Downloading " + url + " to " + path)
  headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0"}
  response = requests.get(url, headers=headers)
  with open(filename, "wb") as file:
    file.write(response.content)
    file.close()

def download_bootstrap():
  bootstrap_test = ".bootstrap/scss/bootstrap.scss"
  bootstrap_dir  = ".bootstrap/bootstrap-" + versions["bootstrap"]
  bootstrap_scss = bootstrap_dir + "/scss"
  bootstrap_src  = "https://github.com/twbs/bootstrap/archive/refs/tags/v" + \
    versions["bootstrap"] + ".tar.gz"

  if not os.path.isfile(bootstrap_test):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    try:
      download_helper(bootstrap_src, tmp.name, False)
      shutil.unpack_archive(tmp.name, ".bootstrap/", "gztar")
      shutil.move(bootstrap_scss, ".bootstrap/")
      shutil.rmtree(bootstrap_dir)
    finally:
      tmp.close()
      os.unlink(tmp.name)

def download():
  css_urls = [
    "https://cdn.jsdelivr.net/npm/highlight.js@" + versions["hljs"] + "/styles/github.min.css",
    "https://cdn.jsdelivr.net/npm/highlight.js@" + versions["hljs"] + "/styles/github-dark-dimmed.min.css",
    "https://unpkg.com/bootstrap-table@" + versions["bootstrap-table"] + "/dist/bootstrap-table.min.css"
    "https://unpkg.com/bootstrap-table@" + versions["bootstrap-table"] + "/dist/extensions/filter-control/bootstrap-table-filter-control.min.css"
  ]
  js_urls = [
    "https://unpkg.com/@popperjs/core@" + versions["popper"] + "/dist/umd/popper.min.js",
    "https://unpkg.com/@popperjs/core@" + versions["popper"] + "/dist/umd/popper.min.js.map",
    "https://unpkg.com/bootstrap-table@" + versions["bootstrap-table"] + "/dist/bootstrap-table.min.js",
    "https://unpkg.com/bootstrap-table@" + versions["bootstrap-table"] + "/dist/extensions/filter-control/bootstrap-table-filter-control.min.js",
    "https://cdn.jsdelivr.net/npm/jquery@" + versions["jquery"] + "/dist/jquery.min.js",
    "https://cdn.jsdelivr.net/npm/jquery@" + versions["jquery"] + "/dist/jquery.min.map",
    "https://cdn.jsdelivr.net/npm/anchor-js@" + versions["anchor"] + "/anchor.min.js",
    "https://cdn.jsdelivr.net/npm/bootstrap@" + versions["bootstrap"] + "/dist/js/bootstrap.min.js",
    "https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@" + versions["hljs"] + "/highlight.min.js",
    "https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@" + versions["hljs"] + "/languages/bash.min.js",
    "https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@" + versions["hljs"] + "/languages/cpp.min.js",
    "https://cdn.jsdelivr.net/gh/sfz/highlight.js@master/dist/sfz.min.js"
  ]
  fa_url  = "https://kit.fontawesome.com/8d25d19870.js"
  fa_path = "mkdocs/docs/assets/js/fontawesome.min.js"

  download_bootstrap()
  download_helper(fa_url, fa_path)

  path = "mkdocs/docs/assets/css"
  for url in css_urls:
    download_helper(url, path)

  path = "mkdocs/docs/assets/js"
  for url in js_urls:
    download_helper(url, path)

def main():
  if not os.path.isfile(os.getcwd() + "/mkdocs.yml"):
    raise SystemExit("Error: You must run this file from the main directory")
  download()

if __name__ == '__main__':
  main()
