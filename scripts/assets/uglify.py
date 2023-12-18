#!/usr/bin/env python3

import os, errno
import subprocess
from css_html_js_minify import process_single_js_file

def silentremove(filename):
  try:
    os.remove(filename)
  except OSError as e:
    if e.errno != errno.ENOENT: # no such file or directory
      raise

def css_compile():
  source = ".assets/scss/style.scss"
  dest   = "docs/assets/css/style.min.css"

  silentremove(dest)
  silentremove(dest + ".map")

  arguments = [
    "poetry", "run", "pysass", "-t", "compressed", "-m",
    source, dest
  ]
  subprocess.Popen(arguments, stdout=subprocess.PIPE)

def js_uglify():
  sourcedir = ".assets/js/"
  for filename in os.listdir(sourcedir):
    source = sourcedir + filename
    dest   = "docs/assets/js/" + os.path.splitext(filename)[0] + ".min.js"
    silentremove(dest)
    process_single_js_file(source, output_path=dest)

def main():
  if not os.path.isfile(os.getcwd() + "/mkdocs.yml"):
    raise SystemExit("Error: You must run this file from the main directory")

  css_compile()
  js_uglify()

if __name__ == '__main__':
  main()
