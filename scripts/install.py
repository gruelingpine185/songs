#!/usr/bin/env python3

import os
import re
import sh

def extract_urls_from_file(pathname):
    urls = []
    with open(pathname, "r") as file:
        for line in file:
            if line[:1] == "#" or line[:1] == "\n":
                pass
            else:
                yt_url_regex = "^https?://youtu.be/([^/]+)"
                url = re.search(yt_url_regex, line)
                urls.append(url.string[:-1])

    return urls

def extract_downloaded_song_paths(file_list):
    downloaded = []
    for path in file_list:
        if os.path.splitext(path)[1] == ".mp3":
            song_path_regex = "\[([^/]+)\]"
            song_path = re.search(song_path_regex, path).group()[1:-1]
            downloaded.append(song_path)

    return downloaded

def create_download_list(song_paths, sorted_urls):
    download_list = []
    for url in sorted_urls:
        url_path = url[17:28]
        if url_path not in song_paths:
            download_list.append(url)
    
    return download_list

def download_songs(download_list):
    yt_dlp = sh.Command("yt-dlp")
    yt_dlp("--extract-audio", "--audio-format", "mp3", *download_list)

def main():
    urls = []
    files_in_dir = os.listdir()
    for path in files_in_dir:
        if os.path.splitext(path)[1] == ".txt":
            urls.extend(extract_urls_from_file(path))

    urls.sort()
    song_paths = extract_downloaded_song_paths(files_in_dir)
    download_list = create_download_list(song_paths, urls);
    print("This may take a while")
    download_songs(download_list)

if __name__ == "__main__":
    main()
