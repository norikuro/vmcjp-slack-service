# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.sddcs.addons.
#---------------------------------------------------------------------------

"""


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


class Credentials(VapiInterface):
    """
    
    """
    CREATE_ADDON_TYPE_HCX = "HCX"
    """
    Possible value for ``addonType`` of method :func:`Credentials.create`.

    """
    GET_ADDON_TYPE_HCX = "HCX"
    """
    Possible value for ``addonType`` of method :func:`Credentials.get`.

    """
    LIST_ADDON_TYPE_HCX = "HCX"
    """
    Possible value for ``addonType`` of method :func:`Credentials.list`.

    """
    UPDATE_ADDON_TYPE_HCX = "HCX"
    """
    Possible value for ``addonType`` of method :func:`Credentials.update`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddcs.addons.credentials'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CredentialsStub)


    def create(self,
               org,
               sddc_id,
               addon_type,
               credentials,
               ):
        """
        Associated a new add on credentials with the SDDC such as HCX

        :type  org: :class:`str`
        :param org: Org id of the associated SDDC (required)
        :type  sddc_id: :class:`str`
        :param sddc_id: Id of the SDDC (required)
        :type  addon_type: :class:`str`
        :param addon_type: Add on type (required)
        :type  credentials: :class:`com.vmware.vmc.model_client.NewCredentials`
        :param credentials: Credentials creation payload (required)
        :rtype: :class:`com.vmware.vmc.model_client.NewCredentials`
        :return: com.vmware.vmc.model.NewCredentials
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Credentials with same name exists with in the scope of addOnType
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid input
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'sddc_id': sddc_id,
                            'addon_type': addon_type,
                            'credentials': credentials,
                            })

    def get(self,
            org,
            sddc_id,
            addon_type,
            name,
            ):
        """
        Get credential details by name

        :type  org: :class:`str`
        :param org: Org id of the associated SDDC (required)
        :type  sddc_id: :class:`str`
        :param sddc_id: Id of the SDDC (required)
        :type  addon_type: :class:`str`
        :param addon_type: Add on type (required)
        :type  name: :class:`str`
        :param name: name of the credentials (required)
        :rtype: :class:`com.vmware.vmc.model_client.NewCredentials`
        :return: com.vmware.vmc.model.NewCredentials
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc_id': sddc_id,
                            'addon_type': addon_type,
                            'name': name,
                            })

    def list(self,
             org,
             sddc_id,
             addon_type,
             ):
        """
        List all the credentials assoicated with an addon type with in a SDDC

        :type  org: :class:`str`
        :param org: Org id of the associated SDDC (required)
        :type  sddc_id: :class:`str`
        :param sddc_id: Id of the SDDC (required)
        :type  addon_type: :class:`str`
        :param addon_type: Add on type (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.NewCredentials`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('list',
                            {
                            'org': org,
                            'sddc_id': sddc_id,
                            'addon_type': addon_type,
                            })

    def update(self,
               org,
               sddc_id,
               addon_type,
               name,
               credentials,
               ):
        """
        Update credential details

        :type  org: :class:`str`
        :param org: Org id of the associated SDDC (required)
        :type  sddc_id: :class:`str`
        :param sddc_id: Id of the SDDC (required)
        :type  addon_type: :class:`str`
        :param addon_type: Add on type (required)
        :type  name: :class:`str`
        :param name: name of the credentials (required)
        :type  credentials: :class:`com.vmware.vmc.model_client.UpdateCredentials`
        :param credentials: Credentials update payload (required)
        :rtype: :class:`com.vmware.vmc.model_client.NewCredentials`
        :return: com.vmware.vmc.model.NewCredentials
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('update',
                            {
                            'org': org,
                            'sddc_id': sddc_id,
                            'addon_type': addon_type,
                            'name': name,
                            'credentials': credentials,
                            })
class _CredentialsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc_id': type.StringType(),
            'addon_type': type.StringType(),
            'credentials': type.ReferenceType('com.vmware.vmc.model_client', 'NewCredentials'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddcId}/addons/{addonType}/credentials',
            request_body_parameter='credentials',
            path_variables={
                'org': 'org',
                'sddc_id': 'sddcId',
                'addon_type': 'addonType',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc_id': type.StringType(),
            'addon_type': type.StringType(),
            'name': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddcId}/addons/{addonType}/credentials/{name}',
            path_variables={
                'org': 'org',
                'sddc_id': 'sddcId',
                'addon_type': 'addonType',
                'name': 'name',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc_id': type.StringType(),
            'addon_type': type.StringType(),
        })
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddcId}/addons/{addonType}/credentials',
            path_variables={
                'org': 'org',
                'sddc_id': 'sddcId',
                'addon_type': 'addonType',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc_id': type.StringType(),
            'addon_type': type.StringType(),
            'name': type.StringType(),
            'credentials': type.ReferenceType('com.vmware.vmc.model_client', 'UpdateCredentials'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddcId}/addons/{addonType}/credentials/{name}',
            request_body_parameter='credentials',
            path_variables={
                'org': 'org',
                'sddc_id': 'sddcId',
                'addon_type': 'addonType',
                'name': 'name',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'NewCredentials'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'NewCredentials'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'NewCredentials')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'NewCredentials'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.addons.credentials',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Credentials': Credentials,
    }

