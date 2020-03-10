import ipaddress

from vmware.vapi.vmc.client import create_vmc_client

def get_vmc_client(token):
    return create_vmc_client(token)

def list_sddcs__(token, org_id):
    vmc_client = get_vmc_client(token)
    sddcs = vmc_client.orgs.Sddcs.list(org_id)
    return [
        {
            "text": sddc.name,
            "value": "{}+{}".format(sddc.name, sddc.id)
        } for sddc in sddcs
    ]

def list_sddcs_(token, org_id):
    vmc_client = get_vmc_client(token)
    sddcs = vmc_client.orgs.Sddcs.list(org_id)
    return [
        {
            "sddc_name": sddc.name,
            "user_name": sddc.user_name,
            "created": sddc.created.isoformat(),
            "num_hosts": len(sddc.resource_config.esx_hosts)
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

def list_region(token, org_id):
    vmc_client = get_vmc_client(token)
    regions = vmc_client.Orgs.get(org_id).properties.values.get("defaultAwsRegions").split(",")
    return [
        {
            "text": region,
            "value": region
        } for region in regions
    ]

def is_network(address):
    try:
        ipaddress.ip_network(address)
        return True
    except ValueError:
        return False

def is_valid_network(address):
    try:
        nw = ipaddress.ip_network(address)
    except ValueError:
        return False
    
    prefix = nw.prefixlen
    if prefix != 23 and prefix != 20 and prefix != 16:
        return False
    
    rs10 = ipaddress.ip_network(u'10.0.0.0/15')
    rs192 = ipaddress.ip_network(u'192.168.1.0/24')
    rs172 = ipaddress.ip_network(u'172.31.0.0/16')

    if nw.subnet_of(rs10):
        return False
    elif rs192.subnet_of(nw):
        return False
    elif nw.subnet_of(rs172):
        return False
    
    nw10 = ipaddress.ip_network(u'10.0.0.0/8')
    nw172 = ipaddress.ip_network(u'172.16.0.0/12')
    nw192 = ipaddress.ip_network(u'192.168.0.0/16')
    
    if nw.subnet_of(nw10):
        return True
    elif nw.subnet_of(nw172):
        return True
    elif nw.subnet_of(nw192):
        return True
    else:
        return False

def list_aws_account(token, org_id):
    vmc_client = get_vmc_client(token)
    accounts = vmc_client.orgs.account_link.ConnectedAccounts.get(org_id)
    return [
        {
            "text": account.account_number,
            "value": "{}+{}".format(
                account.account_number, 
                account.id)
        } for account in accounts
    ]

def list_vpc(
    token, 
    org_id, 
    linked_account_id, 
    region
):
    vmc_client = get_vmc_client(token)
    csbnts = vmc_client.orgs.account_link.CompatibleSubnets.get(
        org_id, 
        linked_account_id=linked_account_id, 
        region=region, 
        sddc=None, 
        force_refresh=None
    )
    vpcs = csbnts.vpc_map.keys()
    return [
        {
            "text": vpc,
            "value": vpc
        } for vpc in vpcs
    ]

def list_subnet(
    token,
    org_id,
    linked_account_id, 
    region,
    vpc_id
):
    vmc_client = get_vmc_client(token)
    csbnts = vmc_client.orgs.account_link.CompatibleSubnets.get(
        org_id, 
        linked_account_id=linked_account_id, 
        region=region, 
        sddc=None, 
        force_refresh=None
    )
    vpc_subnets = csbnts.get_field("vpc_map").get(vpc_id).subnets
    return [
        {
            "text": "{}, {}".format(sub.subnet_id, sub.name),
            "value": sub.subnet_id
        } for sub in vpc_subnets if sub.compatible
    ]

def list_num_hosts(num_hosts):
    return [
        {
            "text": i + 1,
            "value": i + 1
        } for i in range(2, num_hosts)
    ]

def check_sddc_user(token, org_id, sddc_id, user_name):
    vmc_client = get_vmc_client(token)
    sddc = vmc_client.orgs.Sddcs.get(org_id, sddc_id)
    sddc_user_name = sddc.user_name
    if sddc_user_name in user_name:
        return True
    else:
        return False
