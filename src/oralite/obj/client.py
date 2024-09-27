
# Import code from the core module where we setup config
from ..core import config, signer, model, wrapper
from ..log import logger
import oci
import sys



logger.debug(f"OCI_DEVOPS_INVOCATION: {sys.argv[0]}")

# Initialize the container instance client
client =  oci.object_storage.ObjectStorageClient(config)

namespace_name = "idbjyurhyjpo"
namespace = client.get_namespace().data
bucket_name = "infrastructure_model"
object_name = "model.json"


if __name__ == "__main__":
    #resp = client.get_object(namespace_name, bucket_name, object_name)
    print(f"namespace: {namespace}, bucket_name: {bucket_name}")
    resp = client.get_bucket(namespace, bucket_name)
    get_obj = client.get_object(namespace, bucket_name, object_name)
    with open('example_file_retrieved', 'wb') as f:
        for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
            f.write(chunk)
    print(f"{resp.status}, {resp.data}, {dir(resp)}")
    print(f"status: {get_obj.status}")
    # Simple targeting parameter for now, can provide more robust target filtering later
    # if len(sys.argv) <= 1:
    #     logger.error(f"INVOCATION_ERROR: Must provide container instance name")
    #     sys.exit(10)
    # Get the container name from argv
    # container_name = sys.argv[1]
    # Set the container ID
    # container_id = get_container_id(model_containers, container_name)