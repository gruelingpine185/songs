# My Music Playlists

Ad-infested Spotify is quite irritating, so after many years of putting up with 
it, I've decicded that it's time to migrate to a different product; one where I 
can work offline, skip songs when I'd like, and not have to leave the terminal 
ever again.

Each text file (.txt) contains a list of youtube urls, which are downloaded 
into an mp3 format by yt-dlp. The script will read from the files, sort their 
contents (ignoring duplicates), and downlaod the songs.

## Prerequisites

- Requires [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Running

Make the script executable.

```sh
chmod +x ./installer.sh
```

Run the script

```sh
./installer.sh
```

## Contributions

Feel free to extend artist and album recommendations.
