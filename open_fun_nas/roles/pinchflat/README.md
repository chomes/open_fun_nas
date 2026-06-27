# Pinchflat role

## Description

The pinchflat service allows you to download videos from subscribers on youtube that you regularly watch to watch offline.  This is actually complimentary to jellyfin as we recommend setting the download vars to a location that jellyfin can see so you can then pick this up on jellyfin itself.

This service is great for people who watch regular content but want an automative way to download these videos and watch them on their server.

## Setup configs

| Name | Description |
| ---- | ----------- |
| time_zone | Set your timezone i.e. Europe/London [locations](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) |
| pinchflat_download_dir | Location of where the downloads will get stored, we recommend a location in jellyfin storage |
| pinchflat_server_config_dir | Location of where the pinchflat server config can go |
