# m-html

Simple one html file music player.

## Usage

Download [m.html](https://raw.githubusercontent.com/vbezhenar/m-html/main/m.html) file and copy it
into a directory with music files. Serve that directory with any HTTP server and use browser to open
`m.html` file. Ensure that your HTTP server serves directory indices (you should be able to open
something like `http://localhost:8080/` and get list of files and directories). It should just work.

## Example

[Example](https://vbezhenar.github.io/m-html/m.html#example/Jon%20Sayles/Bach/) website
demonstrating UI of the music player. Sound files were downloaded
from [www.freemusicpublicdomain.com](https://www.freemusicpublicdomain.com/) under CREATIVE COMMONS
license.

## Notes

For best experience use servers which support
[MDN: HTTP range requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests),
otherwise seeking might not work.

Tested browsers: Linux Chrome, Linux Firefox, iOS Safari. Tested servers: apache httpd, nginx,
`python -m http.server 8080` (this one does not support HTTP range requests).

Please note that not every browser supports every audio format:
[Wikipedia: Supported audio coding formats](https://en.wikipedia.org/wiki/HTML5_audio#Supported_audio_coding_formats)
.

This project is in WIP state, but it's unlikely to have lots of features, I want to keep it simple.

`httpserver.py` in the repository is used for development and testing and is not intended to be used
by end users. Scripts in `docker` directory used to test some web servers, you might want to check
those scripts if you can't configure your server.

## TODO

* Implement shuffle support.
* Implement "repeat all"/"repeat song" support.
* Implement recursive files retrieval (to play all songs of some artists, for example).
* Show helpful errors in the UI:
    * if user opens m.html from the filesystem.
    * if server responds with something other than HTTP 200 on listing request.
    * if directory is empty.
    * if browser does not support this format.
* Implement offline caching if possible.
