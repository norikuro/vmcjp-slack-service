# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.std.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.std_client`` module provides standard types that can be
used in the interface specification of any class.

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


class AuthenticationScheme(VapiStruct):
    """
    The :class:`AuthenticationScheme` class defines constants for
    authentication scheme identifiers for authentication mechanisms present in
    the vAPI infrastructure shipped by VMware. 
    
    A third party extension can define and implements it's own authentication
    mechanism and define a constant in a different IDL file.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    NO_AUTHENTICATION = "com.vmware.vapi.std.security.no_authentication"
    """
    Indicates that the request doesn't need any authentication.

    """
    SAML_BEARER_TOKEN = "com.vmware.vapi.std.security.saml_bearer_token"
    """
    Indicates that the security context in a request is using a SAML bearer token
    based authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier: com.vmware.vapi.std.security.saml_bearer_token
    * The token itself

     

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.saml_bearer_token',
    'token': 'the token itself'
    }`` vAPI runtime provide convenient factory methods that take SAML bearer token
    and to create the security context that conforms to the above mentioned format.

    """
    SAML_HOK_TOKEN = "com.vmware.vapi.std.security.saml_hok_token"
    """
    Indicates that the security context in a request is using a SAML holder-of-key
    token based authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier: com.vmware.vapi.std.security.saml_hok_token
    * Signature of the request: This includes - algorithm used for signing the
      request, SAML holder of key token and signature digest
    * Request timestamp: This includes the ``created`` and ``expires`` timestamp of
      the request. The timestamp should match the following format -
      YYYY-MM-DDThh:mm:ss.sssZ (e.g. 1878-03-03T19:20:30.451Z).

     

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.saml_hok_token',
    'signature': {
    'alg': 'RS256',
    'samlToken': ...,
    'value': ...,``, 'timestamp': { 'created': '2012-10-26T12:24:18.941Z',
    'expires': '2012-10-26T12:44:18.941Z', } } } vAPI runtime provide convenient
    factory methods that take SAML holder of key token and private key to create
    the security context that conforms to the above mentioned format.

    """
    SESSION_ID = "com.vmware.vapi.std.security.session_id"
    """
    Indicates that the security context in a request is using a session identifier
    based authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier - com.vmware.vapi.std.security.session_id
    * Valid session identifier - This is usually returned by a login method of a
      session manager interface for a particular vAPI service of this authentication
      scheme

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.session_id',
    'sessionId': ....,
    }`` vAPI runtime provides convenient factory methods that take session
    identifier as input parameter and create a security context that conforms to
    the above format.

    """
    USER_PASSWORD = "com.vmware.vapi.std.security.user_pass"
    """
    Indicates that the security context in a request is using username/password
    based authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier - com.vmware.vapi.std.security.user_pass
    * Username
    * Password

     

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.user_pass',
    'userName': ....,
    'password': ...
    }`` 
    vAPI runtime provides convenient factory methods that take username and
    password as input parameters and create a security context that conforms to the
    above format.

    """
    OAUTH_ACCESS_TOKEN = "com.vmware.vapi.std.security.oauth"
    """
    Indicates that the security context in a request is using OAuth2 based
    authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier - com.vmware.vapi.std.security.oauth
    * Valid OAuth2 access token - This is usually acquired by OAuth2 Authorization
      Server after successful authentication of the end user.

     

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.oauth',
    'accesstoken': ....
    }`` 
    vAPI runtime provides convenient factory methods that takes OAuth2 access token
    as input parameter and creates a security context that conforms to the above
    format.

    """




    def __init__(self,
                ):
        """
        """
        VapiStruct.__init__(self)


AuthenticationScheme._set_binding_type(type.StructType(
    'com.vmware.vapi.std.authentication_scheme', {
    },
    AuthenticationScheme,
    False,
    None))



class DynamicID(VapiStruct):
    """
    The ``DynamicID`` class represents an identifier for a resource of an
    arbitrary type.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 type=None,
                 id=None,
                ):
        """
        :type  type: :class:`str`
        :param type: The type of resource being identified (for example
            ``com.acme.Person``). 
            
            Classes that contain methods for creating and deleting resources
            typically contain a class attribute specifying the resource type
            for the resources being created and deleted. The API metamodel
            metadata classes include a class that allows retrieving all the
            known resource types.
        :type  id: :class:`str`
        :param id: The identifier for a resource whose type is specified by
            :attr:`DynamicID.type`.
            When clients pass a value of this class as a parameter, the
            attribute ``type`` must contain the actual resource type. When
            methods return a value of this class as a return value, the
            attribute ``type`` will contain the actual resource type.
        """
        self.type = type
        self.id = id
        VapiStruct.__init__(self)


DynamicID._set_binding_type(type.StructType(
    'com.vmware.vapi.std.dynamic_ID', {
        'type': type.StringType(),
        'id': type.IdType(resource_types=[], resource_type_field_name="type"),
    },
    DynamicID,
    False,
    None))



class LocalizableMessage(VapiStruct):
    """
    The ``LocalizableMessage`` class represents localizable string and message
    template. Classes include one or more localizable message templates in the
    exceptions they report so that clients can display diagnostic messages in
    the native language of the user. Classes can include localizable strings in
    the data returned from methods to allow clients to display localized status
    information in the native language of the user.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 default_message=None,
                 args=None,
                 params=None,
                 localized=None,
                ):
        """
        :type  id: :class:`str`
        :param id: Unique identifier of the localizable string or message template. 
            
            This identifier is typically used to retrieve a locale-specific
            string or message template from a message catalog.
        :type  default_message: :class:`str`
        :param default_message: The value of this localizable string or message template in the
            ``en_US`` (English) locale. If :attr:`LocalizableMessage.id` refers
            to a message template, the default message will contain the
            substituted arguments. This value can be used by clients that do
            not need to display strings and messages in the native language of
            the user. It could also be used as a fallback if a client is unable
            to access the appropriate message catalog.
        :type  args: :class:`list` of :class:`str`
        :param args: Positional arguments to be substituted into the message template.
            This list will be empty if the message uses named arguments or has
            no arguments.
        :type  params: (:class:`dict` of :class:`str` and :class:`LocalizationParam`) or ``None``
        :param params: Named arguments to be substituted into the message template.
            **Warning:** This attribute is part of a new feature in
            development. It may be changed at any time and may not have all
            supported functionality implemented.
            None means that the message template requires no arguments or
            positional arguments are used.
        :type  localized: :class:`str` or ``None``
        :param localized: Localized string value as per request requirements. **Warning:**
            This attribute is part of a new feature in development. It may be
            changed at any time and may not have all supported functionality
            implemented.
            when the client has not requested specific locale the
            implementation may not populate this field to conserve resources.
        """
        self.id = id
        self.default_message = default_message
        self.args = args
        self.params = params
        self.localized = localized
        VapiStruct.__init__(self)


LocalizableMessage._set_binding_type(type.StructType(
    'com.vmware.vapi.std.localizable_message', {
        'id': type.StringType(),
        'default_message': type.StringType(),
        'args': type.ListType(type.StringType()),
        'params': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'LocalizationParam'))),
        'localized': type.OptionalType(type.StringType()),
    },
    LocalizableMessage,
    False,
    None))



class LocalizationParam(VapiStruct):
    """
    This class holds a single message parameter and formatting settings for it.
    The class has fields for :class:`str`, :class:`int`,
    :class:`decimal.Decimal`, date time and nested messages. Only one will be
    used depending on the type of data sent. For date, :class:`decimal.Decimal`
    and :class:`int` it is possible to set additional formatting details.
    **Warning:** This class is part of a new feature in development. It may be
    changed at any time and may not have all supported functionality
    implemented.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 s=None,
                 dt=None,
                 i=None,
                 d=None,
                 l=None,
                 format=None,
                 precision=None,
                ):
        """
        :type  s: :class:`str` or ``None``
        :param s: :class:`str` value associated with the parameter. **Warning:** This
            attribute is part of a new feature in development. It may be
            changed at any time and may not have all supported functionality
            implemented.
            this attribute will be set when :class:`str` value is used.
        :type  dt: :class:`datetime.datetime` or ``None``
        :param dt: Date and time value associated with the parameter. Use the
            ``format`` attribute to specify date and time display style.
            **Warning:** This attribute is part of a new feature in
            development. It may be changed at any time and may not have all
            supported functionality implemented.
            this attribute will be set when date and time value is used.
        :type  i: :class:`long` or ``None``
        :param i: :class:`int` value associated with the parameter. **Warning:** This
            attribute is part of a new feature in development. It may be
            changed at any time and may not have all supported functionality
            implemented.
            this attribute will be set when :class:`int` value is used.
        :type  d: :class:`float` or ``None``
        :param d: The :class:`decimal.Decimal` value associated with the parameter.
            The number of displayed fractional digits is changed via
            ``precision`` attribute. **Warning:** This attribute is part of a
            new feature in development. It may be changed at any time and may
            not have all supported functionality implemented.
            this attribute will be set when :class:`decimal.Decimal` value is
            used.
        :type  l: :class:`NestedLocalizableMessage` or ``None``
        :param l: Nested localizable value associated with the parameter. This is
            useful construct to convert to human readable localized form class
            and :class:`bool` values. It can also be used for proper handling
            of pluralization and gender forms in localization. Recursive
            ``NestedLocalizableMessage`` instances can be used for localizing
            short lists of items. **Warning:** This attribute is part of a new
            feature in development. It may be changed at any time and may not
            have all supported functionality implemented.
            this attribute will be set when nested localization message value
            is used.
        :type  format: :class:`LocalizationParam.DateTimeFormat` or ``None``
        :param format: Format associated with the date and time value in ``dt`` attribute.
            The class attribute ``SHORT_DATETIME`` will be used as default.
            **Warning:** This attribute is part of a new feature in
            development. It may be changed at any time and may not have all
            supported functionality implemented.
            this may not be set if class attribute ``SHORT_DATETIME`` default
            format is appropriate
        :type  precision: :class:`long` or ``None``
        :param precision: Number of fractional digits to include in formatted
            :class:`decimal.Decimal` value. **Warning:** This attribute is part
            of a new feature in development. It may be changed at any time and
            may not have all supported functionality implemented.
            this will be set when exact precision is required for rendering
            :class:`decimal.Decimal` numbers.
        """
        self.s = s
        self.dt = dt
        self.i = i
        self.d = d
        self.l = l
        self.format = format
        self.precision = precision
        VapiStruct.__init__(self)


    class DateTimeFormat(Enum):
        """
        The ``LocalizationParam.DateTimeFormat`` class lists possible date and time
        formatting options. It combines the Unicode CLDR format types - full, long,
        medium and short with 3 different presentations - date only, time only and
        combined date and time presentation. **Warning:** This enumeration is part
        of a new feature in development. It may be changed at any time and may not
        have all supported functionality implemented.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SHORT_DATE = None
        """
        The date and time value will be formatted as short date, for example
        *2019-01-28*. **Warning:** This class attribute is part of a new feature in
        development. It may be changed at any time and may not have all supported
        functionality implemented.

        """
        MED_DATE = None
        """
        The date and time value will be formatted as medium date, for example *2019
        Jan 28*. **Warning:** This class attribute is part of a new feature in
        development. It may be changed at any time and may not have all supported
        functionality implemented.

        """
        LONG_DATE = None
        """
        The date and time value will be formatted as long date, for example *2019
        Jan 28*. **Warning:** This class attribute is part of a new feature in
        development. It may be changed at any time and may not have all supported
        functionality implemented.

        """
        FULL_DATE = None
        """
        The date and time value will be formatted as full date, for example *2019
        Jan 28, Mon*. **Warning:** This class attribute is part of a new feature in
        development. It may be changed at any time and may not have all supported
        functionality implemented.

        """
        SHORT_TIME = None
        """
        The date and time value will be formatted as short time, for example
        *12:59*. **Warning:** This class attribute is part of a new feature in
        development. It may be changed at any time and may not have all supported
        functionality implemented.

        """
        MED_TIME = None
        """
        The date and time value will be formatted as medium time, for example
        *12:59:01*. **Warning:** This class attribute is part of a new feature in
        development. It may be changed at any time and may not have all supported
        functionality implemented.

        """
        LONG_TIME = None
        """
        The date and time value will be formatted as long time, for example
        *12:59:01 Z*. **Warning:** This class attribute is part of a new feature in
        development. It may be changed at any time and may not have all supported
        functionality implemented.

        """
        FULL_TIME = None
        """
        The date and time value will be formatted as full time, for example
        *12:59:01 Z*. **Warning:** This class attribute is part of a new feature in
        development. It may be changed at any time and may not have all supported
        functionality implemented.

        """
        SHORT_DATE_TIME = None
        """
        The date and time value will be formatted as short date and time, for
        example *2019-01-28 12:59*. **Warning:** This class attribute is part of a
        new feature in development. It may be changed at any time and may not have
        all supported functionality implemented.

        """
        MED_DATE_TIME = None
        """
        The date and time value will be formatted as medium date and time, for
        example *2019 Jan 28 12:59:01*. **Warning:** This class attribute is part
        of a new feature in development. It may be changed at any time and may not
        have all supported functionality implemented.

        """
        LONG_DATE_TIME = None
        """
        The date and time value will be formatted as long date and time, for
        example *2019 Jan 28 12:59:01 Z*. **Warning:** This class attribute is part
        of a new feature in development. It may be changed at any time and may not
        have all supported functionality implemented.

        """
        FULL_DATE_TIME = None
        """
        The date and time value will be formatted as full date and time, for
        example *2019 Jan 28, Mon 12:59:01 Z*. **Warning:** This class attribute is
        part of a new feature in development. It may be changed at any time and may
        not have all supported functionality implemented.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`DateTimeFormat` instance.
            """
            Enum.__init__(string)

    DateTimeFormat._set_values([
        DateTimeFormat('SHORT_DATE'),
        DateTimeFormat('MED_DATE'),
        DateTimeFormat('LONG_DATE'),
        DateTimeFormat('FULL_DATE'),
        DateTimeFormat('SHORT_TIME'),
        DateTimeFormat('MED_TIME'),
        DateTimeFormat('LONG_TIME'),
        DateTimeFormat('FULL_TIME'),
        DateTimeFormat('SHORT_DATE_TIME'),
        DateTimeFormat('MED_DATE_TIME'),
        DateTimeFormat('LONG_DATE_TIME'),
        DateTimeFormat('FULL_DATE_TIME'),
    ])
    DateTimeFormat._set_binding_type(type.EnumType(
        'com.vmware.vapi.std.localization_param.date_time_format',
        DateTimeFormat))

LocalizationParam._set_binding_type(type.StructType(
    'com.vmware.vapi.std.localization_param', {
        's': type.OptionalType(type.StringType()),
        'dt': type.OptionalType(type.DateTimeType()),
        'i': type.OptionalType(type.IntegerType()),
        'd': type.OptionalType(type.DoubleType()),
        'l': type.OptionalType(type.ReferenceType(__name__, 'NestedLocalizableMessage')),
        'format': type.OptionalType(type.ReferenceType(__name__, 'LocalizationParam.DateTimeFormat')),
        'precision': type.OptionalType(type.IntegerType()),
    },
    LocalizationParam,
    False,
    None))



class NestedLocalizableMessage(VapiStruct):
    """
    The ``NestedLocalizableMessage`` class represents a nested within a
    parameter localizable string or message template. This class is useful for
    modeling composite messages. Such messages are necessary to do correct
    pluralization of phrases, represent lists of several items etc.
    **Warning:** This class is part of a new feature in development. It may be
    changed at any time and may not have all supported functionality
    implemented.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 params=None,
                ):
        """
        :type  id: :class:`str`
        :param id: Unique identifier of the localizable string or message template. 
            
            This identifier is typically used to retrieve a locale-specific
            string or message template from a message catalog.. **Warning:**
            This attribute is part of a new feature in development. It may be
            changed at any time and may not have all supported functionality
            implemented.
        :type  params: (:class:`dict` of :class:`str` and :class:`LocalizationParam`) or ``None``
        :param params: Named Arguments to be substituted into the message template.
            **Warning:** This attribute is part of a new feature in
            development. It may be changed at any time and may not have all
            supported functionality implemented.
            services will not populate this field when there are no parameters
            to be substituted
        """
        self.id = id
        self.params = params
        VapiStruct.__init__(self)


NestedLocalizableMessage._set_binding_type(type.StructType(
    'com.vmware.vapi.std.nested_localizable_message', {
        'id': type.StringType(),
        'params': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'LocalizationParam'))),
    },
    NestedLocalizableMessage,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
        'activation': 'com.vmware.vapi.std.activation_client.StubFactory',
        'errors': 'com.vmware.vapi.std.errors_client.StubFactory',
        'interposition': 'com.vmware.vapi.std.interposition_client.StubFactory',
        'introspection': 'com.vmware.vapi.std.introspection_client.StubFactory',
    }

