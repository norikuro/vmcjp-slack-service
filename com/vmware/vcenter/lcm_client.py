# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.lcm.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from com.vmware.cis_client import Tasks
from vmware.vapi.stdlib.client.task import Task
from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata

class ApplianceSize(Enum):
    """
    The size of appliance to be deployed.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    TINY = None
    """
    Appliance size of 'tiny', Default vCPUs: 2, Memory: 8GB, VM: 100, Hosts: 10

    """
    SMALL = None
    """
    Appliance size of 'small', Default vCPUs: 4, Memory: 16GB, VM: 1000, Hosts:
    100

    """
    MEDIUM = None
    """
    Appliance size of 'medium', Default vCPUs: 8, Memory: 24GB, VM: 4000,
    Hosts: 400

    """
    LARGE = None
    """
    Appliance size of 'large', Default vCPUs: 16, Memory: 32GB, VM: 10000,
    Hosts: 1000

    """
    XLARGE = None
    """
    Appliance size of 'extra large', Default vCPUs: 24, Memory: 48GB, VM:
    35000, Hosts: 2000

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`ApplianceSize` instance.
        """
        Enum.__init__(string)

ApplianceSize._set_values([
    ApplianceSize('TINY'),
    ApplianceSize('SMALL'),
    ApplianceSize('MEDIUM'),
    ApplianceSize('LARGE'),
    ApplianceSize('XLARGE'),
])
ApplianceSize._set_binding_type(type.EnumType(
    'com.vmware.vcenter.lcm.appliance_size',
    ApplianceSize))



class ApplianceType(Enum):
    """
    The type of appliance to be deployed.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    VCSA_EXTERNAL = None
    """
    Management node.

    """
    VCSA_EMBEDDED = None
    """
    Embedded node.

    """
    PSC = None
    """
    Infrastructure node.

    """
    VMC = None
    """
    VMC node.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`ApplianceType` instance.
        """
        Enum.__init__(string)

ApplianceType._set_values([
    ApplianceType('VCSA_EXTERNAL'),
    ApplianceType('VCSA_EMBEDDED'),
    ApplianceType('PSC'),
    ApplianceType('VMC'),
])
ApplianceType._set_binding_type(type.EnumType(
    'com.vmware.vcenter.lcm.appliance_type',
    ApplianceType))



class StorageSize(Enum):
    """
    The storage size of the appliance to be deployed.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    LARGE = None
    """
    Large storage

    """
    XLARGE = None
    """
    Extra large storage

    """
    REGULAR = None
    """
    Regular storage

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`StorageSize` instance.
        """
        Enum.__init__(string)

StorageSize._set_values([
    StorageSize('LARGE'),
    StorageSize('XLARGE'),
    StorageSize('REGULAR'),
])
StorageSize._set_binding_type(type.EnumType(
    'com.vmware.vcenter.lcm.storage_size',
    StorageSize))




class CeipOnlySso(VapiStruct):
    """
    The SSO definition that only contains CEIP setting.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 ceip_enabled=None,
                ):
        """
        :type  ceip_enabled: :class:`bool` or ``None``
        :param ceip_enabled: This key describes the enabling option for the VMware's Customer
            Experience Improvement Program (CEIP). By default we have
            ``ceipEnabled``: true, which indicates that you are joining CEIP.
            If you prefer not to participate in the VMware's CEIP for this
            product, you must disable CEIP by setting ``ceipEnabled``: false.
            You may join or leave VMware's CEIP for this product at any time.
            If None, defaults to True
        """
        self.ceip_enabled = ceip_enabled
        VapiStruct.__init__(self)


CeipOnlySso._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.ceip_only_sso', {
        'ceip_enabled': type.OptionalType(type.BooleanType()),
    },
    CeipOnlySso,
    False,
    None))



class Connection(VapiStruct):
    """
    Connection information for source/destination location.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 hostname=None,
                 username=None,
                 password=None,
                 https_port=None,
                 ssl_verify=None,
                 ssl_thumbprint=None,
                ):
        """
        :type  hostname: :class:`str`
        :param hostname: The IP address or DNS resolvable name of the ESX/VC host. If a DNS
            resolvable name is provided, it must be resolvable from the machine
            that is running the installer.
        :type  username: :class:`str`
        :param username: A username with administrative privileges on the ESX/VC host.
        :type  password: :class:`str`
        :param password: The password of the 'username' on the ESX/VC host.
        :type  https_port: :class:`long` or ``None``
        :param https_port: The port number for the ESX/VC.
            If None, defaults to 443
        :type  ssl_verify: :class:`bool` or ``None``
        :param ssl_verify: A flag to indicate whether the ssl verification is required.
            If ``sslThumbprint`` is provided, this field can be omitted If
            None, defaults to True
        :type  ssl_thumbprint: :class:`str` or ``None``
        :param ssl_thumbprint: Thumbprint for SSL verification.
            If ``sslVerify`` if false, this field is not required
        """
        self.hostname = hostname
        self.username = username
        self.password = password
        self.https_port = https_port
        self.ssl_verify = ssl_verify
        self.ssl_thumbprint = ssl_thumbprint
        VapiStruct.__init__(self)


Connection._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.connection', {
        'hostname': type.StringType(),
        'username': type.StringType(),
        'password': type.SecretType(),
        'https_port': type.OptionalType(type.IntegerType()),
        'ssl_verify': type.OptionalType(type.BooleanType()),
        'ssl_thumbprint': type.OptionalType(type.StringType()),
    },
    Connection,
    False,
    None))



class DeploymentInfo(VapiStruct):
    """
    Information about the appliance deployed.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 appliance_name=None,
                 appliance_fqdn=None,
                 appliance_ips=None,
                ):
        """
        :type  appliance_name: :class:`str`
        :param appliance_name: The name of the appliance.
        :type  appliance_fqdn: :class:`str` or ``None``
        :param appliance_fqdn: The FQDN of the appliance.
            Not applicable before firstboot.
        :type  appliance_ips: :class:`list` of :class:`str` or ``None``
        :param appliance_ips: The ip addresses of the appliance.
            Not applicable before firstboot.
        """
        self.appliance_name = appliance_name
        self.appliance_fqdn = appliance_fqdn
        self.appliance_ips = appliance_ips
        VapiStruct.__init__(self)


DeploymentInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.deployment_info', {
        'appliance_name': type.StringType(),
        'appliance_fqdn': type.OptionalType(type.StringType()),
        'appliance_ips': type.OptionalType(type.ListType(type.StringType())),
    },
    DeploymentInfo,
    False,
    None))



class DeploymentOption(VapiStruct):
    """
    Container to control deployment.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 skip_options=None,
                ):
        """
        :type  skip_options: :class:`dict` of :class:`DeploymentOption.SkipOptions` and :class:`bool`
        :param skip_options: The options control if a task should be skipped.
        """
        self.skip_options = skip_options
        VapiStruct.__init__(self)


    class SkipOptions(Enum):
        """
        Skippable tasks.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SKIP_SSO_CHECK = None
        """
        Skips the sso check. This should only be used when performing precheck for
        install/upgrade of management node before infrastructure node is deployed.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SkipOptions` instance.
            """
            Enum.__init__(string)

    SkipOptions._set_values([
        SkipOptions('SKIP_SSO_CHECK'),
    ])
    SkipOptions._set_binding_type(type.EnumType(
        'com.vmware.vcenter.lcm.deployment_option.skip_options',
        SkipOptions))

DeploymentOption._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.deployment_option', {
        'skip_options': type.MapType(type.ReferenceType(__name__, 'DeploymentOption.SkipOptions'), type.BooleanType()),
    },
    DeploymentOption,
    False,
    None))



class DestinationLocation(VapiStruct):
    """
    Configuration of destination location.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 esx=None,
                 vcenter=None,
                ):
        """
        :type  esx: :class:`Esx` or ``None``
        :param esx: This section describes the ESX host on which to deploy the
            appliance. Required if you are deploying the appliance directly on
            an ESX host.
            Mutual exclusive between ``esx`` and ``vcenter``
        :type  vcenter: :class:`Vc` or ``None``
        :param vcenter: This subsection describes the vCenter on which to deploy the
            appliance.
            Mutual exclusive between ``esx`` and ``vcenter``
        """
        self.esx = esx
        self.vcenter = vcenter
        VapiStruct.__init__(self)


DestinationLocation._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.destination_location', {
        'esx': type.OptionalType(type.ReferenceType(__name__, 'Esx')),
        'vcenter': type.OptionalType(type.ReferenceType(__name__, 'Vc')),
    },
    DestinationLocation,
    False,
    None))



class EmbeddedReplicatedVcsa(VapiStruct):
    """
    Configuration of the replicated Single Sign-On for Embedded type
    deployment.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 sso_admin_password=None,
                 sso_domain_name=None,
                 partner_hostname=None,
                 ssl_verify=None,
                 ssl_thumbprint=None,
                 https_port=None,
                ):
        """
        :type  sso_admin_password: :class:`str`
        :param sso_admin_password: Administrator password of the existing Single Sign-On to be
            replicated.
        :type  sso_domain_name: :class:`str`
        :param sso_domain_name: Domain name for the remote appliance which is being replicated. For
            example, 'vsphere.local'
        :type  partner_hostname: :class:`str`
        :param partner_hostname: The IP address or DNS resolvable name for the remote appliance.
        :type  ssl_verify: :class:`bool` or ``None``
        :param ssl_verify: A flag to indicate whether the ssl verification is required.
            If ``sslThumbprint`` is provided, this field can be omitted If
            None, defaults to True
        :type  ssl_thumbprint: :class:`str` or ``None``
        :param ssl_thumbprint: SHA1 thumbprint of the server SSL certificate which will be used
            for verification.
            If ``sslVerify`` is set to False, this field can be omitted
        :type  https_port: :class:`long` or ``None``
        :param https_port: The HTTPS port of the external PSC appliance.
            If None, defaults to 443
        """
        self.sso_admin_password = sso_admin_password
        self.sso_domain_name = sso_domain_name
        self.partner_hostname = partner_hostname
        self.ssl_verify = ssl_verify
        self.ssl_thumbprint = ssl_thumbprint
        self.https_port = https_port
        VapiStruct.__init__(self)


EmbeddedReplicatedVcsa._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.embedded_replicated_vcsa', {
        'sso_admin_password': type.SecretType(),
        'sso_domain_name': type.StringType(),
        'partner_hostname': type.StringType(),
        'ssl_verify': type.OptionalType(type.BooleanType()),
        'ssl_thumbprint': type.OptionalType(type.StringType()),
        'https_port': type.OptionalType(type.IntegerType()),
    },
    EmbeddedReplicatedVcsa,
    False,
    None))



class EmbeddedStandaloneVcsa(VapiStruct):
    """
    Configuration of the standalone Single Sign-On for Embedded type
    deployment.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 sso_admin_password=None,
                 sso_domain_name=None,
                ):
        """
        :type  sso_admin_password: :class:`str`
        :param sso_admin_password: Password must conform to the following requirements: 1. At least 8
            characters. 2. No more than 20 characters. 3. At least 1 uppercase
            character. 4. At least 1 lowercase character. 5. At least 1 number.
            6. At least 1 special character (e.g., '!', '(', '\\\\@', etc.). 7.
            Only visible A-Z, a-z, 0-9 and punctuation (spaces are not allowed)
        :type  sso_domain_name: :class:`str`
        :param sso_domain_name: The Single Sign-On domain name to be used to configure this vCenter
            Server Appliance. For example, 'vsphere.local'
        """
        self.sso_admin_password = sso_admin_password
        self.sso_domain_name = sso_domain_name
        VapiStruct.__init__(self)


EmbeddedStandaloneVcsa._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.embedded_standalone_vcsa', {
        'sso_admin_password': type.SecretType(),
        'sso_domain_name': type.StringType(),
    },
    EmbeddedStandaloneVcsa,
    False,
    None))



class Esx(VapiStruct):
    """
    Configuration of ESX.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 connection=None,
                 inventory=None,
                ):
        """
        :type  connection: :class:`Connection`
        :param connection: The configuration to connect to an ESX/VC.
        :type  inventory: :class:`EsxInventory`
        :param inventory: The configuration of ESX inventory.
        """
        self.connection = connection
        self.inventory = inventory
        VapiStruct.__init__(self)


Esx._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.esx', {
        'connection': type.ReferenceType(__name__, 'Connection'),
        'inventory': type.ReferenceType(__name__, 'EsxInventory'),
    },
    Esx,
    False,
    None))



class EsxInventory(VapiStruct):
    """
    Configuration of ESX's inventory.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 datastore_name=None,
                 network_name=None,
                 resource_pool_path=None,
                ):
        """
        :type  datastore_name: :class:`str`
        :param datastore_name: The datastore on which to store the files of the appliance. This
            value has to be either a specific datastore name, or a specific
            datastore in a datastore cluster. The datastore must be accessible
            from the ESX host and must have at least 25 GB of free space.
            Otherwise, the new appliance might not power on.
        :type  network_name: :class:`str` or ``None``
        :param network_name: The network of the ESX host to which the new appliance should
            connect. Omit this parameter if the ESX host has one network.
            If None, defaults to VM Network
        :type  resource_pool_path: :class:`str` or ``None``
        :param resource_pool_path: The path to the resource pool on the ESX host in which the
            appliance will be deployed.
            Not applicable when not in resource pool
        """
        self.datastore_name = datastore_name
        self.network_name = network_name
        self.resource_pool_path = resource_pool_path
        VapiStruct.__init__(self)


EsxInventory._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.esx_inventory', {
        'datastore_name': type.StringType(),
        'network_name': type.OptionalType(type.StringType()),
        'resource_pool_path': type.OptionalType(type.StringType()),
    },
    EsxInventory,
    False,
    None))



class ExistingMigrationAssistant(VapiStruct):
    """
    Configuration of the migration assistant that is already running on the
    source Windows VC.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 ssl_thumbprint=None,
                 https_port=None,
                ):
        """
        :type  ssl_thumbprint: :class:`str`
        :param ssl_thumbprint: The SSL thumbprint of Migration Assistant. The SSL thumbprint can
            be retrieved from the Migration Assistant console and log file.
        :type  https_port: :class:`long` or ``None``
        :param https_port: Migration Assistant port number shown in the Migration Assistant
            console and log file. The default port is 9123.
            If None, defaults to 9123
        """
        self.ssl_thumbprint = ssl_thumbprint
        self.https_port = https_port
        VapiStruct.__init__(self)


ExistingMigrationAssistant._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.existing_migration_assistant', {
        'ssl_thumbprint': type.StringType(),
        'https_port': type.OptionalType(type.IntegerType()),
    },
    ExistingMigrationAssistant,
    False,
    None))



class ExternalTool(VapiStruct):
    """
    Configuration of the external tools used.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 hostname=None,
                 location=None,
                ):
        """
        :type  name: :class:`str`
        :param name: The name of the external tool
        :type  hostname: :class:`str` or ``None``
        :param hostname: The host name of the external tool.
            Can be absent when external tool does not have a host name.
        :type  location: :class:`str`
        :param location: The location of the external tool.
        """
        self.name = name
        self.hostname = hostname
        self.location = location
        VapiStruct.__init__(self)


ExternalTool._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.external_tool', {
        'name': type.StringType(),
        'hostname': type.OptionalType(type.StringType()),
        'location': type.StringType(),
    },
    ExternalTool,
    False,
    None))



class ExternalVcsa(VapiStruct):
    """
    Configuration of the Single Sign-On for Management type deployment.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 sso_admin_password=None,
                 sso_domain_name=None,
                 psc_hostname=None,
                 ssl_verify=None,
                 ssl_thumbprint=None,
                 https_port=None,
                ):
        """
        :type  sso_admin_password: :class:`str`
        :param sso_admin_password: Administrator password of the external PSC to register with.
        :type  sso_domain_name: :class:`str`
        :param sso_domain_name: Domain name of the external PSC. For example, 'vsphere.local'
        :type  psc_hostname: :class:`str`
        :param psc_hostname: The IP address or DNS resolvable name of the remote PSC to which
            this configuring vCenter Server will be registered.
        :type  ssl_verify: :class:`bool` or ``None``
        :param ssl_verify: A flag to indicate whether the SSL verification is required
            If ``sslThumbprint`` is provided, this field can be omitted If
            None, defaults to False
        :type  ssl_thumbprint: :class:`str` or ``None``
        :param ssl_thumbprint: SHA1 thumbprint of the server SSL certificate which will be used
            for verification.
            If ``sslVerify`` is set to False, this field can be omitted.
        :type  https_port: :class:`long` or ``None``
        :param https_port: The HTTPS port of the external PSC appliance.
            If None, defaults to 443
        """
        self.sso_admin_password = sso_admin_password
        self.sso_domain_name = sso_domain_name
        self.psc_hostname = psc_hostname
        self.ssl_verify = ssl_verify
        self.ssl_thumbprint = ssl_thumbprint
        self.https_port = https_port
        VapiStruct.__init__(self)


ExternalVcsa._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.external_vcsa', {
        'sso_admin_password': type.SecretType(),
        'sso_domain_name': type.StringType(),
        'psc_hostname': type.StringType(),
        'ssl_verify': type.OptionalType(type.BooleanType()),
        'ssl_thumbprint': type.OptionalType(type.StringType()),
        'https_port': type.OptionalType(type.IntegerType()),
    },
    ExternalVcsa,
    False,
    None))



class GuestCredential(VapiStruct):
    """
    Configuration of the guest credential.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 os_username=None,
                 os_password=None,
                ):
        """
        :type  os_username: :class:`str`
        :param os_username: Administrator username for the source Windows operating system.
        :type  os_password: :class:`str`
        :param os_password: Administrator user password for the source Windows operating
            system.
        """
        self.os_username = os_username
        self.os_password = os_password
        VapiStruct.__init__(self)


GuestCredential._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.guest_credential', {
        'os_username': type.StringType(),
        'os_password': type.SecretType(),
    },
    GuestCredential,
    False,
    None))



class History(VapiStruct):
    """
    Configuration of the data to be exported during upgrade/migrate.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 defer_import=None,
                 data_set=None,
                ):
        """
        :type  defer_import: :class:`bool` or ``None``
        :param defer_import: A flag to indicate whether the import of historical data should be
            deferred until after upgrade/migrate.
            If None, defaults to False
        :type  data_set: :class:`History.DataSetType` or ``None``
        :param data_set: The type of data to be upgraded/migrated.
            If None, defaults to ALL
        """
        self.defer_import = defer_import
        self.data_set = data_set
        VapiStruct.__init__(self)


    class DataSetType(Enum):
        """
        The type of data to be upgraded/migrated.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        EVENTS_TASKS = None
        """
        event data and task data.

        """
        NONE = None
        """
        core only.

        """
        ALL = None
        """
        core, event and task data.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`DataSetType` instance.
            """
            Enum.__init__(string)

    DataSetType._set_values([
        DataSetType('EVENTS_TASKS'),
        DataSetType('NONE'),
        DataSetType('ALL'),
    ])
    DataSetType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.lcm.history.data_set_type',
        DataSetType))

History._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.history', {
        'defer_import': type.OptionalType(type.BooleanType()),
        'data_set': type.OptionalType(type.ReferenceType(__name__, 'History.DataSetType')),
    },
    History,
    False,
    None))



class MigrationAssistant(VapiStruct):
    """
    Configuration of the migration assistant to be uploaded and started on
    source Windows VC.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 source_location=None,
                 settings=None,
                 guest_credentials=None,
                 migration_assistant_installer_location=None,
                 migration_assistant_installer_location_ssl_verify=None,
                 migration_assistant_installer_location_ssl_thumbprint=None,
                ):
        """
        :type  source_location: :class:`Connection`
        :param source_location: The configuration to connect to an ESX/VC.
        :type  settings: :class:`MigrationAssistantSetting`
        :param settings: Spec to automatically launch the Migration Assistant.
        :type  guest_credentials: :class:`GuestCredential`
        :param guest_credentials: Credentials for the Windows system on which the vCenter server is
            running.
        :type  migration_assistant_installer_location: :class:`str` or ``None``
        :param migration_assistant_installer_location: Installer location of the migration assistant to be uploaded.
        :type  migration_assistant_installer_location_ssl_verify: :class:`bool` or ``None``
        :param migration_assistant_installer_location_ssl_verify: A flag to indicate whether to verify ssl connection.
            when SSL thumbprint is provided, SSL verify is not required.
        :type  migration_assistant_installer_location_ssl_thumbprint: :class:`str` or ``None``
        :param migration_assistant_installer_location_ssl_thumbprint: SSL thumbprint of the source appliance.
            if ssl verify is set to False, thumbprint is not required.
        """
        self.source_location = source_location
        self.settings = settings
        self.guest_credentials = guest_credentials
        self.migration_assistant_installer_location = migration_assistant_installer_location
        self.migration_assistant_installer_location_ssl_verify = migration_assistant_installer_location_ssl_verify
        self.migration_assistant_installer_location_ssl_thumbprint = migration_assistant_installer_location_ssl_thumbprint
        VapiStruct.__init__(self)


MigrationAssistant._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.migration_assistant', {
        'source_location': type.ReferenceType(__name__, 'Connection'),
        'settings': type.ReferenceType(__name__, 'MigrationAssistantSetting'),
        'guest_credentials': type.ReferenceType(__name__, 'GuestCredential'),
        'migration_assistant_installer_location': type.OptionalType(type.StringType()),
        'migration_assistant_installer_location_ssl_verify': type.OptionalType(type.BooleanType()),
        'migration_assistant_installer_location_ssl_thumbprint': type.OptionalType(type.StringType()),
    },
    MigrationAssistant,
    False,
    None))



class MigrationAssistantSetting(VapiStruct):
    """
    Configuration of the setting of migration assistant to be uploaded and
    started on source Windows VC.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 migrated_ip=None,
                 https_port=None,
                 export_dir=None,
                 service_account_password=None,
                ):
        """
        :type  migrated_ip: :class:`str` or ``None``
        :param migrated_ip: The IP address of the network adapter that will be migrated. Only
            required if the Windows vCenter Server has multiple network
            adapters, making its system name resolve to multiple IP addresses.
            May not be applicable.
        :type  https_port: :class:`long` or ``None``
        :param https_port: Migration Assistant port number shown in the Migration Assistant
            console. The default port is 9123
            If None, defaults to 9123
        :type  export_dir: :class:`str` or ``None``
        :param export_dir: Directory to export source configuration and data. Optional.
            If None, defaults to /var/tmp
        :type  service_account_password: :class:`str` or ``None``
        :param service_account_password: The password of the vCenter Server service account. Required only
            if the vCenter Server service is running under a non LocalSystem
            account.
            Service account may not be applicable
        """
        self.migrated_ip = migrated_ip
        self.https_port = https_port
        self.export_dir = export_dir
        self.service_account_password = service_account_password
        VapiStruct.__init__(self)


MigrationAssistantSetting._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.migration_assistant_setting', {
        'migrated_ip': type.OptionalType(type.StringType()),
        'https_port': type.OptionalType(type.IntegerType()),
        'export_dir': type.OptionalType(type.StringType()),
        'service_account_password': type.OptionalType(type.SecretType()),
    },
    MigrationAssistantSetting,
    False,
    None))



class Network(VapiStruct):
    """
    Network configuration of the appliance to be deployed.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'mode',
            {
                'STATIC' : [('hostname', False), ('ip', True), ('dns_servers', True), ('prefix', True), ('gateway', True)],
                'DHCP' : [],
            }
        ),
    ]



    def __init__(self,
                 hostname=None,
                 ip_family=None,
                 mode=None,
                 ip=None,
                 dns_servers=None,
                 prefix=None,
                 gateway=None,
                ):
        """
        :type  hostname: :class:`str` or ``None``
        :param hostname: Primary network identity. Can be either an IP address or a fully
            qualified domain name(FQDN).
            host name may not be applicable
        :type  ip_family: :class:`TemporaryNetwork.IpType` or ``None``
        :param ip_family: Network IP address family.
            If None, defaults to IPV4
        :type  mode: :class:`TemporaryNetwork.NetworkMode`
        :param mode: Network mode.
        :type  ip: :class:`str`
        :param ip: Network IP address. Required for static mode only.
            This attribute is optional and it is only relevant when the value
            of ``mode`` is :attr:`TemporaryNetwork.NetworkMode.STATIC`.
        :type  dns_servers: :class:`list` of :class:`str`
        :param dns_servers: A comma-separated list of IP addresses of DNS servers. A JSON array
            such as ["1.2.3.4", "127.0.0.1"]. Required for static mode only.
            DNS servers must be reachable from the machine that runs CLI
            installer
            This attribute is optional and it is only relevant when the value
            of ``mode`` is :attr:`TemporaryNetwork.NetworkMode.STATIC`.
        :type  prefix: :class:`long`
        :param prefix: Network prefix length. Required for static mode only. Remove if the
            mode is "dhcp". This is the number of bits set in the subnet mask;
            for instance, if the subnet mask is 255.255.255.0, there are 24
            bits in the binary version of the subnet mask, so the prefix length
            is 24. If used, the values must be in the inclusive range of 0 to
            32 for IPv4 and 0 to 128 for IPv6. Required for static mode only.
            This attribute is optional and it is only relevant when the value
            of ``mode`` is :attr:`TemporaryNetwork.NetworkMode.STATIC`.
        :type  gateway: :class:`str`
        :param gateway: Gateway of the network. Required for static mode only.
            This attribute is optional and it is only relevant when the value
            of ``mode`` is :attr:`TemporaryNetwork.NetworkMode.STATIC`.
        """
        self.hostname = hostname
        self.ip_family = ip_family
        self.mode = mode
        self.ip = ip
        self.dns_servers = dns_servers
        self.prefix = prefix
        self.gateway = gateway
        VapiStruct.__init__(self)


Network._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.network', {
        'hostname': type.OptionalType(type.StringType()),
        'ip_family': type.OptionalType(type.ReferenceType(__name__, 'TemporaryNetwork.IpType')),
        'mode': type.ReferenceType(__name__, 'TemporaryNetwork.NetworkMode'),
        'ip': type.OptionalType(type.StringType()),
        'dns_servers': type.OptionalType(type.ListType(type.StringType())),
        'prefix': type.OptionalType(type.IntegerType()),
        'gateway': type.OptionalType(type.StringType()),
    },
    Network,
    False,
    None))



class Notification(VapiStruct):
    """
    Notification messages of a single task.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 time=None,
                 message=None,
                 resolution=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The identifier of the message.
        :type  time: :class:`datetime.datetime` or ``None``
        :param time: The time the notification was raised/found.
            Only :class:`set` if the time information is available.
        :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param message: The notification message.
        :type  resolution: :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
        :param resolution: The resolution message, if any.
            Only :class:`set` for warnings and errors.
        """
        self.id = id
        self.time = time
        self.message = message
        self.resolution = resolution
        VapiStruct.__init__(self)


Notification._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.notification', {
        'id': type.StringType(),
        'time': type.OptionalType(type.DateTimeType()),
        'message': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'resolution': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
    },
    Notification,
    False,
    None))



class PscReplicated(VapiStruct):
    """
    Configuration of the replicated Single Sign-On for PSC type deployment.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 sso_admin_password=None,
                 sso_domain_name=None,
                 partner_hostname=None,
                 ssl_verify=None,
                 ssl_thumbprint=None,
                 https_port=None,
                 sso_site_name=None,
                ):
        """
        :type  sso_admin_password: :class:`str`
        :param sso_admin_password: Administrator password of the PSC to be replicated.
        :type  sso_domain_name: :class:`str`
        :param sso_domain_name: Domain name of the remote PSC. For example, 'vsphere.local'
        :type  partner_hostname: :class:`str`
        :param partner_hostname: The IP address or DNS resolvable name of the remote PSC.
        :type  ssl_verify: :class:`bool` or ``None``
        :param ssl_verify: A flag to indicate whether the SSL verification is required.
            If ``sslThumbprint`` is provided, this field can be omitted If
            None, defaults to False
        :type  ssl_thumbprint: :class:`str` or ``None``
        :param ssl_thumbprint: SHA1 thumbprint of the server SSL certificate which will be used
            for verification.
            If ``sslVerify`` is set to False, this field can be omitted
        :type  https_port: :class:`long` or ``None``
        :param https_port: The HTTPS port of the remote PSC.
            If None, defaults to 443
        :type  sso_site_name: :class:`str` or ``None``
        :param sso_site_name: Site name of the newly deployed PSC.
            Site name may not be applicable
        """
        self.sso_admin_password = sso_admin_password
        self.sso_domain_name = sso_domain_name
        self.partner_hostname = partner_hostname
        self.ssl_verify = ssl_verify
        self.ssl_thumbprint = ssl_thumbprint
        self.https_port = https_port
        self.sso_site_name = sso_site_name
        VapiStruct.__init__(self)


PscReplicated._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.psc_replicated', {
        'sso_admin_password': type.SecretType(),
        'sso_domain_name': type.StringType(),
        'partner_hostname': type.StringType(),
        'ssl_verify': type.OptionalType(type.BooleanType()),
        'ssl_thumbprint': type.OptionalType(type.StringType()),
        'https_port': type.OptionalType(type.IntegerType()),
        'sso_site_name': type.OptionalType(type.StringType()),
    },
    PscReplicated,
    False,
    None))



class PscStandalone(VapiStruct):
    """
    Configuration of the standalone Single Sign-On for Embedded type
    deployment.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 sso_admin_password=None,
                 sso_domain_name=None,
                 sso_site_name=None,
                ):
        """
        :type  sso_admin_password: :class:`str`
        :param sso_admin_password: Password must conform to the following requirements: 1. At least 8
            characters. 2. No more than 20 characters. 3. At least 1 uppercase
            character. 4. At least 1 lowercase character. 5. At least 1 number.
            6. At least 1 special character (e.g., '!', '(', '\\\\@', etc.). 7.
            Only visible A-Z, a-z, 0-9 and punctuation (spaces are not allowed)
        :type  sso_domain_name: :class:`str`
        :param sso_domain_name: Domain name of the newly deployed PSC. For example, 'vsphere.local'
        :type  sso_site_name: :class:`str` or ``None``
        :param sso_site_name: Site name of the PSC.
            Site name may not be applicable
        """
        self.sso_admin_password = sso_admin_password
        self.sso_domain_name = sso_domain_name
        self.sso_site_name = sso_site_name
        VapiStruct.__init__(self)


PscStandalone._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.psc_standalone', {
        'sso_admin_password': type.SecretType(),
        'sso_domain_name': type.StringType(),
        'sso_site_name': type.OptionalType(type.StringType()),
    },
    PscStandalone,
    False,
    None))



class Result(VapiStruct):
    """
    Container of info, warning and error messages associated with a single
    task.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 info=None,
                 warnings=None,
                 errors=None,
                ):
        """
        :type  info: :class:`list` of :class:`Notification` or ``None``
        :param info: Info notification messages reported.
            Only :class:`set` if an info was reported by the task.
        :type  warnings: :class:`list` of :class:`Notification` or ``None``
        :param warnings: Warning notification messages reported.
            Only :class:`set` if an warning was reported by the task.
        :type  errors: :class:`list` of :class:`Notification` or ``None``
        :param errors: Error notification messages reported.
            Only :class:`set` if an error was reported by the task.
        """
        self.info = info
        self.warnings = warnings
        self.errors = errors
        VapiStruct.__init__(self)


Result._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.result', {
        'info': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Notification'))),
        'warnings': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Notification'))),
        'errors': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Notification'))),
    },
    Result,
    False,
    None))



class SourceVcWindows(VapiStruct):
    """
    Configuration of the source Windows VC.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 hostname=None,
                 username=None,
                 password=None,
                 ssl_verify=None,
                 ssl_thumbprint=None,
                ):
        """
        :type  hostname: :class:`str`
        :param hostname: The IP address or FQDN of the source Windows vCenter server to
            migrate. If an FQDN is provided, it must be resolvable from the
            machine that is running the installer.
        :type  username: :class:`str`
        :param username: Single Sign-On administrator user on the source Windows vCenter
            server. For example, administrator\\\\@vsphere.local. Important:
            The user must be administrator\\\\@your_domain_name.
        :type  password: :class:`str`
        :param password: The password of the Single Sign-On administrator on the source
            Windows vCenter server.
        :type  ssl_verify: :class:`bool` or ``None``
        :param ssl_verify: 
        :type  ssl_thumbprint: :class:`str` or ``None``
        :param ssl_thumbprint: 
        """
        self.hostname = hostname
        self.username = username
        self.password = password
        self.ssl_verify = ssl_verify
        self.ssl_thumbprint = ssl_thumbprint
        VapiStruct.__init__(self)


SourceVcWindows._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.source_vc_windows', {
        'hostname': type.StringType(),
        'username': type.StringType(),
        'password': type.SecretType(),
        'ssl_verify': type.OptionalType(type.BooleanType()),
        'ssl_thumbprint': type.OptionalType(type.StringType()),
    },
    SourceVcWindows,
    False,
    None))



class SourceVum(VapiStruct):
    """
    Configuration of the source VUM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 hostname=None,
                 os_username=None,
                 os_password=None,
                 export_dir=None,
                 port=None,
                 start_migration_assistant=None,
                 existing_migration_assistant=None,
                ):
        """
        :type  hostname: :class:`str`
        :param hostname: IP address or fully qualified domain name (FQDN) of the vSphere
            Update Manager host. If an FQDN is provided, it has to be
            resolvable from the machine that is running the installer.
        :type  os_username: :class:`str`
        :param os_username: Administrator username for the source vSphere Update Manager
            Windows operating system.
        :type  os_password: :class:`str`
        :param os_password: Administrator user password for the source vSphere Update Manager
            Windows operating system.
        :type  export_dir: :class:`str` or ``None``
        :param export_dir: Directory to export source configuration and data.
            If None, defaults to for mac/lin: /var/tmp, for windows: %TEMP%
        :type  port: :class:`long` or ``None``
        :param port: The port of the source vum.
            default to be 9123
        :type  start_migration_assistant: :class:`SourceVumMigrationAssistant` or ``None``
        :param start_migration_assistant: Configuration of migration assistant to be deployed to the vSphere
            Upgrade Manager.
            Mutually exclusive between start migration assistant and existing
            migration assistant.
        :type  existing_migration_assistant: :class:`ExistingMigrationAssistant` or ``None``
        :param existing_migration_assistant: Configuration of migration assistant that are already running on
            the vSphere Upgrade Manager.
        """
        self.hostname = hostname
        self.os_username = os_username
        self.os_password = os_password
        self.export_dir = export_dir
        self.port = port
        self.start_migration_assistant = start_migration_assistant
        self.existing_migration_assistant = existing_migration_assistant
        VapiStruct.__init__(self)


SourceVum._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.source_vum', {
        'hostname': type.StringType(),
        'os_username': type.StringType(),
        'os_password': type.SecretType(),
        'export_dir': type.OptionalType(type.StringType()),
        'port': type.OptionalType(type.IntegerType()),
        'start_migration_assistant': type.OptionalType(type.ReferenceType(__name__, 'SourceVumMigrationAssistant')),
        'existing_migration_assistant': type.OptionalType(type.ReferenceType(__name__, 'ExistingMigrationAssistant')),
    },
    SourceVum,
    False,
    None))



class SourceVumMigrationAssistant(VapiStruct):
    """
    Configuration of migration assistant to be deployed to the vSphere Upgrade
    Manager.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 installer_location=None,
                 installer_location_ssl_verify=None,
                 installer_location_ssl_thumbprint=None,
                ):
        """
        :type  installer_location: :class:`str` or ``None``
        :param installer_location: Location of the installer of migration assistant to be uploaded to
            the source vSphere Update Manager.
            Mutually exclusive between start migration assistant and existing
            migration assistant.
        :type  installer_location_ssl_verify: :class:`bool` or ``None``
        :param installer_location_ssl_verify: A flag to indicate whether to verify ssl connection of the location
            of the installer of migration assistant.
            when SSL thumbprint is provided, SSL verify is not required.
        :type  installer_location_ssl_thumbprint: :class:`str` or ``None``
        :param installer_location_ssl_thumbprint: SSL thumbprint of the location of the installer of migration
            assistant.
            if ssl verify is set to False, thumbprint is not required.
        """
        self.installer_location = installer_location
        self.installer_location_ssl_verify = installer_location_ssl_verify
        self.installer_location_ssl_thumbprint = installer_location_ssl_thumbprint
        VapiStruct.__init__(self)


SourceVumMigrationAssistant._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.source_vum_migration_assistant', {
        'installer_location': type.OptionalType(type.StringType()),
        'installer_location_ssl_verify': type.OptionalType(type.BooleanType()),
        'installer_location_ssl_thumbprint': type.OptionalType(type.StringType()),
    },
    SourceVumMigrationAssistant,
    False,
    None))



class Ssh(VapiStruct):
    """
    Setting to enable SSH on the deployed appliance.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 enabled=None,
                ):
        """
        :type  enabled: :class:`bool` or ``None``
        :param enabled: Whether to enable SSH.
            If None, defaults to False
        """
        self.enabled = enabled
        VapiStruct.__init__(self)


Ssh._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.ssh', {
        'enabled': type.OptionalType(type.BooleanType()),
    },
    Ssh,
    False,
    None))



class SubTaskInfo(VapiStruct):
    """
    Container that contains the status information about a single task.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'status',
            {
                'FAILED' : [('error', False), ('start_time', True), ('end_time', True)],
                'RUNNING' : [('start_time', True)],
                'BLOCKED' : [('start_time', True)],
                'SUCCEEDED' : [('start_time', True), ('end_time', True)],
                'PENDING' : [],
            }
        ),
    ]



    def __init__(self,
                 progress=None,
                 last_updated_time=None,
                 result=None,
                 external_tools=None,
                 description=None,
                 service=None,
                 operation=None,
                 parent=None,
                 target=None,
                 status=None,
                 cancelable=None,
                 error=None,
                 start_time=None,
                 end_time=None,
                 user=None,
                ):
        """
        :type  progress: :class:`com.vmware.cis.task_client.Progress`
        :param progress: The progress info of this deployment task.
        :type  last_updated_time: :class:`datetime.datetime`
        :param last_updated_time: The time that the last update is registered.
        :type  result: :class:`Result` or ``None``
        :param result: Result of the task.
            This attribute will be None if result is not available at the
            current step of the task.
        :type  external_tools: :class:`list` of :class:`ExternalTool`
        :param external_tools: External tools used for the deployment.
        :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param description: Description of the operation associated with the task.
        :type  service: :class:`str`
        :param service: Identifier of the service containing the operation.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vapi.service``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vapi.service``.
        :type  operation: :class:`str`
        :param operation: Identifier of the operation associated with the task.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vapi.operation``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vapi.operation``.
        :type  parent: :class:`str` or ``None``
        :param parent: Parent of the current task.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.cis.task``. When methods return a value of this class
            as a return value, the attribute will be an identifier for the
            resource type: ``com.vmware.cis.task``.
            This attribute will be None if the task has no parent.
        :type  target: :class:`com.vmware.vapi.std_client.DynamicID` or ``None``
        :param target: Identifier of the target created by the operation or an existing
            one the operation performed on.
            This attribute will be None if the operation has no target or
            multiple targets.
        :type  status: :class:`com.vmware.cis.task_client.Status`
        :param status: Status of the operation associated with the task.
        :type  cancelable: :class:`bool`
        :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
            value may change as the operation progresses.
        :type  error: :class:`Exception` or ``None``
        :param error: Description of the error if the operation status is "FAILED".
            If None the description of why the operation failed will be
            included in the result of the operation (see
            :attr:`com.vmware.cis.task_client.Info.result`).
        :type  start_time: :class:`datetime.datetime`
        :param start_time: Time when the operation is started.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of
            :attr:`com.vmware.cis.task_client.Status.RUNNING`,
            :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
            :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
            :attr:`com.vmware.cis.task_client.Status.FAILED`.
        :type  end_time: :class:`datetime.datetime`
        :param end_time: Time when the operation is completed.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of
            :attr:`com.vmware.cis.task_client.Status.SUCCEEDED` or
            :attr:`com.vmware.cis.task_client.Status.FAILED`.
        :type  user: :class:`str` or ``None``
        :param user: Name of the user who performed the operation.
            This attribute will be None if the operation is performed by the
            system.
        """
        self.progress = progress
        self.last_updated_time = last_updated_time
        self.result = result
        self.external_tools = external_tools
        self.description = description
        self.service = service
        self.operation = operation
        self.parent = parent
        self.target = target
        self.status = status
        self.cancelable = cancelable
        self.error = error
        self.start_time = start_time
        self.end_time = end_time
        self.user = user
        VapiStruct.__init__(self)


SubTaskInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.sub_task_info', {
        'progress': type.ReferenceType('com.vmware.cis.task_client', 'Progress'),
        'last_updated_time': type.DateTimeType(),
        'result': type.OptionalType(type.ReferenceType(__name__, 'Result')),
        'external_tools': type.ListType(type.ReferenceType(__name__, 'ExternalTool')),
        'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'service': type.IdType(resource_types='com.vmware.vapi.service'),
        'operation': type.IdType(resource_types='com.vmware.vapi.operation'),
        'parent': type.OptionalType(type.IdType()),
        'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        'status': type.ReferenceType('com.vmware.cis.task_client', 'Status'),
        'cancelable': type.BooleanType(),
        'error': type.OptionalType(type.AnyErrorType()),
        'start_time': type.OptionalType(type.DateTimeType()),
        'end_time': type.OptionalType(type.DateTimeType()),
        'user': type.OptionalType(type.StringType()),
    },
    SubTaskInfo,
    False,
    None))



class TaskInfo(VapiStruct):
    """
    The container that contains the status information of a deployment.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'status',
            {
                'RUNNING' : [('progress', True), ('start_time', True)],
                'FAILED' : [('progress', True), ('error', False), ('start_time', True), ('end_time', True)],
                'SUCCEEDED' : [('progress', True), ('start_time', True), ('end_time', True)],
                'BLOCKED' : [('progress', True), ('start_time', True)],
                'PENDING' : [],
            }
        ),
    ]



    def __init__(self,
                 metadata_file=None,
                 state=None,
                 progress=None,
                 last_updated_time=None,
                 subtask_order=None,
                 subtasks=None,
                 appliance_info=None,
                 result=None,
                 additional_info=None,
                 description=None,
                 service=None,
                 operation=None,
                 parent=None,
                 target=None,
                 status=None,
                 cancelable=None,
                 error=None,
                 start_time=None,
                 end_time=None,
                 user=None,
                ):
        """
        :type  metadata_file: :class:`str`
        :param metadata_file: The path of the metadata file.
        :type  state: :class:`str` or ``None``
        :param state: The state of appliance being deployed.
            May not have any state information.
        :type  progress: :class:`com.vmware.cis.task_client.Progress`
        :param progress: The total progress of the deployment operation.
            This attribute is optional and it is only relevant when the value
            of ``#status`` is one of
            :attr:`com.vmware.cis.task_client.Status.RUNNING`,
            :attr:`com.vmware.cis.task_client.Status.FAILED`,
            :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
            :attr:`com.vmware.cis.task_client.Status.BLOCKED`.
        :type  last_updated_time: :class:`datetime.datetime`
        :param last_updated_time: The time that the last update is registered.
        :type  subtask_order: :class:`list` of :class:`list` of :class:`str` or ``None``
        :param subtask_order: The ordered list of subtasks for this deployment operation.
            Only :class:`set` when the appliance state is RUNNING_IN_PROGRESS,
            FAILED, CANCELLED and SUCCEEDED.
        :type  subtasks: (:class:`dict` of :class:`str` and :class:`SubTaskInfo`) or ``None``
        :param subtasks: The map of the deployment subtasks and their status information.
            Only :class:`set` when the appliance state is RUNNING_IN_PROGRESS,
            FAILED, CANCELLED and SUCCEEDED.
        :type  appliance_info: :class:`DeploymentInfo` or ``None``
        :param appliance_info: Information about the appliance deployed.
            Such information may not be available for requests that are not for
            deployment (validation/recommendation).
        :type  result: :class:`DataValue` or ``None``
        :param result: The result of validation or recommendation requests.
            Not applicable for precheck/deployment operation.
        :type  additional_info: :class:`str` or ``None``
        :param additional_info: Additional information that a response may contain.
            Not all response will contain additional information.
        :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param description: Description of the operation associated with the task.
        :type  service: :class:`str`
        :param service: Identifier of the service containing the operation.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vapi.service``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vapi.service``.
        :type  operation: :class:`str`
        :param operation: Identifier of the operation associated with the task.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vapi.operation``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vapi.operation``.
        :type  parent: :class:`str` or ``None``
        :param parent: Parent of the current task.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.cis.task``. When methods return a value of this class
            as a return value, the attribute will be an identifier for the
            resource type: ``com.vmware.cis.task``.
            This attribute will be None if the task has no parent.
        :type  target: :class:`com.vmware.vapi.std_client.DynamicID` or ``None``
        :param target: Identifier of the target created by the operation or an existing
            one the operation performed on.
            This attribute will be None if the operation has no target or
            multiple targets.
        :type  status: :class:`com.vmware.cis.task_client.Status`
        :param status: Status of the operation associated with the task.
        :type  cancelable: :class:`bool`
        :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
            value may change as the operation progresses.
        :type  error: :class:`Exception` or ``None``
        :param error: Description of the error if the operation status is "FAILED".
            If None the description of why the operation failed will be
            included in the result of the operation (see
            :attr:`com.vmware.cis.task_client.Info.result`).
        :type  start_time: :class:`datetime.datetime`
        :param start_time: Time when the operation is started.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of
            :attr:`com.vmware.cis.task_client.Status.RUNNING`,
            :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
            :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
            :attr:`com.vmware.cis.task_client.Status.FAILED`.
        :type  end_time: :class:`datetime.datetime`
        :param end_time: Time when the operation is completed.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of
            :attr:`com.vmware.cis.task_client.Status.SUCCEEDED` or
            :attr:`com.vmware.cis.task_client.Status.FAILED`.
        :type  user: :class:`str` or ``None``
        :param user: Name of the user who performed the operation.
            This attribute will be None if the operation is performed by the
            system.
        """
        self.metadata_file = metadata_file
        self.state = state
        self.progress = progress
        self.last_updated_time = last_updated_time
        self.subtask_order = subtask_order
        self.subtasks = subtasks
        self.appliance_info = appliance_info
        self.result = result
        self.additional_info = additional_info
        self.description = description
        self.service = service
        self.operation = operation
        self.parent = parent
        self.target = target
        self.status = status
        self.cancelable = cancelable
        self.error = error
        self.start_time = start_time
        self.end_time = end_time
        self.user = user
        VapiStruct.__init__(self)


TaskInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.task_info', {
        'metadata_file': type.StringType(),
        'state': type.OptionalType(type.StringType()),
        'progress': type.OptionalType(type.ReferenceType('com.vmware.cis.task_client', 'Progress')),
        'last_updated_time': type.DateTimeType(),
        'subtask_order': type.OptionalType(type.ListType(type.ListType(type.StringType()))),
        'subtasks': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'SubTaskInfo'))),
        'appliance_info': type.OptionalType(type.ReferenceType(__name__, 'DeploymentInfo')),
        'result': type.OptionalType(type.OpaqueType()),
        'additional_info': type.OptionalType(type.StringType()),
        'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'service': type.IdType(resource_types='com.vmware.vapi.service'),
        'operation': type.IdType(resource_types='com.vmware.vapi.operation'),
        'parent': type.OptionalType(type.IdType()),
        'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        'status': type.ReferenceType('com.vmware.cis.task_client', 'Status'),
        'cancelable': type.BooleanType(),
        'error': type.OptionalType(type.AnyErrorType()),
        'start_time': type.OptionalType(type.DateTimeType()),
        'end_time': type.OptionalType(type.DateTimeType()),
        'user': type.OptionalType(type.StringType()),
    },
    TaskInfo,
    False,
    None))



class TemporaryNetwork(VapiStruct):
    """
    Configuration of the temporary network which is used during
    upgrade/migrate.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'mode',
            {
                'STATIC' : [('ip', True), ('dns_servers', True), ('prefix', True), ('gateway', True)],
                'DHCP' : [],
            }
        ),
    ]



    def __init__(self,
                 ip_family=None,
                 mode=None,
                 ip=None,
                 dns_servers=None,
                 prefix=None,
                 gateway=None,
                ):
        """
        :type  ip_family: :class:`TemporaryNetwork.IpType` or ``None``
        :param ip_family: Network IP address family.
            If None, defaults to IPV4
        :type  mode: :class:`TemporaryNetwork.NetworkMode`
        :param mode: Network mode.
        :type  ip: :class:`str`
        :param ip: Network IP address. Required for static mode only.
            This attribute is optional and it is only relevant when the value
            of ``mode`` is :attr:`TemporaryNetwork.NetworkMode.STATIC`.
        :type  dns_servers: :class:`list` of :class:`str`
        :param dns_servers: A comma-separated list of IP addresses of DNS servers. A JSON array
            such as ["1.2.3.4", "127.0.0.1"]. Required for static mode only.
            DNS servers must be reachable from the machine that runs CLI
            installer
            This attribute is optional and it is only relevant when the value
            of ``mode`` is :attr:`TemporaryNetwork.NetworkMode.STATIC`.
        :type  prefix: :class:`long`
        :param prefix: Network prefix length. Required for static mode only. Remove if the
            mode is "dhcp". This is the number of bits set in the subnet mask;
            for instance, if the subnet mask is 255.255.255.0, there are 24
            bits in the binary version of the subnet mask, so the prefix length
            is 24. If used, the values must be in the inclusive range of 0 to
            32 for IPv4 and 0 to 128 for IPv6. Required for static mode only.
            This attribute is optional and it is only relevant when the value
            of ``mode`` is :attr:`TemporaryNetwork.NetworkMode.STATIC`.
        :type  gateway: :class:`str`
        :param gateway: Gateway of the network. Required for static mode only.
            This attribute is optional and it is only relevant when the value
            of ``mode`` is :attr:`TemporaryNetwork.NetworkMode.STATIC`.
        """
        self.ip_family = ip_family
        self.mode = mode
        self.ip = ip
        self.dns_servers = dns_servers
        self.prefix = prefix
        self.gateway = gateway
        VapiStruct.__init__(self)


    class IpType(Enum):
        """
        Network IP address family.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        IPV4 = None
        """
        IPv4 Type of IP address.

        """
        IPV6 = None
        """
        IPv6 Type of IP address.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IpType` instance.
            """
            Enum.__init__(string)

    IpType._set_values([
        IpType('IPV4'),
        IpType('IPV6'),
    ])
    IpType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.lcm.temporary_network.ip_type',
        IpType))

    class NetworkMode(Enum):
        """
        Network mode.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        DHCP = None
        """
        DHCP mode.

        """
        STATIC = None
        """
        Static IP mode.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`NetworkMode` instance.
            """
            Enum.__init__(string)

    NetworkMode._set_values([
        NetworkMode('DHCP'),
        NetworkMode('STATIC'),
    ])
    NetworkMode._set_binding_type(type.EnumType(
        'com.vmware.vcenter.lcm.temporary_network.network_mode',
        NetworkMode))

TemporaryNetwork._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.temporary_network', {
        'ip_family': type.OptionalType(type.ReferenceType(__name__, 'TemporaryNetwork.IpType')),
        'mode': type.ReferenceType(__name__, 'TemporaryNetwork.NetworkMode'),
        'ip': type.OptionalType(type.StringType()),
        'dns_servers': type.OptionalType(type.ListType(type.StringType())),
        'prefix': type.OptionalType(type.IntegerType()),
        'gateway': type.OptionalType(type.StringType()),
    },
    TemporaryNetwork,
    False,
    None))



class Time(VapiStruct):
    """
    NTP setting of the appliance to be deployed.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 ntp_servers=None,
                ):
        """
        :type  ntp_servers: :class:`list` of :class:`str` or ``None``
        :param ntp_servers: To configure NTP time synchronization for the appliance, set the
            value to a comma - separated list of host names or IP addresses of
            Network Time Protocol(NTP) servers. If "ntp_servers" is not
            provided, the appliance clock will be synced to the ESX. For
            example: ["time.nist.gov"].
            Times tool sync will be enabled when ntp server is not provided. If
            None, defaults to []
        """
        self.ntp_servers = ntp_servers
        VapiStruct.__init__(self)


Time._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.time', {
        'ntp_servers': type.OptionalType(type.ListType(type.StringType())),
    },
    Time,
    False,
    None))



class UpgradeDestinationApplianceService(VapiStruct):
    """
    Configurable services of destination appliance for upgrade/migrate
    operation.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 ssh=None,
                ):
        """
        :type  ssh: :class:`Ssh`
        :param ssh: Whether to enable SSH on the vCenter Appliance.
        """
        self.ssh = ssh
        VapiStruct.__init__(self)


UpgradeDestinationApplianceService._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.upgrade_destination_appliance_service', {
        'ssh': type.ReferenceType(__name__, 'Ssh'),
    },
    UpgradeDestinationApplianceService,
    False,
    None))



class UpgradeSourceAppliance(VapiStruct):
    """
    Configuration of the source appliance to be upgraded/migrated.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 hostname=None,
                 sso_admin_username=None,
                 sso_admin_password=None,
                 root_password=None,
                 https_port=None,
                 ssl_verify=None,
                 ssl_thumbprint=None,
                 export_dir=None,
                ):
        """
        :type  hostname: :class:`str`
        :param hostname: The IP address or fully qualified domain name (FQDN) of the vCenter
            Server instance. If an FQDN is provided, it has to be resolvable
            from the machine that is running the installer.
        :type  sso_admin_username: :class:`str`
        :param sso_admin_username: vCenter Single Sign-On administrator user name of the source
            appliance.
        :type  sso_admin_password: :class:`str`
        :param sso_admin_password: vCenter Single Sign-On administrator password of the source
            appliance.
        :type  root_password: :class:`str`
        :param root_password: Password of the operating system root user of the appliance.
        :type  https_port: :class:`long` or ``None``
        :param https_port: The HTTPS port number to connect to the source appliance.
            If None, defaults to 443
        :type  ssl_verify: :class:`bool` or ``None``
        :param ssl_verify: 
        :type  ssl_thumbprint: :class:`str` or ``None``
        :param ssl_thumbprint: 
        :type  export_dir: :class:`str` or ``None``
        :param export_dir: Export directory of the source appliance.
            Default to be "/var/tmp/".
        """
        self.hostname = hostname
        self.sso_admin_username = sso_admin_username
        self.sso_admin_password = sso_admin_password
        self.root_password = root_password
        self.https_port = https_port
        self.ssl_verify = ssl_verify
        self.ssl_thumbprint = ssl_thumbprint
        self.export_dir = export_dir
        VapiStruct.__init__(self)


UpgradeSourceAppliance._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.upgrade_source_appliance', {
        'hostname': type.StringType(),
        'sso_admin_username': type.StringType(),
        'sso_admin_password': type.SecretType(),
        'root_password': type.SecretType(),
        'https_port': type.OptionalType(type.IntegerType()),
        'ssl_verify': type.OptionalType(type.BooleanType()),
        'ssl_thumbprint': type.OptionalType(type.StringType()),
        'export_dir': type.OptionalType(type.StringType()),
    },
    UpgradeSourceAppliance,
    False,
    None))



class Vc(VapiStruct):
    """
    Configuration of the VC that hosts/will host an appliance.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 connection=None,
                 inventory=None,
                ):
        """
        :type  connection: :class:`Connection`
        :param connection: The configuration to connect to an ESX/VC.
        :type  inventory: :class:`VcInventory`
        :param inventory: All names are case-sensitive. you can install the appliance to one
            of the following destinations: 1. A resource pool in a cluster, use
            'cluster_path'. 2. A specific ESX host in a cluster, use
            'host_path'. 3. A resource pool in a specific ESX host being
            managed by the current vCenter, use 'resource_pool_path'. You must
            always provide the 'network_name' key. To install a new appliance
            to a specific ESX host in a cluster, provide the 'host_path' key,
            and the 'datastore_name', e.g. 'host_path':
            '/MyDataCenter/host/MyCluster/10.20.30.40', 'datastore_name': 'Your
            Datastore'. To install a new appliance to a specific resource pool,
            provide the 'resource_pool_path', and the 'datastore_name', e.g.
            'resource_pool_path': '/Your Datacenter Folder/Your
            Datacenter/host/Your Cluster/Resources/Your Resource Pool',
            'datastore_name': 'Your Datastore'. To place a new appliance to a
            virtual machine Folder, provide the 'vm_folder_path', e.g.
            'vm_folder_path': 'VM Folder 0/VM Folder1'.
        """
        self.connection = connection
        self.inventory = inventory
        VapiStruct.__init__(self)


Vc._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.vc', {
        'connection': type.ReferenceType(__name__, 'Connection'),
        'inventory': type.ReferenceType(__name__, 'VcInventory'),
    },
    Vc,
    False,
    None))



class VcInventory(VapiStruct):
    """
    Inventory information about a VCenter.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 vm_folder_path=None,
                 resource_pool_path=None,
                 cluster_path=None,
                 host_path=None,
                 datastore_name=None,
                 datastore_cluster_name=None,
                 network_name=None,
                ):
        """
        :type  vm_folder_path: :class:`str` or ``None``
        :param vm_folder_path: Path of the VM folder. VM folder must be visible by the Data Center
            of the compute resourceFormat:{vm_folder1}/{vm_folder2}e.g.:'VM
            Folder 0/VM Folder1'.
            Mutually exclusive between ``#resource_pool_path``,
            ``#cluster_path``, and ``#host_path``
        :type  resource_pool_path: :class:`str` or ``None``
        :param resource_pool_path: Full path to resource pool. Format: /{datacenter
            folder}/{datacenter name}/host/{host
            name}/{cluster_name}/Resources/{resource pool}. e.g: Your
            Datacenter Folder/Your Datacenter/host/Your Cluster/Resources/Your
            Resource Pool
            Mutually exclusive between ``#resource_pool_path``,
            ``#cluster_path``, and ``#host_path``
        :type  cluster_path: :class:`str` or ``None``
        :param cluster_path: Full path to the cluster. Format: /{datacenter folder}/{datacenter
            name}/host/{cluster_name}. e.g: /Your Datacenter Folder/Your
            Datacenter/host/Your Cluster
            Mutually exclusive between ``#resource_pool_path``,
            ``#cluster_path``, and ``#host_path``
        :type  host_path: :class:`str` or ``None``
        :param host_path: 
        :type  datastore_name: :class:`str` or ``None``
        :param datastore_name: The datastore on which to store the files of the appliance. This
            value has to be either a specific datastore name, or a specific
            datastore in a datastore cluster. The datastore must be accessible
            from the ESX host and must have at least 25 GB of free space.
            Otherwise, the new appliance might not power on.
            Mutually exclusive between ``#datastore_name`` and
            ``#datastore_cluster_name``
        :type  datastore_cluster_name: :class:`str` or ``None``
        :param datastore_cluster_name: The datastore cluster on which to store the files of the appliance.
            Mutually exclusive between ``#datastore_name`` and
            ``#datastore_cluster_name``
        :type  network_name: :class:`str`
        :param network_name: Name of the network. e.g. VM Network
        """
        self.vm_folder_path = vm_folder_path
        self.resource_pool_path = resource_pool_path
        self.cluster_path = cluster_path
        self.host_path = host_path
        self.datastore_name = datastore_name
        self.datastore_cluster_name = datastore_cluster_name
        self.network_name = network_name
        VapiStruct.__init__(self)


VcInventory._set_binding_type(type.StructType(
    'com.vmware.vcenter.lcm.vc_inventory', {
        'vm_folder_path': type.OptionalType(type.StringType()),
        'resource_pool_path': type.OptionalType(type.StringType()),
        'cluster_path': type.OptionalType(type.StringType()),
        'host_path': type.OptionalType(type.StringType()),
        'datastore_name': type.OptionalType(type.StringType()),
        'datastore_cluster_name': type.OptionalType(type.StringType()),
        'network_name': type.StringType(),
    },
    VcInventory,
    False,
    None))



class Install(VapiInterface):
    """
    The service to install Embedded VCSA, PSC, Management VCSA, VMC gateway.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.lcm.install'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InstallStub)

    class Psc(VapiStruct):
        """
        Spec used to configure a Platform Services Controller. This section
        describes how the Platform Services Controller appliance should be
        configured. If unset, either ``#vcsaEmbedded`` or ``#vcsaExternal`` must be
        provided.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     standalone=None,
                     replicated=None,
                     ceip_enabled=None,
                    ):
            """
            :type  standalone: :class:`PscStandalone` or ``None``
            :param standalone: Spec used to configure a standalone Platform Services Controller.
                This section describes how the standalone PSC should be configured.
                Mutually exclusive between ``standalone`` and ``replicated``
            :type  replicated: :class:`PscReplicated` or ``None``
            :param replicated: Spec used to configure a replicated Platform Services Controller.
                This section describes how the replicated PSC should be configured.
                Mutually exclusive between ``standalone`` and ``replicated``
            :type  ceip_enabled: :class:`bool`
            :param ceip_enabled: This key describes the enabling option for the VMware's Customer
                Experience Improvement Program (CEIP). By default we have
                ``ceipEnabled``: true, which indicates that you are joining CEIP.
                If you prefer not to participate in the VMware's CEIP for this
                product, you must disable CEIP by setting ``ceipEnabled``: false.
                You may join or leave VMware's CEIP for this product at any time.
            """
            self.standalone = standalone
            self.replicated = replicated
            self.ceip_enabled = ceip_enabled
            VapiStruct.__init__(self)


    Psc._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.install.psc', {
            'standalone': type.OptionalType(type.ReferenceType(__name__, 'PscStandalone')),
            'replicated': type.OptionalType(type.ReferenceType(__name__, 'PscReplicated')),
            'ceip_enabled': type.BooleanType(),
        },
        Psc,
        False,
        None))


    class VcsaEmbedded(VapiStruct):
        """
        Spec used to configure an embedded vCenter Server. This field describes how
        the embedded vCenter Server appliance should be configured.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     standalone=None,
                     replicated=None,
                     ceip_enabled=None,
                    ):
            """
            :type  standalone: :class:`EmbeddedStandaloneVcsa` or ``None``
            :param standalone: Spec used to configure a standalone embedded vCenter Server. This
                field describes how the standalone vCenter Server appliance should
                be configured.
                Mutually exclusive between ``standalone`` and ``replicated``
            :type  replicated: :class:`EmbeddedReplicatedVcsa` or ``None``
            :param replicated: Spec used to configure a replicated embedded vCenter Server. This
                field describes how the replicated vCenter Server appliance should
                be configured.
                Mutually exclusive between ``standalone`` and ``replicated``
            :type  ceip_enabled: :class:`bool`
            :param ceip_enabled: This key describes the enabling option for the VMware's Customer
                Experience Improvement Program (CEIP). By default we have
                ``ceipEnabled``: true, which indicates that you are joining CEIP.
                If you prefer not to participate in the VMware's CEIP for this
                product, you must disable CEIP by setting ``ceipEnabled``: false.
                You may join or leave VMware's CEIP for this product at any time.
            """
            self.standalone = standalone
            self.replicated = replicated
            self.ceip_enabled = ceip_enabled
            VapiStruct.__init__(self)


    VcsaEmbedded._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.install.vcsa_embedded', {
            'standalone': type.OptionalType(type.ReferenceType(__name__, 'EmbeddedStandaloneVcsa')),
            'replicated': type.OptionalType(type.ReferenceType(__name__, 'EmbeddedReplicatedVcsa')),
            'ceip_enabled': type.BooleanType(),
        },
        VcsaEmbedded,
        False,
        None))


    class ReverseProxy(VapiStruct):
        """
        Port numbers on which the vCenter Server Appliance communicates with the
        other vSphere components.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     http_port=None,
                     https_port=None,
                    ):
            """
            :type  http_port: :class:`long` or ``None``
            :param http_port: Reverse proxy http port.
                If None, defaults to 8080
            :type  https_port: :class:`long` or ``None``
            :param https_port: Reverse proxy https port.
                If None, defaults to 8443
            """
            self.http_port = http_port
            self.https_port = https_port
            VapiStruct.__init__(self)


    ReverseProxy._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.install.reverse_proxy', {
            'http_port': type.OptionalType(type.IntegerType()),
            'https_port': type.OptionalType(type.IntegerType()),
        },
        ReverseProxy,
        False,
        None))


    class DestinationApplianceService(VapiStruct):
        """
        The configuration of vCenter services.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     rhttpproxy=None,
                     ssh=None,
                    ):
            """
            :type  rhttpproxy: :class:`Install.ReverseProxy` or ``None``
            :param rhttpproxy: Port numbers on which the vCenter Server Appliance communicates
                with the other vSphere components.
                Default value used reverse proxy not provided
            :type  ssh: :class:`Ssh`
            :param ssh: Whether to enable SSH on the vCenter Appliance.
            """
            self.rhttpproxy = rhttpproxy
            self.ssh = ssh
            VapiStruct.__init__(self)


    DestinationApplianceService._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.install.destination_appliance_service', {
            'rhttpproxy': type.OptionalType(type.ReferenceType(__name__, 'Install.ReverseProxy')),
            'ssh': type.ReferenceType(__name__, 'Ssh'),
        },
        DestinationApplianceService,
        False,
        None))


    class DestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'appliance_type',
                {
                    'VCSA_EMBEDDED' : [('appliance_size', False), ('appliance_disk_size', False), ('vcsa_embedded', True)],
                    'VCSA_EXTERNAL' : [('appliance_size', False), ('appliance_disk_size', False), ('vcsa_external', True)],
                    'PSC' : [('psc', True)],
                    'VMC' : [('vmc', True)],
                }
            ),
        ]



        def __init__(self,
                     appliance_name=None,
                     appliance_type=None,
                     appliance_size=None,
                     appliance_disk_size=None,
                     root_password=None,
                     thin_disk_mode=None,
                     ova_location=None,
                     ova_location_ssl_verify=None,
                     ova_location_ssl_thumbprint=None,
                     ovftool_location=None,
                     ovftool_location_ssl_verify=None,
                     ovftool_location_ssl_thumbprint=None,
                     services=None,
                     network=None,
                     time=None,
                     ovftool_arguments=None,
                     vcsa_embedded=None,
                     psc=None,
                     vcsa_external=None,
                     vmc=None,
                    ):
            """
            :type  appliance_name: :class:`str`
            :param appliance_name: The name of the appliance to deploy.
            :type  appliance_type: :class:`ApplianceType`
            :param appliance_type: The type of appliance to deploy.
            :type  appliance_size: :class:`ApplianceSize` or ``None``
            :param appliance_size: A size descriptor based on the number of virtual machines which
                will be managed by the new vCenter appliance.
                If None, defaults to SMALL
            :type  appliance_disk_size: :class:`StorageSize` or ``None``
            :param appliance_disk_size: The disk size of the new vCenter appliance.
                If None, defaults to REGULAR
            :type  root_password: :class:`str`
            :param root_password: Password must conform to the following requirements: 1. At least 8
                characters. 2. No more than 20 characters. 3. At least 1 uppercase
                character. 4. At least 1 lowercase character. 5. At least 1 number.
                6. At least 1 special character (e.g., '!', '(', '\\\\@', etc.). 7.
                Only visible A-Z, a-z, 0-9 and punctuation (spaces are not allowed)
            :type  thin_disk_mode: :class:`bool`
            :param thin_disk_mode: Whether to deploy the appliance with thin mode virtual disks.
            :type  ova_location: :class:`str`
            :param ova_location: The location of the OVA file.
            :type  ova_location_ssl_verify: :class:`bool` or ``None``
            :param ova_location_ssl_verify: A flag to indicate whether the ssl verification is required.
                If ``ovaLocationSslThumbprint`` is provided, this field can be
                omitted If None, defaults to True
            :type  ova_location_ssl_thumbprint: :class:`str` or ``None``
            :param ova_location_ssl_thumbprint: SSL thumbprint of ssl verification. If provided, ssl_verify can be
                omitted or set to true. If omitted, ssl_verify must be false. If
                omitted and ssl_verify is true, an error will occur.
                If ova_location_ssl_verify is False, this field can be omitted
            :type  ovftool_location: :class:`str`
            :param ovftool_location: The location of the OVF Tool.
            :type  ovftool_location_ssl_verify: :class:`bool` or ``None``
            :param ovftool_location_ssl_verify: Flag to indicate whether or not to verify the SSL thumbprint of OVF
                Tool location.
                if None, Default to be True.
            :type  ovftool_location_ssl_thumbprint: :class:`str` or ``None``
            :param ovftool_location_ssl_thumbprint: SSL thumbprint of OVF Tool location to be verified.
                When ovftoolLocationSslVerify is set to False, this field can be
                omitted.
            :type  services: :class:`Install.DestinationApplianceService`
            :param services: The configuration of vCenter services.
            :type  network: :class:`Network`
            :param network: The network settings of the appliance to be deployed.
            :type  time: :class:`Time`
            :param time: Configuration of the vCSA time synchronization.
            :type  ovftool_arguments: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
            :param ovftool_arguments: The OVF Tool arguments to be included.
                Not required when no OVF Tool argument to pass through
            :type  vcsa_embedded: :class:`Install.VcsaEmbedded`
            :param vcsa_embedded: Spec used to configure an embedded vCenter Server. This field
                describes how the embedded vCenter Server appliance should be
                configured.
                This attribute is optional and it is only relevant when the value
                of ``applianceType`` is :attr:`ApplianceType.VCSA_EMBEDDED`.
            :type  psc: :class:`Install.Psc`
            :param psc: Spec used to configure a Platform Services Controller. This section
                describes how the Platform Services Controller appliance should be
                configured. If unset, either ``vcsaEmbedded`` or ``vcsaExternal``
                must be provided.
                This attribute is optional and it is only relevant when the value
                of ``applianceType`` is :attr:`ApplianceType.PSC`.
            :type  vcsa_external: :class:`ExternalVcsa`
            :param vcsa_external: Spec used to configure a vCenter Server registered with an external
                PSC. If unset, either vcsa_embedded or psc must be provided.
                This attribute is optional and it is only relevant when the value
                of ``applianceType`` is :attr:`ApplianceType.VCSA_EXTERNAL`.
            :type  vmc: :class:`ExternalVcsa`
            :param vmc: Spec used to configure a vCenter Server registered with an external
                PSC. If unset, either vcsa_embedded or psc must be provided.
                This attribute is optional and it is only relevant when the value
                of ``applianceType`` is :attr:`ApplianceType.VMC`.
            """
            self.appliance_name = appliance_name
            self.appliance_type = appliance_type
            self.appliance_size = appliance_size
            self.appliance_disk_size = appliance_disk_size
            self.root_password = root_password
            self.thin_disk_mode = thin_disk_mode
            self.ova_location = ova_location
            self.ova_location_ssl_verify = ova_location_ssl_verify
            self.ova_location_ssl_thumbprint = ova_location_ssl_thumbprint
            self.ovftool_location = ovftool_location
            self.ovftool_location_ssl_verify = ovftool_location_ssl_verify
            self.ovftool_location_ssl_thumbprint = ovftool_location_ssl_thumbprint
            self.services = services
            self.network = network
            self.time = time
            self.ovftool_arguments = ovftool_arguments
            self.vcsa_embedded = vcsa_embedded
            self.psc = psc
            self.vcsa_external = vcsa_external
            self.vmc = vmc
            VapiStruct.__init__(self)


    DestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.install.destination_appliance', {
            'appliance_name': type.StringType(),
            'appliance_type': type.ReferenceType(__name__, 'ApplianceType'),
            'appliance_size': type.OptionalType(type.ReferenceType(__name__, 'ApplianceSize')),
            'appliance_disk_size': type.OptionalType(type.ReferenceType(__name__, 'StorageSize')),
            'root_password': type.SecretType(),
            'thin_disk_mode': type.BooleanType(),
            'ova_location': type.StringType(),
            'ova_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ova_location_ssl_thumbprint': type.OptionalType(type.StringType()),
            'ovftool_location': type.StringType(),
            'ovftool_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ovftool_location_ssl_thumbprint': type.OptionalType(type.StringType()),
            'services': type.ReferenceType(__name__, 'Install.DestinationApplianceService'),
            'network': type.ReferenceType(__name__, 'Network'),
            'time': type.ReferenceType(__name__, 'Time'),
            'ovftool_arguments': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
            'vcsa_embedded': type.OptionalType(type.ReferenceType(__name__, 'Install.VcsaEmbedded')),
            'psc': type.OptionalType(type.ReferenceType(__name__, 'Install.Psc')),
            'vcsa_external': type.OptionalType(type.ReferenceType(__name__, 'ExternalVcsa')),
            'vmc': type.OptionalType(type.ReferenceType(__name__, 'ExternalVcsa')),
        },
        DestinationAppliance,
        False,
        None))


    class Spec(VapiStruct):
        """


        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_location=None,
                     destination_appliance=None,
                    ):
            """
            :type  destination_location: :class:`DestinationLocation`
            :param destination_location: This subsection describes the ESX or VC on which to deploy the
                appliance.
            :type  destination_appliance: :class:`Install.DestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            """
            self.destination_location = destination_location
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    Spec._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.install.spec', {
            'destination_location': type.ReferenceType(__name__, 'DestinationLocation'),
            'destination_appliance': type.ReferenceType(__name__, 'Install.DestinationAppliance'),
        },
        Spec,
        False,
        None))




    def check_task(self,
              spec,
              options=None,
              ):
        """
        Performs a precheck for the given specification. The result of this
        operation can be queried by calling the cis/tasks/{task-id} with the
        task-id in the response of this call.

        :type  spec: :class:`Install.Spec`
        :param spec:  The specification of the deployment.
        :type  options: :class:`DeploymentOption` or ``None``
        :param options:  The deployment precheck options.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             If the given spec and/or option contains error.
        """
        task_id = self._invoke('check$task',
                                {
                                'spec': spec,
                                'options': options,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance


    def start_task(self,
              spec,
              ):
        """
        Deploys the appliance for the given specification. The result of this
        operation can be queried by calling the cis/tasks/{task-id} with the
        task-id in the response of this call.

        :type  spec: :class:`Install.Spec`
        :param spec:  The specification of the deployment.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             If the given specification contains error.
        """
        task_id = self._invoke('start$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance
class Log(VapiInterface):
    """
    The service that provides logs associated with a task of a given task ID.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.lcm.log'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LogStub)


    def get(self,
            task_id,
            ):
        """
        Retrieves the zipped files that contains operation log, serialized task
        flow, record of all configuration, and a current status of the
        operation.

        :type  task_id: :class:`str`
        :param task_id: The :class:`vmodl.lang_client.ID` of the operation. must exist in
            the server. If for any reason the server reboots during an
            operation, all :class:`vmodl.lang_client.ID`s previously stored is
            lost.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.task``.
        :rtype: :class:`str`
        :return: A zipped file that contains the files mentioned above.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the given ID does not exist in the server. There might be a
            cause of task ID does not exist including, error in taskID, or log
            files been purged by system or manually.
        """
        return self._invoke('get',
                            {
                            'task_id': task_id,
                            })
class Migrate(VapiInterface):
    """
    The service to migrate a windows VC to Embedded VCSA, PSC, and Management
    VCSA.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.lcm.migrate'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MigrateStub)

    class MigrateDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'appliance_type',
                {
                    'VCSA_EMBEDDED' : [('appliance_size', False), ('appliance_disk_size', False), ('vcsa_embedded', True)],
                    'VCSA_EXTERNAL' : [('appliance_size', False), ('appliance_disk_size', False)],
                    'PSC' : [('psc', True)],
                    'VMC' : [],
                }
            ),
        ]



        def __init__(self,
                     appliance_name=None,
                     appliance_type=None,
                     appliance_size=None,
                     appliance_disk_size=None,
                     root_password=None,
                     thin_disk_mode=None,
                     ova_location=None,
                     ova_location_ssl_verify=None,
                     ova_location_ssl_thumbprint=None,
                     ovftool_location=None,
                     ovftool_location_ssl_verify=None,
                     ovftool_location_ssl_thumbprint=None,
                     active_directory_domain=None,
                     active_directory_username=None,
                     active_directory_password=None,
                     services=None,
                     temporary_network=None,
                     history=None,
                     ovftool_arguments=None,
                     vcsa_embedded=None,
                     psc=None,
                    ):
            """
            :type  appliance_name: :class:`str`
            :param appliance_name: The name of the appliance to deploy.
            :type  appliance_type: :class:`ApplianceType` or ``None``
            :param appliance_type: The type of appliance to deploy.
                If None, defaults to VCSA_EMBEDDED
            :type  appliance_size: :class:`ApplianceSize` or ``None``
            :param appliance_size: A size descriptor based on the number of virtual machines which
                will be managed by the new vCenter appliance.
                If None, defaults to SMALL
            :type  appliance_disk_size: :class:`StorageSize` or ``None``
            :param appliance_disk_size: The disk size of the new vCenter appliance.
                If None, defaults to REGULAR
            :type  root_password: :class:`str`
            :param root_password: Password must conform to the following requirements: 1. At least 8
                characters. 2. No more than 20 characters. 3. At least 1 uppercase
                character. 4. At least 1 lowercase character. 5. At least 1 number.
                6. At least 1 special character (e.g., '!', '(', '\\\\@', etc.). 7.
                Only visible A-Z, a-z, 0-9 and punctuation (spaces are not allowed)
            :type  thin_disk_mode: :class:`bool`
            :param thin_disk_mode: Whether to deploy the appliance with thin mode virtual disks.
            :type  ova_location: :class:`str`
            :param ova_location: The location of the OVA file.
            :type  ova_location_ssl_verify: :class:`bool` or ``None``
            :param ova_location_ssl_verify: A flag to indicate whether the ssl verification is required.
                If ``ovaLocationSslThumbprint`` is provided, this field can be
                omitted If None, defaults to True
            :type  ova_location_ssl_thumbprint: :class:`str` or ``None``
            :param ova_location_ssl_thumbprint: SSL thumbprint of ssl verification. If provided, ssl_verify can be
                omitted or set to true. If omitted, ssl_verify must be false. If
                omitted and ssl_verify is true, an error will occur.
                If ova_location_ssl_verify is False, this field can be omitted
            :type  ovftool_location: :class:`str`
            :param ovftool_location: The location of the OVF Tool.
            :type  ovftool_location_ssl_verify: :class:`bool` or ``None``
            :param ovftool_location_ssl_verify: Flag to indicate whether or not to verify the SSL thumbprint of OVF
                Tool location.
                if None, Default to be True.
            :type  ovftool_location_ssl_thumbprint: :class:`str` or ``None``
            :param ovftool_location_ssl_thumbprint: SSL thumbprint of OVF Tool location to be verified.
                When ovftoolLocationSslVerify is set to False, this field can be
                omitted.
            :type  active_directory_domain: :class:`str` or ``None``
            :param active_directory_domain: The name of the Active Directory domain to which the source Windows
                installation is joined. If the source Windows installation is not
                joined to an Active Directory domain, omit this parameter.
                Not required when active directory is not applicable
            :type  active_directory_username: :class:`str` or ``None``
            :param active_directory_username: Administrator user name of the Active Directory domain to which the
                source Windows installation is joined. The format can be either
                'username' or 'username\\\\@domain'
                Not required when active directory is not applicable
            :type  active_directory_password: :class:`str` or ``None``
            :param active_directory_password: Password for the active directory user.
                Not required when active directory is not applicable
            :type  services: :class:`UpgradeDestinationApplianceService`
            :param services: Spec to configure vCenter server services.
            :type  temporary_network: :class:`TemporaryNetwork`
            :param temporary_network: The network settings of the appliance to be deployed.
            :type  history: :class:`History` or ``None``
            :param history: History data to be included in the upgrade and migrate
                Default value will be applied when absent
            :type  ovftool_arguments: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
            :param ovftool_arguments: The OVF Tool arguments to be included.
                Not required when no OVF Tool argument to pass through
            :type  vcsa_embedded: :class:`CeipOnlySso`
            :param vcsa_embedded: Spec used to configure an embedded vCenter Server. This field
                describes how the embedded vCenter Server appliance should be
                configured.
                This attribute is optional and it is only relevant when the value
                of ``applianceType`` is :attr:`ApplianceType.VCSA_EMBEDDED`.
            :type  psc: :class:`CeipOnlySso`
            :param psc: Spec used to configure a Platform Services Controller. This section
                describes how the Platform Services Controller appliance should be
                configured. If unset, either ``vcsaEmbedded`` or ``#vcsaExternal``
                must be provided.
                This attribute is optional and it is only relevant when the value
                of ``applianceType`` is :attr:`ApplianceType.PSC`.
            """
            self.appliance_name = appliance_name
            self.appliance_type = appliance_type
            self.appliance_size = appliance_size
            self.appliance_disk_size = appliance_disk_size
            self.root_password = root_password
            self.thin_disk_mode = thin_disk_mode
            self.ova_location = ova_location
            self.ova_location_ssl_verify = ova_location_ssl_verify
            self.ova_location_ssl_thumbprint = ova_location_ssl_thumbprint
            self.ovftool_location = ovftool_location
            self.ovftool_location_ssl_verify = ovftool_location_ssl_verify
            self.ovftool_location_ssl_thumbprint = ovftool_location_ssl_thumbprint
            self.active_directory_domain = active_directory_domain
            self.active_directory_username = active_directory_username
            self.active_directory_password = active_directory_password
            self.services = services
            self.temporary_network = temporary_network
            self.history = history
            self.ovftool_arguments = ovftool_arguments
            self.vcsa_embedded = vcsa_embedded
            self.psc = psc
            VapiStruct.__init__(self)


    MigrateDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.migrate.migrate_destination_appliance', {
            'appliance_name': type.StringType(),
            'appliance_type': type.OptionalType(type.ReferenceType(__name__, 'ApplianceType')),
            'appliance_size': type.OptionalType(type.ReferenceType(__name__, 'ApplianceSize')),
            'appliance_disk_size': type.OptionalType(type.ReferenceType(__name__, 'StorageSize')),
            'root_password': type.SecretType(),
            'thin_disk_mode': type.BooleanType(),
            'ova_location': type.StringType(),
            'ova_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ova_location_ssl_thumbprint': type.OptionalType(type.StringType()),
            'ovftool_location': type.StringType(),
            'ovftool_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ovftool_location_ssl_thumbprint': type.OptionalType(type.StringType()),
            'active_directory_domain': type.OptionalType(type.StringType()),
            'active_directory_username': type.OptionalType(type.StringType()),
            'active_directory_password': type.OptionalType(type.SecretType()),
            'services': type.ReferenceType(__name__, 'UpgradeDestinationApplianceService'),
            'temporary_network': type.ReferenceType(__name__, 'TemporaryNetwork'),
            'history': type.OptionalType(type.ReferenceType(__name__, 'History')),
            'ovftool_arguments': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
            'vcsa_embedded': type.OptionalType(type.ReferenceType(__name__, 'CeipOnlySso')),
            'psc': type.OptionalType(type.ReferenceType(__name__, 'CeipOnlySso')),
        },
        MigrateDestinationAppliance,
        False,
        None))


    class Spec(VapiStruct):
        """
        Spec to describe the configuration parameters that are required for
        migrating a Windows vCenter Server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_location=None,
                     destination_appliance=None,
                     source_vc_windows=None,
                     existing_migration_assistant=None,
                     start_migration_assistant=None,
                     source_vum_location=None,
                     source_vum=None,
                    ):
            """
            :type  destination_location: :class:`DestinationLocation`
            :param destination_location: This subsection describes the ESX or VC on which to deploy the
                appliance.
            :type  destination_appliance: :class:`Migrate.MigrateDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            :type  source_vc_windows: :class:`SourceVcWindows`
            :param source_vc_windows: Spec to describe the existing Windows vCenter server to migrate.
            :type  existing_migration_assistant: :class:`ExistingMigrationAssistant` or ``None``
            :param existing_migration_assistant: Spec to describe the attributes of a running Migration Assistant on
                the Windows vCenter server.
                Only applicable when migration assistant is already running on the
                source appliance
            :type  start_migration_assistant: :class:`MigrationAssistant` or ``None``
            :param start_migration_assistant: Spec to automate the invocation of Migration Assistant. Automatic
                invocation works only if the source Windows installation is running
                as a virtual machine.
                Only applicable when migration assistant is not running on the
                source appliance.
            :type  source_vum_location: :class:`Connection` or ``None``
            :param source_vum_location: The configuration to connect to an ESX/VC.
            :type  source_vum: :class:`SourceVum` or ``None``
            :param source_vum: This section describes the source vSphere Update Manager (VUM)
                which you want to upgrade.
                Not applicable for appliance not having source vSphere Update
                Manager
            """
            self.destination_location = destination_location
            self.destination_appliance = destination_appliance
            self.source_vc_windows = source_vc_windows
            self.existing_migration_assistant = existing_migration_assistant
            self.start_migration_assistant = start_migration_assistant
            self.source_vum_location = source_vum_location
            self.source_vum = source_vum
            VapiStruct.__init__(self)


    Spec._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.migrate.spec', {
            'destination_location': type.ReferenceType(__name__, 'DestinationLocation'),
            'destination_appliance': type.ReferenceType(__name__, 'Migrate.MigrateDestinationAppliance'),
            'source_vc_windows': type.ReferenceType(__name__, 'SourceVcWindows'),
            'existing_migration_assistant': type.OptionalType(type.ReferenceType(__name__, 'ExistingMigrationAssistant')),
            'start_migration_assistant': type.OptionalType(type.ReferenceType(__name__, 'MigrationAssistant')),
            'source_vum_location': type.OptionalType(type.ReferenceType(__name__, 'Connection')),
            'source_vum': type.OptionalType(type.ReferenceType(__name__, 'SourceVum')),
        },
        Spec,
        False,
        None))




    def check_task(self,
              spec,
              options=None,
              ):
        """
        Performs a precheck for the given specification. The result of this
        operation can be queried by calling the cis/tasks/{task-id} with the
        task-id in the response of this call.

        :type  spec: :class:`Migrate.Spec`
        :param spec:  The specification of the deployment.
        :type  options: :class:`DeploymentOption` or ``None``
        :param options:  The deployment precheck options.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             If the given spec and/or option contains error.
        """
        task_id = self._invoke('check$task',
                                {
                                'spec': spec,
                                'options': options,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance


    def start_task(self,
              spec,
              ):
        """
        Deploys the appliance for the given specification. The result of this
        operation can be queried by calling the cis/tasks/{task-id} with the
        task-id in the response of this call.

        :type  spec: :class:`Migrate.Spec`
        :param spec:  The specification of the deployment.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             If the given specification contains error.
        """
        task_id = self._invoke('start$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance
class Recommendation(VapiInterface):
    """
    The service that provide recommendation.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.lcm.recommendation'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RecommendationStub)

    class DeploymentSizeDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     ova_location=None,
                     ova_location_ssl_verify=None,
                     ova_location_ssl_thumbprint=None,
                    ):
            """
            :type  ova_location: :class:`str` or ``None``
            :param ova_location: The location of the ova file.
                Not required.
            :type  ova_location_ssl_verify: :class:`bool` or ``None``
            :param ova_location_ssl_verify: A flag to indicate whether the ssl verification is required.
                If ``ovaLocationSslThumbprint`` is provided, this field can be
                omitted If None, defaults to True
            :type  ova_location_ssl_thumbprint: :class:`str` or ``None``
            :param ova_location_ssl_thumbprint: SSL thumbprint of ssl verification. If provided, ssl_verify can be
                omitted or set to true. If omitted, ssl_verify must be false. If
                omitted and ssl_verify is true, an error will occur.
                If ova_location_ssl_verify is False, this field can be omitted
            """
            self.ova_location = ova_location
            self.ova_location_ssl_verify = ova_location_ssl_verify
            self.ova_location_ssl_thumbprint = ova_location_ssl_thumbprint
            VapiStruct.__init__(self)


    DeploymentSizeDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.deployment_size_destination_appliance', {
            'ova_location': type.OptionalType(type.StringType()),
            'ova_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ova_location_ssl_thumbprint': type.OptionalType(type.StringType()),
        },
        DeploymentSizeDestinationAppliance,
        False,
        None))


    class MigrateDeploymentSizeRequest(VapiStruct):
        """
        The request for recommending migrate deployment size.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                     source_vc_windows=None,
                     existing_migration_assistant=None,
                     start_migration_assistant=None,
                     source_vum_location=None,
                     source_vum=None,
                    ):
            """
            :type  destination_appliance: :class:`Recommendation.DeploymentSizeDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            :type  source_vc_windows: :class:`SourceVcWindows`
            :param source_vc_windows: Spec to describe the existing Windows vCenter server to migrate.
            :type  existing_migration_assistant: :class:`ExistingMigrationAssistant` or ``None``
            :param existing_migration_assistant: Spec to describe the attributes of a running Migration Assistant on
                the Windows vCenter server.
                Only applicable when migration assistant is already running on the
                source appliance
            :type  start_migration_assistant: :class:`MigrationAssistant` or ``None``
            :param start_migration_assistant: Spec to automate the invocation of Migration Assistant. Automatic
                invocation works only if the source Windows installation is running
                as a virtual machine.
                Only applicable when migration assistant is not running on the
                source appliance.
            :type  source_vum_location: :class:`Connection` or ``None``
            :param source_vum_location: The configuration to connect to an ESX/VC.
            :type  source_vum: :class:`SourceVum` or ``None``
            :param source_vum: This section describes the source vSphere Update Manager (VUM)
                which you want to upgrade.
                Not applicable for appliance not having source vSphere Update
                Manager
            """
            self.destination_appliance = destination_appliance
            self.source_vc_windows = source_vc_windows
            self.existing_migration_assistant = existing_migration_assistant
            self.start_migration_assistant = start_migration_assistant
            self.source_vum_location = source_vum_location
            self.source_vum = source_vum
            VapiStruct.__init__(self)


    MigrateDeploymentSizeRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.migrate_deployment_size_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Recommendation.DeploymentSizeDestinationAppliance'),
            'source_vc_windows': type.ReferenceType(__name__, 'SourceVcWindows'),
            'existing_migration_assistant': type.OptionalType(type.ReferenceType(__name__, 'ExistingMigrationAssistant')),
            'start_migration_assistant': type.OptionalType(type.ReferenceType(__name__, 'MigrationAssistant')),
            'source_vum_location': type.OptionalType(type.ReferenceType(__name__, 'Connection')),
            'source_vum': type.OptionalType(type.ReferenceType(__name__, 'SourceVum')),
        },
        MigrateDeploymentSizeRequest,
        False,
        None))


    class UpgradeDeploymentSizeRequest(VapiStruct):
        """
        The request for recommending upgrade deployment size.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                     source_location=None,
                     source_appliance=None,
                     source_vum=None,
                     source_vum_location=None,
                    ):
            """
            :type  destination_appliance: :class:`Recommendation.DeploymentSizeDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance
            :type  source_location: :class:`Connection`
            :param source_location: The configuration to connect to an ESX/VC.
            :type  source_appliance: :class:`UpgradeSourceAppliance`
            :param source_appliance: Spec to describe the existing appliance to upgrade.
            :type  source_vum: :class:`SourceVum` or ``None``
            :param source_vum: This section describes the source vSphere Update Manager (VUM)
                which you want to upgrade.
                Not applicable for appliance not having source vSphere Update
                Manager
            :type  source_vum_location: :class:`Connection` or ``None``
            :param source_vum_location: The configuration to connect to an ESX/VC.
            """
            self.destination_appliance = destination_appliance
            self.source_location = source_location
            self.source_appliance = source_appliance
            self.source_vum = source_vum
            self.source_vum_location = source_vum_location
            VapiStruct.__init__(self)


    UpgradeDeploymentSizeRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.upgrade_deployment_size_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Recommendation.DeploymentSizeDestinationAppliance'),
            'source_location': type.ReferenceType(__name__, 'Connection'),
            'source_appliance': type.ReferenceType(__name__, 'UpgradeSourceAppliance'),
            'source_vum': type.OptionalType(type.ReferenceType(__name__, 'SourceVum')),
            'source_vum_location': type.OptionalType(type.ReferenceType(__name__, 'Connection')),
        },
        UpgradeDeploymentSizeRequest,
        False,
        None))


    class DatastoreRequest(VapiStruct):
        """
        The request for recommending datastore.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_location=None,
                     destination_appliance=None,
                    ):
            """
            :type  destination_location: :class:`Recommendation.DatastoreDestinationLocation`
            :param destination_location: This subsection describes the ESX or VC on which to deploy the
                appliance.
            :type  destination_appliance: :class:`Recommendation.DatastoreDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            """
            self.destination_location = destination_location
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    DatastoreRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.datastore_request', {
            'destination_location': type.ReferenceType(__name__, 'Recommendation.DatastoreDestinationLocation'),
            'destination_appliance': type.ReferenceType(__name__, 'Recommendation.DatastoreDestinationAppliance'),
        },
        DatastoreRequest,
        False,
        None))


    class DatastoreDestinationAppliance(VapiStruct):
        """
        The configuration of destination appliance to recommend datastore.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     appliance_size=None,
                     appliance_disk_size=None,
                     ova_location=None,
                     ova_location_ssl_verify=None,
                     ova_location_ssl_thumbprint=None,
                    ):
            """
            :type  appliance_size: :class:`ApplianceSize` or ``None``
            :param appliance_size: A size descriptor based on the number of virtual machines which
                will be managed by the new vCenter appliance.
                If None, defaults to SMALL
            :type  appliance_disk_size: :class:`StorageSize` or ``None``
            :param appliance_disk_size: The disk size of the new vCenter appliance.
                If None, defaults to REGULAR
            :type  ova_location: :class:`str` or ``None``
            :param ova_location: The location of the ova file.
                Not required.
            :type  ova_location_ssl_verify: :class:`bool` or ``None``
            :param ova_location_ssl_verify: A flag to indicate whether the ssl verification is required.
                If ``ovaLocationSslThumbprint`` is provided, this field can be
                omitted If None, defaults to True
            :type  ova_location_ssl_thumbprint: :class:`str` or ``None``
            :param ova_location_ssl_thumbprint: SSL thumbprint of ssl verification. If provided, ssl_verify can be
                omitted or set to true. If omitted, ssl_verify must be false. If
                omitted and ssl_verify is true, an error will occur.
                If ova_location_ssl_verify is False, this field can be omitted
            """
            self.appliance_size = appliance_size
            self.appliance_disk_size = appliance_disk_size
            self.ova_location = ova_location
            self.ova_location_ssl_verify = ova_location_ssl_verify
            self.ova_location_ssl_thumbprint = ova_location_ssl_thumbprint
            VapiStruct.__init__(self)


    DatastoreDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.datastore_destination_appliance', {
            'appliance_size': type.OptionalType(type.ReferenceType(__name__, 'ApplianceSize')),
            'appliance_disk_size': type.OptionalType(type.ReferenceType(__name__, 'StorageSize')),
            'ova_location': type.OptionalType(type.StringType()),
            'ova_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ova_location_ssl_thumbprint': type.OptionalType(type.StringType()),
        },
        DatastoreDestinationAppliance,
        False,
        None))


    class DatastoreDestinationLocation(VapiStruct):
        """
        This subsection describes the ESX or VC on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     esx=None,
                     vcenter=None,
                    ):
            """
            :type  esx: :class:`Recommendation.DatastoreEsx` or ``None``
            :param esx: This section describes the ESX host on which to deploy the
                appliance. Required if you are deploying the appliance directly on
                an ESX host.
                Mutual exclusive between ``esx`` and ``vcenter``
            :type  vcenter: :class:`Recommendation.DatastoreVc` or ``None``
            :param vcenter: This subsection describes the vCenter on which to deploy the
                appliance.
                Mutual exclusive between ``esx`` and ``vcenter``
            """
            self.esx = esx
            self.vcenter = vcenter
            VapiStruct.__init__(self)


    DatastoreDestinationLocation._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.datastore_destination_location', {
            'esx': type.OptionalType(type.ReferenceType(__name__, 'Recommendation.DatastoreEsx')),
            'vcenter': type.OptionalType(type.ReferenceType(__name__, 'Recommendation.DatastoreVc')),
        },
        DatastoreDestinationLocation,
        False,
        None))


    class DatastoreEsx(VapiStruct):
        """
        This section describes the ESX host on which to deploy the appliance.
        Required if you are deploying the appliance directly on an ESX host.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            """
            self.connection = connection
            VapiStruct.__init__(self)


    DatastoreEsx._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.datastore_esx', {
            'connection': type.ReferenceType(__name__, 'Connection'),
        },
        DatastoreEsx,
        False,
        None))


    class DatastoreVc(VapiStruct):
        """
        This subsection describes the vCenter on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                     inventory=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            :type  inventory: :class:`Recommendation.DatastoreVcInventory`
            :param inventory: All names are case-sensitive. you can install the appliance to one
                of the following destinations: 1. A resource pool in a cluster, use
                'cluster_path'. 2. A specific ESX host in a cluster, use
                'host_path'. 3. A resource pool in a specific ESX host being
                managed by the current vCenter, use 'resource_pool_path'. You must
                always provide the 'network_name' key. To install a new appliance
                to a specific ESX host in a cluster, provide the 'host_path' key,
                and the 'datastore_name', e.g. 'host_path':
                '/MyDataCenter/host/MyCluster/10.20.30.40', 'datastore_name': 'Your
                Datastore'. To install a new appliance to a specific resource pool,
                provide the 'resource_pool_path', and the 'datastore_name', e.g.
                'resource_pool_path': '/Your Datacenter Folder/Your
                Datacenter/host/Your Cluster/Resources/Your Resource Pool',
                'datastore_name': 'Your Datastore'. To place a new appliance to a
                virtual machine Folder, provide the 'vm_folder_path', e.g.
                'vm_folder_path': 'VM Folder 0/VM Folder1'.
            """
            self.connection = connection
            self.inventory = inventory
            VapiStruct.__init__(self)


    DatastoreVc._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.datastore_vc', {
            'connection': type.ReferenceType(__name__, 'Connection'),
            'inventory': type.ReferenceType(__name__, 'Recommendation.DatastoreVcInventory'),
        },
        DatastoreVc,
        False,
        None))


    class DatastoreVcInventory(VapiStruct):
        """
        All names are case-sensitive. you can install the appliance to one of the
        following destinations: 1. A resource pool in a cluster, use
        'cluster_path'. 2. A specific ESX host in a cluster, use 'host_path'. 3. A
        resource pool in a specific ESX host being managed by the current vCenter,
        use 'resource_pool_path'. You must always provide the 'network_name' key.
        To install a new appliance to a specific ESX host in a cluster, provide the
        'host_path' key, and the 'datastore_name', e.g. 'host_path':
        '/MyDataCenter/host/MyCluster/10.20.30.40', 'datastore_name': 'Your
        Datastore'. To install a new appliance to a specific resource pool, provide
        the 'resource_pool_path', and the 'datastore_name', e.g.
        'resource_pool_path': '/Your Datacenter Folder/Your Datacenter/host/Your
        Cluster/Resources/Your Resource Pool', 'datastore_name': 'Your Datastore'.
        To place a new appliance to a virtual machine Folder, provide the
        'vm_folder_path', e.g. 'vm_folder_path': 'VM Folder 0/VM Folder1'.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     host_path=None,
                    ):
            """
            :type  host_path: :class:`str`
            :param host_path: Full path to an ESX host. Format: /{datacenter folder}/{datacenter
                name}/host/{host name}. e.g: /Your Datacenter Folder/Your
                Datacenter/host/Your Host
            """
            self.host_path = host_path
            VapiStruct.__init__(self)


    DatastoreVcInventory._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.datastore_vc_inventory', {
            'host_path': type.StringType(),
        },
        DatastoreVcInventory,
        False,
        None))


    class DatastoreInfo(VapiStruct):
        """
        Datastore space information. Space information are in GB unit.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     freespace=None,
                     freespace_after_placement=None,
                     required_space=None,
                    ):
            """
            :type  freespace: :class:`float`
            :param freespace: The amount of space that the datastore currently has.
            :type  freespace_after_placement: :class:`float`
            :param freespace_after_placement: The amount of space that the datastore will have after deployment.
            :type  required_space: :class:`float`
            :param required_space: The amount of space that the deployment will occupy.
            """
            self.freespace = freespace
            self.freespace_after_placement = freespace_after_placement
            self.required_space = required_space
            VapiStruct.__init__(self)


    DatastoreInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.recommendation.datastore_info', {
            'freespace': type.DoubleType(),
            'freespace_after_placement': type.DoubleType(),
            'required_space': type.DoubleType(),
        },
        DatastoreInfo,
        False,
        None))




    def scan_migrate_deployment_size_task(self,
                                     spec,
                                     ):
        """
        Recommend deployment sizes based on the configuration given in the
        specification.

        :type  spec: :class:`Recommendation.MigrateDeploymentSizeRequest`
        :param spec: The specification that contains information needed to recommend
            deloyment size.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('scan_migrate_deployment_size$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.MapType(type.StringType(), type.ListType(type.StringType())))
        return task_instance


    def scan_datastore_task(self,
                       spec,
                       ):
        """
        Recommend a datastore for the appliance to be deployed in.

        :type  spec: :class:`Recommendation.DatastoreRequest`
        :param spec: The specification contains the information needed to recommend
            datastore
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('scan_datastore$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.MapType(type.StringType(), type.ReferenceType(__name__, 'Recommendation.DatastoreInfo')))
        return task_instance


    def scan_upgrade_deployment_size_task(self,
                                     spec,
                                     ):
        """
        Recommend deployment sizes based on the configuration given in the
        specification.

        :type  spec: :class:`Recommendation.UpgradeDeploymentSizeRequest`
        :param spec: The specification that contains information needed to recommend
            deloyment size.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('scan_upgrade_deployment_size$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.MapType(type.StringType(), type.ListType(type.StringType())))
        return task_instance
class Upgrade(VapiInterface):
    """
    The service to upgrade an existing appliance to Embedded VCSA, PSC, and
    Management VCSA.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.lcm.upgrade'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpgradeStub)

    class UpgradeDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'appliance_type',
                {
                    'VCSA_EMBEDDED' : [('appliance_size', False), ('appliance_disk_size', False), ('vcsa_embedded', True)],
                    'VCSA_EXTERNAL' : [('appliance_size', False), ('appliance_disk_size', False)],
                    'PSC' : [('psc', True)],
                    'VMC' : [],
                }
            ),
        ]



        def __init__(self,
                     appliance_name=None,
                     appliance_type=None,
                     appliance_size=None,
                     appliance_disk_size=None,
                     thin_disk_mode=None,
                     ova_location=None,
                     ova_location_ssl_verify=None,
                     ova_location_ssl_thumbprint=None,
                     ovftool_location=None,
                     ovftool_location_ssl_verify=None,
                     ovftool_location_ssl_thumbprint=None,
                     services=None,
                     temporary_network=None,
                     history=None,
                     ovftool_arguments=None,
                     vcsa_embedded=None,
                     psc=None,
                    ):
            """
            :type  appliance_name: :class:`str`
            :param appliance_name: The name of the appliance to deploy.
            :type  appliance_type: :class:`ApplianceType`
            :param appliance_type: The type of appliance to deploy.
            :type  appliance_size: :class:`ApplianceSize` or ``None``
            :param appliance_size: A size descriptor based on the number of virtual machines which
                will be managed by the new vCenter appliance.
                If None, defaults to SMALL
            :type  appliance_disk_size: :class:`StorageSize` or ``None``
            :param appliance_disk_size: The disk size of the new vCenter appliance.
                If None, defaults to REGULAR
            :type  thin_disk_mode: :class:`bool`
            :param thin_disk_mode: Whether to deploy the appliance with thin mode virtual disks.
            :type  ova_location: :class:`str`
            :param ova_location: The location of the OVA file.
            :type  ova_location_ssl_verify: :class:`bool` or ``None``
            :param ova_location_ssl_verify: A flag to indicate whether the ssl verification is required.
                If ``ovaLocationSslThumbprint`` is provided, this field can be
                omitted If None, defaults to True
            :type  ova_location_ssl_thumbprint: :class:`str` or ``None``
            :param ova_location_ssl_thumbprint: SSL thumbprint of ssl verification. If provided, ssl_verify can be
                omitted or set to true. If omitted, ssl_verify must be false. If
                omitted and ssl_verify is true, an error will occur.
                If ova_location_ssl_verify is False, this field can be omitted
            :type  ovftool_location: :class:`str`
            :param ovftool_location: The location of the OVF Tool.
            :type  ovftool_location_ssl_verify: :class:`bool` or ``None``
            :param ovftool_location_ssl_verify: Flag to indicate whether or not to verify the SSL thumbprint of OVF
                Tool location.
                Default to be True.
            :type  ovftool_location_ssl_thumbprint: :class:`str` or ``None``
            :param ovftool_location_ssl_thumbprint: SSL thumbprint of OVF Tool location to be verified.
                When ``ovftoolLocationSslVerify`` is set to False, this field can
                be omitted.
            :type  services: :class:`UpgradeDestinationApplianceService`
            :param services: Spec to configure vCenter server services.
            :type  temporary_network: :class:`TemporaryNetwork`
            :param temporary_network: The network settings of the appliance to be deployed.
            :type  history: :class:`History` or ``None``
            :param history: History data to be included in the upgrade and migrate
                Default value will be applied when absent
            :type  ovftool_arguments: (:class:`dict` of :class:`str` and :class:`str`) or ``None``
            :param ovftool_arguments: The OVF Tool arguments to be included.
                Not required when no OVF Tool argument to pass through
            :type  vcsa_embedded: :class:`CeipOnlySso`
            :param vcsa_embedded: Spec used to configure an embedded vCenter Server. This field
                describes how the embedded vCenter Server appliance should be
                configured.
                This attribute is optional and it is only relevant when the value
                of ``applianceType`` is :attr:`ApplianceType.VCSA_EMBEDDED`.
            :type  psc: :class:`CeipOnlySso`
            :param psc: Spec used to configure a Platform Services Controller. This section
                describes how the Platform Services Controller appliance should be
                configured. If unset, either ``vcsaEmbedded`` or ``#vcsaExternal``
                must be provided.
                This attribute is optional and it is only relevant when the value
                of ``applianceType`` is :attr:`ApplianceType.PSC`.
            """
            self.appliance_name = appliance_name
            self.appliance_type = appliance_type
            self.appliance_size = appliance_size
            self.appliance_disk_size = appliance_disk_size
            self.thin_disk_mode = thin_disk_mode
            self.ova_location = ova_location
            self.ova_location_ssl_verify = ova_location_ssl_verify
            self.ova_location_ssl_thumbprint = ova_location_ssl_thumbprint
            self.ovftool_location = ovftool_location
            self.ovftool_location_ssl_verify = ovftool_location_ssl_verify
            self.ovftool_location_ssl_thumbprint = ovftool_location_ssl_thumbprint
            self.services = services
            self.temporary_network = temporary_network
            self.history = history
            self.ovftool_arguments = ovftool_arguments
            self.vcsa_embedded = vcsa_embedded
            self.psc = psc
            VapiStruct.__init__(self)


    UpgradeDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.upgrade.upgrade_destination_appliance', {
            'appliance_name': type.StringType(),
            'appliance_type': type.ReferenceType(__name__, 'ApplianceType'),
            'appliance_size': type.OptionalType(type.ReferenceType(__name__, 'ApplianceSize')),
            'appliance_disk_size': type.OptionalType(type.ReferenceType(__name__, 'StorageSize')),
            'thin_disk_mode': type.BooleanType(),
            'ova_location': type.StringType(),
            'ova_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ova_location_ssl_thumbprint': type.OptionalType(type.StringType()),
            'ovftool_location': type.StringType(),
            'ovftool_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ovftool_location_ssl_thumbprint': type.OptionalType(type.StringType()),
            'services': type.ReferenceType(__name__, 'UpgradeDestinationApplianceService'),
            'temporary_network': type.ReferenceType(__name__, 'TemporaryNetwork'),
            'history': type.OptionalType(type.ReferenceType(__name__, 'History')),
            'ovftool_arguments': type.OptionalType(type.MapType(type.StringType(), type.StringType())),
            'vcsa_embedded': type.OptionalType(type.ReferenceType(__name__, 'CeipOnlySso')),
            'psc': type.OptionalType(type.ReferenceType(__name__, 'CeipOnlySso')),
        },
        UpgradeDestinationAppliance,
        False,
        None))


    class Spec(VapiStruct):
        """
        Spec to describe the configuration parameters that are required for upgrade
        of a vCenter Server Appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_location=None,
                     destination_appliance=None,
                     source_location=None,
                     source_appliance=None,
                     source_vum=None,
                     source_vum_location=None,
                    ):
            """
            :type  destination_location: :class:`DestinationLocation`
            :param destination_location: This subsection describes the ESX or VC on which to deploy the
                appliance.
            :type  destination_appliance: :class:`Upgrade.UpgradeDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance
            :type  source_location: :class:`Connection`
            :param source_location: The configuration to connect to an ESX/VC.
            :type  source_appliance: :class:`UpgradeSourceAppliance`
            :param source_appliance: Spec to describe the existing appliance to upgrade.
            :type  source_vum: :class:`SourceVum` or ``None``
            :param source_vum: This section describes the source vSphere Update Manager (VUM)
                which you want to upgrade.
                Not applicable for appliance not having source vSphere Update
                Manager
            :type  source_vum_location: :class:`Connection` or ``None``
            :param source_vum_location: The configuration to connect to an ESX/VC.
            """
            self.destination_location = destination_location
            self.destination_appliance = destination_appliance
            self.source_location = source_location
            self.source_appliance = source_appliance
            self.source_vum = source_vum
            self.source_vum_location = source_vum_location
            VapiStruct.__init__(self)


    Spec._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.upgrade.spec', {
            'destination_location': type.ReferenceType(__name__, 'DestinationLocation'),
            'destination_appliance': type.ReferenceType(__name__, 'Upgrade.UpgradeDestinationAppliance'),
            'source_location': type.ReferenceType(__name__, 'Connection'),
            'source_appliance': type.ReferenceType(__name__, 'UpgradeSourceAppliance'),
            'source_vum': type.OptionalType(type.ReferenceType(__name__, 'SourceVum')),
            'source_vum_location': type.OptionalType(type.ReferenceType(__name__, 'Connection')),
        },
        Spec,
        False,
        None))




    def check_task(self,
              spec,
              options=None,
              ):
        """
        Performs a precheck for the given specification. The result of this
        operation can be queried by calling the cis/tasks/{task-id} with the
        task-id in the response of this call.

        :type  spec: :class:`Upgrade.Spec`
        :param spec:  The specification of the deployment.
        :type  options: :class:`DeploymentOption` or ``None``
        :param options:  The deployment precheck options.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             If the given spec and/or option contains error.
        """
        task_id = self._invoke('check$task',
                                {
                                'spec': spec,
                                'options': options,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance


    def start_task(self,
              spec,
              ):
        """
        Deploys the appliance for the given specification. The result of this
        operation can be queried by calling the cis/tasks/{task-id} with the
        task-id in the response of this call.

        :type  spec: :class:`Upgrade.Spec`
        :param spec:  The specification of the deployment.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             If the given specification contains error.
        """
        task_id = self._invoke('start$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance
class Validation(VapiInterface):
    """
    The service that provides validation of a section of full deployment
    specification.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.lcm.validation'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ValidationStub)

    class UpgradeSourceApplianceDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     ova_location=None,
                     ova_location_ssl_verify=None,
                     ova_location_ssl_thumbprint=None,
                    ):
            """
            :type  ova_location: :class:`str` or ``None``
            :param ova_location: The location of the ova file.
                Not required.
            :type  ova_location_ssl_verify: :class:`bool` or ``None``
            :param ova_location_ssl_verify: A flag to indicate whether the ssl verification is required.
                If ``ovaLocationSslThumbprint`` is provided, this field can be
                omitted If None, defaults to True
            :type  ova_location_ssl_thumbprint: :class:`str` or ``None``
            :param ova_location_ssl_thumbprint: SSL thumbprint of ssl verification. If provided, ssl_verify can be
                omitted or set to true. If omitted, ssl_verify must be false. If
                omitted and ssl_verify is true, an error will occur.
                If ova_location_ssl_verify is False, this field can be omitted
            """
            self.ova_location = ova_location
            self.ova_location_ssl_verify = ova_location_ssl_verify
            self.ova_location_ssl_thumbprint = ova_location_ssl_thumbprint
            VapiStruct.__init__(self)


    UpgradeSourceApplianceDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.upgrade_source_appliance_destination_appliance', {
            'ova_location': type.OptionalType(type.StringType()),
            'ova_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ova_location_ssl_thumbprint': type.OptionalType(type.StringType()),
        },
        UpgradeSourceApplianceDestinationAppliance,
        False,
        None))


    class UpgradeSourceApplianceRequest(VapiStruct):
        """
        The configuration to validate source appliance for upgrade.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                     source_appliance=None,
                     source_location=None,
                    ):
            """
            :type  destination_appliance: :class:`Validation.UpgradeSourceApplianceDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            :type  source_appliance: :class:`UpgradeSourceAppliance`
            :param source_appliance: The source appliance configuration.
            :type  source_location: :class:`Connection`
            :param source_location: The source location configuration.
            """
            self.destination_appliance = destination_appliance
            self.source_appliance = source_appliance
            self.source_location = source_location
            VapiStruct.__init__(self)


    UpgradeSourceApplianceRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.upgrade_source_appliance_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Validation.UpgradeSourceApplianceDestinationAppliance'),
            'source_appliance': type.ReferenceType(__name__, 'UpgradeSourceAppliance'),
            'source_location': type.ReferenceType(__name__, 'Connection'),
        },
        UpgradeSourceApplianceRequest,
        False,
        None))


    class SourceLocationRequest(VapiStruct):
        """
        This subsection describes the ESX or VC on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     source_location=None,
                    ):
            """
            :type  source_location: :class:`Connection`
            :param source_location: The source location configuration
            """
            self.source_location = source_location
            VapiStruct.__init__(self)


    SourceLocationRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.source_location_request', {
            'source_location': type.ReferenceType(__name__, 'Connection'),
        },
        SourceLocationRequest,
        False,
        None))


    class SourceVumRequest(VapiStruct):
        """
        The request that contains information needed to verify the credentials of
        source vSphere Update Manager and run the migration assistant.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     source_vc_windows=None,
                     source_appliance=None,
                     source_vum_location=None,
                     source_vum=None,
                    ):
            """
            :type  source_vc_windows: :class:`Validation.SourceVumSourceVcWindows` or ``None``
            :param source_vc_windows: Spec to describe the existing Windows vCenter server to migrate.
            :type  source_appliance: :class:`Validation.SourceVumUpgradeSourceAppliance` or ``None``
            :param source_appliance: Source appliance configuration for upgrade service.
            :type  source_vum_location: :class:`Connection` or ``None``
            :param source_vum_location: The configuration to connect to an ESX/VC.
            :type  source_vum: :class:`SourceVum`
            :param source_vum: This section describes the source vSphere Update Manager (VUM)
                which you want to upgrade.
            """
            self.source_vc_windows = source_vc_windows
            self.source_appliance = source_appliance
            self.source_vum_location = source_vum_location
            self.source_vum = source_vum
            VapiStruct.__init__(self)


    SourceVumRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.source_vum_request', {
            'source_vc_windows': type.OptionalType(type.ReferenceType(__name__, 'Validation.SourceVumSourceVcWindows')),
            'source_appliance': type.OptionalType(type.ReferenceType(__name__, 'Validation.SourceVumUpgradeSourceAppliance')),
            'source_vum_location': type.OptionalType(type.ReferenceType(__name__, 'Connection')),
            'source_vum': type.ReferenceType(__name__, 'SourceVum'),
        },
        SourceVumRequest,
        False,
        None))


    class SourceVumUpgradeSourceAppliance(VapiStruct):
        """
        Source appliance configuration for upgrade service.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     sso_admin_username=None,
                     sso_admin_password=None,
                    ):
            """
            :type  sso_admin_username: :class:`str`
            :param sso_admin_username: vCenter Single Sign-On administrator user name of the source
                appliance.
            :type  sso_admin_password: :class:`str`
            :param sso_admin_password: vCenter Single Sign-On administrator password of the source
                appliance.
            """
            self.sso_admin_username = sso_admin_username
            self.sso_admin_password = sso_admin_password
            VapiStruct.__init__(self)


    SourceVumUpgradeSourceAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.source_vum_upgrade_source_appliance', {
            'sso_admin_username': type.StringType(),
            'sso_admin_password': type.SecretType(),
        },
        SourceVumUpgradeSourceAppliance,
        False,
        None))


    class SourceVumSourceVcWindows(VapiStruct):
        """
        Spec to describe the existing Windows vCenter server to migrate.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     username=None,
                     password=None,
                    ):
            """
            :type  username: :class:`str`
            :param username: Single Sign-On administrator user on the source Windows vCenter
                server. For example, administrator\\\\@vsphere.local. Important:
                The user must be administrator\\\\@your_domain_name.
            :type  password: :class:`str`
            :param password: The password of the Single Sign-On administrator on the source
                Windows vCenter server.
            """
            self.username = username
            self.password = password
            VapiStruct.__init__(self)


    SourceVumSourceVcWindows._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.source_vum_source_vc_windows', {
            'username': type.StringType(),
            'password': type.SecretType(),
        },
        SourceVumSourceVcWindows,
        False,
        None))


    class OsPasswordRequest(VapiStruct):
        """
        The request that contains information needed to verify the given password
        conforms password policy.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                    ):
            """
            :type  destination_appliance: :class:`Validation.OsPasswordDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            """
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    OsPasswordRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.os_password_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Validation.OsPasswordDestinationAppliance'),
        },
        OsPasswordRequest,
        False,
        None))


    class OsPasswordDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     root_password=None,
                    ):
            """
            :type  root_password: :class:`str`
            :param root_password: Password must conform to the following requirements: 1. At least 8
                characters. 2. No more than 20 characters. 3. At least 1 uppercase
                character. 4. At least 1 lowercase character. 5. At least 1 number.
                6. At least 1 special character (e.g., '!', '(', '\\\\@', etc.). 7.
                Only visible A-Z, a-z, 0-9 and punctuation (spaces are not allowed)
            """
            self.root_password = root_password
            VapiStruct.__init__(self)


    OsPasswordDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.os_password_destination_appliance', {
            'root_password': type.SecretType(),
        },
        OsPasswordDestinationAppliance,
        False,
        None))


    class NtpServerRequest(VapiStruct):
        """
        A request that contains the information needed to validate the given ntp
        servers.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                    ):
            """
            :type  destination_appliance: :class:`Validation.NtpServerDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            """
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    NtpServerRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.ntp_server_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Validation.NtpServerDestinationAppliance'),
        },
        NtpServerRequest,
        False,
        None))


    class NtpServerDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     time=None,
                    ):
            """
            :type  time: :class:`Time`
            :param time: Configuration of the vCSA time synchronization.
            """
            self.time = time
            VapiStruct.__init__(self)


    NtpServerDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.ntp_server_destination_appliance', {
            'time': type.ReferenceType(__name__, 'Time'),
        },
        NtpServerDestinationAppliance,
        False,
        None))


    class EsxRequest(VapiStruct):
        """
        The request that contains the information to verify esx management status.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_location=None,
                     source_location=None,
                     source_vum_location=None,
                    ):
            """
            :type  destination_location: :class:`Validation.EsxDestinationLocation`
            :param destination_location: This subsection describes the ESX or VC on which to deploy the
                appliance.
            :type  source_location: :class:`Connection` or ``None``
            :param source_location: The configuration to connect to an ESX/VC.
            :type  source_vum_location: :class:`Connection` or ``None``
            :param source_vum_location: The configuration to connect to an ESX/VC.
            """
            self.destination_location = destination_location
            self.source_location = source_location
            self.source_vum_location = source_vum_location
            VapiStruct.__init__(self)


    EsxRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.esx_request', {
            'destination_location': type.ReferenceType(__name__, 'Validation.EsxDestinationLocation'),
            'source_location': type.OptionalType(type.ReferenceType(__name__, 'Connection')),
            'source_vum_location': type.OptionalType(type.ReferenceType(__name__, 'Connection')),
        },
        EsxRequest,
        False,
        None))


    class EsxDestinationLocation(VapiStruct):
        """
        This subsection describes the ESX or VC on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     esx=None,
                     vcenter=None,
                    ):
            """
            :type  esx: :class:`Validation.ContainerWithoutInventory` or ``None``
            :param esx: This section describes the ESX host on which to deploy the
                appliance. Required if you are deploying the appliance directly on
                an ESX host.
                Mutual exclusive between ``esx`` and ``vcenter``
            :type  vcenter: :class:`Validation.ContainerWithoutInventory` or ``None``
            :param vcenter: This subsection describes the vCenter on which to deploy the
                appliance.
                Mutual exclusive between ``esx`` and ``vcenter``
            """
            self.esx = esx
            self.vcenter = vcenter
            VapiStruct.__init__(self)


    EsxDestinationLocation._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.esx_destination_location', {
            'esx': type.OptionalType(type.ReferenceType(__name__, 'Validation.ContainerWithoutInventory')),
            'vcenter': type.OptionalType(type.ReferenceType(__name__, 'Validation.ContainerWithoutInventory')),
        },
        EsxDestinationLocation,
        False,
        None))


    class ContainerWithoutInventory(VapiStruct):
        """
        This section describes the ESX host on which to deploy the appliance.
        Required if you are deploying the appliance directly on an ESX host.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            """
            self.connection = connection
            VapiStruct.__init__(self)


    ContainerWithoutInventory._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.container_without_inventory', {
            'connection': type.ReferenceType(__name__, 'Connection'),
        },
        ContainerWithoutInventory,
        False,
        None))


    class NetworkRequest(VapiStruct):
        """
        The request that contains network information to be validated.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                    ):
            """
            :type  destination_appliance: :class:`Validation.NetworkDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            """
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    NetworkRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.network_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Validation.NetworkDestinationAppliance'),
        },
        NetworkRequest,
        False,
        None))


    class NetworkDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     network=None,
                    ):
            """
            :type  network: :class:`Network`
            :param network: The network settings of the appliance to be deployed.
            """
            self.network = network
            VapiStruct.__init__(self)


    NetworkDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.network_destination_appliance', {
            'network': type.ReferenceType(__name__, 'Network'),
        },
        NetworkDestinationAppliance,
        False,
        None))


    class TemporaryNetworkRequest(VapiStruct):
        """
        The request that contains network information to be validated.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                    ):
            """
            :type  destination_appliance: :class:`Validation.TemporaryNetworkDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            """
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    TemporaryNetworkRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.temporary_network_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Validation.TemporaryNetworkDestinationAppliance'),
        },
        TemporaryNetworkRequest,
        False,
        None))


    class TemporaryNetworkDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     network=None,
                    ):
            """
            :type  network: :class:`TemporaryNetwork`
            :param network: The network settings of the appliance to be deployed.
            """
            self.network = network
            VapiStruct.__init__(self)


    TemporaryNetworkDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.temporary_network_destination_appliance', {
            'network': type.ReferenceType(__name__, 'TemporaryNetwork'),
        },
        TemporaryNetworkDestinationAppliance,
        False,
        None))


    class ApplianceNameRequest(VapiStruct):
        """
        Data container that contains the information needed to validate appliance
        name.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_location=None,
                     destination_appliance=None,
                    ):
            """
            :type  destination_location: :class:`Validation.ApplianceNameDestinationLocation`
            :param destination_location: This subsection describes the ESX or VC on which to deploy the
                appliance.
            :type  destination_appliance: :class:`Validation.ApplianceNameDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            """
            self.destination_location = destination_location
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    ApplianceNameRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.appliance_name_request', {
            'destination_location': type.ReferenceType(__name__, 'Validation.ApplianceNameDestinationLocation'),
            'destination_appliance': type.ReferenceType(__name__, 'Validation.ApplianceNameDestinationAppliance'),
        },
        ApplianceNameRequest,
        False,
        None))


    class ApplianceNameDestinationAppliance(VapiStruct):
        """
        Data container for appliance name information used in validation of
        appliance name request.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     appliance_name=None,
                    ):
            """
            :type  appliance_name: :class:`str`
            :param appliance_name: The name of the appliance to deploy.
            """
            self.appliance_name = appliance_name
            VapiStruct.__init__(self)


    ApplianceNameDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.appliance_name_destination_appliance', {
            'appliance_name': type.StringType(),
        },
        ApplianceNameDestinationAppliance,
        False,
        None))


    class ApplianceNameDestinationLocation(VapiStruct):
        """


        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     esx=None,
                     vcenter=None,
                    ):
            """
            :type  esx: :class:`Validation.ApplianceNameEsx` or ``None``
            :param esx: This section describes the ESX host on which to deploy the
                appliance. Required if you are deploying the appliance directly on
                an ESX host.
                Mutual exclusive between ``esx`` and ``vcenter``
            :type  vcenter: :class:`Validation.ApplianceNameVc` or ``None``
            :param vcenter: This subsection describes the vCenter on which to deploy the
                appliance.
                Mutual exclusive between ``esx`` and ``vcenter``
            """
            self.esx = esx
            self.vcenter = vcenter
            VapiStruct.__init__(self)


    ApplianceNameDestinationLocation._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.appliance_name_destination_location', {
            'esx': type.OptionalType(type.ReferenceType(__name__, 'Validation.ApplianceNameEsx')),
            'vcenter': type.OptionalType(type.ReferenceType(__name__, 'Validation.ApplianceNameVc')),
        },
        ApplianceNameDestinationLocation,
        False,
        None))


    class ApplianceNameEsx(VapiStruct):
        """
        This section describes the ESX host on which to deploy the appliance.
        Required if you are deploying the appliance directly on an ESX host.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            """
            self.connection = connection
            VapiStruct.__init__(self)


    ApplianceNameEsx._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.appliance_name_esx', {
            'connection': type.ReferenceType(__name__, 'Connection'),
        },
        ApplianceNameEsx,
        False,
        None))


    class ApplianceNameEsxInventory(VapiStruct):
        """
        The configuration of ESX inventory.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     resource_pool_path=None,
                    ):
            """
            :type  resource_pool_path: :class:`str` or ``None``
            :param resource_pool_path: The path to the resource pool on the ESX host in which the
                appliance will be deployed.
                Not applicable when not in resource pool
            """
            self.resource_pool_path = resource_pool_path
            VapiStruct.__init__(self)


    ApplianceNameEsxInventory._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.appliance_name_esx_inventory', {
            'resource_pool_path': type.OptionalType(type.StringType()),
        },
        ApplianceNameEsxInventory,
        False,
        None))


    class ApplianceNameVc(VapiStruct):
        """
        This subsection describes the vCenter on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                     inventory=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            :type  inventory: :class:`Validation.ApplianceNameVcInventory`
            :param inventory: All names are case-sensitive. you can install the appliance to one
                of the following destinations: 1. A resource pool in a cluster, use
                'cluster_path'. 2. A specific ESX host in a cluster, use
                'host_path'. 3. A resource pool in a specific ESX host being
                managed by the current vCenter, use 'resource_pool_path'. You must
                always provide the 'network_name' key. To install a new appliance
                to a specific ESX host in a cluster, provide the 'host_path' key,
                and the 'datastore_name', e.g. 'host_path':
                '/MyDataCenter/host/MyCluster/10.20.30.40', 'datastore_name': 'Your
                Datastore'. To install a new appliance to a specific resource pool,
                provide the 'resource_pool_path', and the 'datastore_name', e.g.
                'resource_pool_path': '/Your Datacenter Folder/Your
                Datacenter/host/Your Cluster/Resources/Your Resource Pool',
                'datastore_name': 'Your Datastore'. To place a new appliance to a
                virtual machine Folder, provide the 'vm_folder_path', e.g.
                'vm_folder_path': 'VM Folder 0/VM Folder1'.
            """
            self.connection = connection
            self.inventory = inventory
            VapiStruct.__init__(self)


    ApplianceNameVc._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.appliance_name_vc', {
            'connection': type.ReferenceType(__name__, 'Connection'),
            'inventory': type.ReferenceType(__name__, 'Validation.ApplianceNameVcInventory'),
        },
        ApplianceNameVc,
        False,
        None))


    class ApplianceNameVcInventory(VapiStruct):
        """
        All names are case-sensitive. you can install the appliance to one of the
        following destinations: 1. A resource pool in a cluster, use
        'cluster_path'. 2. A specific ESX host in a cluster, use 'host_path'. 3. A
        resource pool in a specific ESX host being managed by the current vCenter,
        use 'resource_pool_path'. You must always provide the 'network_name' key.
        To install a new appliance to a specific ESX host in a cluster, provide the
        'host_path' key, and the 'datastore_name', e.g. 'host_path':
        '/MyDataCenter/host/MyCluster/10.20.30.40', 'datastore_name': 'Your
        Datastore'. To install a new appliance to a specific resource pool, provide
        the 'resource_pool_path', and the 'datastore_name', e.g.
        'resource_pool_path': '/Your Datacenter Folder/Your Datacenter/host/Your
        Cluster/Resources/Your Resource Pool', 'datastore_name': 'Your Datastore'.
        To place a new appliance to a virtual machine Folder, provide the
        'vm_folder_path', e.g. 'vm_folder_path': 'VM Folder 0/VM Folder1'.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vm_folder_path=None,
                     resource_pool_path=None,
                     cluster_path=None,
                     host_path=None,
                    ):
            """
            :type  vm_folder_path: :class:`str` or ``None``
            :param vm_folder_path: 
            :type  resource_pool_path: :class:`str` or ``None``
            :param resource_pool_path: Full path to resource pool. Format: /{datacenter
                folder}/{datacenter name}/host/{host
                name}/{cluster_name}/Resources/{resource pool}. e.g: /Your
                Datacenter Folder/Your Datacenter/host/Your Cluster/Resources/Your
                Resource Pool
                Mutually exclusive between ``#resource_pool_path``,
                ``#cluster_path``, and ``#host_path``
            :type  cluster_path: :class:`str` or ``None``
            :param cluster_path: Full path to the cluster. Format: /{datacenter folder}/{datacenter
                name}/host/{cluster_name}. e.g: /Your Datacenter Folder/Your
                Datacenter/host/Your Cluster
                Mutually exclusive between ``#resource_pool_path``,
                ``#cluster_path``, and ``#host_path``
            :type  host_path: :class:`str` or ``None``
            :param host_path: Full path to an ESX host. Format: /{datacenter folder}/{datacenter
                name}/host/{host name}. e.g: /Your Datacenter Folder/Your
                Datacenter/host/Your Host
                Mutually exclusive between ``#resource_pool_path``,
                ``#cluster_path``, and ``#host_path``
            """
            self.vm_folder_path = vm_folder_path
            self.resource_pool_path = resource_pool_path
            self.cluster_path = cluster_path
            self.host_path = host_path
            VapiStruct.__init__(self)


    ApplianceNameVcInventory._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.appliance_name_vc_inventory', {
            'vm_folder_path': type.OptionalType(type.StringType()),
            'resource_pool_path': type.OptionalType(type.StringType()),
            'cluster_path': type.OptionalType(type.StringType()),
            'host_path': type.OptionalType(type.StringType()),
        },
        ApplianceNameVcInventory,
        False,
        None))


    class DestinationLocationRequest(VapiStruct):
        """
        This subsection describes the ESX or VC on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_location=None,
                    ):
            """
            :type  destination_location: :class:`Validation.ValidationDestinationLocation`
            :param destination_location: The destination location configuration.
            """
            self.destination_location = destination_location
            VapiStruct.__init__(self)


    DestinationLocationRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.destination_location_request', {
            'destination_location': type.ReferenceType(__name__, 'Validation.ValidationDestinationLocation'),
        },
        DestinationLocationRequest,
        False,
        None))


    class ValidationDestinationLocation(VapiStruct):
        """
        This subsection describes the ESX or VC on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     esx=None,
                     vcenter=None,
                    ):
            """
            :type  esx: :class:`Validation.DestinationLocationEsx` or ``None``
            :param esx: This section describes the ESX host on which to deploy the
                appliance. Required if you are deploying the appliance directly on
                an ESX host.
                Mutual exclusive between ``esx`` and ``vcenter``
            :type  vcenter: :class:`Validation.DestinationLocationVc` or ``None``
            :param vcenter: This subsection describes the vCenter on which to deploy the
                appliance.
                Mutual exclusive between ``esx`` and ``vcenter``
            """
            self.esx = esx
            self.vcenter = vcenter
            VapiStruct.__init__(self)


    ValidationDestinationLocation._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.validation_destination_location', {
            'esx': type.OptionalType(type.ReferenceType(__name__, 'Validation.DestinationLocationEsx')),
            'vcenter': type.OptionalType(type.ReferenceType(__name__, 'Validation.DestinationLocationVc')),
        },
        ValidationDestinationLocation,
        False,
        None))


    class DestinationLocationEsx(VapiStruct):
        """
        This section describes the ESX host on which to deploy the appliance.
        Required if you are deploying the appliance directly on an ESX host.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            """
            self.connection = connection
            VapiStruct.__init__(self)


    DestinationLocationEsx._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.destination_location_esx', {
            'connection': type.ReferenceType(__name__, 'Connection'),
        },
        DestinationLocationEsx,
        False,
        None))


    class DestinationLocationVc(VapiStruct):
        """
        This subsection describes the vCenter on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                     inventory=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            :type  inventory: :class:`VcInventory` or ``None``
            :param inventory: All names are case-sensitive. you can install the appliance to one
                of the following destinations: 1. A resource pool in a cluster, use
                'cluster_path'. 2. A specific ESX host in a cluster, use
                'host_path'. 3. A resource pool in a specific ESX host being
                managed by the current vCenter, use 'resource_pool_path'. You must
                always provide the 'network_name' key. To install a new appliance
                to a specific ESX host in a cluster, provide the 'host_path' key,
                and the 'datastore_name', e.g. 'host_path':
                '/MyDataCenter/host/MyCluster/10.20.30.40', 'datastore_name': 'Your
                Datastore'. To install a new appliance to a specific resource pool,
                provide the 'resource_pool_path', and the 'datastore_name', e.g.
                'resource_pool_path': '/Your Datacenter Folder/Your
                Datacenter/host/Your Cluster/Resources/Your Resource Pool',
                'datastore_name': 'Your Datastore'. To place a new appliance to a
                virtual machine Folder, provide the 'vm_folder_path', e.g.
                'vm_folder_path': 'VM Folder 0/VM Folder1'.
            """
            self.connection = connection
            self.inventory = inventory
            VapiStruct.__init__(self)


    DestinationLocationVc._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.destination_location_vc', {
            'connection': type.ReferenceType(__name__, 'Connection'),
            'inventory': type.OptionalType(type.ReferenceType(__name__, 'VcInventory')),
        },
        DestinationLocationVc,
        False,
        None))


    class HostConfigRequest(VapiStruct):
        """
        Data container that contains the information needed to validate appliance
        name.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_location=None,
                     destination_appliance=None,
                    ):
            """
            :type  destination_location: :class:`Validation.HostConfigDestinationLocation`
            :param destination_location: This subsection describes the ESX or VC on which to deploy the
                appliance.
            :type  destination_appliance: :class:`Validation.HostConfigDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            """
            self.destination_location = destination_location
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    HostConfigRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.host_config_request', {
            'destination_location': type.ReferenceType(__name__, 'Validation.HostConfigDestinationLocation'),
            'destination_appliance': type.ReferenceType(__name__, 'Validation.HostConfigDestinationAppliance'),
        },
        HostConfigRequest,
        False,
        None))


    class HostConfigDestinationAppliance(VapiStruct):
        """
        Data container for appliance name information used in validation of
        appliance name request.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'appliance_type',
                {
                    'VCSA_EXTERNAL' : [],
                    'VCSA_EMBEDDED' : [],
                    'PSC' : [],
                    'VMC' : [],
                }
            ),
        ]



        def __init__(self,
                     appliance_name=None,
                     appliance_type=None,
                     appliance_size=None,
                     appliance_disk_size=None,
                     thin_disk_mode=None,
                     ova_location=None,
                     ova_location_ssl_verify=None,
                     ova_location_ssl_thumbprint=None,
                    ):
            """
            :type  appliance_name: :class:`str`
            :param appliance_name: The name of the appliance to deploy.
            :type  appliance_type: :class:`ApplianceType`
            :param appliance_type: The type of appliance to deploy.
            :type  appliance_size: :class:`ApplianceSize` or ``None``
            :param appliance_size: A size descriptor based on the number of virtual machines which
                will be managed by the new vCenter appliance.
                If None, defaults to SMALL
            :type  appliance_disk_size: :class:`StorageSize` or ``None``
            :param appliance_disk_size: The disk size of the new vCenter appliance.
                If None, defaults to REGULAR
            :type  thin_disk_mode: :class:`bool`
            :param thin_disk_mode: Whether to deploy the appliance with thin mode virtual disks.
            :type  ova_location: :class:`str` or ``None``
            :param ova_location: The location of the ova file.
                Not required.
            :type  ova_location_ssl_verify: :class:`bool` or ``None``
            :param ova_location_ssl_verify: A flag to indicate whether the ssl verification is required.
                If ``ovaLocationSslThumbprint`` is provided, this field can be
                omitted If None, defaults to True
            :type  ova_location_ssl_thumbprint: :class:`str` or ``None``
            :param ova_location_ssl_thumbprint: SSL thumbprint of ssl verification. If provided, ssl_verify can be
                omitted or set to true. If omitted, ssl_verify must be false. If
                omitted and ssl_verify is true, an error will occur.
                If ova_location_ssl_verify is False, this field can be omitted
            """
            self.appliance_name = appliance_name
            self.appliance_type = appliance_type
            self.appliance_size = appliance_size
            self.appliance_disk_size = appliance_disk_size
            self.thin_disk_mode = thin_disk_mode
            self.ova_location = ova_location
            self.ova_location_ssl_verify = ova_location_ssl_verify
            self.ova_location_ssl_thumbprint = ova_location_ssl_thumbprint
            VapiStruct.__init__(self)


    HostConfigDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.host_config_destination_appliance', {
            'appliance_name': type.StringType(),
            'appliance_type': type.ReferenceType(__name__, 'ApplianceType'),
            'appliance_size': type.OptionalType(type.ReferenceType(__name__, 'ApplianceSize')),
            'appliance_disk_size': type.OptionalType(type.ReferenceType(__name__, 'StorageSize')),
            'thin_disk_mode': type.BooleanType(),
            'ova_location': type.OptionalType(type.StringType()),
            'ova_location_ssl_verify': type.OptionalType(type.BooleanType()),
            'ova_location_ssl_thumbprint': type.OptionalType(type.StringType()),
        },
        HostConfigDestinationAppliance,
        False,
        None))


    class HostConfigDestinationLocation(VapiStruct):
        """
        This subsection describes the ESX or VC on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     esx=None,
                     vcenter=None,
                    ):
            """
            :type  esx: :class:`Validation.HostConfigEsx` or ``None``
            :param esx: This section describes the ESX host on which to deploy the
                appliance. Required if you are deploying the appliance directly on
                an ESX host.
                Mutual exclusive between ``esx`` and ``vcenter``
            :type  vcenter: :class:`Validation.HostConfigVc` or ``None``
            :param vcenter: This subsection describes the vCenter on which to deploy the
                appliance.
                Mutual exclusive between ``esx`` and ``vcenter``
            """
            self.esx = esx
            self.vcenter = vcenter
            VapiStruct.__init__(self)


    HostConfigDestinationLocation._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.host_config_destination_location', {
            'esx': type.OptionalType(type.ReferenceType(__name__, 'Validation.HostConfigEsx')),
            'vcenter': type.OptionalType(type.ReferenceType(__name__, 'Validation.HostConfigVc')),
        },
        HostConfigDestinationLocation,
        False,
        None))


    class HostConfigEsx(VapiStruct):
        """
        This section describes the ESX host on which to deploy the appliance.
        Required if you are deploying the appliance directly on an ESX host.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                     inventory=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            :type  inventory: :class:`Validation.HostConfigEsxInventory`
            :param inventory: The configuration of ESX inventory.
            """
            self.connection = connection
            self.inventory = inventory
            VapiStruct.__init__(self)


    HostConfigEsx._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.host_config_esx', {
            'connection': type.ReferenceType(__name__, 'Connection'),
            'inventory': type.ReferenceType(__name__, 'Validation.HostConfigEsxInventory'),
        },
        HostConfigEsx,
        False,
        None))


    class HostConfigEsxInventory(VapiStruct):
        """
        The configuration of ESX inventory.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore_name=None,
                     resource_pool_path=None,
                    ):
            """
            :type  datastore_name: :class:`str`
            :param datastore_name: The datastore on which to store the files of the appliance. This
                value has to be either a specific datastore name, or a specific
                datastore in a datastore cluster. The datastore must be accessible
                from the ESX host and must have at least 25 GB of free space.
                Otherwise, the new appliance might not power on.
            :type  resource_pool_path: :class:`str` or ``None``
            :param resource_pool_path: The path to the resource pool on the ESX host in which the
                appliance will be deployed.
                Not applicable when not in resource pool
            """
            self.datastore_name = datastore_name
            self.resource_pool_path = resource_pool_path
            VapiStruct.__init__(self)


    HostConfigEsxInventory._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.host_config_esx_inventory', {
            'datastore_name': type.StringType(),
            'resource_pool_path': type.OptionalType(type.StringType()),
        },
        HostConfigEsxInventory,
        False,
        None))


    class HostConfigVc(VapiStruct):
        """
        This subsection describes the vCenter on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     connection=None,
                     inventory=None,
                    ):
            """
            :type  connection: :class:`Connection`
            :param connection: The configuration to connect to an ESX/VC.
            :type  inventory: :class:`Validation.HostConfigVcInventory`
            :param inventory: All names are case-sensitive. you can install the appliance to one
                of the following destinations: 1. A resource pool in a cluster, use
                'cluster_path'. 2. A specific ESX host in a cluster, use
                'host_path'. 3. A resource pool in a specific ESX host being
                managed by the current vCenter, use 'resource_pool_path'. You must
                always provide the 'network_name' key. To install a new appliance
                to a specific ESX host in a cluster, provide the 'host_path' key,
                and the 'datastore_name', e.g. 'host_path':
                '/MyDataCenter/host/MyCluster/10.20.30.40', 'datastore_name': 'Your
                Datastore'. To install a new appliance to a specific resource pool,
                provide the 'resource_pool_path', and the 'datastore_name', e.g.
                'resource_pool_path': '/Your Datacenter Folder/Your
                Datacenter/host/Your Cluster/Resources/Your Resource Pool',
                'datastore_name': 'Your Datastore'. To place a new appliance to a
                virtual machine Folder, provide the 'vm_folder_path', e.g.
                'vm_folder_path': 'VM Folder 0/VM Folder1'.
            """
            self.connection = connection
            self.inventory = inventory
            VapiStruct.__init__(self)


    HostConfigVc._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.host_config_vc', {
            'connection': type.ReferenceType(__name__, 'Connection'),
            'inventory': type.ReferenceType(__name__, 'Validation.HostConfigVcInventory'),
        },
        HostConfigVc,
        False,
        None))


    class HostConfigVcInventory(VapiStruct):
        """
        All names are case-sensitive. you can install the appliance to one of the
        following destinations: 1. A resource pool in a cluster, use
        'cluster_path'. 2. A specific ESX host in a cluster, use 'host_path'. 3. A
        resource pool in a specific ESX host being managed by the current vCenter,
        use 'resource_pool_path'. You must always provide the 'network_name' key.
        To install a new appliance to a specific ESX host in a cluster, provide the
        'host_path' key, and the 'datastore_name', e.g. 'host_path':
        '/MyDataCenter/host/MyCluster/10.20.30.40', 'datastore_name': 'Your
        Datastore'. To install a new appliance to a specific resource pool, provide
        the 'resource_pool_path', and the 'datastore_name', e.g.
        'resource_pool_path': '/Your Datacenter Folder/Your Datacenter/host/Your
        Cluster/Resources/Your Resource Pool', 'datastore_name': 'Your Datastore'.
        To place a new appliance to a virtual machine Folder, provide the
        'vm_folder_path', e.g. 'vm_folder_path': 'VM Folder 0/VM Folder1'.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vm_folder_path=None,
                     resource_pool_path=None,
                     cluster_path=None,
                     host_path=None,
                     datastore_name=None,
                     datastore_cluster_name=None,
                    ):
            """
            :type  vm_folder_path: :class:`str` or ``None``
            :param vm_folder_path: Path of the VM folder. VM folder must be visible by the Data Center
                of the compute resourceFormat:{vm_folder1}/{vm_folder2}e.g.:'VM
                Folder 0/VM Folder1'.
                Mutually exclusive between ``#resource_pool_path``,
                ``#cluster_path``, and ``#host_path``
            :type  resource_pool_path: :class:`str` or ``None``
            :param resource_pool_path: Full path to resource pool. Format: /{datacenter
                folder}/{datacenter name}/host/{host
                name}/{cluster_name}/Resources/{resource pool}. e.g: /Your
                Datacenter Folder/Your Datacenter/host/Your Cluster/Resources/Your
                Resource Pool
                Mutually exclusive between ``#resource_pool_path``,
                ``#cluster_path``, and ``#host_path``
            :type  cluster_path: :class:`str` or ``None``
            :param cluster_path: Full path to the cluster. Format: /{datacenter folder}/{datacenter
                name}/host/{cluster_name}. e.g: /Your Datacenter Folder/Your
                Datacenter/host/Your Cluster
                Mutually exclusive between ``#resource_pool_path``,
                ``#cluster_path``, and ``#host_path``
            :type  host_path: :class:`str` or ``None``
            :param host_path: 
            :type  datastore_name: :class:`str` or ``None``
            :param datastore_name: The datastore on which to store the files of the appliance. This
                value has to be either a specific datastore name, or a specific
                datastore in a datastore cluster. The datastore must be accessible
                from the ESX host and must have at least 25 GB of free space.
                Otherwise, the new appliance might not power on.
                Mutually exclusive between ``#datastore_name`` and
                ``#datastore_cluster_name``
            :type  datastore_cluster_name: :class:`str` or ``None``
            :param datastore_cluster_name: The datastore cluster on which to store the files of the appliance.
                Mutually exclusive between ``#datastore_name`` and
                ``#datastore_cluster_name``
            """
            self.vm_folder_path = vm_folder_path
            self.resource_pool_path = resource_pool_path
            self.cluster_path = cluster_path
            self.host_path = host_path
            self.datastore_name = datastore_name
            self.datastore_cluster_name = datastore_cluster_name
            VapiStruct.__init__(self)


    HostConfigVcInventory._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.host_config_vc_inventory', {
            'vm_folder_path': type.OptionalType(type.StringType()),
            'resource_pool_path': type.OptionalType(type.StringType()),
            'cluster_path': type.OptionalType(type.StringType()),
            'host_path': type.OptionalType(type.StringType()),
            'datastore_name': type.OptionalType(type.StringType()),
            'datastore_cluster_name': type.OptionalType(type.StringType()),
        },
        HostConfigVcInventory,
        False,
        None))


    class MigrateSourceApplianceRequest(VapiStruct):
        """
        This subsection describes the ESX or VC on which to deploy the appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                     source_vc_windows=None,
                     existing_migration_assistant=None,
                     start_migration_assistant=None,
                     source_vum_location=None,
                     source_vum=None,
                    ):
            """
            :type  destination_appliance: :class:`Recommendation.DeploymentSizeDestinationAppliance`
            :param destination_appliance: Spec to describe the new appliance.
            :type  source_vc_windows: :class:`SourceVcWindows`
            :param source_vc_windows: Spec to describe the existing Windows vCenter server to migrate.
            :type  existing_migration_assistant: :class:`ExistingMigrationAssistant` or ``None``
            :param existing_migration_assistant: Spec to describe the attributes of a running Migration Assistant on
                the Windows vCenter server.
                Only applicable when migration assistant is already running on the
                source appliance
            :type  start_migration_assistant: :class:`MigrationAssistant` or ``None``
            :param start_migration_assistant: Spec to automate the invocation of Migration Assistant. Automatic
                invocation works only if the source Windows installation is running
                as a virtual machine.
                Only applicable when migration assistant is not running on the
                source appliance.
            :type  source_vum_location: :class:`Connection` or ``None``
            :param source_vum_location: The configuration to connect to an ESX/VC.
            :type  source_vum: :class:`SourceVum` or ``None``
            :param source_vum: This section describes the source vSphere Update Manager (VUM)
                which you want to upgrade.
                Not applicable for appliance not having source vSphere Update
                Manager
            """
            self.destination_appliance = destination_appliance
            self.source_vc_windows = source_vc_windows
            self.existing_migration_assistant = existing_migration_assistant
            self.start_migration_assistant = start_migration_assistant
            self.source_vum_location = source_vum_location
            self.source_vum = source_vum
            VapiStruct.__init__(self)


    MigrateSourceApplianceRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.migrate_source_appliance_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Recommendation.DeploymentSizeDestinationAppliance'),
            'source_vc_windows': type.ReferenceType(__name__, 'SourceVcWindows'),
            'existing_migration_assistant': type.OptionalType(type.ReferenceType(__name__, 'ExistingMigrationAssistant')),
            'start_migration_assistant': type.OptionalType(type.ReferenceType(__name__, 'MigrationAssistant')),
            'source_vum_location': type.OptionalType(type.ReferenceType(__name__, 'Connection')),
            'source_vum': type.OptionalType(type.ReferenceType(__name__, 'SourceVum')),
        },
        MigrateSourceApplianceRequest,
        False,
        None))


    class SsoConfigurationRequest(VapiStruct):
        """
        The request that contains information needed to verify the Single Sign-On
        configuration.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     destination_appliance=None,
                    ):
            """
            :type  destination_appliance: :class:`Validation.SsoConfigurationDestinationAppliance`
            :param destination_appliance: Destination appliance configuration needed to validate Single
                Sign-On.
            """
            self.destination_appliance = destination_appliance
            VapiStruct.__init__(self)


    SsoConfigurationRequest._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.sso_configuration_request', {
            'destination_appliance': type.ReferenceType(__name__, 'Validation.SsoConfigurationDestinationAppliance'),
        },
        SsoConfigurationRequest,
        False,
        None))


    class SsoConfigurationDestinationAppliance(VapiStruct):
        """
        Spec to describe the new appliance.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vcsa_embedded=None,
                     psc=None,
                     vcsa_external=None,
                    ):
            """
            :type  vcsa_embedded: :class:`Validation.SsoConfigurationVcsaEmbedded` or ``None``
            :param vcsa_embedded: Configuration of Single Sign-On for deploying Embedded.
                Mutuall exclusive between embedded, PSC, and management node.
            :type  psc: :class:`Validation.SsoConfigurationPsc` or ``None``
            :param psc: Configuration of Single Sign-On for deploying PSC.
                Mutuall exclusive between embedded, PSC, and management node.
            :type  vcsa_external: :class:`ExternalVcsa` or ``None``
            :param vcsa_external: Configuration of Single Sign-On for deploying management node.
                Mutuall exclusive between embedded, PSC, and management node.
            """
            self.vcsa_embedded = vcsa_embedded
            self.psc = psc
            self.vcsa_external = vcsa_external
            VapiStruct.__init__(self)


    SsoConfigurationDestinationAppliance._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.sso_configuration_destination_appliance', {
            'vcsa_embedded': type.OptionalType(type.ReferenceType(__name__, 'Validation.SsoConfigurationVcsaEmbedded')),
            'psc': type.OptionalType(type.ReferenceType(__name__, 'Validation.SsoConfigurationPsc')),
            'vcsa_external': type.OptionalType(type.ReferenceType(__name__, 'ExternalVcsa')),
        },
        SsoConfigurationDestinationAppliance,
        False,
        None))


    class SsoConfigurationVcsaEmbedded(VapiStruct):
        """
        Spec used to configure an embedded vCenter Server. This field describes how
        the embedded vCenter Server appliance should be configured.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     standalone=None,
                     replicated=None,
                    ):
            """
            :type  standalone: :class:`EmbeddedStandaloneVcsa` or ``None``
            :param standalone: Spec used to configure a standalone embedded vCenter Server. This
                field describes how the standalone vCenter Server appliance should
                be configured.
                Mutually exclusive between ``standalone`` and ``replicated``
            :type  replicated: :class:`EmbeddedReplicatedVcsa` or ``None``
            :param replicated: Spec used to configure a replicated embedded vCenter Server. This
                field describes how the replicated vCenter Server appliance should
                be configured.
                Mutually exclusive between ``standalone`` and ``replicated``
            """
            self.standalone = standalone
            self.replicated = replicated
            VapiStruct.__init__(self)


    SsoConfigurationVcsaEmbedded._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.sso_configuration_vcsa_embedded', {
            'standalone': type.OptionalType(type.ReferenceType(__name__, 'EmbeddedStandaloneVcsa')),
            'replicated': type.OptionalType(type.ReferenceType(__name__, 'EmbeddedReplicatedVcsa')),
        },
        SsoConfigurationVcsaEmbedded,
        False,
        None))


    class SsoConfigurationPsc(VapiStruct):
        """
        Spec used to configure a Platform Services Controller. This section
        describes how the Platform Services Controller appliance should be
        configured. If unset, either ``#vcsaEmbedded`` or ``#vcsaExternal`` must be
        provided.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     standalone=None,
                     replicated=None,
                    ):
            """
            :type  standalone: :class:`PscStandalone` or ``None``
            :param standalone: Spec used to configure a standalone Platform Services Controller.
                This section describes how the standalone PSC should be configured.
                Mutually exclusive between ``standalone`` and ``replicated``
            :type  replicated: :class:`PscReplicated` or ``None``
            :param replicated: Spec used to configure a replicated Platform Services Controller.
                This section describes how the replicated PSC should be configured.
                Mutually exclusive between ``standalone`` and ``replicated``
            """
            self.standalone = standalone
            self.replicated = replicated
            VapiStruct.__init__(self)


    SsoConfigurationPsc._set_binding_type(type.StructType(
        'com.vmware.vcenter.lcm.validation.sso_configuration_psc', {
            'standalone': type.OptionalType(type.ReferenceType(__name__, 'PscStandalone')),
            'replicated': type.OptionalType(type.ReferenceType(__name__, 'PscReplicated')),
        },
        SsoConfigurationPsc,
        False,
        None))




    def check_appliance_name_task(self,
                             spec,
                             ):
        """
        Validate the name of the appliance to be deployed. 
        
        #. 1. Return False if the there is already an appliance that has the
           same name as given in the spec exist in the path.

        :type  spec: :class:`Validation.ApplianceNameRequest`
        :param spec: The configuration needed to validate the name of the appliance to
            be deployed.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_appliance_name$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance


    def check_os_password_task(self,
                          spec,
                          ):
        """
        Validate if the given password conforms password policy. 
        
        #. 1. Return False if the password in the spec violates password policy

        :type  spec: :class:`Validation.OsPasswordRequest`
        :param spec: The configuration needed to validate the given password against
            password policy.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_os_password$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance


    def check_network_task(self,
                      spec,
                      ):
        """
        Check to see if the given network configuration is valid. 
        
        #. 1. Return False if the given network will cause conflict.
        #. 2. Always return True if network mode is set to DHCP.

        :type  spec: :class:`Validation.NetworkRequest`
        :param spec:  The configuration needed to validate network.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_network$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance


    def check_host_config_task(self,
                          spec,
                          ):
        """
        Validate the host configuration. 
        
        #. 1. Return False if the provided appliance type, appliance size, and
           disk size combination is not valid.
        #. 2. Return False if the provided deployment path does not have
           sufficient memory allocated.
        #. 3. Return False if the provided deployment path does not have
           sufficient cpu allocated.
        #. 3. Return False if the provided deployment path does not have
           sufficient datastore space.

        :type  spec: :class:`Validation.HostConfigRequest`
        :param spec:  The configuration needed to validate host configuration.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_host_config$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance


    def check_destination_location_task(self,
                                   spec,
                                   ):
        """
        Validate the ESX of the appliance to be deployed.

        :type  spec: :class:`Validation.DestinationLocationRequest`
        :param spec: The configuration needed to validate the ESX of the appliance to be
            deployed.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_destination_location$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance


    def check_temporary_network_task(self,
                                spec,
                                ):
        """
        Check to see if the given network configuration is valid. 
        
        #. 1. Return False if the given network will cause conflict.
        #. 2. Always return True if network mode is set to DHCP.

        :type  spec: :class:`Validation.TemporaryNetworkRequest`
        :param spec:  The configuration needed to validate network.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_temporary_network$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance


    def check_source_vum_task(self,
                         spec,
                         ):
        """
        Validate the source VUM configuration.

        :type  spec: :class:`Validation.SourceVumRequest`
        :param spec:  The configuration needed to validate the source VUM.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_source_vum$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance


    def check_upgrade_source_appliance_task(self,
                                       spec,
                                       ):
        """
        Validate the source appliance to be upgraded. 
        
        #. 1. Return False if the provided source appliance credentials are
           incorrect
        #. 2. Return False if the provided source location credentials are
           incorrect.
        #. 3. Return False if upgrade runner precheck results in error.
        #. 4. Return False if export directory provided is invalid.

        :type  spec: :class:`Validation.UpgradeSourceApplianceRequest`
        :param spec:  The configuration of the source appliance to be upgraded.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_upgrade_source_appliance$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance


    def check_migrate_source_appliance_task(self,
                                       spec,
                                       ):
        """
        Validate the source appliance to be migrated. 
        
        #. 1. Return False if the provided source windows vc credentials are
           incorrect
        #. 2. Return False if migration assistant precheck results in error.

        :type  spec: :class:`Validation.MigrateSourceApplianceRequest`
        :param spec:  The configuration of the source appliance to be migrated.
        :rtype: :class:  `vmware.vapi.stdlib.client.task.Task`
        :return: Task instance
        """
        task_id = self._invoke('check_migrate_source_appliance$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.BooleanType())
        return task_instance
class _InstallStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Install.Spec'),
            'options': type.OptionalType(type.ReferenceType(__name__, 'DeploymentOption')),
        })
        check_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        check_input_value_validator_list = [
        ]
        check_output_validator_list = [
        ]
        check_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/install?action=check',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for start operation
        start_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Install.Spec'),
        })
        start_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        start_input_value_validator_list = [
        ]
        start_output_validator_list = [
        ]
        start_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/install?action=start',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'check$task': {
                'input_type': check_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_error_dict,
                'input_value_validator_list': check_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'start$task': {
                'input_type': start_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': start_error_dict,
                'input_value_validator_list': start_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'check': check_rest_metadata,
            'start': start_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.lcm.install',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _LogStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'task_id': type.IdType(resource_types='com.vmware.cis.task'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/lcm/logs/{taskId}',
            path_variables={
                'task_id': 'taskId',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.URIType(),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.lcm.log',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _MigrateStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Migrate.Spec'),
            'options': type.OptionalType(type.ReferenceType(__name__, 'DeploymentOption')),
        })
        check_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        check_input_value_validator_list = [
        ]
        check_output_validator_list = [
        ]
        check_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/migration?action=check',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for start operation
        start_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Migrate.Spec'),
        })
        start_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        start_input_value_validator_list = [
        ]
        start_output_validator_list = [
        ]
        start_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/migration?action=start',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'check$task': {
                'input_type': check_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_error_dict,
                'input_value_validator_list': check_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'start$task': {
                'input_type': start_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': start_error_dict,
                'input_value_validator_list': start_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'check': check_rest_metadata,
            'start': start_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.lcm.migrate',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _RecommendationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for scan_migrate_deployment_size operation
        scan_migrate_deployment_size_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Recommendation.MigrateDeploymentSizeRequest'),
        })
        scan_migrate_deployment_size_error_dict = {}
        scan_migrate_deployment_size_input_value_validator_list = [
        ]
        scan_migrate_deployment_size_output_validator_list = [
        ]
        scan_migrate_deployment_size_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/recommendation?action=scan-migrate-deployment-size',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for scan_datastore operation
        scan_datastore_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Recommendation.DatastoreRequest'),
        })
        scan_datastore_error_dict = {}
        scan_datastore_input_value_validator_list = [
        ]
        scan_datastore_output_validator_list = [
        ]
        scan_datastore_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/recommendation?action=scan-datastore',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for scan_upgrade_deployment_size operation
        scan_upgrade_deployment_size_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Recommendation.UpgradeDeploymentSizeRequest'),
        })
        scan_upgrade_deployment_size_error_dict = {}
        scan_upgrade_deployment_size_input_value_validator_list = [
        ]
        scan_upgrade_deployment_size_output_validator_list = [
        ]
        scan_upgrade_deployment_size_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/recommendation?action=scan-upgrade-deployment-size',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'scan_migrate_deployment_size$task': {
                'input_type': scan_migrate_deployment_size_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': scan_migrate_deployment_size_error_dict,
                'input_value_validator_list': scan_migrate_deployment_size_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'scan_datastore$task': {
                'input_type': scan_datastore_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': scan_datastore_error_dict,
                'input_value_validator_list': scan_datastore_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'scan_upgrade_deployment_size$task': {
                'input_type': scan_upgrade_deployment_size_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': scan_upgrade_deployment_size_error_dict,
                'input_value_validator_list': scan_upgrade_deployment_size_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'scan_migrate_deployment_size': scan_migrate_deployment_size_rest_metadata,
            'scan_datastore': scan_datastore_rest_metadata,
            'scan_upgrade_deployment_size': scan_upgrade_deployment_size_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.lcm.recommendation',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _UpgradeStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Upgrade.Spec'),
            'options': type.OptionalType(type.ReferenceType(__name__, 'DeploymentOption')),
        })
        check_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        check_input_value_validator_list = [
        ]
        check_output_validator_list = [
        ]
        check_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/upgrade?action=check',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for start operation
        start_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Upgrade.Spec'),
        })
        start_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        start_input_value_validator_list = [
        ]
        start_output_validator_list = [
        ]
        start_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/upgrade?action=start',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'check$task': {
                'input_type': check_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_error_dict,
                'input_value_validator_list': check_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'start$task': {
                'input_type': start_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': start_error_dict,
                'input_value_validator_list': start_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'check': check_rest_metadata,
            'start': start_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.lcm.upgrade',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ValidationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for check_appliance_name operation
        check_appliance_name_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.ApplianceNameRequest'),
        })
        check_appliance_name_error_dict = {}
        check_appliance_name_input_value_validator_list = [
        ]
        check_appliance_name_output_validator_list = [
        ]
        check_appliance_name_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-appliance-name',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_os_password operation
        check_os_password_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.OsPasswordRequest'),
        })
        check_os_password_error_dict = {}
        check_os_password_input_value_validator_list = [
        ]
        check_os_password_output_validator_list = [
        ]
        check_os_password_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-os-password',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_network operation
        check_network_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.NetworkRequest'),
        })
        check_network_error_dict = {}
        check_network_input_value_validator_list = [
        ]
        check_network_output_validator_list = [
        ]
        check_network_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-network',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_host_config operation
        check_host_config_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.HostConfigRequest'),
        })
        check_host_config_error_dict = {}
        check_host_config_input_value_validator_list = [
        ]
        check_host_config_output_validator_list = [
        ]
        check_host_config_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-host-config',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_destination_location operation
        check_destination_location_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.DestinationLocationRequest'),
        })
        check_destination_location_error_dict = {}
        check_destination_location_input_value_validator_list = [
        ]
        check_destination_location_output_validator_list = [
        ]
        check_destination_location_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-destination-location',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_temporary_network operation
        check_temporary_network_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.TemporaryNetworkRequest'),
        })
        check_temporary_network_error_dict = {}
        check_temporary_network_input_value_validator_list = [
        ]
        check_temporary_network_output_validator_list = [
        ]
        check_temporary_network_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-temporary-network',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_source_vum operation
        check_source_vum_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.SourceVumRequest'),
        })
        check_source_vum_error_dict = {}
        check_source_vum_input_value_validator_list = [
        ]
        check_source_vum_output_validator_list = [
        ]
        check_source_vum_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-source-vum',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_upgrade_source_appliance operation
        check_upgrade_source_appliance_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.UpgradeSourceApplianceRequest'),
        })
        check_upgrade_source_appliance_error_dict = {}
        check_upgrade_source_appliance_input_value_validator_list = [
        ]
        check_upgrade_source_appliance_output_validator_list = [
        ]
        check_upgrade_source_appliance_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-upgrade-source-appliance',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_migrate_source_appliance operation
        check_migrate_source_appliance_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Validation.MigrateSourceApplianceRequest'),
        })
        check_migrate_source_appliance_error_dict = {}
        check_migrate_source_appliance_input_value_validator_list = [
        ]
        check_migrate_source_appliance_output_validator_list = [
        ]
        check_migrate_source_appliance_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/lcm/validation?action=check-migrate-source-appliance',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'check_appliance_name$task': {
                'input_type': check_appliance_name_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_appliance_name_error_dict,
                'input_value_validator_list': check_appliance_name_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check_os_password$task': {
                'input_type': check_os_password_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_os_password_error_dict,
                'input_value_validator_list': check_os_password_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check_network$task': {
                'input_type': check_network_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_network_error_dict,
                'input_value_validator_list': check_network_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check_host_config$task': {
                'input_type': check_host_config_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_host_config_error_dict,
                'input_value_validator_list': check_host_config_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check_destination_location$task': {
                'input_type': check_destination_location_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_destination_location_error_dict,
                'input_value_validator_list': check_destination_location_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check_temporary_network$task': {
                'input_type': check_temporary_network_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_temporary_network_error_dict,
                'input_value_validator_list': check_temporary_network_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check_source_vum$task': {
                'input_type': check_source_vum_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_source_vum_error_dict,
                'input_value_validator_list': check_source_vum_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check_upgrade_source_appliance$task': {
                'input_type': check_upgrade_source_appliance_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_upgrade_source_appliance_error_dict,
                'input_value_validator_list': check_upgrade_source_appliance_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'check_migrate_source_appliance$task': {
                'input_type': check_migrate_source_appliance_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': check_migrate_source_appliance_error_dict,
                'input_value_validator_list': check_migrate_source_appliance_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'check_appliance_name': check_appliance_name_rest_metadata,
            'check_os_password': check_os_password_rest_metadata,
            'check_network': check_network_rest_metadata,
            'check_host_config': check_host_config_rest_metadata,
            'check_destination_location': check_destination_location_rest_metadata,
            'check_temporary_network': check_temporary_network_rest_metadata,
            'check_source_vum': check_source_vum_rest_metadata,
            'check_upgrade_source_appliance': check_upgrade_source_appliance_rest_metadata,
            'check_migrate_source_appliance': check_migrate_source_appliance_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.lcm.validation',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Install': Install,
        'Log': Log,
        'Migrate': Migrate,
        'Recommendation': Recommendation,
        'Upgrade': Upgrade,
        'Validation': Validation,
    }

