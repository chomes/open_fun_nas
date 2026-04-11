# Tailscale

This module creates and sets up tailscale on your local machine so you can use it to connect it to the system.

We will use this so you can remotely access your packages.

## Requirements

* You need to create an auth key, we recomend a permanent one so you don't have to re-auth again.
* To do this:
  * Login to tailscale admin console: [https://login.tailscale.com/admin/machines]
  * Add device > Linux server
  * Add a tag if you'd like you'll need to create one in managed tags
  * Choose to use it as an exit node, this means traffic gets routed from it on your phone.
  * Auth key expiration, this just sets how long the key can be used to auth your server before you have to create a new key.  This doesn't mean it's not a permanent key it just sets for how long key can be used to activate your device.
  * Generate script and copy the key it starts with `tskey-auth` and put this in the vars tailscale_auth_key.
