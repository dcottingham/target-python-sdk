# coding: utf-8

"""
    Adobe Target Delivery API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DeliveryRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'request_id': 'str',
        'impression_id': 'str',
        'id': 'VisitorId',
        'environment_id': 'int',
        '_property': 'ModelProperty',
        'trace': 'Trace',
        'context': 'Context',
        'experience_cloud': 'ExperienceCloud',
        'execute': 'ExecuteRequest',
        'prefetch': 'PrefetchRequest',
        'telemetry': 'Telemetry',
        'notifications': 'list[Notification]',
        'qa_mode': 'QAMode',
        'preview': 'Preview'
    }

    attribute_map = {
        'request_id': 'requestId',
        'impression_id': 'impressionId',
        'id': 'id',
        'environment_id': 'environmentId',
        '_property': 'property',
        'trace': 'trace',
        'context': 'context',
        'experience_cloud': 'experienceCloud',
        'execute': 'execute',
        'prefetch': 'prefetch',
        'telemetry': 'telemetry',
        'notifications': 'notifications',
        'qa_mode': 'qaMode',
        'preview': 'preview'
    }

    def __init__(self, request_id=None, impression_id=None, id=None, environment_id=None, _property=None, trace=None, context=None, experience_cloud=None, execute=None, prefetch=None, telemetry=None, notifications=None, qa_mode=None, preview=None):  # noqa: E501
        """DeliveryRequest - a model defined in OpenAPI"""  # noqa: E501

        self._request_id = None
        self._impression_id = None
        self._id = None
        self._environment_id = None
        self.__property = None
        self._trace = None
        self._context = None
        self._experience_cloud = None
        self._execute = None
        self._prefetch = None
        self._telemetry = None
        self._notifications = None
        self._qa_mode = None
        self._preview = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if impression_id is not None:
            self.impression_id = impression_id
        if id is not None:
            self.id = id
        if environment_id is not None:
            self.environment_id = environment_id
        if _property is not None:
            self._property = _property
        if trace is not None:
            self.trace = trace
        self.context = context
        if experience_cloud is not None:
            self.experience_cloud = experience_cloud
        if execute is not None:
            self.execute = execute
        if prefetch is not None:
            self.prefetch = prefetch
        if telemetry is not None:
            self.telemetry = telemetry
        if notifications is not None:
            self.notifications = notifications
        if qa_mode is not None:
            self.qa_mode = qa_mode
        if preview is not None:
            self.preview = preview

    @property
    def request_id(self):
        """Gets the request_id of this DeliveryRequest.  # noqa: E501

        The request ID that will be returned in the response. In case it is not provided, an UUID is generated and returned automatically.   # noqa: E501

        :return: The request_id of this DeliveryRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DeliveryRequest.

        The request ID that will be returned in the response. In case it is not provided, an UUID is generated and returned automatically.   # noqa: E501

        :param request_id: The request_id of this DeliveryRequest.  # noqa: E501
        :type: str
        """
        if request_id is not None and len(request_id) > 128:
            raise ValueError("Invalid value for `request_id`, length must be less than or equal to `128`")  # noqa: E501

        self._request_id = request_id

    @property
    def impression_id(self):
        """Gets the impression_id of this DeliveryRequest.  # noqa: E501

        If not present it will be automatically generated (UUID). If present,  second and subsequent requests with the same id will not increment impressions to activities/metrics. Similar to page id.   # noqa: E501

        :return: The impression_id of this DeliveryRequest.  # noqa: E501
        :rtype: str
        """
        return self._impression_id

    @impression_id.setter
    def impression_id(self, impression_id):
        """Sets the impression_id of this DeliveryRequest.

        If not present it will be automatically generated (UUID). If present,  second and subsequent requests with the same id will not increment impressions to activities/metrics. Similar to page id.   # noqa: E501

        :param impression_id: The impression_id of this DeliveryRequest.  # noqa: E501
        :type: str
        """
        if impression_id is not None and len(impression_id) > 128:
            raise ValueError("Invalid value for `impression_id`, length must be less than or equal to `128`")  # noqa: E501

        self._impression_id = impression_id

    @property
    def id(self):
        """Gets the id of this DeliveryRequest.  # noqa: E501


        :return: The id of this DeliveryRequest.  # noqa: E501
        :rtype: VisitorId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeliveryRequest.


        :param id: The id of this DeliveryRequest.  # noqa: E501
        :type: VisitorId
        """

        self._id = id

    @property
    def environment_id(self):
        """Gets the environment_id of this DeliveryRequest.  # noqa: E501

        Valid client environment id. If not specified host will be determined base on the provided host.  # noqa: E501

        :return: The environment_id of this DeliveryRequest.  # noqa: E501
        :rtype: int
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this DeliveryRequest.

        Valid client environment id. If not specified host will be determined base on the provided host.  # noqa: E501

        :param environment_id: The environment_id of this DeliveryRequest.  # noqa: E501
        :type: int
        """

        self._environment_id = environment_id

    @property
    def _property(self):
        """Gets the _property of this DeliveryRequest.  # noqa: E501


        :return: The _property of this DeliveryRequest.  # noqa: E501
        :rtype: ModelProperty
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this DeliveryRequest.


        :param _property: The _property of this DeliveryRequest.  # noqa: E501
        :type: ModelProperty
        """

        self.__property = _property

    @property
    def trace(self):
        """Gets the trace of this DeliveryRequest.  # noqa: E501


        :return: The trace of this DeliveryRequest.  # noqa: E501
        :rtype: Trace
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this DeliveryRequest.


        :param trace: The trace of this DeliveryRequest.  # noqa: E501
        :type: Trace
        """

        self._trace = trace

    @property
    def context(self):
        """Gets the context of this DeliveryRequest.  # noqa: E501


        :return: The context of this DeliveryRequest.  # noqa: E501
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this DeliveryRequest.


        :param context: The context of this DeliveryRequest.  # noqa: E501
        :type: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def experience_cloud(self):
        """Gets the experience_cloud of this DeliveryRequest.  # noqa: E501


        :return: The experience_cloud of this DeliveryRequest.  # noqa: E501
        :rtype: ExperienceCloud
        """
        return self._experience_cloud

    @experience_cloud.setter
    def experience_cloud(self, experience_cloud):
        """Sets the experience_cloud of this DeliveryRequest.


        :param experience_cloud: The experience_cloud of this DeliveryRequest.  # noqa: E501
        :type: ExperienceCloud
        """

        self._experience_cloud = experience_cloud

    @property
    def execute(self):
        """Gets the execute of this DeliveryRequest.  # noqa: E501


        :return: The execute of this DeliveryRequest.  # noqa: E501
        :rtype: ExecuteRequest
        """
        return self._execute

    @execute.setter
    def execute(self, execute):
        """Sets the execute of this DeliveryRequest.


        :param execute: The execute of this DeliveryRequest.  # noqa: E501
        :type: ExecuteRequest
        """

        self._execute = execute

    @property
    def prefetch(self):
        """Gets the prefetch of this DeliveryRequest.  # noqa: E501


        :return: The prefetch of this DeliveryRequest.  # noqa: E501
        :rtype: PrefetchRequest
        """
        return self._prefetch

    @prefetch.setter
    def prefetch(self, prefetch):
        """Sets the prefetch of this DeliveryRequest.


        :param prefetch: The prefetch of this DeliveryRequest.  # noqa: E501
        :type: PrefetchRequest
        """

        self._prefetch = prefetch

    @property
    def telemetry(self):
        """Gets the telemetry of this DeliveryRequest.  # noqa: E501


        :return: The telemetry of this DeliveryRequest.  # noqa: E501
        :rtype: Telemetry
        """
        return self._telemetry

    @telemetry.setter
    def telemetry(self, telemetry):
        """Sets the telemetry of this DeliveryRequest.


        :param telemetry: The telemetry of this DeliveryRequest.  # noqa: E501
        :type: Telemetry
        """

        self._telemetry = telemetry

    @property
    def notifications(self):
        """Gets the notifications of this DeliveryRequest.  # noqa: E501

        Notifications for the displayed content, clicked selectors, and/or visited views or mboxes.  # noqa: E501

        :return: The notifications of this DeliveryRequest.  # noqa: E501
        :rtype: list[Notification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this DeliveryRequest.

        Notifications for the displayed content, clicked selectors, and/or visited views or mboxes.  # noqa: E501

        :param notifications: The notifications of this DeliveryRequest.  # noqa: E501
        :type: list[Notification]
        """

        self._notifications = notifications

    @property
    def qa_mode(self):
        """Gets the qa_mode of this DeliveryRequest.  # noqa: E501


        :return: The qa_mode of this DeliveryRequest.  # noqa: E501
        :rtype: QAMode
        """
        return self._qa_mode

    @qa_mode.setter
    def qa_mode(self, qa_mode):
        """Sets the qa_mode of this DeliveryRequest.


        :param qa_mode: The qa_mode of this DeliveryRequest.  # noqa: E501
        :type: QAMode
        """

        self._qa_mode = qa_mode

    @property
    def preview(self):
        """Gets the preview of this DeliveryRequest.  # noqa: E501


        :return: The preview of this DeliveryRequest.  # noqa: E501
        :rtype: Preview
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this DeliveryRequest.


        :param preview: The preview of this DeliveryRequest.  # noqa: E501
        :type: Preview
        """

        self._preview = preview

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeliveryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
