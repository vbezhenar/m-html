#!/usr/bin/env python

import os
import sys
import time
import urllib

import flask
import werkzeug

music_dir = os.environ.get("HTTPSERVER_MUSIC_DIR")
if music_dir is None or not os.path.isdir(music_dir):
    sys.stderr.write("set HTTPSERVER_MUSIC_DIR=~/Music\n")
    exit(1)
artificial_delay = os.environ.get("HTTPSERVER_ARTIFICIAL_DELAY")
if artificial_delay is not None:
    artificial_delay = float(artificial_delay)
app = flask.Flask(__name__)


# simulate apache httpd
directory_index_template = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of {{path}}</title>
 </head>
 <body>
<h1>Index of {{path}}</h1>
<ul><li><a href="{{parent_path | urlencode}}"> Parent Directory</a></li>
{% for child in children %}
<li><a href="{{child | urlencode}}"> {{child}}</a></li>
{% endfor %}
</ul>
</body></html>
"""


@app.route("/music/", defaults={"path": ""})
@app.route("/music/<path:path>")
def default_route(path):
    if artificial_delay is not None:
        time.sleep(artificial_delay)
    if path == "m.html":
        return flask.send_from_directory(app.root_path, path)
    if path == "" or path.endswith("/"):
        fs_dir = werkzeug.security.safe_join(music_dir, path)
        if not os.path.isdir(fs_dir):
            return flask.abort(404)
        full_path = urllib.parse.urljoin("/music/", path)
        template_path = full_path.removesuffix("/")
        template_parent_path =  urllib.parse.urljoin(full_path, "..")
        template_children = []
        with os.scandir(fs_dir) as it:
            for entry in it:
                template_children.append(entry.name + ("/" if entry.is_dir() else ""))
        return flask.render_template_string(
            directory_index_template,
            path=template_path,
            parent_path=template_parent_path,
            children=template_children
        )
    return flask.send_from_directory(music_dir, path)
