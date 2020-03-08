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

def get_max_num_hosts(token, org_id):
# get deployable number of hosts
# 1 host is for Storage EDRS
    
    vmc_client = get_vmc_client(token)
    
    sddcs = vmc_client.orgs.Sddcs.list(org_id)
    
    i = 0
    for sddc in sddcs:
        i += len(sddc.resource_config.esx_hosts)
    max_hosts = (int(vmc_client.Orgs.get(org_id).properties.values["sddcLimit"]) - 1) - i
#    if max_hosts < 1:
#        return max_hosts
#    else:
#        return 1 if max_hosts < 3 else max_hosts
    return 4 #for test

#def get_max_num_hosts_zerocloud(token, org_id): #for internal use
#    vmc_client = get_vmc_client(token)
#    return int(vmc_client.Orgs.get(org_id).properties.values["maxHostsPerSddcOnCreate"])
