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


class ExecuteRequest(object):
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
        'page_load': 'RequestDetails',
        'mboxes': 'list[MboxRequest]'
    }

    attribute_map = {
        'page_load': 'pageLoad',
        'mboxes': 'mboxes'
    }

    def __init__(self, page_load=None, mboxes=None):  # noqa: E501
        """ExecuteRequest - a model defined in OpenAPI"""  # noqa: E501

        self._page_load = None
        self._mboxes = None
        self.discriminator = None

        if page_load is not None:
            self.page_load = page_load
        if mboxes is not None:
            self.mboxes = mboxes

    @property
    def page_load(self):
        """Gets the page_load of this ExecuteRequest.  # noqa: E501


        :return: The page_load of this ExecuteRequest.  # noqa: E501
        :rtype: RequestDetails
        """
        return self._page_load

    @page_load.setter
    def page_load(self, page_load):
        """Sets the page_load of this ExecuteRequest.


        :param page_load: The page_load of this ExecuteRequest.  # noqa: E501
        :type: RequestDetails
        """

        self._page_load = page_load

    @property
    def mboxes(self):
        """Gets the mboxes of this ExecuteRequest.  # noqa: E501

        An array of mboxes other than global mbox.  # noqa: E501

        :return: The mboxes of this ExecuteRequest.  # noqa: E501
        :rtype: list[MboxRequest]
        """
        return self._mboxes

    @mboxes.setter
    def mboxes(self, mboxes):
        """Sets the mboxes of this ExecuteRequest.

        An array of mboxes other than global mbox.  # noqa: E501

        :param mboxes: The mboxes of this ExecuteRequest.  # noqa: E501
        :type: list[MboxRequest]
        """

        self._mboxes = mboxes

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
        if not isinstance(other, ExecuteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other