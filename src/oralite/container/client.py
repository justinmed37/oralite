
# Import code from the core module where we setup config
from ..core import config, signer, model, wrapper
from ..log import logger
import oci
import sys


# Get the container ID of the corresponding resource by NAME
def get_container_id(list, name):
    id = ""
    for each in list:
        if each["display_name"] == name:
            id = each["id"]
    return id

logger.debug(f"OCI_DEVOPS_INVOCATION: {sys.argv[0]}")

# Initialize the container instance client
client =  oci.container_instances.ContainerInstanceClient(config)
container_id = ""
model_containers = model['containers'][0]["items"]

if __name__ == "__main__":
    # Simple targeting parameter for now, can provide more robust target filtering later
    if len(sys.argv) <= 1:
        logger.error(f"INVOCATION_ERROR: Must provide container instance name")
        sys.exit(10)
    # Get the container name from argv
    container_name = sys.argv[1]
    # Set the container ID
    container_id = get_container_id(model_containers, container_name)