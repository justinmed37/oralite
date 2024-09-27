
# Import code from the core module where we setup config
from ..core import config, signer, model, wrapper
from ..log import logger
import oci
import sys


# Get the container ID of the corresponding resource by NAME
def get_ajd_id(list, name):
    id = ""
    for each in list:
        logger.info(f"display_names: {each['display_name']}")
        if each["display_name"] == name:
            id = each["id"]
            logger.info(f"{each['display_name']}: {id}")
    return id


client =  oci.database.DatabaseClient(config)
database_id = ""
model_ajds = model['auto_dbs']

if __name__ == "__main__":
    # logs
    logger.debug(f"OCI_DEVOPS_INVOCATION: {sys.argv[0]}")

    # Initialize the container instance client


    # Simple targeting parameter for now, can provide more robust target filtering later
    
    if len(sys.argv) <= 1:
        logger.error(f"INVOCATION_ERROR: Must provide container instance name")
        sys.exit(10)

    # Get the container name from argv
    database_name = sys.argv[1]
    logger.debug(f"DATABASE_NAME: {database_name}")
    # logger.debug(f"AUTO_DBS: {model['auto_dbs']}")
    # Set the container ID
    database_id = get_ajd_id(model_ajds, database_name)
    logger.info(f"database_id: {database_id}")