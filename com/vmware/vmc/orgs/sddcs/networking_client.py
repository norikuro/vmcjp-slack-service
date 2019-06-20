# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.sddcs.networking.
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


class ConnectivityTests(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddcs.networking.connectivity_tests'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ConnectivityTestsStub)


    def get(self,
            org,
            sddc,
            ):
        """
        Retrieve metadata for connectivity tests.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :rtype: :class:`com.vmware.vmc.model_client.ConnectivityValidationGroups`
        :return: com.vmware.vmc.model.ConnectivityValidationGroups
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            })

    def post(self,
             org,
             sddc,
             request_info,
             action,
             ):
        """
        ConnectivityValidationGroupResultWrapper will be available at
        task.params['test_result'].

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  request_info: :class:`com.vmware.vmc.model_client.ConnectivityValidationGroup`
        :param request_info: request information (required)
        :type  action: :class:`str`
        :param action: If = 'start', start connectivity tests. (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('post',
                            {
                            'org': org,
                            'sddc': sddc,
                            'request_info': request_info,
                            'action': action,
                            })
class _ConnectivityTestsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networking/connectivity-tests',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for post operation
        post_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'request_info': type.ReferenceType('com.vmware.vmc.model_client', 'ConnectivityValidationGroup'),
            'action': type.StringType(),
        })
        post_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        post_input_value_validator_list = [
        ]
        post_output_validator_list = [
        ]
        post_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networking/connectivity-tests',
            request_body_parameter='request_info',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'action': 'action',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'ConnectivityValidationGroups'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'post': {
                'input_type': post_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': post_error_dict,
                'input_value_validator_list': post_input_value_validator_list,
                'output_validator_list': post_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'post': post_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.networking.connectivity_tests',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ConnectivityTests': ConnectivityTests,
    }

