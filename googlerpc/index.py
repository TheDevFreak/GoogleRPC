import json
import os
import time
from googlerpc import rpc

file = os.path.expandvars(os.path.join('%AppData%\Google Play Music Desktop Player\json_store\playback.json'))

rpc = rpc.DiscordRPC('397050772807745536', verbose=False)
rpc.start()


def getplaying():
    with open(file) as f:
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
        payload["details"] = song
        payload["state"] = artist
        payload["timestamps"]["start"] = int(time.time() - (progress * 0.001))
    else:
        payload["details"] = f"❚❚ Paused"

    rpc.send_rich_presence(payload)


def main():
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
