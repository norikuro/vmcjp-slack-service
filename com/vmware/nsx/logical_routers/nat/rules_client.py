# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.logical_routers.nat.rules.
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


class Statistics(VapiInterface):
    """
    
    """
    GETPERLOGICALROUTER_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Statistics.getperlogicalrouter`.

    """
    GETPERLOGICALROUTER_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Statistics.getperlogicalrouter`.

    """
    GETPERRULE_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Statistics.getperrule`.

    """
    GETPERRULE_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Statistics.getperrule`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatisticsStub)


    def getperlogicalrouter(self,
                            logical_router_id,
                            source=None,
                            ):
        """
        Returns the summation of statistics for all rules from all nodes for
        the Specified Logical Router. Also gives the per transport node
        statistics for provided logical router. The query parameter
        \\\\"source=realtime\\\\" is not supported.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.NatStatisticsPerLogicalRouter`
        :return: com.vmware.nsx.model.NatStatisticsPerLogicalRouter
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
        return self._invoke('getperlogicalrouter',
                            {
                            'logical_router_id': logical_router_id,
                            'source': source,
                            })

    def getperrule(self,
                   logical_router_id,
                   rule_id,
                   source=None,
                   ):
        """
        Returns the summation of statistics from all nodes for the Specified
        Logical Router NAT Rule. Query parameter \\\\"source=realtime\\\\" is
        the only supported source.

        :type  logical_router_id: :class:`str`
        :param logical_router_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.NatStatisticsPerRule`
        :return: com.vmware.nsx.model.NatStatisticsPerRule
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
        return self._invoke('getperrule',
                            {
                            'logical_router_id': logical_router_id,
                            'rule_id': rule_id,
                            'source': source,
                            })
class _StatisticsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for getperlogicalrouter operation
        getperlogicalrouter_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'source': type.OptionalType(type.StringType()),
        })
        getperlogicalrouter_error_dict = {
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
        getperlogicalrouter_input_value_validator_list = [
        ]
        getperlogicalrouter_output_validator_list = [
        ]
        getperlogicalrouter_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-routers/{logical-router-id}/nat/rules/statistics',
            path_variables={
                'logical_router_id': 'logical-router-id',
            },
            query_parameters={
                'source': 'source',
            }
        )

        # properties for getperrule operation
        getperrule_input_type = type.StructType('operation-input', {
            'logical_router_id': type.StringType(),
            'rule_id': type.StringType(),
            'source': type.OptionalType(type.StringType()),
        })
        getperrule_error_dict = {
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
        getperrule_input_value_validator_list = [
        ]
        getperrule_output_validator_list = [
        ]
        getperrule_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/logical-routers/{logical-router-id}/nat/rules/{rule-id}/statistics',
            path_variables={
                'logical_router_id': 'logical-router-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
                'source': 'source',
            }
        )

        operations = {
            'getperlogicalrouter': {
                'input_type': getperlogicalrouter_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NatStatisticsPerLogicalRouter'),
                'errors': getperlogicalrouter_error_dict,
                'input_value_validator_list': getperlogicalrouter_input_value_validator_list,
                'output_validator_list': getperlogicalrouter_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'getperrule': {
                'input_type': getperrule_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'NatStatisticsPerRule'),
                'errors': getperrule_error_dict,
                'input_value_validator_list': getperrule_input_value_validator_list,
                'output_validator_list': getperrule_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'getperlogicalrouter': getperlogicalrouter_rest_metadata,
            'getperrule': getperrule_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.logical_routers.nat.rules.statistics',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Statistics': Statistics,
    }

