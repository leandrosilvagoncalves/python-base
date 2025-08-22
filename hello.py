#! /usr/bin/env python3
"""Multilanguage Hello World.

Depending on language defined on systems environment variables, the program will print "Hello World" in the specified language.

Usage:
You must have LANG set in your environment variables. example:
 export LANG=pt_BR

Execution:

    python3 hello.py
    or
    /hello.py
"""
__version__ = "0.0.1"
__author__ = "Leandro Goncalves"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour, le Monde!"
elif current_language == "es_ES":
    msg = "¡Hola, Mundo!"
    

print(msg)


