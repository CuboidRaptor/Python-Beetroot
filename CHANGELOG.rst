=========
Changelog
=========

Version number \= 1.Major.Minor.Patch

- | 1.1 ; I added Chatbot, and then removed it, because it's a steaming heap of trash. I also added the changelog that you're reading. Also added README.rst to PyPI page.
  |
- | 1.1.1 ; Reorganized files and classes and made changes to documentation. Also added totally_not_a_rickroll() and pixelgrab(), and also mousepixelgrab().
  |

- | 1.1.1.1 ; Minor bugfix to strhash()
  |

- | 1.1.1.2 ; Added minor obfuscation functions
  |

- | 1.1.1.3 ; Changed name of bhash() to bytehash()
  |

- | 1.1.1.4 ; Fixed bug where rST didn't render on PyPI
  |

- | 1.1.1.5 ; Added mem()
  |

- | 1.1.1.6 ; Added swapmem()
  |

- | 1.1.1.7 ; Minor fixes, changed obfuscation functions
  |

- | 1.1.1.8 ; Minor bugfixes to allow Unicode as well as ISO-8859-1 in strobfuscate() and strunobfuscate(),
  | Strings incompatible with both will probably explode or something idk
  |
  
- | 1.1.2 ; Reorganized and moved functions to classes, yt class is also now a thing and you can use yt.search(), also added kwargs to some functions
  |

- | 1.1.2.1 ; Added yt.dl()
  |

- | 1.1.2.2 ; Added remove() and siteize(). Added more bugfixes to README.rst to help render.
  |

- | 1.1.2.3 ; Bugfixes to json file functions.
  |

- | 1.1.3 ; Added text class, text.udown() and text.zalgo()
  | Added swap()
  |
  
- | 1.1.3.1 ; Upgraded text.zalgo(), uses zalgo-text so it doesn't look stupid now. Also added argument "crazy" to adjust craziness level of zalgo text
  |
  
- | 1.1.3.2 ; Made minor changes to documentation
  |
  
- | 1.1.3.3 ; Added bugfixes to text class and mem class.
  |
  
- | 1.1.3.4 ; Added taskkill() and crash().
  |
  
- | 1.1.3.5 ; Added admin().
  |
  
- | 1.1.3.6 ; Added hashl.dehash()
  |
  
- | 1.1.3.7 ; Added isAdmin() and bugfixes to crash()
  |
  
- | 1.1.3.8 ; Added cython()
  |
  
- | 1.1.3.9 ; Added bugfix to allow float craziness values to text.zalgo()
  |
  
- | 1.1.3.10 ; Added text.rouxls() to Rouxls-ify text.
  | Thiseth is the greatest worketh of artst ever created by thy human. This is approvedst by Thy Duke of Puzzles!
  |
  
- | 1.1.3.11 ; Changed text.rouxls() to make it more Rouxls-like.
  | I agree-eth, this shalt be knownest as thy greatest worketh in thy historie of thy darkners
  |
  
- | 1.1.3.12 ; Removed lsep(), as I found .split() does kinda the same thing and so this function is literally useless
  |

- | 1.1.3.13 ; Made Rouxls text engine better and changed cython()
  |

- | 1.1.3.14 ; Added text.spamton(), it kinda sucks tho. Also if you play Deltarune you know who that is. Also changed text.rouxls()
  | YES [[Kris]]!! GOOD JOB!!!! BUT WHY SETTLE FOR [this] [[LittleSponge]] WHEN YOU CAN BUY [SPAMTON G. SPAMTON]'s [[[STUFF]]???!?!!?
  |
  
- | 1.1.3.15 ; me stahp yoose os.system() and yoose subprocess.call() insted
  |
  
- | 1.1.3.16 ; Improvements to cython()
  |

- | 1.1.4 ; Added text.greek() and text.russian(). Note that this isn't an actual translator, and just swaps the characters.
  | This means that if you use text.greek(), Greek people still won't understand what you say.
  | I also improved the text.spamton() function.
  |
  
- | 1.1.4.1 ; Added text.reverse, reverses text, so "Hello, world!" becomes "!dlrow ,olleH".
  |

- | 1.1.5 ; Added printn() and getch(), also fixed bug where metadata attributes refused to show, and added comp class for
  | various compression methods, all using hybrid zlib/lzma.
  |
  
- | 1.1.5.1 ; Changes to documentation and added pkl.pkl() and pkl.unpkl().
  |

- | 1.1.6 ; Added text.b65536encode() and text.b65536decode().
  | Also removed hashl.bytehash() and merged it into hashl.hashf().
  | Merged obf byte functions into string functions, creating generic ones.
  | Merged byte function from comp.
  | Changed names of classes for easier debugging (for the users, not me)
  | Used kwargs in file.jdump()
  | Merged file.bdump() with file.dump()
  | Added annotations
  | Updated crash() to use bugs instead of taskkill()
  |
  
- | 1.1.6.1 ; Added math class
  | Updated crash() to work properly
  |
  
- | 1.1.6.2 ; Added text.phoneencode() and text.phonedecode()
  | Added missing items to documentation
  | Added pypath argument to cython()
  |
  
- | 1.1.6.3 ; Fixed bugs in beetroot.cython()
  | Added file.mkdir() and file.rmdir()
  |
  
- | 1.1.6.4 ; Added text.dotify() and text.spaceify()
  |

- | 1.1.7 ; Added recursion() context manager. Also added suppress() and speed().
  | Added retargs().
  | Used instances for stopwatch().
  
- | 1.1.7.1 ; Added cyclesort()
  | Added swap()
  | Bugfixes to quicksort()
  | Heavily modified printn() to use args
  | Changed taskkill()
  | Added errprint() and errprintn().
  | Added nocython argument to speed() in case people can't install Cython
  | Added isSorted()
  |
  
- | 1.1.7.2 ; 
  | Added b_round()
  | Added ensure_ascii option to file.jdump() and set to False, should prevent stupid non-Unicode problems
  | Added delchar()
  |