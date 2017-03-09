import homeassistant.remote as remote
import homeassistant.bootstrap as bootstrap

# Location of the Master API: host, password, port.
# Password and port are optional.
remote_api = remote.API("192.168.1.120", "autom@t10n", 8123)

# Initialize slave
hass = remote.HomeAssistant(remote_api)

# To add an interface to the slave on localhost:8123
bootstrap.setup_component(hass, 'frontend')

hass.start()
hass.block_till_stopped()
