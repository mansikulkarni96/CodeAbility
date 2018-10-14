import re

raw_synonyms = {
   'zero':'0',
   'one':'1',
   'two':'2',
   'three':'3',
   'four':'4',
   'five':'5',
   'six':'6',
   'seven':'7',
   'eight':'8',
   'nine':'9',
   'ten':'10',
   'alpha':'a',
   'beta':'b',
   'charlie':'c',
   'delta':'d',
   'epsilon':'e',
   'foxtrot':'f',
   'golf':'g',
   'hotel':'h',
   'india':'i',
   'julia':'j',
   'kilo':'k',
   'lima':'l',
   'mike':'m',
   'november':'n',
   'october':'o',
   'papa':'p',
   'quebec':'q',
   'romeo':'r',
   'sierra':'s',
   'tango':'t',
   'uniform':'u',
   'victor':'v',
   'whiskey':'w',
   'x-ray':'x',
   'yankee':'y',
   'zulu':'z',
   '[+]':'plus',
   '[-]':'minus',
   'free':'three',
   'return to': 'return',
   'create 4': 'create for',
   'next to': 'next',
   'ranch': 'range',
   '4 range': 'for range',
   'four range': 'for range',
   'the': '',
   'when': 'if',
   'find': 'define',
   'parameter':'parameters',
   'perimeter':'parameters',
   'clear':'create',
   'x':'times',
   '[*]':'times'
   }

synonyms = {("(^|[^A-Za-z])" + k + "([^A-Za-z]|$)"): " " + v + " " for (k, v) in raw_synonyms.items()}