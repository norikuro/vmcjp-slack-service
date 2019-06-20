# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.node.users.
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


class SshKeys(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SshKeysStub)


    def addsshkey(self,
                  userid,
                  ssh_key_properties,
                  ):
        """
        Add SSH public key to authorized_keys file for node user

        :type  userid: :class:`str`
        :param userid: User id of the user (required)
        :type  ssh_key_properties: :class:`com.vmware.nsx.model_client.SshKeyProperties`
        :param ssh_key_properties: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('addsshkey',
                            {
                            'userid': userid,
                            'ssh_key_properties': ssh_key_properties,
                            })

    def list(self,
             userid,
             ):
        """
        Returns a list of all SSH keys from authorized_keys file for node user

        :type  userid: :class:`str`
        :param userid: User id of the user (required)
        :rtype: :class:`com.vmware.nsx.model_client.SshKeyPropertiesListResult`
        :return: com.vmware.nsx.model.SshKeyPropertiesListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'userid': userid,
                            })

    def removesshkey(self,
                     userid,
                     ssh_key_base_properties,
                     ):
        """
        Remove SSH public key from authorized_keys file for node user

        :type  userid: :class:`str`
        :param userid: User id of the user (required)
        :type  ssh_key_base_properties: :class:`com.vmware.nsx.model_client.SshKeyBaseProperties`
        :param ssh_key_base_properties: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('removesshkey',
                            {
                            'userid': userid,
                            'ssh_key_base_properties': ssh_key_base_properties,
                            })
class _SshKeysStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for addsshkey operation
        addsshkey_input_type = type.StructType('operation-input', {
            'userid': type.StringType(),
            'ssh_key_properties': type.ReferenceType('com.vmware.nsx.model_client', 'SshKeyProperties'),
        })
        addsshkey_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        addsshkey_input_value_validator_list = [
        ]
        addsshkey_output_validator_list = [
        ]
        addsshkey_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/node/users/{userid}/ssh-keys?action=add_ssh_key',
            request_body_parameter='ssh_key_properties',
            path_variables={
                'userid': 'userid',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'userid': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/node/users/{userid}/ssh-keys',
            path_variables={
                'userid': 'userid',
            },
            query_parameters={
            }
        )

        # properties for removesshkey operation
        removesshkey_input_type = type.StructType('operation-input', {
            'userid': type.StringType(),
            'ssh_key_base_properties': type.ReferenceType('com.vmware.nsx.model_client', 'SshKeyBaseProperties'),
        })
        removesshkey_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        removesshkey_input_value_validator_list = [
        ]
        removesshkey_output_validator_list = [
        ]
        removesshkey_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/node/users/{userid}/ssh-keys?action=remove_ssh_key',
            request_body_parameter='ssh_key_base_properties',
            path_variables={
                'userid': 'userid',
            },
            query_parameters={
            }
        )

        operations = {
            'addsshkey': {
                'input_type': addsshkey_input_type,
                'output_type': type.VoidType(),
                'errors': addsshkey_error_dict,
                'input_value_validator_list': addsshkey_input_value_validator_list,
                'output_validator_list': addsshkey_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'SshKeyPropertiesListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'removesshkey': {
                'input_type': removesshkey_input_type,
                'output_type': type.VoidType(),
                'errors': removesshkey_error_dict,
                'input_value_validator_list': removesshkey_input_value_validator_list,
                'output_validator_list': removesshkey_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'addsshkey': addsshkey_rest_metadata,
            'list': list_rest_metadata,
            'removesshkey': removesshkey_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.node.users.ssh_keys',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'SshKeys': SshKeys,
    }

