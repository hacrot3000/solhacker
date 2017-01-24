solhacker
---------

convert flash cookie (sol) to plaintext (python repr) and back.

requires PyAMF and python 2
(tested only with pyamf 0.6.1 and python 2).

script expects input from stdin and writes output to stdout.

use case: hack savegames of stupid flash games.

example:

1. play stupid flash game.
2. find flash cookie. usually `~/.macromedia/blah.../flashcookie.sol`.
3. convert flash cookie to plaintext:

        solhacker < flashcookie.sol > pythonrepr.txt

4. edit `pythonrepr.txt` then convert back to flash cookie:

        solhacker < pythonrepr.txt > flashcookie.sol

5. start stupid flash game again and marvel at your wealth and powers.
or be disappointed if it didn't work.

notes:

* script is simple and stupid.
does no error checking and no error handling.
* script tries to detect if input is flash cookie
by converting the flash cookie to plaintext.
if that fails it will try to convert plaintext to flash cookie.
if that also fails then script will just give up.
* more and more flash games try to protect their save files
by encoding the data in some mime format or something.
in that case this script is practically useless.
* this script is old. it was written years ago
(around the time pyamf 0.6.1 was released).
i just brushed it up to put it on github.

License
-------

Copyright 2017 Lesmana Zimmer

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details.

