# Nextcloud

This role will deploy the nextcloud server setup

## Requirements

The role should install everything you need but there are some things you should be aware of regarding some of the configs.

### Nextcloud compose file

When you are required to provide passwords for mysql or nextcloud if they are special characters `$%&` you need to provide a extra value if you want to use it otherwise it will not work i.e. `Pa$$$$word` will make it `Pa$$word`.

### SMTP setings

The SMTP env vars, may or may not work, I have personally found issues with doing this and have to manually set this up in the nextcloud instance but your millage may vary.

### Trusted domains

We recommend setting a trusted domain to something other then the hostname of the servers local 127.0.0.1.  This is due to onlyoffice.  You should use an ip address of your LAN and or the public ip address of the server.

## Collabora docs

I had issues with using onlyoffice with https so I've pivoted to collabora, after testing this on my own nas server I have got this functioning as expected.  Using the `nextcloud_collabora_docserver_enable` which is true by default will install and configure it.

Some important caveates when using this:

* It is expected that you have certbot or ssl certificates ready to use
* We will deploy the proxy server configuration for you, you just provide the information
* Your client machine will need to resolve the DNS of the office server for this to work along with your server
