from .client import *

# Pass the client function and container_id to the function wrapper
response = wrapper(client.get_autonomous_database, database_id)
logger.debug(f"RESPONSE_DATA: \n {response.data}")