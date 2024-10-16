# !/usr/bin/env bash

song_list=()

load_from_file() {
  local filepath="$1"
  local songs=$(cat $filepath)
  for line in songs; do
      song_list+=("$songs")
  done
}

create_mp3s() {
  local sorted_song_list=$(echo "$song_list" | sort -u)  
  echo "$sorted_song_list" | xargs yt-dlp --extract-audio --audio-format mp3
}

main() {
  local files=$(ls *.txt)
  for file in "$files"; do
    load_from_file "$file"
  done

  create_mp3s
}

main
