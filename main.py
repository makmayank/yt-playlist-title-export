from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re
from pytube import YouTube
from pytube import Playlist


if __name__ == "__main__":
    urls = pd.read_csv('./youtube.csv')
    save_path = "./music_playlist_titles.txt"
    titles=[]
    i=0
    for url in urls.itertuples(index=False, name=None):
        print(f'Running for {url[2]}.')
        playlist = Playlist(url[4])
        try:
            
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            print('Number of videos in playlist: %s' % len(playlist.video_urls))
            for url in playlist.video_urls:
                yt = YouTube(url)
                titles.append(yt.title + " By"+ yt.author)
            # save to file
            
            with open(save_path, 'a', encoding="utf-8") as f:
                # write out the playlist name
                f.write(f'PLAYLIST :{playlist.title}\n\n')

                # write out the music titles
                for t in titles:
                    f.write(f'{t}\n')
        except:
            print(f"Error getting playlist for: {url[2]}")
            