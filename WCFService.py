# OData Python Client and Server Libraries ver. 1.0.0

# Copyright (c) Microsoft Corporation
# All rights reserved. 

# MIT License

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import odata_client_python
from odata_service_context import *
from codegen_base import *

class AccessLevel:
    Read = 1
    Write = 2
    _None = 0
    ReadWrite = 3
    Execute = 4

    @staticmethod
    def get_enum_type_namespace():
        return "Microsoft.Test.OData.Services.ODataWCFService"

    @staticmethod
    def get_enum_value_from_string(enum_string):
        if enum_string == "Read":
            return AccessLevel.Read
        if enum_string == "Write":
            return AccessLevel.Write
        if enum_string == "None":
            return AccessLevel._None
        if enum_string == "ReadWrite":
            return AccessLevel.ReadWrite
        if enum_string == "Execute":
            return AccessLevel.Execute
        return 0

    @staticmethod
    def get_string_from_enum_value(enum_value):
        if enum_value == AccessLevel.Read:
            return "Read"
        if enum_value == AccessLevel.Write:
            return "Write"
        if enum_value == AccessLevel._None:
            return "None"
        if enum_value == AccessLevel.ReadWrite:
            return "ReadWrite"
        if enum_value == AccessLevel.Execute:
            return "Execute"
        return ""

class Color:
    Blue = 4
    Green = 2
    Red = 1

    @staticmethod
    def get_enum_type_namespace():
        return "Microsoft.Test.OData.Services.ODataWCFService"

    @staticmethod
    def get_enum_value_from_string(enum_string):
        if enum_string == "Blue":
            return Color.Blue
        if enum_string == "Green":
            return Color.Green
        if enum_string == "Red":
            return Color.Red
        return 0

    @staticmethod
    def get_string_from_enum_value(enum_value):
        if enum_value == Color.Blue:
            return "Blue"
        if enum_value == Color.Green:
            return "Green"
        if enum_value == Color.Red:
            return "Red"
        return ""

class CompanyCategory:
    Communication = 1
    Electronics = 2
    IT = 0
    Others = 4

    @staticmethod
    def get_enum_type_namespace():
        return "Microsoft.Test.OData.Services.ODataWCFService"

    @staticmethod
    def get_enum_value_from_string(enum_string):
        if enum_string == "Communication":
            return CompanyCategory.Communication
        if enum_string == "Electronics":
            return CompanyCategory.Electronics
        if enum_string == "IT":
            return CompanyCategory.IT
        if enum_string == "Others":
            return CompanyCategory.Others
        return 0

    @staticmethod
    def get_string_from_enum_value(enum_value):
        if enum_value == CompanyCategory.Communication:
            return "Communication"
        if enum_value == CompanyCategory.Electronics:
            return "Electronics"
        if enum_value == CompanyCategory.IT:
            return "IT"
        if enum_value == CompanyCategory.Others:
            return "Others"
        return ""

class AccountInfo(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)
        self._lastname = None
        self._firstname = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"AccountInfo"

    @staticmethod
    def get_full_name():
        return AccountInfo._namespace + '.' + AccountInfo._typename

    @staticmethod
    def get_type_name():
        return AccountInfo._typename

    def get_lastname(self):
        return self._lastname

    def set_lastname(self, property_value):
        self._lastname = property_value

    def _get_lastname_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("LastName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._lastname = primitive_value.to_string()
            except:
                self._lastname = primitive_value.to_string()

    def _set_lastname_to_complex(self, complex):
        if complex is None or self._lastname is None:
            return
        complex.set_value("LastName", self._lastname)


    def get_firstname(self):
        return self._firstname

    def set_firstname(self, property_value):
        self._firstname = property_value

    def _get_firstname_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("FirstName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._firstname = primitive_value.to_string()
            except:
                self._firstname = primitive_value.to_string()

    def _set_firstname_to_complex(self, complex):
        if complex is None or self._firstname is None:
            return
        complex.set_value("FirstName", self._firstname)


    @staticmethod
    def create_instance_from_complex(complex_value, service_context):
        if complex_value is None:
            return None
        real_type_name = complex_value.get_value_type().get_name()
        if real_type_name != "AccountInfo":
            if real_type_name in AccountInfo._derived_creator_map:
                instance = AccountInfo._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = AccountInfo(service_context)
        instance.from_value(complex_value)
        return instance

    def from_value(self, complex_value):
        self._type_base__from_value(complex_value)
        self._get_lastname_from_complex(complex_value)
        self._get_firstname_from_complex(complex_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        complex_type = self._service_context.get_edm_model().find_complex_type(self._typename)
        complex_value = odata_client_python.odata_complex_value(complex_type)
        self._set_lastname_to_complex(complex_value)
        self._set_firstname_to_complex(complex_value)
        if self._namespace != "" and self._typename != "":
            complex_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return complex_value

    __to_value = to_value

class Address(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)
        self._postalcode = None
        self._city = None
        self._street = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Address"

    @staticmethod
    def get_full_name():
        return Address._namespace + '.' + Address._typename

    @staticmethod
    def get_type_name():
        return Address._typename

    def get_postalcode(self):
        return self._postalcode

    def set_postalcode(self, property_value):
        self._postalcode = property_value

    def _get_postalcode_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("PostalCode", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._postalcode = primitive_value.to_string()
            except:
                self._postalcode = primitive_value.to_string()

    def _set_postalcode_to_complex(self, complex):
        if complex is None or self._postalcode is None:
            return
        complex.set_value("PostalCode", self._postalcode)


    def get_city(self):
        return self._city

    def set_city(self, property_value):
        self._city = property_value

    def _get_city_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("City", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._city = primitive_value.to_string()
            except:
                self._city = primitive_value.to_string()

    def _set_city_to_complex(self, complex):
        if complex is None or self._city is None:
            return
        complex.set_value("City", self._city)


    def get_street(self):
        return self._street

    def set_street(self, property_value):
        self._street = property_value

    def _get_street_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("Street", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._street = primitive_value.to_string()
            except:
                self._street = primitive_value.to_string()

    def _set_street_to_complex(self, complex):
        if complex is None or self._street is None:
            return
        complex.set_value("Street", self._street)


    @staticmethod
    def create_instance_from_complex(complex_value, service_context):
        if complex_value is None:
            return None
        real_type_name = complex_value.get_value_type().get_name()
        if real_type_name != "Address":
            if real_type_name in Address._derived_creator_map:
                instance = Address._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Address(service_context)
        instance.from_value(complex_value)
        return instance

    def from_value(self, complex_value):
        self._type_base__from_value(complex_value)
        self._get_postalcode_from_complex(complex_value)
        self._get_city_from_complex(complex_value)
        self._get_street_from_complex(complex_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        complex_type = self._service_context.get_edm_model().find_complex_type(self._typename)
        complex_value = odata_client_python.odata_complex_value(complex_type)
        self._set_postalcode_to_complex(complex_value)
        self._set_city_to_complex(complex_value)
        self._set_street_to_complex(complex_value)
        if self._namespace != "" and self._typename != "":
            complex_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return complex_value

    __to_value = to_value

class CityInformation(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)
        self._iscapital = False
        self._countryregion = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"CityInformation"

    @staticmethod
    def get_full_name():
        return CityInformation._namespace + '.' + CityInformation._typename

    @staticmethod
    def get_type_name():
        return CityInformation._typename

    def get_iscapital(self):
        return self._iscapital

    def set_iscapital(self, property_value):
        self._iscapital = property_value

    def _get_iscapital_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("IsCapital", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._iscapital = primitive_value.to_string() == 'true'
            except:
                self._iscapital = primitive_value.to_string()

    def _set_iscapital_to_complex(self, complex):
        if complex is None or self._iscapital is None:
            return
        complex.set_value("IsCapital", self._iscapital)


    def get_countryregion(self):
        return self._countryregion

    def set_countryregion(self, property_value):
        self._countryregion = property_value

    def _get_countryregion_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("CountryRegion", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._countryregion = primitive_value.to_string()
            except:
                self._countryregion = primitive_value.to_string()

    def _set_countryregion_to_complex(self, complex):
        if complex is None or self._countryregion is None:
            return
        complex.set_value("CountryRegion", self._countryregion)


    @staticmethod
    def create_instance_from_complex(complex_value, service_context):
        if complex_value is None:
            return None
        real_type_name = complex_value.get_value_type().get_name()
        if real_type_name != "CityInformation":
            if real_type_name in CityInformation._derived_creator_map:
                instance = CityInformation._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = CityInformation(service_context)
        instance.from_value(complex_value)
        return instance

    def from_value(self, complex_value):
        self._type_base__from_value(complex_value)
        self._get_iscapital_from_complex(complex_value)
        self._get_countryregion_from_complex(complex_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        complex_type = self._service_context.get_edm_model().find_complex_type(self._typename)
        complex_value = odata_client_python.odata_complex_value(complex_type)
        self._set_iscapital_to_complex(complex_value)
        self._set_countryregion_to_complex(complex_value)
        if self._namespace != "" and self._typename != "":
            complex_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return complex_value

    __to_value = to_value

class CompanyAddress(Address):

    def __init__(self, service_context):
        Address.__init__(self, service_context)
        self._companyname = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"CompanyAddress"

    @staticmethod
    def get_full_name():
        return CompanyAddress._namespace + '.' + CompanyAddress._typename

    @staticmethod
    def get_type_name():
        return CompanyAddress._typename

    def get_companyname(self):
        return self._companyname

    def set_companyname(self, property_value):
        self._companyname = property_value

    def _get_companyname_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("CompanyName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._companyname = primitive_value.to_string()
            except:
                self._companyname = primitive_value.to_string()

    def _set_companyname_to_complex(self, complex):
        if complex is None or self._companyname is None:
            return
        complex.set_value("CompanyName", self._companyname)


    @staticmethod
    def create_instance_from_complex(complex_value, service_context):
        if complex_value is None:
            return None
        real_type_name = complex_value.get_value_type().get_name()
        if real_type_name != "CompanyAddress":
            if real_type_name in CompanyAddress._derived_creator_map:
                instance = CompanyAddress._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = CompanyAddress(service_context)
        instance.from_value(complex_value)
        return instance

    def from_value(self, complex_value):
        self._Address__from_value(complex_value)
        self._get_companyname_from_complex(complex_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        complex_type = self._service_context.get_edm_model().find_complex_type(self._typename)
        complex_value = self._Address__to_value()
        complex_value.set_value_type(complex_type)
        self._set_companyname_to_complex(complex_value)
        if self._namespace != "" and self._typename != "":
            complex_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return complex_value

    __to_value = to_value

class HomeAddress(Address):

    def __init__(self, service_context):
        Address.__init__(self, service_context)
        self._familyname = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"HomeAddress"

    @staticmethod
    def get_full_name():
        return HomeAddress._namespace + '.' + HomeAddress._typename

    @staticmethod
    def get_type_name():
        return HomeAddress._typename

    def get_familyname(self):
        return self._familyname

    def set_familyname(self, property_value):
        self._familyname = property_value

    def _get_familyname_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("FamilyName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._familyname = primitive_value.to_string()
            except:
                self._familyname = primitive_value.to_string()

    def _set_familyname_to_complex(self, complex):
        if complex is None or self._familyname is None:
            return
        complex.set_value("FamilyName", self._familyname)


    @staticmethod
    def create_instance_from_complex(complex_value, service_context):
        if complex_value is None:
            return None
        real_type_name = complex_value.get_value_type().get_name()
        if real_type_name != "HomeAddress":
            if real_type_name in HomeAddress._derived_creator_map:
                instance = HomeAddress._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = HomeAddress(service_context)
        instance.from_value(complex_value)
        return instance

    def from_value(self, complex_value):
        self._Address__from_value(complex_value)
        self._get_familyname_from_complex(complex_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        complex_type = self._service_context.get_edm_model().find_complex_type(self._typename)
        complex_value = self._Address__to_value()
        complex_value.set_value_type(complex_type)
        self._set_familyname_to_complex(complex_value)
        if self._namespace != "" and self._typename != "":
            complex_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return complex_value

    __to_value = to_value

class GiftCard(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._giftcardid = 0
        self._experationdate = None
        self._amount = 0.0
        self._ownername = None
        self._giftcardno = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"GiftCard"

    @staticmethod
    def get_full_name():
        return GiftCard._namespace + '.' + GiftCard._typename

    @staticmethod
    def get_type_name():
        return GiftCard._typename

    def get_giftcardid(self):
        return self._giftcardid

    def set_giftcardid(self, property_value):
        self._giftcardid = property_value

    def _get_giftcardid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("GiftCardID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._giftcardid = int(primitive_value.to_string())
            except:
                self._giftcardid = primitive_value.to_string()

    def _set_giftcardid_to_entity(self, entity):
        if entity is None or self._giftcardid is None:
            return
        entity.set_value("GiftCardID", self._giftcardid)


    def GetActualAmount(self, bonusRate):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "GetActualAmount"
        parameters = odata_client_python.vector_odata_parameter()
        if bonusRate is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(bonusRate)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("bonusRate", primitive_value))
        return self._service_context.operation_query_primitive(function_query_url, parameters, True, "double")


    def get_experationdate(self):
        return self._experationdate

    def set_experationdate(self, property_value):
        self._experationdate = property_value

    def _get_experationdate_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ExperationDate", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._experationdate = eval(primitive_value.to_string())
            except:
                self._experationdate = primitive_value.to_string()

    def _set_experationdate_to_entity(self, entity):
        if entity is None or self._experationdate is None:
            return
        entity.set_value("ExperationDate", self._experationdate)


    def get_amount(self):
        return self._amount

    def set_amount(self, property_value):
        self._amount = property_value

    def _get_amount_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Amount", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._amount = float(primitive_value.to_string())
            except:
                self._amount = primitive_value.to_string()

    def _set_amount_to_entity(self, entity):
        if entity is None or self._amount is None:
            return
        entity.set_value("Amount", self._amount)


    def get_ownername(self):
        return self._ownername

    def set_ownername(self, property_value):
        self._ownername = property_value

    def _get_ownername_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("OwnerName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._ownername = primitive_value.to_string()
            except:
                self._ownername = primitive_value.to_string()

    def _set_ownername_to_entity(self, entity):
        if entity is None or self._ownername is None:
            return
        entity.set_value("OwnerName", self._ownername)


    def get_giftcardno(self):
        return self._giftcardno

    def set_giftcardno(self, property_value):
        self._giftcardno = property_value

    def _get_giftcardno_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("GiftCardNO", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._giftcardno = primitive_value.to_string()
            except:
                self._giftcardno = primitive_value.to_string()

    def _set_giftcardno_to_entity(self, entity):
        if entity is None or self._giftcardno is None:
            return
        entity.set_value("GiftCardNO", self._giftcardno)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "GiftCard":
            if real_type_name in GiftCard._derived_creator_map:
                instance = GiftCard._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = GiftCard(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_giftcardid_from_entity(entity_value)
        self._get_experationdate_from_entity(entity_value)
        self._get_amount_from_entity(entity_value)
        self._get_ownername_from_entity(entity_value)
        self._get_giftcardno_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_giftcardid_to_entity(entity_value)
        self._set_experationdate_to_entity(entity_value)
        self._set_amount_to_entity(entity_value)
        self._set_ownername_to_entity(entity_value)
        self._set_giftcardno_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class OrderDetail(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._orderid = 0
        self._productordered = None
        self._associatedorder = None
        self._orderplaced = None
        self._quantity = 0
        self._unitprice = 0.0
        self._productid = 0

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"OrderDetail"

    @staticmethod
    def get_full_name():
        return OrderDetail._namespace + '.' + OrderDetail._typename

    @staticmethod
    def get_type_name():
        return OrderDetail._typename

    def get_orderid(self):
        return self._orderid

    def set_orderid(self, property_value):
        self._orderid = property_value

    def _get_orderid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("OrderID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._orderid = int(primitive_value.to_string())
            except:
                self._orderid = primitive_value.to_string()

    def _set_orderid_to_entity(self, entity):
        if entity is None or self._orderid is None:
            return
        entity.set_value("OrderID", self._orderid)


    def get_productordered(self):
        return self._productordered

    def set_productordered(self, property_values):
        self._productordered = property_values

    def add_to_productordered(self, property_value):
        if self._productordered is None:
            self._productordered = []
        self._productordered.append(property_value)

    def load_productordered(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "ProductOrdered"
        values = self._service_context.query(path)
        if values is None:
            return
        self._productordered = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._productordered.append(Product.create_instance_from_entity(entity_value, self._service_context))

    def _get_productordered_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ProductOrdered", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._productordered = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._productordered.append(Product.create_instance_from_entity(entity_value, self._service_context))


    def get_associatedorder(self):
        return self._associatedorder

    def set_associatedorder(self, navitation_value):
        self._associatedorder = navitation_value

    def load_associatedorder(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "AssociatedOrder"
        values = self._service_context.query(path)
        if values is None:
            return
        self._associatedorder = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._associatedorder = Order.create_instance_from_entity(entity_value, self._service_context)

    def _get_associatedorder_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("AssociatedOrder", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._associatedorder = Order.create_instance_from_entity(entity_value, self._service_context)


    def get_orderplaced(self):
        return self._orderplaced

    def set_orderplaced(self, property_value):
        self._orderplaced = property_value

    def _get_orderplaced_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("OrderPlaced", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._orderplaced = eval(primitive_value.to_string())
            except:
                self._orderplaced = primitive_value.to_string()

    def _set_orderplaced_to_entity(self, entity):
        if entity is None or self._orderplaced is None:
            return
        entity.set_value("OrderPlaced", self._orderplaced)


    def get_quantity(self):
        return self._quantity

    def set_quantity(self, property_value):
        self._quantity = property_value

    def _get_quantity_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Quantity", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._quantity = int(primitive_value.to_string())
            except:
                self._quantity = primitive_value.to_string()

    def _set_quantity_to_entity(self, entity):
        if entity is None or self._quantity is None:
            return
        entity.set_value("Quantity", self._quantity)


    def get_unitprice(self):
        return self._unitprice

    def set_unitprice(self, property_value):
        self._unitprice = property_value

    def _get_unitprice_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("UnitPrice", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._unitprice = float(primitive_value.to_string())
            except:
                self._unitprice = primitive_value.to_string()

    def _set_unitprice_to_entity(self, entity):
        if entity is None or self._unitprice is None:
            return
        entity.set_value("UnitPrice", self._unitprice)


    def get_productid(self):
        return self._productid

    def set_productid(self, property_value):
        self._productid = property_value

    def _get_productid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ProductID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._productid = int(primitive_value.to_string())
            except:
                self._productid = primitive_value.to_string()

    def _set_productid_to_entity(self, entity):
        if entity is None or self._productid is None:
            return
        entity.set_value("ProductID", self._productid)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "OrderDetail":
            if real_type_name in OrderDetail._derived_creator_map:
                instance = OrderDetail._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = OrderDetail(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_orderid_from_entity(entity_value)
        self._get_productordered_from_entity(entity_value)
        self._get_associatedorder_from_entity(entity_value)
        self._get_orderplaced_from_entity(entity_value)
        self._get_quantity_from_entity(entity_value)
        self._get_unitprice_from_entity(entity_value)
        self._get_productid_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_orderid_to_entity(entity_value)
        self._set_orderplaced_to_entity(entity_value)
        self._set_quantity_to_entity(entity_value)
        self._set_unitprice_to_entity(entity_value)
        self._set_productid_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Department(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._company = None
        self._departmentno = None
        self._departmentid = 0
        self._name = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Department"

    @staticmethod
    def get_full_name():
        return Department._namespace + '.' + Department._typename

    @staticmethod
    def get_type_name():
        return Department._typename

    def get_company(self):
        return self._company

    def set_company(self, navitation_value):
        self._company = navitation_value

    def load_company(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Company"
        values = self._service_context.query(path)
        if values is None:
            return
        self._company = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._company = Company.create_instance_from_entity(entity_value, self._service_context)

    def _get_company_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Company", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._company = Company.create_instance_from_entity(entity_value, self._service_context)


    def get_departmentno(self):
        return self._departmentno

    def set_departmentno(self, property_value):
        self._departmentno = property_value

    def _get_departmentno_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("DepartmentNO", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._departmentno = primitive_value.to_string()
            except:
                self._departmentno = primitive_value.to_string()

    def _set_departmentno_to_entity(self, entity):
        if entity is None or self._departmentno is None:
            return
        entity.set_value("DepartmentNO", self._departmentno)


    def get_departmentid(self):
        return self._departmentid

    def set_departmentid(self, property_value):
        self._departmentid = property_value

    def _get_departmentid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("DepartmentID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._departmentid = int(primitive_value.to_string())
            except:
                self._departmentid = primitive_value.to_string()

    def _set_departmentid_to_entity(self, entity):
        if entity is None or self._departmentid is None:
            return
        entity.set_value("DepartmentID", self._departmentid)


    def get_name(self):
        return self._name

    def set_name(self, property_value):
        self._name = property_value

    def _get_name_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Name", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._name = primitive_value.to_string()
            except:
                self._name = primitive_value.to_string()

    def _set_name_to_entity(self, entity):
        if entity is None or self._name is None:
            return
        entity.set_value("Name", self._name)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Department":
            if real_type_name in Department._derived_creator_map:
                instance = Department._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Department(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_company_from_entity(entity_value)
        self._get_departmentno_from_entity(entity_value)
        self._get_departmentid_from_entity(entity_value)
        self._get_name_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_departmentno_to_entity(entity_value)
        self._set_departmentid_to_entity(entity_value)
        self._set_name_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Asset(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._assetid = 0
        self._name = None
        self._number = 0

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Asset"

    @staticmethod
    def get_full_name():
        return Asset._namespace + '.' + Asset._typename

    @staticmethod
    def get_type_name():
        return Asset._typename

    def get_assetid(self):
        return self._assetid

    def set_assetid(self, property_value):
        self._assetid = property_value

    def _get_assetid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("AssetID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._assetid = int(primitive_value.to_string())
            except:
                self._assetid = primitive_value.to_string()

    def _set_assetid_to_entity(self, entity):
        if entity is None or self._assetid is None:
            return
        entity.set_value("AssetID", self._assetid)


    def get_name(self):
        return self._name

    def set_name(self, property_value):
        self._name = property_value

    def _get_name_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Name", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._name = primitive_value.to_string()
            except:
                self._name = primitive_value.to_string()

    def _set_name_to_entity(self, entity):
        if entity is None or self._name is None:
            return
        entity.set_value("Name", self._name)


    def get_number(self):
        return self._number

    def set_number(self, property_value):
        self._number = property_value

    def _get_number_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Number", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._number = int(primitive_value.to_string())
            except:
                self._number = primitive_value.to_string()

    def _set_number_to_entity(self, entity):
        if entity is None or self._number is None:
            return
        entity.set_value("Number", self._number)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Asset":
            if real_type_name in Asset._derived_creator_map:
                instance = Asset._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Asset(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_assetid_from_entity(entity_value)
        self._get_name_from_entity(entity_value)
        self._get_number_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_assetid_to_entity(entity_value)
        self._set_name_to_entity(entity_value)
        self._set_number_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Statement(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._transactiondescription = None
        self._amount = 0.0
        self._statementid = 0
        self._transactiontype = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Statement"

    @staticmethod
    def get_full_name():
        return Statement._namespace + '.' + Statement._typename

    @staticmethod
    def get_type_name():
        return Statement._typename

    def get_transactiondescription(self):
        return self._transactiondescription

    def set_transactiondescription(self, property_value):
        self._transactiondescription = property_value

    def _get_transactiondescription_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("TransactionDescription", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._transactiondescription = primitive_value.to_string()
            except:
                self._transactiondescription = primitive_value.to_string()

    def _set_transactiondescription_to_entity(self, entity):
        if entity is None or self._transactiondescription is None:
            return
        entity.set_value("TransactionDescription", self._transactiondescription)


    def get_amount(self):
        return self._amount

    def set_amount(self, property_value):
        self._amount = property_value

    def _get_amount_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Amount", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._amount = float(primitive_value.to_string())
            except:
                self._amount = primitive_value.to_string()

    def _set_amount_to_entity(self, entity):
        if entity is None or self._amount is None:
            return
        entity.set_value("Amount", self._amount)


    def get_statementid(self):
        return self._statementid

    def set_statementid(self, property_value):
        self._statementid = property_value

    def _get_statementid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("StatementID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._statementid = int(primitive_value.to_string())
            except:
                self._statementid = primitive_value.to_string()

    def _set_statementid_to_entity(self, entity):
        if entity is None or self._statementid is None:
            return
        entity.set_value("StatementID", self._statementid)


    def get_transactiontype(self):
        return self._transactiontype

    def set_transactiontype(self, property_value):
        self._transactiontype = property_value

    def _get_transactiontype_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("TransactionType", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._transactiontype = primitive_value.to_string()
            except:
                self._transactiontype = primitive_value.to_string()

    def _set_transactiontype_to_entity(self, entity):
        if entity is None or self._transactiontype is None:
            return
        entity.set_value("TransactionType", self._transactiontype)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Statement":
            if real_type_name in Statement._derived_creator_map:
                instance = Statement._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Statement(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_transactiondescription_from_entity(entity_value)
        self._get_amount_from_entity(entity_value)
        self._get_statementid_from_entity(entity_value)
        self._get_transactiontype_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_transactiondescription_to_entity(entity_value)
        self._set_amount_to_entity(entity_value)
        self._set_statementid_to_entity(entity_value)
        self._set_transactiontype_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class PaymentInstrument(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._billingstatements = None
        self._thestoredpi = None
        self._backupstoredpi = None
        self._paymentinstrumentid = 0
        self._createddate = None
        self._friendlyname = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"PaymentInstrument"

    @staticmethod
    def get_full_name():
        return PaymentInstrument._namespace + '.' + PaymentInstrument._typename

    @staticmethod
    def get_type_name():
        return PaymentInstrument._typename

    def get_billingstatements(self):
        return self._billingstatements

    def set_billingstatements(self, property_values):
        self._billingstatements = property_values

    def add_to_billingstatements(self, property_value):
        if self._billingstatements is None:
            self._billingstatements = []
        self._billingstatements.append(property_value)

    def load_billingstatements(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "BillingStatements"
        values = self._service_context.query(path)
        if values is None:
            return
        self._billingstatements = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._billingstatements.append(Statement.create_instance_from_entity(entity_value, self._service_context))

    def _get_billingstatements_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("BillingStatements", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._billingstatements = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._billingstatements.append(Statement.create_instance_from_entity(entity_value, self._service_context))


    def get_thestoredpi(self):
        return self._thestoredpi

    def set_thestoredpi(self, navitation_value):
        self._thestoredpi = navitation_value

    def load_thestoredpi(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "TheStoredPI"
        values = self._service_context.query(path)
        if values is None:
            return
        self._thestoredpi = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._thestoredpi = StoredPI.create_instance_from_entity(entity_value, self._service_context)

    def _get_thestoredpi_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("TheStoredPI", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._thestoredpi = StoredPI.create_instance_from_entity(entity_value, self._service_context)


    def get_backupstoredpi(self):
        return self._backupstoredpi

    def set_backupstoredpi(self, navitation_value):
        self._backupstoredpi = navitation_value

    def load_backupstoredpi(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "BackupStoredPI"
        values = self._service_context.query(path)
        if values is None:
            return
        self._backupstoredpi = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._backupstoredpi = StoredPI.create_instance_from_entity(entity_value, self._service_context)

    def _get_backupstoredpi_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("BackupStoredPI", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._backupstoredpi = StoredPI.create_instance_from_entity(entity_value, self._service_context)


    def get_paymentinstrumentid(self):
        return self._paymentinstrumentid

    def set_paymentinstrumentid(self, property_value):
        self._paymentinstrumentid = property_value

    def _get_paymentinstrumentid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("PaymentInstrumentID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._paymentinstrumentid = int(primitive_value.to_string())
            except:
                self._paymentinstrumentid = primitive_value.to_string()

    def _set_paymentinstrumentid_to_entity(self, entity):
        if entity is None or self._paymentinstrumentid is None:
            return
        entity.set_value("PaymentInstrumentID", self._paymentinstrumentid)


    def get_createddate(self):
        return self._createddate

    def set_createddate(self, property_value):
        self._createddate = property_value

    def _get_createddate_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CreatedDate", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._createddate = eval(primitive_value.to_string())
            except:
                self._createddate = primitive_value.to_string()

    def _set_createddate_to_entity(self, entity):
        if entity is None or self._createddate is None:
            return
        entity.set_value("CreatedDate", self._createddate)


    def get_friendlyname(self):
        return self._friendlyname

    def set_friendlyname(self, property_value):
        self._friendlyname = property_value

    def _get_friendlyname_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("FriendlyName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._friendlyname = primitive_value.to_string()
            except:
                self._friendlyname = primitive_value.to_string()

    def _set_friendlyname_to_entity(self, entity):
        if entity is None or self._friendlyname is None:
            return
        entity.set_value("FriendlyName", self._friendlyname)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "PaymentInstrument":
            if real_type_name in PaymentInstrument._derived_creator_map:
                instance = PaymentInstrument._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = PaymentInstrument(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_billingstatements_from_entity(entity_value)
        self._get_thestoredpi_from_entity(entity_value)
        self._get_backupstoredpi_from_entity(entity_value)
        self._get_paymentinstrumentid_from_entity(entity_value)
        self._get_createddate_from_entity(entity_value)
        self._get_friendlyname_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_paymentinstrumentid_to_entity(entity_value)
        self._set_createddate_to_entity(entity_value)
        self._set_friendlyname_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class ProductReview(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._comment = None
        self._author = None
        self._revisionid = 0
        self._reviewtitle = None
        self._productdetailid = 0
        self._productid = 0

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"ProductReview"

    @staticmethod
    def get_full_name():
        return ProductReview._namespace + '.' + ProductReview._typename

    @staticmethod
    def get_type_name():
        return ProductReview._typename

    def get_comment(self):
        return self._comment

    def set_comment(self, property_value):
        self._comment = property_value

    def _get_comment_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Comment", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._comment = primitive_value.to_string()
            except:
                self._comment = primitive_value.to_string()

    def _set_comment_to_entity(self, entity):
        if entity is None or self._comment is None:
            return
        entity.set_value("Comment", self._comment)


    def get_author(self):
        return self._author

    def set_author(self, property_value):
        self._author = property_value

    def _get_author_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Author", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._author = primitive_value.to_string()
            except:
                self._author = primitive_value.to_string()

    def _set_author_to_entity(self, entity):
        if entity is None or self._author is None:
            return
        entity.set_value("Author", self._author)


    def get_revisionid(self):
        return self._revisionid

    def set_revisionid(self, property_value):
        self._revisionid = property_value

    def _get_revisionid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("RevisionID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._revisionid = int(primitive_value.to_string())
            except:
                self._revisionid = primitive_value.to_string()

    def _set_revisionid_to_entity(self, entity):
        if entity is None or self._revisionid is None:
            return
        entity.set_value("RevisionID", self._revisionid)


    def get_reviewtitle(self):
        return self._reviewtitle

    def set_reviewtitle(self, property_value):
        self._reviewtitle = property_value

    def _get_reviewtitle_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ReviewTitle", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._reviewtitle = primitive_value.to_string()
            except:
                self._reviewtitle = primitive_value.to_string()

    def _set_reviewtitle_to_entity(self, entity):
        if entity is None or self._reviewtitle is None:
            return
        entity.set_value("ReviewTitle", self._reviewtitle)


    def get_productdetailid(self):
        return self._productdetailid

    def set_productdetailid(self, property_value):
        self._productdetailid = property_value

    def _get_productdetailid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ProductDetailID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._productdetailid = int(primitive_value.to_string())
            except:
                self._productdetailid = primitive_value.to_string()

    def _set_productdetailid_to_entity(self, entity):
        if entity is None or self._productdetailid is None:
            return
        entity.set_value("ProductDetailID", self._productdetailid)


    def get_productid(self):
        return self._productid

    def set_productid(self, property_value):
        self._productid = property_value

    def _get_productid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ProductID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._productid = int(primitive_value.to_string())
            except:
                self._productid = primitive_value.to_string()

    def _set_productid_to_entity(self, entity):
        if entity is None or self._productid is None:
            return
        entity.set_value("ProductID", self._productid)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "ProductReview":
            if real_type_name in ProductReview._derived_creator_map:
                instance = ProductReview._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = ProductReview(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_comment_from_entity(entity_value)
        self._get_author_from_entity(entity_value)
        self._get_revisionid_from_entity(entity_value)
        self._get_reviewtitle_from_entity(entity_value)
        self._get_productdetailid_from_entity(entity_value)
        self._get_productid_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_comment_to_entity(entity_value)
        self._set_author_to_entity(entity_value)
        self._set_revisionid_to_entity(entity_value)
        self._set_reviewtitle_to_entity(entity_value)
        self._set_productdetailid_to_entity(entity_value)
        self._set_productid_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Product(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._covercolors = []
        self._name = None
        self._quantityinstock = 0
        self._discontinued = False
        self._quantityperunit = None
        self._details = None
        self._useraccess = None
        self._unitprice = 0.0
        self._skincolor = None
        self._productid = 0

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Product"

    @staticmethod
    def get_full_name():
        return Product._namespace + '.' + Product._typename

    @staticmethod
    def get_type_name():
        return Product._typename

    def AddAccessRight(self, accessRight):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "AddAccessRight"
        parameters = odata_client_python.vector_odata_parameter()
        if accessRight is not None:
            enum_string = AccessLevel.get_string_from_enum_value(accessRight)
            enum_type = odata_client_python.edm_enum_type("", "", "", False)
            enum_value = odata_client_python.odata_enum_value(enum_type, enum_string)
            if enum_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("accessRight", enum_value))
        return self._service_context.operation_query_enum(function_query_url, parameters, False, AccessLevel)


    def get_covercolors(self):
        return self._covercolors

    def set_covercolors(self, property_values):
        self._covercolors = property_values

    def add_to_covercolors(self, property_value):
        if self._covercolors is None:
            self._covercolors = []
        self._covercolors.append(property_value)

    def _get_covercolors_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CoverColors", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._covercolors = []
        for odata_value in property_collection_value.get_collection_values():
            enum_value = odata_client_python.to_enum_value(odata_value)
            if enum_value is None:
                continue
            self._covercolors.append(Color.get_enum_value_from_string(enum_value.to_string()))

    def _set_covercolors_to_entity(self, entity):
        if self._covercolors is None:
            return
        if entity is None or entity.get_value_type() is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("CoverColors")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.odata_collection_value(collection_value_type)
        for property in self._covercolors:
            collection_value.add_collection_value(odata_client_python.odata_enum_value(collection_value_type.get_element_type(), Color.get_string_from_enum_value(property)))
        entity.set_value("CoverColors", collection_value)


    def get_name(self):
        return self._name

    def set_name(self, property_value):
        self._name = property_value

    def _get_name_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Name", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._name = primitive_value.to_string()
            except:
                self._name = primitive_value.to_string()

    def _set_name_to_entity(self, entity):
        if entity is None or self._name is None:
            return
        entity.set_value("Name", self._name)


    def get_quantityinstock(self):
        return self._quantityinstock

    def set_quantityinstock(self, property_value):
        self._quantityinstock = property_value

    def _get_quantityinstock_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("QuantityInStock", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._quantityinstock = int(primitive_value.to_string())
            except:
                self._quantityinstock = primitive_value.to_string()

    def _set_quantityinstock_to_entity(self, entity):
        if entity is None or self._quantityinstock is None:
            return
        entity.set_value("QuantityInStock", self._quantityinstock)


    def get_discontinued(self):
        return self._discontinued

    def set_discontinued(self, property_value):
        self._discontinued = property_value

    def _get_discontinued_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Discontinued", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._discontinued = primitive_value.to_string() == 'true'
            except:
                self._discontinued = primitive_value.to_string()

    def _set_discontinued_to_entity(self, entity):
        if entity is None or self._discontinued is None:
            return
        entity.set_value("Discontinued", self._discontinued)


    def GetProductDetails(self, count):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "GetProductDetails"
        parameters = odata_client_python.vector_odata_parameter()
        if count is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(count)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("count", primitive_value))
        return self._service_context.operation_query_entityset(function_query_url, parameters, True, ProductDetail)


    def get_quantityperunit(self):
        return self._quantityperunit

    def set_quantityperunit(self, property_value):
        self._quantityperunit = property_value

    def _get_quantityperunit_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("QuantityPerUnit", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._quantityperunit = primitive_value.to_string()
            except:
                self._quantityperunit = primitive_value.to_string()

    def _set_quantityperunit_to_entity(self, entity):
        if entity is None or self._quantityperunit is None:
            return
        entity.set_value("QuantityPerUnit", self._quantityperunit)


    def get_details(self):
        return self._details

    def set_details(self, property_values):
        self._details = property_values

    def add_to_details(self, property_value):
        if self._details is None:
            self._details = []
        self._details.append(property_value)

    def load_details(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Details"
        values = self._service_context.query(path)
        if values is None:
            return
        self._details = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._details.append(ProductDetail.create_instance_from_entity(entity_value, self._service_context))

    def _get_details_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Details", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._details = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._details.append(ProductDetail.create_instance_from_entity(entity_value, self._service_context))


    def get_useraccess(self):
        return self._useraccess

    def set_useraccess(self, property_value):
        self._useraccess = property_value

    def _get_useraccess_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("UserAccess", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        enum_value = odata_client_python.to_enum_value(property_value)
        if enum_value is not None:
            self._useraccess = AccessLevel.get_enum_value_from_string(enum_value.to_string())

    def _set_useraccess_to_entity(self, entity):
        if entity is None or self._useraccess is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("UserAccess")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        enum_value = odata_client_python.odata_enum_value(property_type, AccessLevel.get_string_from_enum_value(self._useraccess))
        entity.set_value("UserAccess", enum_value)


    def get_unitprice(self):
        return self._unitprice

    def set_unitprice(self, property_value):
        self._unitprice = property_value

    def _get_unitprice_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("UnitPrice", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._unitprice = float(primitive_value.to_string())
            except:
                self._unitprice = primitive_value.to_string()

    def _set_unitprice_to_entity(self, entity):
        if entity is None or self._unitprice is None:
            return
        entity.set_value("UnitPrice", self._unitprice)


    def get_skincolor(self):
        return self._skincolor

    def set_skincolor(self, property_value):
        self._skincolor = property_value

    def _get_skincolor_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("SkinColor", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        enum_value = odata_client_python.to_enum_value(property_value)
        if enum_value is not None:
            self._skincolor = Color.get_enum_value_from_string(enum_value.to_string())

    def _set_skincolor_to_entity(self, entity):
        if entity is None or self._skincolor is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("SkinColor")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        enum_value = odata_client_python.odata_enum_value(property_type, Color.get_string_from_enum_value(self._skincolor))
        entity.set_value("SkinColor", enum_value)


    def get_productid(self):
        return self._productid

    def set_productid(self, property_value):
        self._productid = property_value

    def _get_productid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ProductID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._productid = int(primitive_value.to_string())
            except:
                self._productid = primitive_value.to_string()

    def _set_productid_to_entity(self, entity):
        if entity is None or self._productid is None:
            return
        entity.set_value("ProductID", self._productid)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Product":
            if real_type_name in Product._derived_creator_map:
                instance = Product._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Product(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_covercolors_from_entity(entity_value)
        self._get_name_from_entity(entity_value)
        self._get_quantityinstock_from_entity(entity_value)
        self._get_discontinued_from_entity(entity_value)
        self._get_quantityperunit_from_entity(entity_value)
        self._get_details_from_entity(entity_value)
        self._get_useraccess_from_entity(entity_value)
        self._get_unitprice_from_entity(entity_value)
        self._get_skincolor_from_entity(entity_value)
        self._get_productid_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_covercolors_to_entity(entity_value)
        self._set_name_to_entity(entity_value)
        self._set_quantityinstock_to_entity(entity_value)
        self._set_discontinued_to_entity(entity_value)
        self._set_quantityperunit_to_entity(entity_value)
        self._set_useraccess_to_entity(entity_value)
        self._set_unitprice_to_entity(entity_value)
        self._set_skincolor_to_entity(entity_value)
        self._set_productid_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Club(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._clubid = 0
        self._name = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Club"

    @staticmethod
    def get_full_name():
        return Club._namespace + '.' + Club._typename

    @staticmethod
    def get_type_name():
        return Club._typename

    def get_clubid(self):
        return self._clubid

    def set_clubid(self, property_value):
        self._clubid = property_value

    def _get_clubid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ClubID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._clubid = int(primitive_value.to_string())
            except:
                self._clubid = primitive_value.to_string()

    def _set_clubid_to_entity(self, entity):
        if entity is None or self._clubid is None:
            return
        entity.set_value("ClubID", self._clubid)


    def get_name(self):
        return self._name

    def set_name(self, property_value):
        self._name = property_value

    def _get_name_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Name", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._name = primitive_value.to_string()
            except:
                self._name = primitive_value.to_string()

    def _set_name_to_entity(self, entity):
        if entity is None or self._name is None:
            return
        entity.set_value("Name", self._name)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Club":
            if real_type_name in Club._derived_creator_map:
                instance = Club._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Club(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_clubid_from_entity(entity_value)
        self._get_name_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_clubid_to_entity(entity_value)
        self._set_name_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Company(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._name = None
        self._companycategory = None
        self._companyid = 0
        self._employees = None
        self._revenue = 0
        self._departments = None
        self._coredepartment = None
        self._vipcustomer = None
        self._address = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Company"

    @staticmethod
    def get_full_name():
        return Company._namespace + '.' + Company._typename

    @staticmethod
    def get_type_name():
        return Company._typename

    def get_name(self):
        return self._name

    def set_name(self, property_value):
        self._name = property_value

    def _get_name_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Name", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._name = primitive_value.to_string()
            except:
                self._name = primitive_value.to_string()

    def _set_name_to_entity(self, entity):
        if entity is None or self._name is None:
            return
        entity.set_value("Name", self._name)


    def get_companycategory(self):
        return self._companycategory

    def set_companycategory(self, property_value):
        self._companycategory = property_value

    def _get_companycategory_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CompanyCategory", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        enum_value = odata_client_python.to_enum_value(property_value)
        if enum_value is not None:
            self._companycategory = CompanyCategory.get_enum_value_from_string(enum_value.to_string())

    def _set_companycategory_to_entity(self, entity):
        if entity is None or self._companycategory is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("CompanyCategory")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        enum_value = odata_client_python.odata_enum_value(property_type, CompanyCategory.get_string_from_enum_value(self._companycategory))
        entity.set_value("CompanyCategory", enum_value)


    def get_companyid(self):
        return self._companyid

    def set_companyid(self, property_value):
        self._companyid = property_value

    def _get_companyid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CompanyID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._companyid = int(primitive_value.to_string())
            except:
                self._companyid = primitive_value.to_string()

    def _set_companyid_to_entity(self, entity):
        if entity is None or self._companyid is None:
            return
        entity.set_value("CompanyID", self._companyid)


    def get_employees(self):
        return self._employees

    def set_employees(self, property_values):
        self._employees = property_values

    def add_to_employees(self, property_value):
        if self._employees is None:
            self._employees = []
        self._employees.append(property_value)

    def load_employees(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Employees"
        values = self._service_context.query(path)
        if values is None:
            return
        self._employees = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._employees.append(Employee.create_instance_from_entity(entity_value, self._service_context))

    def _get_employees_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Employees", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._employees = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._employees.append(Employee.create_instance_from_entity(entity_value, self._service_context))


    def get_revenue(self):
        return self._revenue

    def set_revenue(self, property_value):
        self._revenue = property_value

    def _get_revenue_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Revenue", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._revenue = int(primitive_value.to_string())
            except:
                self._revenue = primitive_value.to_string()

    def _set_revenue_to_entity(self, entity):
        if entity is None or self._revenue is None:
            return
        entity.set_value("Revenue", self._revenue)


    def get_departments(self):
        return self._departments

    def set_departments(self, property_values):
        self._departments = property_values

    def add_to_departments(self, property_value):
        if self._departments is None:
            self._departments = []
        self._departments.append(property_value)

    def load_departments(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Departments"
        values = self._service_context.query(path)
        if values is None:
            return
        self._departments = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._departments.append(Department.create_instance_from_entity(entity_value, self._service_context))

    def _get_departments_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Departments", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._departments = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._departments.append(Department.create_instance_from_entity(entity_value, self._service_context))


    def IncreaseRevenue(self, IncreaseValue):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "IncreaseRevenue"
        parameters = odata_client_python.vector_odata_parameter()
        if IncreaseValue is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(IncreaseValue)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("IncreaseValue", primitive_value))
        return self._service_context.operation_query_primitive(function_query_url, parameters, False, "int64_t")


    def get_coredepartment(self):
        return self._coredepartment

    def set_coredepartment(self, navitation_value):
        self._coredepartment = navitation_value

    def load_coredepartment(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "CoreDepartment"
        values = self._service_context.query(path)
        if values is None:
            return
        self._coredepartment = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._coredepartment = Department.create_instance_from_entity(entity_value, self._service_context)

    def _get_coredepartment_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CoreDepartment", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._coredepartment = Department.create_instance_from_entity(entity_value, self._service_context)


    def get_vipcustomer(self):
        return self._vipcustomer

    def set_vipcustomer(self, navitation_value):
        self._vipcustomer = navitation_value

    def load_vipcustomer(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "VipCustomer"
        values = self._service_context.query(path)
        if values is None:
            return
        self._vipcustomer = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._vipcustomer = Customer.create_instance_from_entity(entity_value, self._service_context)

    def _get_vipcustomer_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("VipCustomer", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._vipcustomer = Customer.create_instance_from_entity(entity_value, self._service_context)


    def get_address(self):
        return self._address

    def set_address(self, property_value):
        self._address = property_value

    def _get_address_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Address", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Complex:
            complex_value = odata_client_python.to_complex_value(property_value)
            self._address = Address.create_instance_from_complex(complex_value, self._service_context)

    def _set_address_to_entity(self, entity):
        if entity is None or self._address is None:
            return
        entity.set_value("Address", self._address.to_value())


    def GetEmployeesCount(self):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "GetEmployeesCount"
        parameters = odata_client_python.vector_odata_parameter()
        return self._service_context.operation_query_primitive(function_query_url, parameters, True, "int32_t")


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Company":
            if real_type_name in Company._derived_creator_map:
                instance = Company._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Company(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_name_from_entity(entity_value)
        self._get_companycategory_from_entity(entity_value)
        self._get_companyid_from_entity(entity_value)
        self._get_employees_from_entity(entity_value)
        self._get_revenue_from_entity(entity_value)
        self._get_departments_from_entity(entity_value)
        self._get_coredepartment_from_entity(entity_value)
        self._get_vipcustomer_from_entity(entity_value)
        self._get_address_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_name_to_entity(entity_value)
        self._set_companycategory_to_entity(entity_value)
        self._set_companyid_to_entity(entity_value)
        self._set_revenue_to_entity(entity_value)
        self._set_address_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class LabourUnion(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._labourunionid = 0
        self._name = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"LabourUnion"

    @staticmethod
    def get_full_name():
        return LabourUnion._namespace + '.' + LabourUnion._typename

    @staticmethod
    def get_type_name():
        return LabourUnion._typename

    def ChangeLabourUnionName(self, name):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "ChangeLabourUnionName"
        parameters = odata_client_python.vector_odata_parameter()
        if name is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(name)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("name", primitive_value))
        return self._service_context.operation_query_void(function_query_url, parameters, False)


    def get_labourunionid(self):
        return self._labourunionid

    def set_labourunionid(self, property_value):
        self._labourunionid = property_value

    def _get_labourunionid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("LabourUnionID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._labourunionid = int(primitive_value.to_string())
            except:
                self._labourunionid = primitive_value.to_string()

    def _set_labourunionid_to_entity(self, entity):
        if entity is None or self._labourunionid is None:
            return
        entity.set_value("LabourUnionID", self._labourunionid)


    def get_name(self):
        return self._name

    def set_name(self, property_value):
        self._name = property_value

    def _get_name_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Name", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._name = primitive_value.to_string()
            except:
                self._name = primitive_value.to_string()

    def _set_name_to_entity(self, entity):
        if entity is None or self._name is None:
            return
        entity.set_value("Name", self._name)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "LabourUnion":
            if real_type_name in LabourUnion._derived_creator_map:
                instance = LabourUnion._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = LabourUnion(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_labourunionid_from_entity(entity_value)
        self._get_name_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_labourunionid_to_entity(entity_value)
        self._set_name_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class CreditCardPI(PaymentInstrument):

    def __init__(self, service_context):
        PaymentInstrument.__init__(self, service_context)

        self._holdername = None
        self._cvv = None
        self._experationdate = None
        self._creditrecords = None
        self._cardnumber = None
        self._balance = 0.0

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"CreditCardPI"

    @staticmethod
    def get_full_name():
        return CreditCardPI._namespace + '.' + CreditCardPI._typename

    @staticmethod
    def get_type_name():
        return CreditCardPI._typename

    def get_holdername(self):
        return self._holdername

    def set_holdername(self, property_value):
        self._holdername = property_value

    def _get_holdername_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("HolderName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._holdername = primitive_value.to_string()
            except:
                self._holdername = primitive_value.to_string()

    def _set_holdername_to_entity(self, entity):
        if entity is None or self._holdername is None:
            return
        entity.set_value("HolderName", self._holdername)


    def get_cvv(self):
        return self._cvv

    def set_cvv(self, property_value):
        self._cvv = property_value

    def _get_cvv_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CVV", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._cvv = primitive_value.to_string()
            except:
                self._cvv = primitive_value.to_string()

    def _set_cvv_to_entity(self, entity):
        if entity is None or self._cvv is None:
            return
        entity.set_value("CVV", self._cvv)


    def get_experationdate(self):
        return self._experationdate

    def set_experationdate(self, property_value):
        self._experationdate = property_value

    def _get_experationdate_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ExperationDate", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._experationdate = eval(primitive_value.to_string())
            except:
                self._experationdate = primitive_value.to_string()

    def _set_experationdate_to_entity(self, entity):
        if entity is None or self._experationdate is None:
            return
        entity.set_value("ExperationDate", self._experationdate)


    def get_creditrecords(self):
        return self._creditrecords

    def set_creditrecords(self, property_values):
        self._creditrecords = property_values

    def add_to_creditrecords(self, property_value):
        if self._creditrecords is None:
            self._creditrecords = []
        self._creditrecords.append(property_value)

    def load_creditrecords(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "CreditRecords"
        values = self._service_context.query(path)
        if values is None:
            return
        self._creditrecords = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._creditrecords.append(CreditRecord.create_instance_from_entity(entity_value, self._service_context))

    def _get_creditrecords_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CreditRecords", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._creditrecords = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._creditrecords.append(CreditRecord.create_instance_from_entity(entity_value, self._service_context))


    def get_cardnumber(self):
        return self._cardnumber

    def set_cardnumber(self, property_value):
        self._cardnumber = property_value

    def _get_cardnumber_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CardNumber", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._cardnumber = primitive_value.to_string()
            except:
                self._cardnumber = primitive_value.to_string()

    def _set_cardnumber_to_entity(self, entity):
        if entity is None or self._cardnumber is None:
            return
        entity.set_value("CardNumber", self._cardnumber)


    def get_balance(self):
        return self._balance

    def set_balance(self, property_value):
        self._balance = property_value

    def _get_balance_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Balance", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._balance = float(primitive_value.to_string())
            except:
                self._balance = primitive_value.to_string()

    def _set_balance_to_entity(self, entity):
        if entity is None or self._balance is None:
            return
        entity.set_value("Balance", self._balance)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "CreditCardPI":
            if real_type_name in CreditCardPI._derived_creator_map:
                instance = CreditCardPI._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = CreditCardPI(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._PaymentInstrument__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_holdername_from_entity(entity_value)
        self._get_cvv_from_entity(entity_value)
        self._get_experationdate_from_entity(entity_value)
        self._get_creditrecords_from_entity(entity_value)
        self._get_cardnumber_from_entity(entity_value)
        self._get_balance_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = self._PaymentInstrument__to_value()
        entity_value.set_value_type(entity_type)
        self._set_holdername_to_entity(entity_value)
        self._set_cvv_to_entity(entity_value)
        self._set_experationdate_to_entity(entity_value)
        self._set_cardnumber_to_entity(entity_value)
        self._set_balance_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Subscription(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._category = None
        self._subscriptionid = 0
        self._createddate = None
        self._templateguid = None
        self._title = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Subscription"

    @staticmethod
    def get_full_name():
        return Subscription._namespace + '.' + Subscription._typename

    @staticmethod
    def get_type_name():
        return Subscription._typename

    def get_category(self):
        return self._category

    def set_category(self, property_value):
        self._category = property_value

    def _get_category_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Category", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._category = primitive_value.to_string()
            except:
                self._category = primitive_value.to_string()

    def _set_category_to_entity(self, entity):
        if entity is None or self._category is None:
            return
        entity.set_value("Category", self._category)


    def get_subscriptionid(self):
        return self._subscriptionid

    def set_subscriptionid(self, property_value):
        self._subscriptionid = property_value

    def _get_subscriptionid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("SubscriptionID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._subscriptionid = int(primitive_value.to_string())
            except:
                self._subscriptionid = primitive_value.to_string()

    def _set_subscriptionid_to_entity(self, entity):
        if entity is None or self._subscriptionid is None:
            return
        entity.set_value("SubscriptionID", self._subscriptionid)


    def get_createddate(self):
        return self._createddate

    def set_createddate(self, property_value):
        self._createddate = property_value

    def _get_createddate_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CreatedDate", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._createddate = eval(primitive_value.to_string())
            except:
                self._createddate = primitive_value.to_string()

    def _set_createddate_to_entity(self, entity):
        if entity is None or self._createddate is None:
            return
        entity.set_value("CreatedDate", self._createddate)


    def get_templateguid(self):
        return self._templateguid

    def set_templateguid(self, property_value):
        self._templateguid = property_value

    def _get_templateguid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("TemplateGuid", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._templateguid = primitive_value.to_string()
            except:
                self._templateguid = primitive_value.to_string()

    def _set_templateguid_to_entity(self, entity):
        if entity is None or self._templateguid is None:
            return
        entity.set_value("TemplateGuid", self._templateguid)


    def get_title(self):
        return self._title

    def set_title(self, property_value):
        self._title = property_value

    def _get_title_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Title", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._title = primitive_value.to_string()
            except:
                self._title = primitive_value.to_string()

    def _set_title_to_entity(self, entity):
        if entity is None or self._title is None:
            return
        entity.set_value("Title", self._title)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Subscription":
            if real_type_name in Subscription._derived_creator_map:
                instance = Subscription._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Subscription(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_category_from_entity(entity_value)
        self._get_subscriptionid_from_entity(entity_value)
        self._get_createddate_from_entity(entity_value)
        self._get_templateguid_from_entity(entity_value)
        self._get_title_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_category_to_entity(entity_value)
        self._set_subscriptionid_to_entity(entity_value)
        self._set_createddate_to_entity(entity_value)
        self._set_templateguid_to_entity(entity_value)
        self._set_title_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Account(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._availablesubscriptiontemplatess = None
        self._mygiftcard = None
        self._accountinfo = None
        self._mypaymentinstruments = None
        self._activesubscriptions = None
        self._countryregion = None
        self._accountid = 0

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Account"

    @staticmethod
    def get_full_name():
        return Account._namespace + '.' + Account._typename

    @staticmethod
    def get_type_name():
        return Account._typename

    def get_availablesubscriptiontemplatess(self):
        return self._availablesubscriptiontemplatess

    def set_availablesubscriptiontemplatess(self, property_values):
        self._availablesubscriptiontemplatess = property_values

    def add_to_availablesubscriptiontemplatess(self, property_value):
        if self._availablesubscriptiontemplatess is None:
            self._availablesubscriptiontemplatess = []
        self._availablesubscriptiontemplatess.append(property_value)

    def load_availablesubscriptiontemplatess(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "AvailableSubscriptionTemplatess"
        values = self._service_context.query(path)
        if values is None:
            return
        self._availablesubscriptiontemplatess = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._availablesubscriptiontemplatess.append(Subscription.create_instance_from_entity(entity_value, self._service_context))

    def _get_availablesubscriptiontemplatess_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("AvailableSubscriptionTemplatess", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._availablesubscriptiontemplatess = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._availablesubscriptiontemplatess.append(Subscription.create_instance_from_entity(entity_value, self._service_context))


    def GetDefaultPI(self):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "GetDefaultPI"
        parameters = odata_client_python.vector_odata_parameter()
        return self._service_context.operation_query_entityset(function_query_url, parameters, True, PaymentInstrument)


    def RefreshDefaultPI(self, newDate):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "RefreshDefaultPI"
        parameters = odata_client_python.vector_odata_parameter()
        if newDate is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(newDate)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("newDate", primitive_value))
        return self._service_context.operation_query_entityset(function_query_url, parameters, False, PaymentInstrument)


    def get_mygiftcard(self):
        return self._mygiftcard

    def set_mygiftcard(self, navitation_value):
        self._mygiftcard = navitation_value

    def load_mygiftcard(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "MyGiftCard"
        values = self._service_context.query(path)
        if values is None:
            return
        self._mygiftcard = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._mygiftcard = GiftCard.create_instance_from_entity(entity_value, self._service_context)

    def _get_mygiftcard_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("MyGiftCard", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._mygiftcard = GiftCard.create_instance_from_entity(entity_value, self._service_context)


    def get_accountinfo(self):
        return self._accountinfo

    def set_accountinfo(self, property_value):
        self._accountinfo = property_value

    def _get_accountinfo_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("AccountInfo", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Complex:
            complex_value = odata_client_python.to_complex_value(property_value)
            self._accountinfo = AccountInfo.create_instance_from_complex(complex_value, self._service_context)

    def _set_accountinfo_to_entity(self, entity):
        if entity is None or self._accountinfo is None:
            return
        entity.set_value("AccountInfo", self._accountinfo.to_value())


    def GetAccountInfo(self):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "GetAccountInfo"
        parameters = odata_client_python.vector_odata_parameter()
        return self._service_context.operation_query_complex(function_query_url, parameters, True, AccountInfo)


    def get_mypaymentinstruments(self):
        return self._mypaymentinstruments

    def set_mypaymentinstruments(self, property_values):
        self._mypaymentinstruments = property_values

    def add_to_mypaymentinstruments(self, property_value):
        if self._mypaymentinstruments is None:
            self._mypaymentinstruments = []
        self._mypaymentinstruments.append(property_value)

    def load_mypaymentinstruments(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "MyPaymentInstruments"
        values = self._service_context.query(path)
        if values is None:
            return
        self._mypaymentinstruments = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._mypaymentinstruments.append(PaymentInstrument.create_instance_from_entity(entity_value, self._service_context))

    def _get_mypaymentinstruments_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("MyPaymentInstruments", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._mypaymentinstruments = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._mypaymentinstruments.append(PaymentInstrument.create_instance_from_entity(entity_value, self._service_context))


    def get_activesubscriptions(self):
        return self._activesubscriptions

    def set_activesubscriptions(self, property_values):
        self._activesubscriptions = property_values

    def add_to_activesubscriptions(self, property_value):
        if self._activesubscriptions is None:
            self._activesubscriptions = []
        self._activesubscriptions.append(property_value)

    def load_activesubscriptions(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "ActiveSubscriptions"
        values = self._service_context.query(path)
        if values is None:
            return
        self._activesubscriptions = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._activesubscriptions.append(Subscription.create_instance_from_entity(entity_value, self._service_context))

    def _get_activesubscriptions_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ActiveSubscriptions", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._activesubscriptions = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._activesubscriptions.append(Subscription.create_instance_from_entity(entity_value, self._service_context))


    def get_countryregion(self):
        return self._countryregion

    def set_countryregion(self, property_value):
        self._countryregion = property_value

    def _get_countryregion_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CountryRegion", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._countryregion = primitive_value.to_string()
            except:
                self._countryregion = primitive_value.to_string()

    def _set_countryregion_to_entity(self, entity):
        if entity is None or self._countryregion is None:
            return
        entity.set_value("CountryRegion", self._countryregion)


    def get_accountid(self):
        return self._accountid

    def set_accountid(self, property_value):
        self._accountid = property_value

    def _get_accountid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("AccountID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._accountid = int(primitive_value.to_string())
            except:
                self._accountid = primitive_value.to_string()

    def _set_accountid_to_entity(self, entity):
        if entity is None or self._accountid is None:
            return
        entity.set_value("AccountID", self._accountid)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Account":
            if real_type_name in Account._derived_creator_map:
                instance = Account._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Account(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_availablesubscriptiontemplatess_from_entity(entity_value)
        self._get_mygiftcard_from_entity(entity_value)
        self._get_accountinfo_from_entity(entity_value)
        self._get_mypaymentinstruments_from_entity(entity_value)
        self._get_activesubscriptions_from_entity(entity_value)
        self._get_countryregion_from_entity(entity_value)
        self._get_accountid_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_accountinfo_to_entity(entity_value)
        self._set_countryregion_to_entity(entity_value)
        self._set_accountid_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Person(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._parent = None
        self._firstname = None
        self._personid = 0
        self._lastname = None
        self._middlename = None
        self._numbers = []
        self._homeaddress = None
        self._emails = []

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Person"

    @staticmethod
    def get_full_name():
        return Person._namespace + '.' + Person._typename

    @staticmethod
    def get_type_name():
        return Person._typename

    def ResetAddress(self, addresses, index):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "ResetAddress"
        parameters = odata_client_python.vector_odata_parameter()
        if isinstance(addresses, (list, tuple)):
            collection_value = odata_client_python.odata_collection_value(odata_client_python.edm_collection_type("action parameter"))
            for ins in addresses:
                if  isinstance(ins, Address):
                    value = ins.to_value()
                    if value is not None:
                        collection_value.add_collection_value(value)
            parameters.push_back(odata_client_python.odata_parameter("addresses", collection_value))
        if index is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(index)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("index", primitive_value))
        return self._service_context.operation_query_entityset(function_query_url, parameters, False, Person)


    def get_parent(self):
        return self._parent

    def set_parent(self, navitation_value):
        self._parent = navitation_value

    def load_parent(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Parent"
        values = self._service_context.query(path)
        if values is None:
            return
        self._parent = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._parent = Person.create_instance_from_entity(entity_value, self._service_context)

    def _get_parent_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Parent", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._parent = Person.create_instance_from_entity(entity_value, self._service_context)


    def get_firstname(self):
        return self._firstname

    def set_firstname(self, property_value):
        self._firstname = property_value

    def _get_firstname_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("FirstName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._firstname = primitive_value.to_string()
            except:
                self._firstname = primitive_value.to_string()

    def _set_firstname_to_entity(self, entity):
        if entity is None or self._firstname is None:
            return
        entity.set_value("FirstName", self._firstname)


    def get_personid(self):
        return self._personid

    def set_personid(self, property_value):
        self._personid = property_value

    def _get_personid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("PersonID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._personid = int(primitive_value.to_string())
            except:
                self._personid = primitive_value.to_string()

    def _set_personid_to_entity(self, entity):
        if entity is None or self._personid is None:
            return
        entity.set_value("PersonID", self._personid)


    def get_lastname(self):
        return self._lastname

    def set_lastname(self, property_value):
        self._lastname = property_value

    def _get_lastname_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("LastName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._lastname = primitive_value.to_string()
            except:
                self._lastname = primitive_value.to_string()

    def _set_lastname_to_entity(self, entity):
        if entity is None or self._lastname is None:
            return
        entity.set_value("LastName", self._lastname)


    def GetHomeAddress(self):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "GetHomeAddress"
        parameters = odata_client_python.vector_odata_parameter()
        return self._service_context.operation_query_complex(function_query_url, parameters, True, HomeAddress)


    def get_middlename(self):
        return self._middlename

    def set_middlename(self, property_value):
        self._middlename = property_value

    def _get_middlename_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("MiddleName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._middlename = primitive_value.to_string()
            except:
                self._middlename = primitive_value.to_string()

    def _set_middlename_to_entity(self, entity):
        if entity is None or self._middlename is None:
            return
        entity.set_value("MiddleName", self._middlename)


    def get_numbers(self):
        return self._numbers

    def set_numbers(self, property_values):
        self._numbers = property_values

    def add_to_numbers(self, property_value):
        if self._numbers is None:
            self._numbers = []
        self._numbers.append(property_value)

    def _get_numbers_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Numbers", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._numbers = []
        for odata_value in property_collection_value.get_collection_values():
            primitive_value = odata_client_python.to_primitive_value(odata_value)
            if primitive_value is None:
                continue
            try:
                value = primitive_value.to_string()
            except:
                value = primitive_value.to_string()
            self._numbers.append(value)

    def _set_numbers_to_entity(self, entity):
        if self._numbers is None:
            return
        if entity is None or entity.get_value_type() is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("Numbers")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.odata_collection_value(collection_value_type)
        for primitive in self._numbers:
            collection_value.add_collection_value(odata_client_python.odata_primitive_value.make_primitive_value(primitive))
        entity.set_value("Numbers", collection_value)


    def get_homeaddress(self):
        return self._homeaddress

    def set_homeaddress(self, property_value):
        self._homeaddress = property_value

    def _get_homeaddress_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("HomeAddress", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Complex:
            complex_value = odata_client_python.to_complex_value(property_value)
            self._homeaddress = Address.create_instance_from_complex(complex_value, self._service_context)

    def _set_homeaddress_to_entity(self, entity):
        if entity is None or self._homeaddress is None:
            return
        entity.set_value("HomeAddress", self._homeaddress.to_value())


    def get_emails(self):
        return self._emails

    def set_emails(self, property_values):
        self._emails = property_values

    def add_to_emails(self, property_value):
        if self._emails is None:
            self._emails = []
        self._emails.append(property_value)

    def _get_emails_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Emails", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._emails = []
        for odata_value in property_collection_value.get_collection_values():
            primitive_value = odata_client_python.to_primitive_value(odata_value)
            if primitive_value is None:
                continue
            try:
                value = primitive_value.to_string()
            except:
                value = primitive_value.to_string()
            self._emails.append(value)

    def _set_emails_to_entity(self, entity):
        if self._emails is None:
            return
        if entity is None or entity.get_value_type() is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("Emails")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.odata_collection_value(collection_value_type)
        for primitive in self._emails:
            collection_value.add_collection_value(odata_client_python.odata_primitive_value.make_primitive_value(primitive))
        entity.set_value("Emails", collection_value)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Person":
            if real_type_name in Person._derived_creator_map:
                instance = Person._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Person(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_parent_from_entity(entity_value)
        self._get_firstname_from_entity(entity_value)
        self._get_personid_from_entity(entity_value)
        self._get_lastname_from_entity(entity_value)
        self._get_middlename_from_entity(entity_value)
        self._get_numbers_from_entity(entity_value)
        self._get_homeaddress_from_entity(entity_value)
        self._get_emails_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_firstname_to_entity(entity_value)
        self._set_personid_to_entity(entity_value)
        self._set_lastname_to_entity(entity_value)
        self._set_middlename_to_entity(entity_value)
        self._set_numbers_to_entity(entity_value)
        self._set_homeaddress_to_entity(entity_value)
        self._set_emails_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class ProductDetail(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._description = None
        self._productname = None
        self._reviews = None
        self._relatedproduct = None
        self._productdetailid = 0
        self._productid = 0

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"ProductDetail"

    @staticmethod
    def get_full_name():
        return ProductDetail._namespace + '.' + ProductDetail._typename

    @staticmethod
    def get_type_name():
        return ProductDetail._typename

    def get_description(self):
        return self._description

    def set_description(self, property_value):
        self._description = property_value

    def _get_description_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Description", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._description = primitive_value.to_string()
            except:
                self._description = primitive_value.to_string()

    def _set_description_to_entity(self, entity):
        if entity is None or self._description is None:
            return
        entity.set_value("Description", self._description)


    def get_productname(self):
        return self._productname

    def set_productname(self, property_value):
        self._productname = property_value

    def _get_productname_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ProductName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._productname = primitive_value.to_string()
            except:
                self._productname = primitive_value.to_string()

    def _set_productname_to_entity(self, entity):
        if entity is None or self._productname is None:
            return
        entity.set_value("ProductName", self._productname)


    def get_reviews(self):
        return self._reviews

    def set_reviews(self, property_values):
        self._reviews = property_values

    def add_to_reviews(self, property_value):
        if self._reviews is None:
            self._reviews = []
        self._reviews.append(property_value)

    def load_reviews(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Reviews"
        values = self._service_context.query(path)
        if values is None:
            return
        self._reviews = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._reviews.append(ProductReview.create_instance_from_entity(entity_value, self._service_context))

    def _get_reviews_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Reviews", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._reviews = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._reviews.append(ProductReview.create_instance_from_entity(entity_value, self._service_context))


    def GetRelatedProduct(self):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "GetRelatedProduct"
        parameters = odata_client_python.vector_odata_parameter()
        return self._service_context.operation_query_entityset(function_query_url, parameters, True, Product)


    def get_relatedproduct(self):
        return self._relatedproduct

    def set_relatedproduct(self, navitation_value):
        self._relatedproduct = navitation_value

    def load_relatedproduct(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "RelatedProduct"
        values = self._service_context.query(path)
        if values is None:
            return
        self._relatedproduct = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._relatedproduct = Product.create_instance_from_entity(entity_value, self._service_context)

    def _get_relatedproduct_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("RelatedProduct", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._relatedproduct = Product.create_instance_from_entity(entity_value, self._service_context)


    def get_productdetailid(self):
        return self._productdetailid

    def set_productdetailid(self, property_value):
        self._productdetailid = property_value

    def _get_productdetailid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ProductDetailID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._productdetailid = int(primitive_value.to_string())
            except:
                self._productdetailid = primitive_value.to_string()

    def _set_productdetailid_to_entity(self, entity):
        if entity is None or self._productdetailid is None:
            return
        entity.set_value("ProductDetailID", self._productdetailid)


    def get_productid(self):
        return self._productid

    def set_productid(self, property_value):
        self._productid = property_value

    def _get_productid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ProductID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._productid = int(primitive_value.to_string())
            except:
                self._productid = primitive_value.to_string()

    def _set_productid_to_entity(self, entity):
        if entity is None or self._productid is None:
            return
        entity.set_value("ProductID", self._productid)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "ProductDetail":
            if real_type_name in ProductDetail._derived_creator_map:
                instance = ProductDetail._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = ProductDetail(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_description_from_entity(entity_value)
        self._get_productname_from_entity(entity_value)
        self._get_reviews_from_entity(entity_value)
        self._get_relatedproduct_from_entity(entity_value)
        self._get_productdetailid_from_entity(entity_value)
        self._get_productid_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_description_to_entity(entity_value)
        self._set_productname_to_entity(entity_value)
        self._set_productdetailid_to_entity(entity_value)
        self._set_productid_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Order(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._orderid = 0
        self._customerfororder = None
        self._loggedinemployee = None
        self._shelflife = None
        self._orderdetails = None
        self._ordershelflifes = []
        self._orderdate = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Order"

    @staticmethod
    def get_full_name():
        return Order._namespace + '.' + Order._typename

    @staticmethod
    def get_type_name():
        return Order._typename

    def get_orderid(self):
        return self._orderid

    def set_orderid(self, property_value):
        self._orderid = property_value

    def _get_orderid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("OrderID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._orderid = int(primitive_value.to_string())
            except:
                self._orderid = primitive_value.to_string()

    def _set_orderid_to_entity(self, entity):
        if entity is None or self._orderid is None:
            return
        entity.set_value("OrderID", self._orderid)


    def get_customerfororder(self):
        return self._customerfororder

    def set_customerfororder(self, navitation_value):
        self._customerfororder = navitation_value

    def load_customerfororder(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "CustomerForOrder"
        values = self._service_context.query(path)
        if values is None:
            return
        self._customerfororder = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._customerfororder = Customer.create_instance_from_entity(entity_value, self._service_context)

    def _get_customerfororder_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CustomerForOrder", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._customerfororder = Customer.create_instance_from_entity(entity_value, self._service_context)


    def get_loggedinemployee(self):
        return self._loggedinemployee

    def set_loggedinemployee(self, navitation_value):
        self._loggedinemployee = navitation_value

    def load_loggedinemployee(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "LoggedInEmployee"
        values = self._service_context.query(path)
        if values is None:
            return
        self._loggedinemployee = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._loggedinemployee = Employee.create_instance_from_entity(entity_value, self._service_context)

    def _get_loggedinemployee_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("LoggedInEmployee", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._loggedinemployee = Employee.create_instance_from_entity(entity_value, self._service_context)


    def get_shelflife(self):
        return self._shelflife

    def set_shelflife(self, property_value):
        self._shelflife = property_value

    def _get_shelflife_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("ShelfLife", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._shelflife = eval(primitive_value.to_string())
            except:
                self._shelflife = primitive_value.to_string()

    def _set_shelflife_to_entity(self, entity):
        if entity is None or self._shelflife is None:
            return
        entity.set_value("ShelfLife", self._shelflife)


    def get_orderdetails(self):
        return self._orderdetails

    def set_orderdetails(self, property_values):
        self._orderdetails = property_values

    def add_to_orderdetails(self, property_value):
        if self._orderdetails is None:
            self._orderdetails = []
        self._orderdetails.append(property_value)

    def load_orderdetails(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "OrderDetails"
        values = self._service_context.query(path)
        if values is None:
            return
        self._orderdetails = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._orderdetails.append(OrderDetail.create_instance_from_entity(entity_value, self._service_context))

    def _get_orderdetails_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("OrderDetails", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._orderdetails = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._orderdetails.append(OrderDetail.create_instance_from_entity(entity_value, self._service_context))


    def get_ordershelflifes(self):
        return self._ordershelflifes

    def set_ordershelflifes(self, property_values):
        self._ordershelflifes = property_values

    def add_to_ordershelflifes(self, property_value):
        if self._ordershelflifes is None:
            self._ordershelflifes = []
        self._ordershelflifes.append(property_value)

    def _get_ordershelflifes_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("OrderShelfLifes", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._ordershelflifes = []
        for odata_value in property_collection_value.get_collection_values():
            primitive_value = odata_client_python.to_primitive_value(odata_value)
            if primitive_value is None:
                continue
            try:
                value = eval(primitive_value.to_string())
            except:
                value = primitive_value.to_string()
            self._ordershelflifes.append(value)

    def _set_ordershelflifes_to_entity(self, entity):
        if self._ordershelflifes is None:
            return
        if entity is None or entity.get_value_type() is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("OrderShelfLifes")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.odata_collection_value(collection_value_type)
        for primitive in self._ordershelflifes:
            collection_value.add_collection_value(odata_client_python.odata_primitive_value.make_primitive_value(primitive))
        entity.set_value("OrderShelfLifes", collection_value)


    def get_orderdate(self):
        return self._orderdate

    def set_orderdate(self, property_value):
        self._orderdate = property_value

    def _get_orderdate_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("OrderDate", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._orderdate = eval(primitive_value.to_string())
            except:
                self._orderdate = primitive_value.to_string()

    def _set_orderdate_to_entity(self, entity):
        if entity is None or self._orderdate is None:
            return
        entity.set_value("OrderDate", self._orderdate)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Order":
            if real_type_name in Order._derived_creator_map:
                instance = Order._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Order(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_orderid_from_entity(entity_value)
        self._get_customerfororder_from_entity(entity_value)
        self._get_loggedinemployee_from_entity(entity_value)
        self._get_shelflife_from_entity(entity_value)
        self._get_orderdetails_from_entity(entity_value)
        self._get_ordershelflifes_from_entity(entity_value)
        self._get_orderdate_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_orderid_to_entity(entity_value)
        self._set_shelflife_to_entity(entity_value)
        self._set_ordershelflifes_to_entity(entity_value)
        self._set_orderdate_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class StoredPI(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._storedpiid = 0
        self._createddate = None
        self._piname = None
        self._pitype = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"StoredPI"

    @staticmethod
    def get_full_name():
        return StoredPI._namespace + '.' + StoredPI._typename

    @staticmethod
    def get_type_name():
        return StoredPI._typename

    def get_storedpiid(self):
        return self._storedpiid

    def set_storedpiid(self, property_value):
        self._storedpiid = property_value

    def _get_storedpiid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("StoredPIID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._storedpiid = int(primitive_value.to_string())
            except:
                self._storedpiid = primitive_value.to_string()

    def _set_storedpiid_to_entity(self, entity):
        if entity is None or self._storedpiid is None:
            return
        entity.set_value("StoredPIID", self._storedpiid)


    def get_createddate(self):
        return self._createddate

    def set_createddate(self, property_value):
        self._createddate = property_value

    def _get_createddate_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CreatedDate", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._createddate = eval(primitive_value.to_string())
            except:
                self._createddate = primitive_value.to_string()

    def _set_createddate_to_entity(self, entity):
        if entity is None or self._createddate is None:
            return
        entity.set_value("CreatedDate", self._createddate)


    def get_piname(self):
        return self._piname

    def set_piname(self, property_value):
        self._piname = property_value

    def _get_piname_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("PIName", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._piname = primitive_value.to_string()
            except:
                self._piname = primitive_value.to_string()

    def _set_piname_to_entity(self, entity):
        if entity is None or self._piname is None:
            return
        entity.set_value("PIName", self._piname)


    def get_pitype(self):
        return self._pitype

    def set_pitype(self, property_value):
        self._pitype = property_value

    def _get_pitype_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("PIType", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._pitype = primitive_value.to_string()
            except:
                self._pitype = primitive_value.to_string()

    def _set_pitype_to_entity(self, entity):
        if entity is None or self._pitype is None:
            return
        entity.set_value("PIType", self._pitype)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "StoredPI":
            if real_type_name in StoredPI._derived_creator_map:
                instance = StoredPI._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = StoredPI(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_storedpiid_from_entity(entity_value)
        self._get_createddate_from_entity(entity_value)
        self._get_piname_from_entity(entity_value)
        self._get_pitype_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_storedpiid_to_entity(entity_value)
        self._set_createddate_to_entity(entity_value)
        self._set_piname_to_entity(entity_value)
        self._set_pitype_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class CreditRecord(type_base):

    def __init__(self, service_context):
        type_base.__init__(self, service_context)

        self._isgood = False
        self._reason = None
        self._creditrecordid = 0
        self._createddate = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"CreditRecord"

    @staticmethod
    def get_full_name():
        return CreditRecord._namespace + '.' + CreditRecord._typename

    @staticmethod
    def get_type_name():
        return CreditRecord._typename

    def get_isgood(self):
        return self._isgood

    def set_isgood(self, property_value):
        self._isgood = property_value

    def _get_isgood_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("IsGood", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._isgood = primitive_value.to_string() == 'true'
            except:
                self._isgood = primitive_value.to_string()

    def _set_isgood_to_entity(self, entity):
        if entity is None or self._isgood is None:
            return
        entity.set_value("IsGood", self._isgood)


    def get_reason(self):
        return self._reason

    def set_reason(self, property_value):
        self._reason = property_value

    def _get_reason_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Reason", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._reason = primitive_value.to_string()
            except:
                self._reason = primitive_value.to_string()

    def _set_reason_to_entity(self, entity):
        if entity is None or self._reason is None:
            return
        entity.set_value("Reason", self._reason)


    def get_creditrecordid(self):
        return self._creditrecordid

    def set_creditrecordid(self, property_value):
        self._creditrecordid = property_value

    def _get_creditrecordid_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CreditRecordID", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._creditrecordid = int(primitive_value.to_string())
            except:
                self._creditrecordid = primitive_value.to_string()

    def _set_creditrecordid_to_entity(self, entity):
        if entity is None or self._creditrecordid is None:
            return
        entity.set_value("CreditRecordID", self._creditrecordid)


    def get_createddate(self):
        return self._createddate

    def set_createddate(self, property_value):
        self._createddate = property_value

    def _get_createddate_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("CreatedDate", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._createddate = eval(primitive_value.to_string())
            except:
                self._createddate = primitive_value.to_string()

    def _set_createddate_to_entity(self, entity):
        if entity is None or self._createddate is None:
            return
        entity.set_value("CreatedDate", self._createddate)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "CreditRecord":
            if real_type_name in CreditRecord._derived_creator_map:
                instance = CreditRecord._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = CreditRecord(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._type_base__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_isgood_from_entity(entity_value)
        self._get_reason_from_entity(entity_value)
        self._get_creditrecordid_from_entity(entity_value)
        self._get_createddate_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)
        self._set_isgood_to_entity(entity_value)
        self._set_reason_to_entity(entity_value)
        self._set_creditrecordid_to_entity(entity_value)
        self._set_createddate_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Employee(Person):

    def __init__(self, service_context):
        Person.__init__(self, service_context)

        self._company = None
        self._datehired = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Employee"

    @staticmethod
    def get_full_name():
        return Employee._namespace + '.' + Employee._typename

    @staticmethod
    def get_type_name():
        return Employee._typename

    def get_company(self):
        return self._company

    def set_company(self, navitation_value):
        self._company = navitation_value

    def load_company(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Company"
        values = self._service_context.query(path)
        if values is None:
            return
        self._company = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._company = Company.create_instance_from_entity(entity_value, self._service_context)

    def _get_company_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Company", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._company = Company.create_instance_from_entity(entity_value, self._service_context)


    def get_datehired(self):
        return self._datehired

    def set_datehired(self, property_value):
        self._datehired = property_value

    def _get_datehired_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("DateHired", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._datehired = eval(primitive_value.to_string())
            except:
                self._datehired = primitive_value.to_string()

    def _set_datehired_to_entity(self, entity):
        if entity is None or self._datehired is None:
            return
        entity.set_value("DateHired", self._datehired)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Employee":
            if real_type_name in Employee._derived_creator_map:
                instance = Employee._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Employee(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._Person__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_company_from_entity(entity_value)
        self._get_datehired_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = self._Person__to_value()
        entity_value.set_value_type(entity_type)
        self._set_datehired_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class PublicCompany(Company):

    def __init__(self, service_context):
        Company.__init__(self, service_context)

        self._stockexchange = None
        self._club = None
        self._assets = None
        self._labourunion = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"PublicCompany"

    @staticmethod
    def get_full_name():
        return PublicCompany._namespace + '.' + PublicCompany._typename

    @staticmethod
    def get_type_name():
        return PublicCompany._typename

    def get_stockexchange(self):
        return self._stockexchange

    def set_stockexchange(self, property_value):
        self._stockexchange = property_value

    def _get_stockexchange_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("StockExchange", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._stockexchange = primitive_value.to_string()
            except:
                self._stockexchange = primitive_value.to_string()

    def _set_stockexchange_to_entity(self, entity):
        if entity is None or self._stockexchange is None:
            return
        entity.set_value("StockExchange", self._stockexchange)


    def get_club(self):
        return self._club

    def set_club(self, navitation_value):
        self._club = navitation_value

    def load_club(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Club"
        values = self._service_context.query(path)
        if values is None:
            return
        self._club = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._club = Club.create_instance_from_entity(entity_value, self._service_context)

    def _get_club_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Club", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._club = Club.create_instance_from_entity(entity_value, self._service_context)


    def get_assets(self):
        return self._assets

    def set_assets(self, property_values):
        self._assets = property_values

    def add_to_assets(self, property_value):
        if self._assets is None:
            self._assets = []
        self._assets.append(property_value)

    def load_assets(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Assets"
        values = self._service_context.query(path)
        if values is None:
            return
        self._assets = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._assets.append(Asset.create_instance_from_entity(entity_value, self._service_context))

    def _get_assets_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Assets", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._assets = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._assets.append(Asset.create_instance_from_entity(entity_value, self._service_context))


    def get_labourunion(self):
        return self._labourunion

    def set_labourunion(self, navitation_value):
        self._labourunion = navitation_value

    def load_labourunion(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "LabourUnion"
        values = self._service_context.query(path)
        if values is None:
            return
        self._labourunion = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._labourunion = LabourUnion.create_instance_from_entity(entity_value, self._service_context)

    def _get_labourunion_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("LabourUnion", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._labourunion = LabourUnion.create_instance_from_entity(entity_value, self._service_context)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "PublicCompany":
            if real_type_name in PublicCompany._derived_creator_map:
                instance = PublicCompany._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = PublicCompany(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._Company__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_stockexchange_from_entity(entity_value)
        self._get_club_from_entity(entity_value)
        self._get_assets_from_entity(entity_value)
        self._get_labourunion_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = self._Company__to_value()
        entity_value.set_value_type(entity_type)
        self._set_stockexchange_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class Customer(Person):

    def __init__(self, service_context):
        Person.__init__(self, service_context)

        self._city = None
        self._company = None
        self._birthday = None
        self._orders = None
        self._timebetweenlasttwoorders = None

    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""

    _namespace = r"Microsoft.Test.OData.Services.ODataWCFService"
    _typename = r"Customer"

    @staticmethod
    def get_full_name():
        return Customer._namespace + '.' + Customer._typename

    @staticmethod
    def get_type_name():
        return Customer._typename

    def get_city(self):
        return self._city

    def set_city(self, property_value):
        self._city = property_value

    def _get_city_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("City", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._city = primitive_value.to_string()
            except:
                self._city = primitive_value.to_string()

    def _set_city_to_entity(self, entity):
        if entity is None or self._city is None:
            return
        entity.set_value("City", self._city)


    def get_company(self):
        return self._company

    def set_company(self, navitation_value):
        self._company = navitation_value

    def load_company(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Company"
        values = self._service_context.query(path)
        if values is None:
            return
        self._company = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._company = Company.create_instance_from_entity(entity_value, self._service_context)

    def _get_company_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Company", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._company = Company.create_instance_from_entity(entity_value, self._service_context)


    def get_birthday(self):
        return self._birthday

    def set_birthday(self, property_value):
        self._birthday = property_value

    def _get_birthday_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Birthday", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._birthday = eval(primitive_value.to_string())
            except:
                self._birthday = primitive_value.to_string()

    def _set_birthday_to_entity(self, entity):
        if entity is None or self._birthday is None:
            return
        entity.set_value("Birthday", self._birthday)


    def get_orders(self):
        return self._orders

    def set_orders(self, property_values):
        self._orders = property_values

    def add_to_orders(self, property_value):
        if self._orders is None:
            self._orders = []
        self._orders.append(property_value)

    def load_orders(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "Orders"
        values = self._service_context.query(path)
        if values is None:
            return
        self._orders = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._orders.append(Order.create_instance_from_entity(entity_value, self._service_context))

    def _get_orders_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("Orders", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._orders = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._orders.append(Order.create_instance_from_entity(entity_value, self._service_context))


    def get_timebetweenlasttwoorders(self):
        return self._timebetweenlasttwoorders

    def set_timebetweenlasttwoorders(self, property_value):
        self._timebetweenlasttwoorders = property_value

    def _get_timebetweenlasttwoorders_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("TimeBetweenLastTwoOrders", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._timebetweenlasttwoorders = eval(primitive_value.to_string())
            except:
                self._timebetweenlasttwoorders = primitive_value.to_string()

    def _set_timebetweenlasttwoorders_to_entity(self, entity):
        if entity is None or self._timebetweenlasttwoorders is None:
            return
        entity.set_value("TimeBetweenLastTwoOrders", self._timebetweenlasttwoorders)


    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "Customer":
            if real_type_name in Customer._derived_creator_map:
                instance = Customer._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = Customer(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._Person__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)
        self._get_city_from_entity(entity_value)
        self._get_company_from_entity(entity_value)
        self._get_birthday_from_entity(entity_value)
        self._get_orders_from_entity(entity_value)
        self._get_timebetweenlasttwoorders_from_entity(entity_value)

    __from_value = from_value

    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = self._Person__to_value()
        entity_value.set_value_type(entity_type)
        self._set_city_to_entity(entity_value)
        self._set_birthday_to_entity(entity_value)
        self._set_timebetweenlasttwoorders_to_entity(entity_value)
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value

class InMemoryEntities(odata_service_context):

    def __init__(self, baseAddress, options=odata_client_python.client_options()):
        odata_service_context.__init__(self, baseAddress, options)

    def query_productdetails(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("ProductDetails", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(ProductDetail.create_instance_from_entity(entity_value, self))
        return ret

    def query_vipcustomer(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("VipCustomer", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return None
            return Customer.create_instance_from_entity(entity_value, self)
        else:
            return None

    def GetProductsByAccessLevel(self, accessLevel):
        function_query_url = "GetProductsByAccessLevel"
        parameters = odata_client_python.vector_odata_parameter()
        if accessLevel is not None:
            enum_string = AccessLevel.get_string_from_enum_value(accessLevel)
            enum_type = odata_client_python.edm_enum_type("", "", "", False)
            enum_value = odata_client_python.odata_enum_value(enum_type, enum_string)
            if enum_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("accessLevel", enum_value))
        return self.operation_query_primitive(function_query_url, parameters, True, "::utility::string_t")


    def ResetBossEmail(self, emails):
        function_query_url = "ResetBossEmail"
        parameters = odata_client_python.vector_odata_parameter()
        if isinstance(emails, (list, tuple)):
            collection_value = odata_client_python.odata_collection_value(odata_client_python.edm_collection_type("action parameter"))
            for value in emails:
                if value is None:
                    continue
                primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(value)
                if primitive_value is not None:
                    collection_value.add_collection_value(primitive_value)
            parameters.push_back(odata_client_python.odata_parameter("emails", collection_value))
        return self.operation_query_primitive(function_query_url, parameters, False, "::utility::string_t")


    def query_departments(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("Departments", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(Department.create_instance_from_entity(entity_value, self))
        return ret

    def GetPerson(self, address):
        function_query_url = "GetPerson"
        parameters = odata_client_python.vector_odata_parameter()
        if isinstance(address, Address):
            value = address.to_value()
            if value is not None:
                parameters.push_back(odata_client_python.odata_parameter("address", value))
        return self.operation_query_entityset(function_query_url, parameters, True, Person)


    def query_customers(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("Customers", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(Customer.create_instance_from_entity(entity_value, self))
        return ret

    def query_people(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("People", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(Person.create_instance_from_entity(entity_value, self))
        return ret

    def query_products(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("Products", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(Product.create_instance_from_entity(entity_value, self))
        return ret

    def Discount(self, percentage):
        function_query_url = "Discount"
        parameters = odata_client_python.vector_odata_parameter()
        if percentage is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(percentage)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("percentage", primitive_value))
        return self.operation_query_void(function_query_url, parameters, False)


    def query_subscriptiontemplates(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("SubscriptionTemplates", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(Subscription.create_instance_from_entity(entity_value, self))
        return ret

    def GetBossEmails(self, start, count):
        function_query_url = "GetBossEmails"
        parameters = odata_client_python.vector_odata_parameter()
        if start is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(start)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("start", primitive_value))
        if count is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(count)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("count", primitive_value))
        return self.operation_query_primitive(function_query_url, parameters, True, "::utility::string_t")


    def query_boss(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("Boss", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return None
            return Person.create_instance_from_entity(entity_value, self)
        else:
            return None

    def GetPerson2(self, city):
        function_query_url = "GetPerson2"
        parameters = odata_client_python.vector_odata_parameter()
        if city is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(city)
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("city", primitive_value))
        return self.operation_query_entityset(function_query_url, parameters, True, Person)


    def query_productreviews(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("ProductReviews", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(ProductReview.create_instance_from_entity(entity_value, self))
        return ret

    def query_orders(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("Orders", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(Order.create_instance_from_entity(entity_value, self))
        return ret

    def query_publiccompany(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("PublicCompany", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return None
            return Company.create_instance_from_entity(entity_value, self)
        else:
            return None

    def query_defaultstoredpi(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("DefaultStoredPI", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return None
            return StoredPI.create_instance_from_entity(entity_value, self)
        else:
            return None

    def query_company(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("Company", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return None
            return Company.create_instance_from_entity(entity_value, self)
        else:
            return None

    def query_labourunion(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("LabourUnion", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return None
            return LabourUnion.create_instance_from_entity(entity_value, self)
        else:
            return None

    def ResetDataSource(self):
        function_query_url = "ResetDataSource"
        parameters = odata_client_python.vector_odata_parameter()
        return self.operation_query_void(function_query_url, parameters, False)


    def GetAllProducts(self):
        function_query_url = "GetAllProducts"
        parameters = odata_client_python.vector_odata_parameter()
        return self.operation_query_entityset(function_query_url, parameters, True, Product)


    def query_accounts(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("Accounts", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(Account.create_instance_from_entity(entity_value, self))
        return ret

    def query_employees(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("Employees", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(Employee.create_instance_from_entity(entity_value, self))
        return ret

    def query_orderdetails(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("OrderDetails", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(OrderDetail.create_instance_from_entity(entity_value, self))
        return ret

    def ResetBossAddress(self, address):
        function_query_url = "ResetBossAddress"
        parameters = odata_client_python.vector_odata_parameter()
        if isinstance(address, Address):
            value = address.to_value()
            if value is not None:
                parameters.push_back(odata_client_python.odata_parameter("address", value))
        return self.operation_query_complex(function_query_url, parameters, False, Address)


    def GetDefaultColor(self):
        function_query_url = "GetDefaultColor"
        parameters = odata_client_python.vector_odata_parameter()
        return self.operation_query_enum(function_query_url, parameters, True, Color)


    def query_storedpis(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("StoredPIs", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(StoredPI.create_instance_from_entity(entity_value, self))
        return ret
PaymentInstrument._derived_creator_map = {"CreditCardPI" : CreditCardPI, }
Company._derived_creator_map = {"PublicCompany" : PublicCompany, }
Address._derived_creator_map = {"CompanyAddress" : CompanyAddress, "HomeAddress" : HomeAddress, }
Person._derived_creator_map = {"Employee" : Employee, "Customer" : Customer, }
