"""Testing the use of dnacentersdk Python package."""
from dnacentersdk import DNACenterAPI
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable annoying HTTP warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

which_dnac = "devnet"
devnet = {
    "debug": False,
    "username": "devnetuser",
    "password": "Cisco123!",
    "base_url": "https://sandboxdnac2.cisco.com:443",
    "public_cert": False,
    "version": "1.3.0",
}
if which_dnac == "devnet":
    api = DNACenterAPI(
        username=devnet["username"],
        password=devnet["password"],
        base_url=devnet["base_url"],
        verify=devnet["public_cert"],
        debug=devnet["debug"],
        version=devnet["version"],
    )
else:
    print("No DNA Center connection information provided.  Exiting.")
    exit(0)

results = {}

print(api.devices.get_device_list())  # Permissions issue

results["workflows"] = api.pnp.get_workflows()
results["client_health"] = api.clients.get_overall_client_health()
results["all_device_configs"] = api.devices.get_device_config_for_all_devices()

print(results)
