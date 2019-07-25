# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.system_config.
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


class DeploymentType(VapiInterface):
    """
    The ``DeploymentType`` class provides methods to get/set the type of the
    appliance. This class was added in vSphere API 6.7.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.system_config.deployment_type'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DeploymentTypeStub)

    class Info(VapiStruct):
        """
        The ``DeploymentType.Info`` class contains the fields used to get the
        appliance type. This class was added in vSphere API 6.7.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                    ):
            """
            :type  type: :class:`com.vmware.vcenter.deployment_client.ApplianceType`
            :param type: The type of the appliance. This attribute was added in vSphere API
                6.7.
            """
            self.type = type
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.deployment_type.info', {
            'type': type.ReferenceType('com.vmware.vcenter.deployment_client', 'ApplianceType'),
        },
        Info,
        False,
        None))


    class ReconfigureSpec(VapiStruct):
        """
        The ``DeploymentType.ReconfigureSpec`` class contains the fields used to
        get and set the appliance type. This class was added in vSphere API 6.7.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                     remote_psc=None,
                    ):
            """
            :type  type: :class:`com.vmware.vcenter.deployment_client.ApplianceType`
            :param type: The type of the appliance. This attribute was added in vSphere API
                6.7.
            :type  remote_psc: :class:`com.vmware.vcenter.deployment_client.RemotePscSpec` or ``None``
            :param remote_psc: External PSC to register with when reconfiguring a VCSA_EMBEDDED
                appliance to a VCSA_EXTERNAL appliance. This attribute was added in
                vSphere API 6.7.
                Only required when reconfiguring an VCSA_EMBEDDED node to a
                VCSA_EXTERNAL.
            """
            self.type = type
            self.remote_psc = remote_psc
            VapiStruct.__init__(self)


    ReconfigureSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.deployment_type.reconfigure_spec', {
            'type': type.ReferenceType('com.vmware.vcenter.deployment_client', 'ApplianceType'),
            'remote_psc': type.OptionalType(type.ReferenceType('com.vmware.vcenter.deployment_client', 'RemotePscSpec')),
        },
        ReconfigureSpec,
        False,
        None))


    class DomainInfo(VapiStruct):
        """
        The ``DeploymentType.DomainInfo`` class contains information used to join
        the converged node to the AD domain. This is used when participating PSC
        node is already joined to AD. This class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     ad_domain_name=None,
                     ad_domain_admin_username=None,
                     ad_domain_admin_password=None,
                     dns_server=None,
                    ):
            """
            :type  ad_domain_name: :class:`str`
            :param ad_domain_name: The Platform Services Controller node's AD domain name if exits.
                This attribute was added in vSphere API 6.7.2.
            :type  ad_domain_admin_username: :class:`str`
            :param ad_domain_admin_username: The AD domain username with privileges to join any machine to the
                provided domain. This attribute was added in vSphere API 6.7.2.
            :type  ad_domain_admin_password: :class:`str`
            :param ad_domain_admin_password: AD domain password with privileges to join any machine to the
                provided domain. This attribute was added in vSphere API 6.7.2.
            :type  dns_server: :class:`str`
            :param dns_server: IP address of the DNS server of the Active Directory server. This
                attribute was added in vSphere API 6.7.2.
            """
            self.ad_domain_name = ad_domain_name
            self.ad_domain_admin_username = ad_domain_admin_username
            self.ad_domain_admin_password = ad_domain_admin_password
            self.dns_server = dns_server
            VapiStruct.__init__(self)


    DomainInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.deployment_type.domain_info', {
            'ad_domain_name': type.StringType(),
            'ad_domain_admin_username': type.StringType(),
            'ad_domain_admin_password': type.SecretType(),
            'dns_server': type.StringType(),
        },
        DomainInfo,
        False,
        None))


    class PscInfo(VapiStruct):
        """
        The ``DeploymentType.PscInfo`` class contains information about Platform
        Services Controller node participating in reconfiguration. This class was
        added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     sso_admin_username=None,
                     sso_admin_password=None,
                     skip_ad_domain_join=None,
                     ad_domain=None,
                    ):
            """
            :type  sso_admin_username: :class:`str`
            :param sso_admin_username: The SSO administrator username for example
                "administrator\\\\@vsphere.local". This attribute was added in
                vSphere API 6.7.2.
            :type  sso_admin_password: :class:`str`
            :param sso_admin_password: The SSO administrator account password. This attribute was added in
                vSphere API 6.7.2.
            :type  skip_ad_domain_join: :class:`bool` or ``None``
            :param skip_ad_domain_join: A flag to skip domain join operation for embedded node during
                convergence. If the Platform Services Controller node is joined to
                an AD domain, the same is expected to be configured for converged
                embedded node, but there can be situations (e.g. no domain admin
                credentials with VI admin) during convergence when needs to be done
                later via existing UI option. This attribute was added in vSphere
                API 6.7.2.
                If :class:`set` will skip AD domain join operations
            :type  ad_domain: :class:`DeploymentType.DomainInfo` or ``None``
            :param ad_domain: Information about the domain which Platform Services Controller
                node is joined to. The reconfigured machine will be joined to the
                same domain. This attribute was added in vSphere API 6.7.2.
                If :class:`set` then converged embedded node will be joined to this
                AD domain.
            """
            self.sso_admin_username = sso_admin_username
            self.sso_admin_password = sso_admin_password
            self.skip_ad_domain_join = skip_ad_domain_join
            self.ad_domain = ad_domain
            VapiStruct.__init__(self)


    PscInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.deployment_type.psc_info', {
            'sso_admin_username': type.StringType(),
            'sso_admin_password': type.SecretType(),
            'skip_ad_domain_join': type.OptionalType(type.BooleanType()),
            'ad_domain': type.OptionalType(type.ReferenceType(__name__, 'DeploymentType.DomainInfo')),
        },
        PscInfo,
        False,
        None))


    class ConvergenceSpec(VapiStruct):
        """
        The ``DeploymentType.ConvergenceSpec`` class contains information used for
        vCenter external to embedded PSC convergence operation. This class was
        added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     psc=None,
                     replication_partner_hostname=None,
                     only_precheck=None,
                    ):
            """
            :type  psc: :class:`DeploymentType.PscInfo`
            :param psc: The information about the Platform Service Controller. This
                attribute was added in vSphere API 6.7.2.
            :type  replication_partner_hostname: :class:`str` or ``None``
            :param replication_partner_hostname: The (earlier converged) embedded node with which the Platform
                Services Controller replication has to be set during convergence.
                This attribute was added in vSphere API 6.7.2.
                If :class:`set` then the converged embedded node will be set in
                replication mode with this node.
            :type  only_precheck: :class:`bool` or ``None``
            :param only_precheck: Flag to pass if only pre-check to be performed. This attribute was
                added in vSphere API 6.7.2.
                If :class:`set` will perform only pre-checks.
            """
            self.psc = psc
            self.replication_partner_hostname = replication_partner_hostname
            self.only_precheck = only_precheck
            VapiStruct.__init__(self)


    ConvergenceSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.deployment_type.convergence_spec', {
            'psc': type.ReferenceType(__name__, 'DeploymentType.PscInfo'),
            'replication_partner_hostname': type.OptionalType(type.StringType()),
            'only_precheck': type.OptionalType(type.BooleanType()),
        },
        ConvergenceSpec,
        False,
        None))



    def get(self):
        """
        Get the type of the vCenter appliance. This method was added in vSphere
        API 6.7.


        :rtype: :class:`DeploymentType.Info`
        :return: The type of the vCenter appliance.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if appliance is not in CONFIGURED state.
        """
        return self._invoke('get', None)

    def reconfigure(self,
                    spec,
                    ):
        """
        Reconfigure the type of the vCenter appliance. This method was added in
        vSphere API 6.7.

        :type  spec: :class:`DeploymentType.ReconfigureSpec`
        :param spec: ReconfigureSpec to set the appliance type.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the appliance is in CONFIGURED state and if not changing the
            type from VCSA_EMBEDDED to VCSA_EXTERNAL.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if external PSC credentials are not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is not in INITIALIZED or CONFIGURED state.
        """
        return self._invoke('reconfigure',
                            {
                            'spec': spec,
                            })


    def convert_to_vcsa_embedded_task(self,
                                 spec,
                                 ):
        """
        Convert the type of the vCenter appliance to vCSA embedded. This method
        was added in vSphere API 6.7.2.

        :type  spec: :class:`DeploymentType.ConvergenceSpec`
        :param spec: ConvergenceSpec to provide all needed information for convergence
            operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the appliance is in not a management node.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is already an embedded node.
        """
        task_id = self._invoke('convert_to_vcsa_embedded$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance
class PscRegistration(VapiInterface):
    """
    The ``PscRegistration`` class provides methods to get and set the
    PSC_EXTERNAL appliance a VCSA_EXTERNAL appliance is registered with. This
    class was added in vSphere API 6.7.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.system_config.psc_registration'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PscRegistrationStub)

    class Info(VapiStruct):
        """
        The ``PscRegistration.Info`` class has fields to specify information about
        the PSC node. This class was added in vSphere API 6.7.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     address=None,
                     https_port=None,
                     sso_domain=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: The IP address or DNS resolvable name of the PSC this appliance is
                registered with. This attribute was added in vSphere API 6.7.
            :type  https_port: :class:`long`
            :param https_port: The HTTPs port used by the external PSC. This attribute was added
                in vSphere API 6.7.
            :type  sso_domain: :class:`str`
            :param sso_domain: The Single Sign-On domain name of the external PSC. This attribute
                was added in vSphere API 6.7.
            """
            self.address = address
            self.https_port = https_port
            self.sso_domain = sso_domain
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.psc_registration.info', {
            'address': type.StringType(),
            'https_port': type.IntegerType(),
            'sso_domain': type.StringType(),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Get information of the PSC that this appliance is registered with. This
        method was added in vSphere API 6.7.


        :rtype: :class:`PscRegistration.Info`
        :return: Info structure containing information about the external PSC node
            this appliance is registered with.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is in NOT_INITIALIZED state.
        """
        return self._invoke('get', None)

    def repoint(self,
                spec,
                ):
        """
        Repoint this vCenter Server appliance to a different external PSC. This
        method was added in vSphere API 6.7.

        :type  spec: :class:`com.vmware.vcenter.deployment_client.RemotePscSpec`
        :param spec: RemotePscSpec structure containing information about the external
            PSC node to repoint this vCenter Server appliance to.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the passed external PSC credentials is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the passed external PSC is not a replicating with the current
            PSC this appliance is registered with.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the current appliance is not of the type VCSA_EXTERNAL.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is NOT in CONFIGURED state.
        """
        return self._invoke('repoint',
                            {
                            'spec': spec,
                            })
class _DeploymentTypeStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/system-config/deployment-type',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for reconfigure operation
        reconfigure_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'DeploymentType.ReconfigureSpec'),
        })
        reconfigure_error_dict = {
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        reconfigure_input_value_validator_list = [
        ]
        reconfigure_output_validator_list = [
        ]
        reconfigure_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/system-config/deployment-type',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for convert_to_vcsa_embedded operation
        convert_to_vcsa_embedded_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'DeploymentType.ConvergenceSpec'),
        })
        convert_to_vcsa_embedded_error_dict = {
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        convert_to_vcsa_embedded_input_value_validator_list = [
        ]
        convert_to_vcsa_embedded_output_validator_list = [
        ]
        convert_to_vcsa_embedded_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/system-config/deployment-type?action=convert-to-vcsa-embedded',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'DeploymentType.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reconfigure': {
                'input_type': reconfigure_input_type,
                'output_type': type.VoidType(),
                'errors': reconfigure_error_dict,
                'input_value_validator_list': reconfigure_input_value_validator_list,
                'output_validator_list': reconfigure_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'convert_to_vcsa_embedded$task': {
                'input_type': convert_to_vcsa_embedded_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': convert_to_vcsa_embedded_error_dict,
                'input_value_validator_list': convert_to_vcsa_embedded_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'reconfigure': reconfigure_rest_metadata,
            'convert_to_vcsa_embedded': convert_to_vcsa_embedded_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.system_config.deployment_type',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PscRegistrationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/system-config/psc-registration',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for repoint operation
        repoint_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType('com.vmware.vcenter.deployment_client', 'RemotePscSpec'),
        })
        repoint_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        repoint_input_value_validator_list = [
        ]
        repoint_output_validator_list = [
        ]
        repoint_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/system-config/psc-registration',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'PscRegistration.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'repoint': {
                'input_type': repoint_input_type,
                'output_type': type.VoidType(),
                'errors': repoint_error_dict,
                'input_value_validator_list': repoint_input_value_validator_list,
                'output_validator_list': repoint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'repoint': repoint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.system_config.psc_registration',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'DeploymentType': DeploymentType,
        'PscRegistration': PscRegistration,
    }

