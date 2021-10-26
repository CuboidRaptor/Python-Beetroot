.. |ss| raw:: html

   <strike>
   
.. |se| raw:: html

   </strike>
   
.. |bs| raw:: html

   <b>
   
.. |be| raw:: html

   </b>
   
.. |is| raw:: html

   <i>
   
.. |ie| raw:: html

   </i>

===============
Python-Beetroot
===============

Beetroot, a general purpose library full of random python functions that I thought were useful. Has file manipulation, random, tts and more!
Have fun using it!

Also, to make JSON dumping and reading faster, do ``pip install ujson`` or ``pip install simplejson``

If you find a problem, feel free to report it `here <https://github.com/CuboidRaptor/Python-Beetroot/issues>`_.

Warnings/Known Issues:
======================

- beetroot.file.bdump() might not work too well, use with caution.

- |ss| beetroot.chatbot is a dumpster fire, avoid using until I get around to fixing it.
  Even if I do fix it, It'll involve tons of hacky fixes trying to work around the enormous amount of bugs in ChatterBot,
  so on second thought, just don't ever use this class. Ever. |se| Nvm, ChatterBot has been removed, it's just too annoying to work with.

- beetroot.file.delete() doesn't throw errors when trying to delete non-existent files, wtf.

Different extras:
=================

- beetroot[all]

- beetroot[tts]

- |ss| beetroot[chatbot] |se| No. No. No. No.

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

Miscellaneous stuff:
====================

- beetroot.strhash(text, secure=<bool>) ; Hashes a string or non-bytestring that can be converted to string.

- beetroot.bytehash(text, secure=<bool>) ; Hashes a bytestring.

- beetroot.objtype(obj) ; python type(), but better

- beetroot.test() ; Literally just a hello world program.

- beetroot.quicksort(arr) ; Quicksort, which in most cases is slightly faster than Python3's default Timsort.

- beetroot.lsep(string, seperator) ; basically .split() but it removes empty or all-whitespace strings from output.

- beetroot.execfile(file) ; Execute .py script

- beetroot.systemstats() ; Returns [Username, OS, OS version, OS architecture, computer nodename, IP address, MAC address]

- beetroot.unline(string) ; Makes a multi-line string a single-line string

- beetroot.reline(string) ; Reverses beetroot.unline()

- beetroot.pixelgrab(x, y) ; Grabs the colour of the pixel on your screen at (x, y)

- beetroot.mousepixelgrab() ; Grabs colour of the pixel at your mouse

Amazing functions that should be called whenever possible
=========================================================

- beetroot.beetroot() ; A great function that you should call whenever you can

- beetroot.totally_not_a_rickroll() ; Totally not a rickroll.