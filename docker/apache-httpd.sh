#!/bin/sh

if [ -z "$1" ]
then
	echo 2>&1 Usage: "$0" ~/Music
	exit 1
fi

htdocs_dir=$(realpath "$1")
script_dir=$(dirname "$0")
mhtml_path=$(realpath "$script_dir"/../m.html)

echo "http://localhost:8080/m.html"
docker run -it --rm -p 8080:80 \
  -v "$htdocs_dir":/usr/local/apache2/htdocs:rw \
  -v "$mhtml_path":/usr/local/apache2/htdocs/m.html:ro \
  httpd:2.4
