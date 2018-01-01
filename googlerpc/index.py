import json
import os
import sys
import time
from googlerpc import rpc

try:
    from argparse import ArgumentParser as ArgParser
except ImportError:
    from optparse import OptionParser as ArgParser

__version__ = "1.0.5.2"

if sys.platform == "linux":
    file = os.path.expanduser('~') + "/.config/Google Play Music Desktop Player/json_store/playback.json"
elif sys.platform == "win32":
    file = os.path.expandvars(os.path.join('%AppData%\Google Play Music Desktop Player\json_store\playback.json'))
elif sys.platform == "darwin":
    os.path.expanduser('~') + "/Library/Application Support/Google Play Music Desktop Player/json_store/playback.json"
else:
    print("Unsupported OS, sorry")
    exit()

rpc = rpc.DiscordRPC('397050772807745536', verbose=False)
rpc.start()


def getplaying():
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
        return data


def update_presence():
    try:
        result = getplaying()
    except Exception as e:
        print("Exception:", e)

    payload = {
        "details": "",
        "timestamps": {
            "start": int(time.time()),
        },
        "assets": {
            'large_text': 'Google Play Music',
            'large_image': 'google_play'
        },
    }

    song = result["song"]["title"]
    artist = result["song"]["artist"]
    progress = result["time"]["current"]
    is_playing = result["playing"]

    if is_playing:
        payload["details"] = f"🎵 {song}"
        payload["state"] = f"👤 {artist}"
        payload["timestamps"]["start"] = int(time.time() - (progress * 0.001))
    else:
        payload["details"] = f"❚❚ Paused"

    rpc.send_rich_presence(payload)


def version():
    print(f"GoogleRPC {__version__}")
    sys.exit(0)


def parse_args():
    description = (
        'A Google Play Music song displayer for Discord\n'
        '--------------------------------------------------------------------------\n'
        'https://github.com/AlexFlipnote/googlerpc')

    parser = ArgParser(description=description)
    # Give optparse.OptionParser an `add_argument` method for
    # compatibility with argparse.ArgumentParser
    try:
        parser.add_argument = parser.add_option
    except AttributeError:
        pass

    parser.add_argument('--version', action='store_true', help='Show the version number and exit')

    options = parser.parse_args()
    if isinstance(options, tuple):
        args = options[0]
    else:
        args = options
    return args


def main():
    args = parse_args()

    if args.version:
        version()

    print("Loaded DiscordRPC")
    print("Loaded Google Play Music song info")
    print("----------------------------------------")
    try:
        cache_song = ''
        while True:
            update_presence()
            # NOTE: Mostly for debug
            # result = getplaying()
            # print(f"{result['song']['title']} by {result['song']['artist']}")
            result = getplaying()
            if cache_song != result['song']:
                cache_song = result['song']
                print(f"{result['song']['artist']} - {result['song']['title']}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("----------------------------------------")
        print('Closing DiscordRPC and Google Play Music song info...')


if __name__ == '__main__':
    main()
