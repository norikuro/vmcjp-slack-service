from vmware.vapi.vmc.client import create_vmc_client

def get_vmc_client(token):
    return create_vmc_client(token, session=session)


