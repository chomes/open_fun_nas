# Jellyfin

Jellyfin is a replacement for Plex.  It provides the same services as Plex does but it's major advantage is not requiring to check in if you have no internet.  Plex doesn't function if you have no internet connection which makes it less appealing for home servers.

## Configurtion

We enable users to have certain settings based on their servers function.

| Value | Description |
| ------- | ------------- |
| time_zone | Time Zone region Europe/London i.e. |
| enable_gpu | If you have a gpu and you want to do transcoding set this to true, otherwise leave as false |
| render_group_number | To enable gpu rendering provide the guid of the render group that docker can access |
| video_group_number | To enable gpu rendering for some systems we add the video group guid as it may be required |
| storage_dir | The location of where media and server configs will be stored |
| media_dir | Specify the folder name inside the storage_dir where media should go |
