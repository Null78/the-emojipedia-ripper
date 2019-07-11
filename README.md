# the-emojipedia-ripper
Extract all the different styles of emoji from emojipedia.org into PNG format with the highest possible quality using multithreading 

# Dependencies:

* Python 3
* [bs4](https://pypi.org/project/beautifulsoup4/)


# How to use:
```
$ python3 the-emojipedia-ripper.py -h
usage: the-emojipedia-ripper.py [-h] [-t ]
            [--apple | --samsung | --twitter | --whatsapp | --messenger | --facebook | --microsoft | --google | --mozilla | --htc | --lg | --joypixels | --kddi | --docomo | --emojidex | --softbank]

Extract all different styles of emojis from 'emojipedia.org'

optional arguments:
  -h, --help           show this help message and exit
  -t [], --threads []  Number of Threads (default: 8)
  --apple, --ios       Extract latest Apple ios emojis in PNG format
  --samsung            Extract the latest Samsung emojis in PNG format
  --twitter            Extract the latest Twitter emojis in PNG format
  --whatsapp           Extract the latest WhatsApp emojis in PNG format
  --messenger          Extract the latest Messenger emojis in PNG format
  --facebook           Extract the latest Facebook emojis in PNG format
  --microsoft          Extract the latest Microsoft emojis in PNG format
  --google             Extract the latest Google emojis in PNG format
  --mozilla            Extract the latest Mozilla emojis in PNG format
  --htc                Extract the latest HTC emojis in PNG format
  --lg                 Extract the latest LG emojis in PNG format
  --joypixels          Extract the latest JoyPixels emojis in PNG format
  --kddi               Extract the latest au KDDI emojis in PNG format
  --docomo             Extract the latest Docomo emojis in PNG format
  --emojidex           Extract the latest Emojidex emojis in PNG format
  --softbank           Extract the latest SoftBank emojis in PNG format
  ```
