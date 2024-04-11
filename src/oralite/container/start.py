from .client import *


# Client function to be run
client_function = client.start_container_instance

# Pass the client function and container_id to the function wrapper
def main(func, id):
    response = wrapper(func, id)
    print(response.data) # print output when executed from cli

if __name__ == "__main__":
    main(client_function, container_id)