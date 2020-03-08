from vmware.vapi.vmc.client import create_vmc_client

def get_vmc_client(token):
    return create_vmc_client(token)

def list_sddcs(token, org_id):
    vmc_client = get_vmc_client(token)
    sddcs = vmc_client.orgs.Sddcs.list(org_id)
    return [
        {
            "text": sddc.name,
            "value": "{}+{}".format(sddc.name, sddc.id)
        } for sddc in sddcs
    ]
