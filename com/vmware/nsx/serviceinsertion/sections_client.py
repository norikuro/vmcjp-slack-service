# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.serviceinsertion.sections.
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


class Rules(VapiInterface):
    """
    
    """
    CREATE_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Rules.create`.

    """
    CREATE_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Rules.create`.

    """
    CREATE_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Rules.create`.

    """
    CREATE_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Rules.create`.

    """
    CREATEMULTIPLE_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Rules.createmultiple`.

    """
    CREATEMULTIPLE_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Rules.createmultiple`.

    """
    CREATEMULTIPLE_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Rules.createmultiple`.

    """
    CREATEMULTIPLE_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Rules.createmultiple`.

    """
    LIST_FILTER_TYPE_FILTER = "FILTER"
    """
    Possible value for ``filterType`` of method :func:`Rules.list`.

    """
    LIST_FILTER_TYPE_SEARCH = "SEARCH"
    """
    Possible value for ``filterType`` of method :func:`Rules.list`.

    """
    REVISE_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Rules.revise`.

    """
    REVISE_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Rules.revise`.

    """
    REVISE_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Rules.revise`.

    """
    REVISE_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Rules.revise`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.sections.rules'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RulesStub)


    def create(self,
               section_id,
               service_insertion_rule,
               id=None,
               operation=None,
               ):
        """
        Adds a new serviceinsertion rule in existing serviceinsertion section.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  service_insertion_rule: :class:`com.vmware.nsx.model_client.ServiceInsertionRule`
        :param service_insertion_rule: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionRule`
        :return: com.vmware.nsx.model.ServiceInsertionRule
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
                            'section_id': section_id,
                            'service_insertion_rule': service_insertion_rule,
                            'id': id,
                            'operation': operation,
                            })

    def createmultiple(self,
                       section_id,
                       service_insertion_rule_list,
                       id=None,
                       operation=None,
                       ):
        """
        Create multiple serviceinsertion rules in existing serviceinsertion
        section bounded by limit of 1000 serviceinsertion rules per section.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  service_insertion_rule_list: :class:`com.vmware.nsx.model_client.ServiceInsertionRuleList`
        :param service_insertion_rule_list: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionRuleList`
        :return: com.vmware.nsx.model.ServiceInsertionRuleList
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
        return self._invoke('createmultiple',
                            {
                            'section_id': section_id,
                            'service_insertion_rule_list': service_insertion_rule_list,
                            'id': id,
                            'operation': operation,
                            })

    def delete(self,
               section_id,
               rule_id,
               ):
        """
        Delete existing serviceinsertion rule in a serviceinsertion section.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
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
                            'section_id': section_id,
                            'rule_id': rule_id,
                            })

    def get(self,
            section_id,
            rule_id,
            ):
        """
        Return existing serviceinsertion rule information in a serviceinsertion
        section.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionRule`
        :return: com.vmware.nsx.model.ServiceInsertionRule
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
                            'section_id': section_id,
                            'rule_id': rule_id,
                            })

    def list(self,
             section_id,
             applied_tos=None,
             cursor=None,
             destinations=None,
             filter_type=None,
             included_fields=None,
             page_size=None,
             services=None,
             sort_ascending=None,
             sort_by=None,
             sources=None,
             ):
        """
        Return all serviceinsertion rule(s) information for a given
        serviceinsertion section.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  applied_tos: :class:`str` or ``None``
        :param applied_tos: AppliedTo's referenced by this section or section's Distributed
            Service Rules . (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  destinations: :class:`str` or ``None``
        :param destinations: Destinations referenced by this section's Distributed Service Rules
            . (optional)
        :type  filter_type: :class:`str` or ``None``
        :param filter_type: Filter type (optional, default to FILTER)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  services: :class:`str` or ``None``
        :param services: NSService referenced by this section's Distributed Service Rules .
            (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  sources: :class:`str` or ``None``
        :param sources: Sources referenced by this section's Distributed Service Rules .
            (optional)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionRuleListResult`
        :return: com.vmware.nsx.model.ServiceInsertionRuleListResult
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
                            'section_id': section_id,
                            'applied_tos': applied_tos,
                            'cursor': cursor,
                            'destinations': destinations,
                            'filter_type': filter_type,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'services': services,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'sources': sources,
                            })

    def revise(self,
               section_id,
               rule_id,
               service_insertion_rule,
               id=None,
               operation=None,
               ):
        """
        Modifies existing serviceinsertion rule along with relative position
        among other serviceinsertion rules inside a serviceinsertion section.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
        :type  service_insertion_rule: :class:`com.vmware.nsx.model_client.ServiceInsertionRule`
        :param service_insertion_rule: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionRule`
        :return: com.vmware.nsx.model.ServiceInsertionRule
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
        return self._invoke('revise',
                            {
                            'section_id': section_id,
                            'rule_id': rule_id,
                            'service_insertion_rule': service_insertion_rule,
                            'id': id,
                            'operation': operation,
                            })

    def update(self,
               section_id,
               rule_id,
               service_insertion_rule,
               ):
        """
        Modifies existing serviceinsertion rule in a serviceinsertion section.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  rule_id: :class:`str`
        :param rule_id: (required)
        :type  service_insertion_rule: :class:`com.vmware.nsx.model_client.ServiceInsertionRule`
        :param service_insertion_rule: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ServiceInsertionRule`
        :return: com.vmware.nsx.model.ServiceInsertionRule
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
        return self._invoke('update',
                            {
                            'section_id': section_id,
                            'rule_id': rule_id,
                            'service_insertion_rule': service_insertion_rule,
                            })
class _RulesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'service_insertion_rule': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRule'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
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
            HasFieldsOfValidator()
        ]
        create_output_validator_list = [
            HasFieldsOfValidator()
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/sections/{section-id}/rules',
            request_body_parameter='service_insertion_rule',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for createmultiple operation
        createmultiple_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'service_insertion_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRuleList'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        createmultiple_error_dict = {
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
        createmultiple_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        createmultiple_output_validator_list = [
            HasFieldsOfValidator()
        ]
        createmultiple_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/sections/{section-id}/rules?action=create_multiple',
            request_body_parameter='service_insertion_rule_list',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'rule_id': type.StringType(),
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
            url_template='/api/v1/serviceinsertion/sections/{section-id}/rules/{rule-id}',
            path_variables={
                'section_id': 'section-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'rule_id': type.StringType(),
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
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/serviceinsertion/sections/{section-id}/rules/{rule-id}',
            path_variables={
                'section_id': 'section-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'applied_tos': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'destinations': type.OptionalType(type.StringType()),
            'filter_type': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'services': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'sources': type.OptionalType(type.StringType()),
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/serviceinsertion/sections/{section-id}/rules',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'applied_tos': 'applied_tos',
                'cursor': 'cursor',
                'destinations': 'destinations',
                'filter_type': 'filter_type',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'services': 'services',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'sources': 'sources',
            },
            content_type='application/json'
        )

        # properties for revise operation
        revise_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'rule_id': type.StringType(),
            'service_insertion_rule': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRule'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        revise_error_dict = {
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
        revise_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        revise_output_validator_list = [
            HasFieldsOfValidator()
        ]
        revise_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/serviceinsertion/sections/{section-id}/rules/{rule-id}?action=revise',
            request_body_parameter='service_insertion_rule',
            path_variables={
                'section_id': 'section-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'rule_id': type.StringType(),
            'service_insertion_rule': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRule'),
        })
        update_error_dict = {
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
        update_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/serviceinsertion/sections/{section-id}/rules/{rule-id}',
            request_body_parameter='service_insertion_rule',
            path_variables={
                'section_id': 'section-id',
                'rule_id': 'rule-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRule'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'createmultiple': {
                'input_type': createmultiple_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRuleList'),
                'errors': createmultiple_error_dict,
                'input_value_validator_list': createmultiple_input_value_validator_list,
                'output_validator_list': createmultiple_output_validator_list,
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
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRule'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRuleListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revise': {
                'input_type': revise_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRule'),
                'errors': revise_error_dict,
                'input_value_validator_list': revise_input_value_validator_list,
                'output_validator_list': revise_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ServiceInsertionRule'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'createmultiple': createmultiple_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'revise': revise_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.sections.rules',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Rules': Rules,
    }

