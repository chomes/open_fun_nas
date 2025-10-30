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

## Onlyoffice

We deploy the onlyoffice doc server as a container, it is fine to have it on the same machine, but nextcloud and onlyoffice do not play well if the hostname points to 127.0.0.1.  Which is why trusted domains should point to a LAN address instead.

Only office is deployed by default but set the `nextcloud_onlyoffice_docserver_enable` to false if you don't want it installed.

### After install

Once you've installed the server go to the web interface of the doc server and enable the admin panel and set it to enable on boot.  **DO NOT ENABLE THE TEST DOC SERVER THIS IS NOT NEEDED**.

Please make sure you login to the doc server on a hostname that does not direct to local link address (127.0.0.1) as testing the doc server will not work.

Use `docker logs onlyoffice-server` to get the token for the admin panel and go to it and create a password.

* Enable local ips to connect and public ip addresses
* Configure other things you want

### Nextcloud integration

* In nextcloud install the only office app
* Go to Administration Settings > ONLYOFFICE
* Set the following settings:
  * only office doc server address - Set it as a LAN IP:8080
  * secret key - This is the jwt token you created
  * Advance settings > Authorization Header - AuthorizationJwt
* Click save, it should be successful and you can now work on docs!