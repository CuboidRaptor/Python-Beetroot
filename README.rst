===============
Python-Beetroot
===============

Beetroot, a general purpose library full of random python functions that I thought were useful. Has file manipulation, random, tts and more!
Have fun using it!

Also, to make JSON dumping and reading faster, do ``pip install ujson`` or ``pip install simplejson``

If you find a problem, feel free to report it `here <https://github.com/CuboidRaptor/Python-Beetroot/issues>`_.

To install the bare minimum from pip, use ``pip install beetroot``, to install all dependencies for all classes, use ``pip install beetroot[all]``

Upgrading python-beetroot uses the command ``pip install --upgrade beetroot``

Warnings/Known Issues:
======================

- beetroot.file.bdump() might not work too well, use with caution.

- beetroot.file.delete() doesn't throw errors when trying to delete non-existent files, *wtf*.

- beetroot.crash() doesn't even do anything, damn my horrible python skills

- Yay I fixed the previous crash() bug but the damn thing broke OMFG I DIDN'T EVEN TOUCH ANYTHING WHAT WHY AAAAAAAAAAAA

- fixed it, still uses the old system

Different extras installation thingies:
=======================================

- beetroot[all]

- beetroot[tts]

- beetroot[img]

- beetroot[yt]

- beetroot[text]

- beetroot[ram]

- beetroot[keyboard]

- beetroot[cython]

- beetroot[speed]

Functions and uses:
===================

Bad Obfuscation Stuff:
======================

- beetroot.obf.obfuscate(string) ; Minorly obfuscates objects, this is definitely not secure, don't rely on this being irreversible or secure. If you want to obfuscate Python 3 code, use beetroot.cython()

- beetroot.obf.unobfuscate(string) ; Deobfuscates objects made by beetroot.strobfuscate()

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

- beetroot.file.dump(file, data) ; Dumps data to file as string or bytestring

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

Hash stuff:
===========

- beetroot.hashl.hashf(text, secure=<bool>) ; Hashes an object.

- beetroot.hashl.dehash(hash) ; Dehashes a hash, this totally works and is definitely possible and is absolutely not a
  dumb joke that I'm making...

Miscellaneous stuff:
====================

- beetroot.objtype(obj) ; python type(), but better

- beetroot.test() ; Literally just a hello world program.

- beetroot.quicksort(arr) ; Quicksort, which in most cases is slightly faster than Python3's default Timsort.

- beetroot.cyclesort(arr) ; Significantly slower than beetroot.quicksort(), but uses less memory.

- beetroot.swap(array, index_1, index_2) ; Swaps 2 items in list.

- beetroot.execfile(file) ; Execute .py script

- beetroot.sys_stats ; A variable that contains [Username, OS name, OS version, OS architecture, computer nodename, Local IP address, Public IP Address, MAC address]

- beetroot.unline(string) ; Makes a multi-line string a single-line string

- beetroot.reline(string) ; Reverses beetroot.unline()

- beetroot.pixelgrab(x, y) ; Grabs the colour of the pixel on your screen at (x, y), requires PIL, use ``pip install pillow``

- beetroot.mousepixelgrab() ; Grabs colour of the pixel at your mouse, requires PIL and pyautogui, use ``pip install pillow pyautogui`` or ``pip install beetroot[img]``

- beetroot.remove(str, item_to_remove) ; Removes all occurences of item_to_remove in str

- beetroot.siteize(str) ; Makes text into site names, for example "hello there" becomes "www.HelloThere.com"

- beetroot.taskkill(task, killamount=1) ; I see a task and I **E A T** it. Pass tasks to it through the "task" argument.
  killamount argument determines how many instances will be killed. Use None for all.

- beetroot.crash() ; Crashes pyth-
  Basically sends python SIGKILL.

- beetroot.admin() ; Requests UAC elevation on Windows.

- beetroot.cython(file, pypath=<path>) ; Generates a cython extension and cleans up afterwards. Requires python installed on PATH to use.
  Or whatever the Unix equivalent of PATH is.
  Uses pypath to find your python installation, or you can not include it and it uses sys.executable instead.

- beetroot.getch() ; Input, but it only waits for one character.

- beetroot.delchar() ; Deletes the last character from stdout

- beetroot.recursion() ; A context manager that lets you temporarily set your recursion depth. Use
  with beetroot.recursion(<some recursion limit here>):
  <do something here>
  Your recursion limit will be reset after.
  
- beetroot.suppress() ; A suppression context manager, use it with the "with" keyword like beetroot.recursion(). This will
  temporarily suppres stdout and stderr, preventing anything from being printed to console, even with sys.stderr.write.
  This will, however, not silence error messages, although that's probably a good thing.
  
- beetroot.speed() ; Use as a decorator, memoizes and Cython compiles code to **MASSIVELY** speed up code. I think. If you are using
  this with random functions, use the nocache=True argument.

- beetroot.retargs() ; Returns a list of all arguments of function.

- beetroot.locate() ; Throws an error, allows you to locate your beetroot installation.

- beetroot.strlist() ; Makes every single item in a list a string, with str() or .decode(), with proper bytestring handling.

- beetroot.errprint() ; Prints stuff to stderr.

- beetroot.isSorted() ; Checks if a list is sorted without actually sorting it.

- beetroot.progBar(<length of bar>) ; Makes a Progress bar. use "inf" for infinity length progress bar. Don't print output while progress bar is loading.

- beetroot.screen_size ; Returns dimensions of screen.

- beetroot.maxint ; Maximum size of integer that fits in a C function (i.e things like sys.setrecursionlimit()).

- beetroot.segfault() ; Forces python to segfault using a recursion bug.

- beetroot.func() ; Takes an object and creates a function that returns that object.

- beetroot.analyze() ; Analyzes a function, returns a score based on it's randomness by checking collisions.
  WARNING: Not great, a literal incrementation function would be reported as very random. UAYOR.

- beetroot.delayWrite(string, delay=<some number>, out=<stdout/stderr>) ; Writes stuff to stdout, one letter at a time.

- beetroot.tree(size) ; Builds a text tree and returns it. Inspired by code.golf.

- | beetroot.Defer() ; Golang "defer" feature in python. Can be used many ways. Let's say you need to write "b" to "a.txt" and then print "Done".

.. code:: python
	
	#Uses lambda and context managers
	with beetroot.Defer() as defer:
		f = open("a.txt", "w")
		defer(lambda: print("Done"))
		defer(lambda: f.close())
		f.write("b")
		
	#Uses args and context managers
	with beetroot.Defer() as defer:
		f = open("a.txt", "w")
		defer(print, "Done")
		defer(f.close)
		f.write("b")
		
	#Functions also work
	@beetroot.Defer
	def main(defer):
		f = open("a.txt", "w")
		defer(lambda: print("Done"))
		defer(lambda: f.close())
		f.write("b")
		
	main()
	
- beetroot.glubfubcode() ; Pass in the six numbers that the guy in the Vault of Secrets gives you for "cod3breaker", and give him the return of this function. For Geometry Dash, because I got bored.

Memory functions and stuff:
===========================

- beetroot.mem.mem() ; Returns [All memory, currently used memory, available memory].

- beetroot.mem.swapmem() ; Same thing as beetroot.mem(), except it's Swap memory instead.

Youtube garbage:
================

- beetroot.yt.search(search_term) ; Enter a search term, the function returns the link for the first hit on that search. Requires youtube-search, use ``pip install youtube-search`` or ``pip install beetroot[yt]``

- beetroot.yt.dl(url, filename, fileformat, playlist=<bool>) ; Downloads a video or playlist from url. Valid codecs include mp3, ogg, wav, m4a, aac, flac, mp4, webm, avi, opus, mkv, mov, flv, aiff and wma.
  Requires youtube-dl, use ``pip install youtube-dl`` or ``pip install beetroot[yt]``
  
Text manipulation stuff:
========================

- beetroot.text.udown(text) ; Flips text upside-down

- beetroot.text.zalgo(text, crazy=<int>) ; Adds zalgo to text, change crazy argument to modify craziness of zalgo text,
  default value is 1
  
- beetroot.text.rouxls(sentence) ; Rouxls-ify text so it sounds stupid.

- beetroot.text.spamton(text) ; Spamtonify text so you sound like [[Spamton G. Spamton]]

- beetroot.text.greek(text) ; Replaces English alphabet with Greek alphabet.

- beetroot.text.russian(text) ; Replaces English alphabet with Cyrillic alphabet.

- beetroot.text.reverse(text) ; Self-explanatory. Reverses text.

- beetroot.text.b65536encode(text) ; Encodes text into Base65536.

- beetroot.text.base65536decode(text) ; Decodes Base65536.

- beetroot.text.phoneencode(text) ; Encodes text using a cellphone keypad

- beetroot.text.phonedecode(text) ; Reverses beetroot.text.phoneencode()

- beetroot.text.dotify(text) ; Dotifies text, so "hi there" becomes "H.I. T.H.E.R.E."

- beetroot.text.spaceify(text) ; Spaceifies text, so "hi there" becomes "h i   t h e r e"

- beetroot.text.dc_weirdify(text) ; Applies a random number of random discord mini-MD effects to each char, making your string look weird in Discord or any service that supports mini-MarkDown.

- beetroot.text.blank ; A blank invisible zero-width char for your zero-width needs.

- beetroot.text.section ; A ?? Character. Did this when I found minecraft hightlights these as delimiters.

Compression class:
==================

- beetroot.comp.compress(string) ; Compress an object using hybrid zlib/lzma

- beetroot.comp.decompress(string) ; Reverses beetroot.comp.compress().

M A T H .
=========

- beetroot.math.increment(n) ; Increments n.

- beetroot.math.double(n) ; Doubles n.

- beetroot.math.square(n) ; Squares n.

- beetroot.math.sqrt(n) ; Square roots n.

- beetroot.math.factorial(n) ; Calculates the factorial of a number.

- beetroot.math.b_round(n, a) ; Rounds "n" to "a" decimal digits. Much more accurate than python's default round() (i think, i hope)

- beetroot.math.prec(n) ; Converts to a Decimal, better for precision (bcuz floats r weird)

- beetroot.math.isPrime(n) ; Checks if a number is prime. Returns a bool.

- beetroot.math.mround(a, b) ; Rounds a to the closest multiple of b.

PICKLES.
========

- beetroot.pkl.pkl(file_path_to_output_delicious_pickle, pickle) ; pass data and it gets turned into a big green pickle.

- beetroot.pkl.unpkl(file_path_to_load_delicious_pickle_from) ; load pickle from pickle to eat pickle loaded from pickle.

An amazing function that should be called whenever possible
===========================================================

- beetroot.totally_not_a_rickroll() ; Totally not a rickroll.