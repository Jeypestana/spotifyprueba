import json
import pandas as pd

file_json = "taylor_swift_spotify.json"
file_csv = "dataset.csv"

with open(file_json, "r") as file:
    data = json.load(file)

# tracks
tracks_info = pd.json_normalize(
    data,
    record_path=["albums", "tracks"],
    meta=["artist_id", "artist_name", "artist_popularity"],
)
# tracks_info

# albums
albums_info = pd.json_normalize(
    data["albums"],
    record_path="tracks",
    sep="_",
    meta=["album_id", "album_name", "album_release_date", "album_total_tracks"],
)
# albums_info

# concact
df1 = pd.concat(
    [
        tracks_info,
        albums_info[
            ["album_id", "album_name", "album_release_date", "album_total_tracks"]
        ],
    ],
    axis=1,
    ignore_index=False,
)
df1.to_csv(file_csv, index=False)  # Export
# df1
