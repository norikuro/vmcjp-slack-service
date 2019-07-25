# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.tier_0s.locale_services.
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


class Bgp(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.bgp'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BgpStub)


    def get(self,
            tier0_id,
            locale_service_id,
            ):
        """
        Read BGP routing config

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.BgpRoutingConfig`
        :return: com.vmware.nsx_policy.model.BgpRoutingConfig
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            })

    def patch(self,
              tier0_id,
              locale_service_id,
              bgp_routing_config,
              ):
        """
        If an BGP routing config not present, create BGP routing config. If it
        already exists, update the routing config.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  bgp_routing_config: :class:`com.vmware.nsx_policy.model_client.BgpRoutingConfig`
        :param bgp_routing_config: (required)
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
        return self._invoke('patch',
                            {
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'bgp_routing_config': bgp_routing_config,
                            })

    def update(self,
               tier0_id,
               locale_service_id,
               bgp_routing_config,
               ):
        """
        If BGP routing config is not already present, create BGP routing
        config. If it already exists, replace the BGP routing config with this
        object.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  bgp_routing_config: :class:`com.vmware.nsx_policy.model_client.BgpRoutingConfig`
        :param bgp_routing_config: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.BgpRoutingConfig`
        :return: com.vmware.nsx_policy.model.BgpRoutingConfig
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'bgp_routing_config': bgp_routing_config,
                            })
class L2vpnContext(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_context'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _L2vpnContextStub)


    def get(self,
            tier0_id,
            locale_service_id,
            ):
        """
        Read L2Vpn Context.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L2VpnContext`
        :return: com.vmware.nsx_policy.model.L2VpnContext
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            })
class L3vpnContext(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpn_context'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _L3vpnContextStub)


    def get(self,
            tier0_id,
            locale_service_id,
            ):
        """
        Read the L3Vpn Context under tier-0.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3VpnContext`
        :return: com.vmware.nsx_policy.model.L3VpnContext
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            })

    def patch(self,
              tier0_id,
              locale_service_id,
              l3_vpn_context,
              ):
        """
        Create the new L3Vpn Context under tier-0 if it does not exist. If the
        L3Vpn Context already exists under tier-0, merge with the the existing
        one. This is a patch. If the passed L3VpnContext has new L3VpnRules,
        add them to the existing L3VpnContext. If the passed L3VpnContext also
        has existing L3VpnRules, update the existing L3VpnRules.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3_vpn_context: :class:`com.vmware.nsx_policy.model_client.L3VpnContext`
        :param l3_vpn_context: (required)
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
        return self._invoke('patch',
                            {
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3_vpn_context': l3_vpn_context,
                            })

    def update(self,
               tier0_id,
               locale_service_id,
               l3_vpn_context,
               ):
        """
        Create the new L3Vpn Context under tier-0 if it does not exist. If the
        L3Vpn Context already exists under tier-0, replace the the existing
        one. This is a full replace.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3_vpn_context: :class:`com.vmware.nsx_policy.model_client.L3VpnContext`
        :param l3_vpn_context: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3VpnContext`
        :return: com.vmware.nsx_policy.model.L3VpnContext
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3_vpn_context': l3_vpn_context,
                            })
class L3vpns(VapiInterface):
    """
    
    """
    LIST_L3VPN_SESSION_POLICYBASEDL3VPNSESSION = "PolicyBasedL3VpnSession"
    """
    Possible value for ``l3vpnSession`` of method :func:`L3vpns.list`.

    """
    LIST_L3VPN_SESSION_ROUTEBASEDL3VPNSESSION = "RouteBasedL3VpnSession"
    """
    Possible value for ``l3vpnSession`` of method :func:`L3vpns.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpns'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _L3vpnsStub)


    def delete(self,
               tier0_id,
               locale_service_id,
               l3vpn_id,
               ):
        """
        Delete the L3Vpn with the given id.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            })

    def get(self,
            tier0_id,
            locale_service_id,
            l3vpn_id,
            ):
        """
        Read the L3Vpn with the given id. No sensitive data is returned as part
        of the response.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :return: com.vmware.nsx_policy.model.L3Vpn
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            })

    def list(self,
             tier0_id,
             locale_service_id,
             cursor=None,
             included_fields=None,
             l3vpn_session=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Paginated list of L3Vpns.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  l3vpn_session: :class:`str` or ``None``
        :param l3vpn_session: Resource type of L3Vpn Session (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3VpnListResult`
        :return: com.vmware.nsx_policy.model.L3VpnListResult
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'l3vpn_session': l3vpn_session,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              tier0_id,
              locale_service_id,
              l3vpn_id,
              l3_vpn,
              ):
        """
        Create the new L3Vpn if it does not exist. If the L3Vpn already exists,
        merge with the the existing one. This is a patch. - If the passed L3Vpn
        is a policy-based one and has new L3VpnRules, add them to the existing
        L3VpnRules. - If the passed L3Vpn is a policy-based one and also has
        existing L3VpnRules, update the existing L3VpnRules.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :type  l3_vpn: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :param l3_vpn: (required)
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
        return self._invoke('patch',
                            {
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            'l3_vpn': l3_vpn,
                            })

    def showsensitivedata(self,
                          tier0_id,
                          locale_service_id,
                          l3vpn_id,
                          ):
        """
        Read the L3Vpn with the given id. Sensitive data is returned as part of
        the response.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :return: com.vmware.nsx_policy.model.L3Vpn
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
        return self._invoke('showsensitivedata',
                            {
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            })

    def update(self,
               tier0_id,
               locale_service_id,
               l3vpn_id,
               l3_vpn,
               ):
        """
        Create a new L3Vpn if the L3Vpn with given id does not already exist.
        If the L3Vpn with the given id already exists, replace the existing
        L3Vpn. This a full replace.

        :type  tier0_id: :class:`str`
        :param tier0_id: (required)
        :type  locale_service_id: :class:`str`
        :param locale_service_id: (required)
        :type  l3vpn_id: :class:`str`
        :param l3vpn_id: (required)
        :type  l3_vpn: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :param l3_vpn: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.L3Vpn`
        :return: com.vmware.nsx_policy.model.L3Vpn
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
                            'tier0_id': tier0_id,
                            'locale_service_id': locale_service_id,
                            'l3vpn_id': l3vpn_id,
                            'l3_vpn': l3_vpn,
                            })
class _BgpStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'bgp_routing_config': type.ReferenceType('com.vmware.nsx_policy.model_client', 'BgpRoutingConfig'),
        })
        patch_error_dict = {
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
        patch_input_value_validator_list = [
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp',
            request_body_parameter='bgp_routing_config',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'bgp_routing_config': type.ReferenceType('com.vmware.nsx_policy.model_client', 'BgpRoutingConfig'),
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
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/bgp',
            request_body_parameter='bgp_routing_config',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'BgpRoutingConfig'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'BgpRoutingConfig'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.bgp',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _L2vpnContextStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l2vpn-context',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L2VpnContext'),
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
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_context',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _L3vpnContextStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpn-context',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3_vpn_context': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3VpnContext'),
        })
        patch_error_dict = {
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
        patch_input_value_validator_list = [
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpn-context',
            request_body_parameter='l3_vpn_context',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3_vpn_context': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3VpnContext'),
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
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpn-context',
            request_body_parameter='l3_vpn_context',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3VpnContext'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3VpnContext'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpn_context',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _L3vpnsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'l3vpn_session': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'l3vpn_session': 'l3vpn_session',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
            'l3_vpn': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
        })
        patch_error_dict = {
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
        patch_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}',
            request_body_parameter='l3_vpn',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for showsensitivedata operation
        showsensitivedata_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
        })
        showsensitivedata_error_dict = {
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
        showsensitivedata_input_value_validator_list = [
        ]
        showsensitivedata_output_validator_list = [
            HasFieldsOfValidator()
        ]
        showsensitivedata_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}?action=show_sensitive_data',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tier0_id': type.StringType(),
            'locale_service_id': type.StringType(),
            'l3vpn_id': type.StringType(),
            'l3_vpn': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
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
            url_template='/policy/api/v1/infra/tier-0s/{tier-0-id}/locale-services/{locale-service-id}/l3vpns/{l3vpn-id}',
            request_body_parameter='l3_vpn',
            path_variables={
                'tier0_id': 'tier-0-id',
                'locale_service_id': 'locale-service-id',
                'l3vpn_id': 'l3vpn-id',
            },
            query_parameters={
            },
            content_type='application/json'
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
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3VpnListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'showsensitivedata': {
                'input_type': showsensitivedata_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
                'errors': showsensitivedata_error_dict,
                'input_value_validator_list': showsensitivedata_input_value_validator_list,
                'output_validator_list': showsensitivedata_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'L3Vpn'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'patch': patch_rest_metadata,
            'showsensitivedata': showsensitivedata_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpns',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Bgp': Bgp,
        'L2vpnContext': L2vpnContext,
        'L3vpnContext': L3vpnContext,
        'L3vpns': L3vpns,
        'bgp': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.bgp_client.StubFactory',
        'l2vpn_context': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l2vpn_context_client.StubFactory',
        'l3vpns': 'com.vmware.nsx_policy.infra.tier_0s.locale_services.l3vpns_client.StubFactory',
    }

