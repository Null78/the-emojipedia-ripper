import argparse
import os
import urllib
from threading import Thread
from urllib.request import urlopen, Request
import bs4

parser = argparse.ArgumentParser(description="Extract all different styles of emojis from \'emojipedia.org\'")
parser.add_argument('-t', '--threads', nargs='?', metavar='', type=int, help="Number of Threads (default: 8)",
                    default=8)

group = parser.add_mutually_exclusive_group()

group.add_argument('--apple', '--ios', help="Extract latest Apple ios emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/apple/")
group.add_argument('--samsung', help="Extract the latest Samsung emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/samsung/")
group.add_argument('--twitter', help="Extract the latest Twitter emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/twitter/")
group.add_argument('--whatsapp', help="Extract the latest WhatsApp emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/whatsapp/")
group.add_argument('--messenger', help="Extract the latest Messenger emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/messenger/")
group.add_argument('--facebook', help="Extract the latest Facebook emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/facebook/")
group.add_argument('--microsoft', help="Extract the latest Microsoft emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/microsoft/")
group.add_argument('--google', help="Extract the latest Google emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/google/")
group.add_argument('--mozilla', help="Extract the latest Mozilla emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/mozilla/")
group.add_argument('--htc', help="Extract latest HTC emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/htc/")
group.add_argument('--lg', help="Extract the latest LG emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/lg/")
group.add_argument('--joypixels', help="Extract the latest JoyPixels emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/joypixels/")
group.add_argument('--kddi', help="Extract the latest au KDDI emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/au-kddi/")
group.add_argument('--docomo', help="Extract the latest Docomo emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/docomo/")
group.add_argument('--emojidex', help="Extract the latest Emojidex emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/emojidex/")
group.add_argument('--softbank', help="Extract the latest SoftBank emojis in PNG format", action="store_const",
                   const="https://emojipedia.org/softbank/")
args = parser.parse_args()

count = 0
queue = set()
done = set()
retry = set()


def get_web_page(page_link):
    print('Requesting Page ...')
    # emojipedia.org have security that reject urllib request so we have to use headers
    req = Request(page_link, headers={'User-Agent': 'Mozilla/5.0'})

    # read the response (page content) and decode so we can extract the links
    page = urlopen(req).read().decode()
    page_data = bs4.BeautifulSoup(page, 'lxml')

    print('Extracting Links ...')

    # first 21 emojis have srcset attributes with 144 quality but the rest have data-src attributes with 72 quality
    for tags in page_data.find_all('img', {'srcset': True}):
        queue.add(tags['srcset'][0:-3].replace('/144/', '/320/'))  # each link end with ' 2x' so cut the last three letters
        # replacing the quality 144 with 320 to get the highest possible

    for tags in page_data.find_all('img', {'data-src': True}):
        queue.add(tags['data-src'].replace('/72/', '/320/'))
    threads(queue, args.threads)


def downloading(links):
    for imgs in links:

        if imgs not in done:
            # add the link to the done set so we don't download it twice
            done.add(imgs)

            try:
                urllib.request.urlretrieve(imgs, path + '/' + imgs.split('/')[-1])

                # count variable have to be declared outside the function so it's not going to reset each time a thread start
                # print out the name if the downloaded image
                global count
                count += 1

                print(str(count) + '\nDone:  ' + imgs.split('/')[-1] + '\n')

            except:
                # if something wrong happned remove the link from
                done.remove(imgs)
                print(("Error with file: " + str(imgs.split('/')[-1])))
                raise




def threads(queue, thread):
    print('Start Downloading ...')
    threads = []
    for i in range(1, thread + 1):
        th = Thread(target=downloading, args=(queue,))
        threads.append(th)
        th.start()
    return threads



if __name__ == '__main__':
    # making a folder for each emoji style

    if args.apple is not None:
        path = 'Apple'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.apple)

    elif args.samsung is not None:

        path = 'Samsung'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.samsung)

    elif args.microsoft is not None:
        path = 'microsoft'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.microsoft)

    elif args.google is not None:
        path = 'Google'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.google)

    elif args.twitter is not None:
        path = 'Twitter'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.twitter)

    elif args.whatsapp is not None:
        path = 'WhatAapp'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.google)

    elif args.messenger is not None:
        path = 'Messenger'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.messenger)

    elif args.facebook is not None:
        path = 'Facebook'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.facebook)

    elif args.mozilla is not None:
        path = 'Mozilla'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.mozilla)

    elif args.htc is not None:
        path = 'HTC'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.htc)

    elif args.lg is not None:
        path = 'LG'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.lg)

    elif args.joypixels is not None:
        path = 'JoyPixels'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.joypixels)

    elif args.kddi is not None:
        path = 'au KDDI'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.kddi)

    elif args.docomo is not None:
        path = 'Docomo'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.docomo)

    elif args.emojidex is not None:
        path = 'Emojidex'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.emojidex)

    elif args.softbank is not None:
        path = 'SoftBank'
        if not os.path.exists(path):
            os.makedirs(path)
        get_web_page(args.softbank)
