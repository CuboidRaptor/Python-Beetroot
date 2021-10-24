===========
Python-Beet
===========

Beet, a general purpose library full of random python functions that I thought were useful. Has file manipulation, random, tts and more!
Have fun using it!

Also, to make JSON dumping and reading faster, do ``pip install ujson`` or ``pip install simplejson``

Warnings:
=========

- beetroot.file.bdump() might not work too well, use with caution.

- beetroot.chatbot is a dumpster fire, avoid using until I get around to fixing it.

Different extras:
=================

- beetroot[all]

- beetroot[tts]

- beetroot[chatbot]

Functions and uses:
===================

Random stuff:
=============

- beetroot.random.randint(start, end) ; generates random number but using SystemRandom

- beetroot.random.srandint(seed, start, end) ; generates seeded pseudorandom number

Stopwatch stuff:
================

- beetroot.stopwatch.start() ; Starts global stopwatch

- beetroot.stopwatch.stop() ; Stops global stopwatch and returns time in milliseconds between start and stop

File Manipulation stuff:
========================

- beetroot.file.move(start, end) ; Moves files

- beetroot.file.rename(start, end) ; Renames files

- beetroot.file.delete(file_to_delete, force=<bool>) ; Deletes files

- beetroot.file.dump(file, data) ; Dumps data to file as string

- beetroot.file.bdump(file, data) ; Dumps data to file as bytestring (doesn't work too well)

- beetroot.file.jdump(file, data, pp=<bool>) ; Dumps data

- beetroot.file.load(file) ; Reads data from file as string

- beetroot.file.bload(file) ; Reads data from file as bytestring

- beetroot.file.jload(file) ; Reads data from file as JSON object

TTS stuff:
==========

- beetroot.tts.say(text) ; Reads text with tts installed, requires pyttsx3 to be installed or use ``pip install beetroot[tts]``

- beetroot.tts.changeRate(text) ; Changes global tts talk speed, requires pyttsx3 to be installed or use ``pip install beetroot[tts]``

- beetroot.tts.changeVoice(text) ; Changes global tts voice you can pick ids from 0-n, depending on how many voices you have on your computer, requires pyttsx3 to be installed or use ``pip install beetroot[tts]``

- beetroot.tts.changeVolume(text) ; Changes global tts volume, requires pyttsx3 to be installed or use ``pip install beetroot[tts]``

Chatbot AI stuff:
=================

- beetroot.chatbot.train([["foo", "bar", "baz"], ["qux", "quux"]]) ; Trains chatbot using list of lists showing conversation, check out `the ChatterBot docs <https://chatterbot.readthedocs.io/en/stable/quickstart.html#training-your-chatbot>`_ for more details, this als requires ChatterBot, spaCy, pytz and sqlalchemy, as do all of the beetroot.chatbot functions.

- beetroot.chatbot.response(foo) ; Returns response from the chatbot for input foo. Also, sqlalchemy uses a deprecated function, so if you get ``AttributeError: module 'time' has no attribute 'clock'`` then modify the code and replace ``time.clock`` with ``time.perf_counter``
  If you get ``AttributeError: module 'collections' has no attribute 'Hashable'``, then delete or comment ``if not isinstance(key, collections.Hashable):`` and everything within that block.

Miscelaneous stuff:
===================

- beetroot.strhash(text, secure=<bool>) ; Hashes a string or non-bytestring that can be converted to string.

- beetroot.bhash(text, secure=<bool>) ; Hashes a bytestring.

- beetroot.objtype(obj) ; python type(), but better

- beetroot.test() ; Literally just a hello world program.

- beetroot.quicksort(arr) ; Quicksort, which in most cases is slightly faster than Python3's default Timsort.

- beetroot.lsep(string, seperator) ; basically .split() but it removes empty or all-whitespace strings from output.

- beetroot.execfile(file) ; Execute .py script

- beetroot.systemstats() ; Returns [Username, OS, OS version, OS architecture, computer nodename, IP address, MAC address]

- beetroot.unline(string) ; Makes a multi-line string a single-line string

- beetroot.reline(string) ; Reverses beetroot.unline()

An amazing function that should be called whenever possible
===========================================================

- beetroot.beetroot() ; A great function that you should call whenever you can