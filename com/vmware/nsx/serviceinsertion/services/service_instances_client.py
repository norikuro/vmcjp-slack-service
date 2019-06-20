# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.serviceinsertion.services.service_instances.
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


class InstanceEndpoints(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InstanceEndpointsStub)


    def create(self,
               service_id,
               service_instance_id,
               instance_endpoint,
               ):
        """
        Adds a new instance endpoint. It belongs to one service instance and is
        attached to one service attachment. It represents a redirection target
        for a Rule.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
        :type  instance_endpoint: :class:`com.vmware.nsx.model_client.InstanceEndpoint`
        :param instance_endpoint: (required)
        :rtype: :class:`com.vmware.nsx.model_client.InstanceEndpoint`
        :return: com.vmware.nsx.model.InstanceEndpoint
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
        return self._invoke('create',
                            {
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            'instance_endpoint': instance_endpoint,
                            })

    def delete(self,
               service_id,
               service_instance_id,
               instance_endpoint,
               ):
        """
        Delete instance endpoint information for a given instace endpoint.
        Please make sure to delete all the Service Insertion Rules, which refer
        to this Endpoint as 'redirect_tos' target.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
        :type  instance_endpoint: :class:`str`
        :param instance_endpoint: (required)
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
        return self._invoke('delete',
                            {
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            'instance_endpoint': instance_endpoint,
                            })

    def get(self,
            service_id,
            service_instance_id,
            instance_endpoint,
            ):
        """
        Returns detailed Endpoint information for a given InstanceEndpoint.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
        :type  instance_endpoint: :class:`str`
        :param instance_endpoint: (required)
        :rtype: :class:`com.vmware.nsx.model_client.InstanceEndpoint`
        :return: com.vmware.nsx.model.InstanceEndpoint
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
        return self._invoke('get',
                            {
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            'instance_endpoint': instance_endpoint,
                            })

    def list(self,
             service_id,
             service_instance_id,
             ):
        """
        List all InstanceEndpoints of a service instance.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.InstanceEndpointListResult`
        :return: com.vmware.nsx.model.InstanceEndpointListResult
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
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            })
class InstanceRuntimes(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InstanceRuntimesStub)


    def delete(self,
               service_id,
               service_instance_id,
               ):
        """
        Undeploy one service VM as standalone or two service VMs as HA.
        Associated deployment information and instance runtime will also be
        deleted once service VMs have been un-deployed successfully.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
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
        return self._invoke('delete',
                            {
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            })

    def deploy(self,
               service_id,
               service_instance_id,
               ):
        """
        Deploys one service VM as standalone, or two service VMs as HA where
        one VM is active and another one is standby. During the deployment of
        service VMs, service will be set up based on deployment events using
        callbacks.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
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
        return self._invoke('deploy',
                            {
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            })

    def list(self,
             service_id,
             service_instance_id,
             ):
        """
        Returns list of instance runtimes of service VMs being deployed for a
        given service instance id

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.InstanceRuntimeListResult`
        :return: com.vmware.nsx.model.InstanceRuntimeListResult
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
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            })

    def upgrade(self,
                service_id,
                service_instance_id,
                ):
        """
        Upgrade service VMs using newer version of OVF. In case of HA, the
        stand-by service VM will be upgrade first. Once it has been upgraded,
        it switches to be the Active one and then the other VM will be upgrade.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
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
        return self._invoke('upgrade',
                            {
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            })
class _InstanceEndpointsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'instance_endpoint': type.ReferenceType('com.vmware.nsx.model_client', 'InstanceEndpoint'),
        })
        create_error_dict = {
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
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-endpoints',
            request_body_parameter='instance_endpoint',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'instance_endpoint': type.StringType(),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-endpoints/{instance-endpoint}',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
                'instance_endpoint': 'instance-endpoint',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'instance_endpoint': type.StringType(),
        })
        get_error_dict = {
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
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-endpoints/{instance-endpoint}',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
                'instance_endpoint': 'instance-endpoint',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-endpoints',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'InstanceEndpoint'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
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
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'InstanceEndpoint'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'InstanceEndpointListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.services.service_instances.instance_endpoints',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _InstanceRuntimesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes?action=delete',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            }
        )

        # properties for deploy operation
        deploy_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
        })
        deploy_error_dict = {
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
        deploy_input_value_validator_list = [
        ]
        deploy_output_validator_list = [
        ]
        deploy_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes?action=deploy',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            }
        )

        # properties for upgrade operation
        upgrade_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
        })
        upgrade_error_dict = {
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
        upgrade_input_value_validator_list = [
        ]
        upgrade_output_validator_list = [
        ]
        upgrade_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes?action=upgrade',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
            },
            query_parameters={
            }
        )

        operations = {
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'deploy': {
                'input_type': deploy_input_type,
                'output_type': type.VoidType(),
                'errors': deploy_error_dict,
                'input_value_validator_list': deploy_input_value_validator_list,
                'output_validator_list': deploy_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'InstanceRuntimeListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'upgrade': {
                'input_type': upgrade_input_type,
                'output_type': type.VoidType(),
                'errors': upgrade_error_dict,
                'input_value_validator_list': upgrade_input_value_validator_list,
                'output_validator_list': upgrade_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'deploy': deploy_rest_metadata,
            'list': list_rest_metadata,
            'upgrade': upgrade_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.services.service_instances.instance_runtimes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'InstanceEndpoints': InstanceEndpoints,
        'InstanceRuntimes': InstanceRuntimes,
    }

