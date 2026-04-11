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

### Extra tips

#### Tuning

Run `docker exec nextcloud-compose php occ db:add-missing-indices` to add the extra database tables you may be missing

#### Collabora setup

Upgraded to using nextcloud in https and have found that onlyoffice doesn't work entirely

I have since installed the built in collabora server and after many weeks of failing to get it to work I have sorted it out.  Here's how I've done this.

* Enforce https on your nextcloud `docker exec nextcloud-compose php occ config:system:set overwriteprotocol --value="https"`
* As I'm using nginx as my proxy server I have had to set up the following configuration for it

```nginx
server {
    listen 80;
    server_name DOMAIN;

    return 301 https://$host$request_uri;
}


server {
    listen 443 ssl;
    server_name DOMAIN;

    ssl_certificate /etc/letsencrypt/live/DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/DOMAIN/privkey.pem;


    location / {
        proxy_pass http://LOCAL_IP_OF_SERVER:8000;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

}
```

* Set up proxy server on docker container to be the local host ip of your nginx server `docker exec nextcloud-compose php occ config:system:set trusted_proxies 0 --value=NGINX_SERVER_IP`
* You may/have to use 0.0.0.0/0 for allowing wopi requests as many people have had issues tying this down to your local subnet or a external ip.  This is done in nextcloud in Administration Settings > Office > Allow list for wopi requests
* You may have to set your `wopi_global_url` to the same as your `wopi_url` run `docker exec nextcloud-compose php occ config:list richdouments` and if the global wopi url isn't the same do `docker exec nextcloud-compose php occ config:app:set richdocumets public_wopi_url --value="WOPI_URL"`
  * **IMPORTANT: Please make sure to remove the \ when adding the url in the value nextcloud will do that on your behalf**
* If you need to restart your container and then you should have a fully functional document editor in https!
