# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.compute.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.compute_client`` module provides classes for managing
compute policies.

"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

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


class Policies(VapiInterface):
    """
    The ``Policies`` class provides methods to manage compute policies. A
    compute policy defines the intended behavior for a collection of vSphere
    objects identified by a tag. A compute policy is an instance of a
    capability. It is created by providing a value for the creation type
    specified by the capability. See
    :attr:`com.vmware.vcenter.compute.policies_client.Capabilities.Info.create_spec_type`.
    **Warning:** This class is available as technical preview. It may be
    changed in a future release.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.compute.Policy"
    """
    The resource type for the compute policy. **Warning:** This class attribute is
    available as technical preview. It may be changed in a future release.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.compute.policies'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PoliciesStub)

    class Summary(VapiStruct):
        """
        The ``Policies.Summary`` class contains commonly used information about a
        compute policy. **Warning:** This class is available as technical preview.
        It may be changed in a future release.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     policy=None,
                     name=None,
                     description=None,
                     capability=None,
                    ):
            """
            :type  policy: :class:`str`
            :param policy: Identifier of the policy. **Warning:** This attribute is available
                as technical preview. It may be changed in a future release.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.compute.Policy``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.compute.Policy``.
            :type  name: :class:`str`
            :param name: Name of the policy. **Warning:** This attribute is available as
                technical preview. It may be changed in a future release.
            :type  description: :class:`str`
            :param description: Description of the policy. **Warning:** This attribute is available
                as technical preview. It may be changed in a future release.
            :type  capability: :class:`str`
            :param capability: Identifier of the capability this policy is based on. **Warning:**
                This attribute is available as technical preview. It may be changed
                in a future release.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.compute.policies.Capability``. When methods
                return a value of this class as a return value, the attribute will
                be an identifier for the resource type:
                ``com.vmware.vcenter.compute.policies.Capability``.
            """
            self.policy = policy
            self.name = name
            self.description = description
            self.capability = capability
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.compute.policies.summary', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.compute.Policy'),
            'name': type.StringType(),
            'description': type.StringType(),
            'capability': type.IdType(resource_types='com.vmware.vcenter.compute.policies.Capability'),
        },
        Summary,
        False,
        None))



    def create(self,
               spec,
               ):
        """
        Creates a new compute policy. **Warning:** This method is available as
        technical preview. It may be changed in a future release.

        :type  spec: :class:`vmware.vapi.struct.VapiStruct`
        :param spec: Specification for the new policy to be created. The new policy will
            be an instance of the capability that has the creation type (see
            :attr:`com.vmware.vcenter.compute.policies_client.Capabilities.Info.create_spec_type`)
            equal to the type of the specified value (see ``spec``).
            The parameter must contain all the attributes defined in
            :class:`com.vmware.vcenter.compute.policies_client.CreateSpec`.
        :rtype: :class:`str`
        :return: The identifier of the newly created policy. Use this identifier to
            get or destroy the policy.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.compute.Policy``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if a policy with the same name is already present on this vCenter
            server.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if a parameter passed in the spec is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 100 policies are created.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``ComputePolicy.Manage``.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })

    def list(self):
        """
        Returns information about the compute policies available in this
        vCenter server. **Warning:** This method is available as technical
        preview. It may be changed in a future release.


        :rtype: :class:`list` of :class:`Policies.Summary`
        :return: The list of compute policies available on this vCenter server.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('list', None)

    def get(self,
            policy,
            ):
        """
        Returns information about a specific compute policy. **Warning:** This
        method is available as technical preview. It may be changed in a future
        release.

        :type  policy: :class:`str`
        :param policy: Identifier of the policy for which information should be retrieved.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.compute.Policy``.
        :rtype: :class:`vmware.vapi.struct.VapiStruct`
        :return: Detailed information about the specified compute policy. The
            returned value can be converted to the information type of the
            capability that this policy is based on. See
            :attr:`com.vmware.vcenter.compute.policies_client.Capabilities.Info.info_type`.
            The return value will contain all the attributes defined in
            :class:`com.vmware.vcenter.compute.policies_client.Info`.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a policy with this identifier does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'policy': policy,
                            })

    def delete(self,
               policy,
               ):
        """
        Deletes a specific compute policy. **Warning:** This method is
        available as technical preview. It may be changed in a future release.

        :type  policy: :class:`str`
        :param policy: Identifier of the policy to be deleted.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.compute.Policy``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a policy with this identifier does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``ComputePolicy.Manage``.
        """
        return self._invoke('delete',
                            {
                            'policy': policy,
                            })
class _PoliciesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.vcenter.compute.policies_client', 'CreateSpec')]),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/compute/policies',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/compute/policies',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.compute.Policy'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/compute/policies/{policy}',
            path_variables={
                'policy': 'policy',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.compute.Policy'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/compute/policies/{policy}',
            path_variables={
                'policy': 'policy',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.compute.Policy'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Policies.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [type.ReferenceType('com.vmware.vcenter.compute.policies_client', 'Info')]),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.compute.policies',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Policies': Policies,
        'policies': 'com.vmware.vcenter.compute.policies_client.StubFactory',
    }

