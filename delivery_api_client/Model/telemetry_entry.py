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


class TelemetryEntry(object):
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
        'timestamp': 'int',
        'execution': 'int',
        'features': 'TelemetryFeatures'
    }

    attribute_map = {
        'request_id': 'requestId',
        'timestamp': 'timestamp',
        'execution': 'execution',
        'features': 'features'
    }

    def __init__(self, request_id=None, timestamp=None, execution=None, features=None):
        """TelemetryEntry - a model defined in OpenAPI"""

        self._request_id = None
        self._timestamp = None
        self._execution = None
        self._features = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if timestamp is not None:
            self.timestamp = timestamp
        if execution is not None:
            self.execution = execution
        if features is not None:
            self.features = features

    @property
    def request_id(self):
        """Gets the request_id of this TelemetryEntry.

        Request Id

        :return: The request_id of this TelemetryEntry.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this TelemetryEntry.

        Request Id

        :param request_id: The request_id of this TelemetryEntry.
        :type: str
        """

        self._request_id = request_id

    @property
    def timestamp(self):
        """Gets the timestamp of this TelemetryEntry.

        Timestamp of the entry, in milliseconds elapsed since UNIX epoch.

        :return: The timestamp of this TelemetryEntry.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TelemetryEntry.

        Timestamp of the entry, in milliseconds elapsed since UNIX epoch.

        :param timestamp: The timestamp of this TelemetryEntry.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def execution(self):
        """Gets the execution of this TelemetryEntry.

        Execution time in milliseconds.

        :return: The execution of this TelemetryEntry.
        :rtype: int
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        """Sets the execution of this TelemetryEntry.

        Execution time in milliseconds.

        :param execution: The execution of this TelemetryEntry.
        :type: int
        """

        self._execution = execution

    @property
    def features(self):
        """Gets the features of this TelemetryEntry.


        :return: The features of this TelemetryEntry.
        :rtype: TelemetryFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this TelemetryEntry.


        :param features: The features of this TelemetryEntry.
        :type: TelemetryFeatures
        """

        self._features = features

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
        if not isinstance(other, TelemetryEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
