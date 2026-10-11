# Letsencrypt

This role installs and configures a letsencrypt certificate for your multiple domains.  It is purely based on cloudflare's API registration so it will install all plugins required to use it.

## vars

* letsencrypt_certificate_name: The name of the certificate, I suggest using your primary domain name
* letsencrypt_cloudflare_api_token: The api token key from cloudflare, get this from the website and put it in the var file
* letsencrypt_domain_email: Required to register the domain with lets encrypt
* letsencrypt_domais:  This is a list, either provide 1 domain or multiple sub domains.
