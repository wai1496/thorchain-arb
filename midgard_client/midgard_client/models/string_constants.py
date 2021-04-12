# coding: utf-8

"""
    Midgard Public API

    The Midgard Public API queries THORChain and any chains linked via the Bifröst and prepares information about the network to be readily available for public users. The API parses transaction event data from THORChain and stores them in a time-series database to make time-dependent queries easy. Midgard does not hold critical information. To interact with BEPSwap and Asgardex, users should query THORChain directly.  # noqa: E501

    OpenAPI spec version: 2.0.0-alpha.3
    Contact: devs@thorchain.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StringConstants(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_pool_status': 'str'
    }

    attribute_map = {
        'default_pool_status': 'DefaultPoolStatus'
    }

    def __init__(self, default_pool_status=None):  # noqa: E501
        """StringConstants - a model defined in Swagger"""  # noqa: E501
        self._default_pool_status = None
        self.discriminator = None
        self.default_pool_status = default_pool_status

    @property
    def default_pool_status(self):
        """Gets the default_pool_status of this StringConstants.  # noqa: E501


        :return: The default_pool_status of this StringConstants.  # noqa: E501
        :rtype: str
        """
        return self._default_pool_status

    @default_pool_status.setter
    def default_pool_status(self, default_pool_status):
        """Sets the default_pool_status of this StringConstants.


        :param default_pool_status: The default_pool_status of this StringConstants.  # noqa: E501
        :type: str
        """
        if default_pool_status is None:
            raise ValueError("Invalid value for `default_pool_status`, must not be `None`")  # noqa: E501

        self._default_pool_status = default_pool_status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(StringConstants, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StringConstants):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
