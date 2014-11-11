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

# class_name, edm_namespace, edm_name
EDM_INFO = r"""
    _namespace = r"{1}"
    _typename = r"{2}"

    @staticmethod
    def get_full_name():
        return {0}._namespace + '.' + {0}._typename

    @staticmethod
    def get_type_name():
        return {0}._typename
"""

GET_ROOT_URL = r"""
    def get_root_url(self):
        if self._service_context is not None:
            return self._service_context.get_root_url()
        else:
            return ""
"""

# edm_namespace
GET_ENUM_TYPE_NAMESPACE = r"""
    @staticmethod
    def get_enum_type_namespace():
        return "{0}"
"""

BEGIN_GET_ENUM_TYPE_FROM_STRING = r"""
    @staticmethod
    def get_enum_value_from_string(enum_string):"""

# class_name, edm_name, class_member_name
ON_GET_ENUM_TYPE_FROM_STRING = r"""
        if enum_string == "{1}":
            return {0}.{2}"""

END_GET_ENUM_TYPE_FROM_STRING = r"""
        return 0
"""

BEGIN_GET_STRING_FROM_ENUM_TYPE = r"""
    @staticmethod
    def get_string_from_enum_value(enum_value):"""

# class_name, edm_name, class_member_name
ON_GET_STRING_FROM_ENUM_TYPE = r'''
        if enum_value == {0}.{2}:
            return "{1}"'''

END_GET_STRING_FROM_ENUM_TYPE = r"""
        return ""
"""

# base_class_name
BEGIN_COMPLEX_CONSTRUCTOR = r"""
    def __init__(self, service_context):
        {0}.__init__(self, service_context)"""

# class_member_name, default_value
ON_PROPERTY_IN_COMPLEX_CONSTRUCTOR = r"""
        self._{0} = {1}"""

# class_member_name, edm_name, primitive_resolver
PRIMITIVE_PROPERTY_IN_COMPLEX_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_value):
        self._{0} = property_value

    def _get_{0}_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._{0} = {2}
            except:
                self._{0} = primitive_value.to_string()

    def _set_{0}_to_complex(self, complex):
        if complex is None or self._{0} is None:
            return
        complex.set_value("{1}", self._{0})
"""

# class_member_name, edm_name, class_member_type
COMPLEX_PROPERTY_IN_COMPLEX_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_value):
        self._{0} = property_value

    def _get_{0}_from_complex(self, complex):
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Complex:
            complex_value = odata_client_python.to_complex_value(property_value)
            self._{0} = {2}.create_instance_from_complex(complex_value, self._service_context)

    def _set_{0}_to_complex(self, complex):
        if complex is None or self._{0} is None:
            return
        complex.set_value("{1}", self._{0}.to_value())
"""

# class_member_name, edm_name, class_member_type
ENUM_PROPERTY_IN_COMPLEX_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_value):
        self._{0} = property_value

    def _get_{0}_from_complex(self, complex):
        if complex is None:
            return
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        enum_value = odata_client_python.to_enum_value(property_value)
        if enum_value is not None:
            self._{0} = {2}.get_enum_value_from_string(enum_value.to_string())

    def _set_{0}_to_complex(self, complex):
        if complex is None or self._{0} is None:
            return
        complex_type = odata_client_python.to_complex_type(complex.get_value_type())
        if complex_type is None:
            return
        edm_property = complex_type.find_property("{1}")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        enum_value = odata_client_python.odata_enum_value(property_type, {2}.get_string_from_enum_value(self._{0}))
        complex.set_value("{1}", enum_value)
"""

# class_member_name, edm_name, primitive_resolver
COLLECTION_PRIMITIVE_PROPERTY_IN_COMPLEX_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_values):
        self._{0} = property_values

    def add_to_{0}(self, property_value):
        if self._{0} is None:
            self._{0} = []
        self._{0}.append(property_value)

    def _get_{0}_from_complex(self, complex):
        if complex is None:
            return
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._{0} = []
        for odata_value in property_collection_value.get_collection_values():
            primitive_value = odata_client_python.to_primitive_value(odata_value)
            if primitive_value is None:
                continue
            try:
                value = {2}
            except:
                value = primitive_value.to_string()
            self._{0}.append(value)

    def _set_{0}_to_complex(self, complex):
        if complex is None or self._{0} is None:
            return
        complex_type = odata_client_python.to_complex_type(complex.get_value_type())
        if complex_type is None:
            return
        edm_property = complex_type.find_property("{1}")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.to_collection_value(collection_value_type)
        for primitive in self._{0}:
            collection_value.add_collection_value(odata_client_python.odata_primitive_value.make_primitive_value(primitive))
        complex.set_value("{1}", collection_value)
"""

# class_member_name, edm_name, class_member_type
COLLECTION_ENUM_PROPERTY_IN_COMPLEX_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_values):
        self._{0} = property_values

    def add_to_{0}(self, property_value):
        if self._{0} is None:
            self._{0} = []
        self._{0}.append(property_value)

    def _get_{0}_from_complex(self, complex):
        if complex is None:
            return
        property_value = odata_client_python.odata_value()
        if not complex.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._{0} = []
        for odata_value in property_collection_value.get_collection_values():
            enum_value = odata_client_python.to_enum_value(odata_value)
            if enum_value is None:
                continue
            self._{0}.append({2}.get_enum_value_from_string(enum_value.to_string()))

    def _set_{0}_to_complex(self, complex):
        if self._{0} is None:
            return
        if complex is None or complex.get_value_type() is None:
            return
        complex_type = odata_client_python.to_complex_type(complex.get_value_type())
        if complex_type is None:
            return
        edm_property = complex_type.find_property("{1}")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.odata_collection_value(collection_value_type)
        for property in self._{0}:
            collection_value.add_collection_value(odata_client_python.odata_enum_value(collection_value_type.get_element_type(), {2}.get_string_from_enum_value(property)))
        complex.set_value("{1}", collection_value)
"""

# class_name, base_class_name
BEGIN_COMPLEX_INSTANCE_CREATOR = r"""
    @staticmethod
    def create_instance_from_complex(complex_value, service_context):
        if complex_value is None:
            return None
        real_type_name = complex_value.get_value_type().get_name()
        if real_type_name != "{0}":
            if real_type_name in {0}._derived_creator_map:
                instance = {0}._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = {0}(service_context)
        instance.from_value(complex_value)
        return instance

    def from_value(self, complex_value):
        self._{1}__from_value(complex_value)"""

# class_member_name
ON_PROPERTY_IN_COMPLEX_INSTANCE_CREATOR = r"""
        self._get_{0}_from_complex(complex_value)"""

END_COMPLEX_INSTANCE_CREATOR = r"""

    __from_value = from_value
"""

BEGIN_TO_COMPLEX_VALUE = r"""
    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        complex_type = self._service_context.get_edm_model().find_complex_type(self._typename)
        complex_value = odata_client_python.odata_complex_value(complex_type)"""

# base_class_name
BEGIN_TO_COMPLEX_VALUE_WITH_BASE_CLASS = r"""
    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        complex_type = self._service_context.get_edm_model().find_complex_type(self._typename)
        complex_value = self._{0}__to_value()
        complex_value.set_value_type(complex_type)"""

# class_member_name
ON_TO_COMPLEX_VALUE = r"""
        self._set_{0}_to_complex(complex_value)"""

END_TO_COMPLEX_VALUE = r"""
        if self._namespace != "" and self._typename != "":
            complex_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return complex_value

    __to_value = to_value
"""

# base_class_name
BEGIN_ENTITY_CONSTRUCTOR = r"""
    def __init__(self, service_context):
        {0}.__init__(self, service_context)
"""

# class_member_name, default_value
ON_PROPERTY_IN_ENTITY_CONSTRUCTOR = r"""
        self._{0} = {1}"""

# class_member_name, edm_name, primitive_resolver
PRIMITIVE_PROPERTY_IN_ENTITY_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_value):
        self._{0} = property_value

    def _get_{0}_from_entity(self, entity):
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        primitive_value = odata_client_python.to_primitive_value(property_value)
        if primitive_value is not None:
            try:
                self._{0} = {2}
            except:
                self._{0} = primitive_value.to_string()

    def _set_{0}_to_entity(self, entity):
        if entity is None or self._{0} is None:
            return
        entity.set_value("{1}", self._{0})
"""

# class_member_name, edm_name, class_member_type
ENUM_PROPERTY_IN_ENTITY_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_value):
        self._{0} = property_value

    def _get_{0}_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        enum_value = odata_client_python.to_enum_value(property_value)
        if enum_value is not None:
            self._{0} = {2}.get_enum_value_from_string(enum_value.to_string())

    def _set_{0}_to_entity(self, entity):
        if entity is None or self._{0} is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("{1}")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        enum_value = odata_client_python.odata_enum_value(property_type, {2}.get_string_from_enum_value(self._{0}))
        entity.set_value("{1}", enum_value)
"""

# class_member_name, edm_name, class_member_type
COMPLEX_PROPERTY_IN_ENTITY_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_value):
        self._{0} = property_value

    def _get_{0}_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Complex:
            complex_value = odata_client_python.to_complex_value(property_value)
            self._{0} = {2}.create_instance_from_complex(complex_value, self._service_context)

    def _set_{0}_to_entity(self, entity):
        if entity is None or self._{0} is None:
            return
        entity.set_value("{1}", self._{0}.to_value())
"""

# class_member_name, edm_name, class_member_type
NAVIGATION_PROPERTY_IN_ENTITY_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, navitation_value):
        self._{0} = navitation_value

    def load_{0}(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "{1}"
        values = self._service_context.query(path)
        if values is None:
            return
        self._{0} = None
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return
            self._{0} = {2}.create_instance_from_entity(entity_value, self._service_context)

    def _get_{0}_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        if property_value.get_value_type().get_type_kind() == odata_client_python.Entity:
            entity_value = odata_client_python.to_entity_value(property_value)
            self._{0} = {2}.create_instance_from_entity(entity_value, self._service_context)
"""

# class_member_name, edm_name, primitive_resolver
COLLECTION_PRIMITIVE_PROPERTY_IN_ENTITY_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_values):
        self._{0} = property_values

    def add_to_{0}(self, property_value):
        if self._{0} is None:
            self._{0} = []
        self._{0}.append(property_value)

    def _get_{0}_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._{0} = []
        for odata_value in property_collection_value.get_collection_values():
            primitive_value = odata_client_python.to_primitive_value(odata_value)
            if primitive_value is None:
                continue
            try:
                value = {2}
            except:
                value = primitive_value.to_string()
            self._{0}.append(value)

    def _set_{0}_to_entity(self, entity):
        if self._{0} is None:
            return
        if entity is None or entity.get_value_type() is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("{1}")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.odata_collection_value(collection_value_type)
        for primitive in self._{0}:
            collection_value.add_collection_value(odata_client_python.odata_primitive_value.make_primitive_value(primitive))
        entity.set_value("{1}", collection_value)
"""

# class_member_name, edm_name, class_member_type
COLLECTION_ENUM_PROPERTY_IN_ENTITY_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_values):
        self._{0} = property_values

    def add_to_{0}(self, property_value):
        if self._{0} is None:
            self._{0} = []
        self._{0}.append(property_value)

    def _get_{0}_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._{0} = []
        for odata_value in property_collection_value.get_collection_values():
            enum_value = odata_client_python.to_enum_value(odata_value)
            if enum_value is None:
                continue
            self._{0}.append({2}.get_enum_value_from_string(enum_value.to_string()))

    def _set_{0}_to_entity(self, entity):
        if self._{0} is None:
            return
        if entity is None or entity.get_value_type() is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("{1}")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.odata_collection_value(collection_value_type)
        for property in self._{0}:
            collection_value.add_collection_value(odata_client_python.odata_enum_value(collection_value_type.get_element_type(), {2}.get_string_from_enum_value(property)))
        entity.set_value("{1}", collection_value)
"""

# class_member_name, edm_name, class_member_type
COLLECTION_COMPLEX_PROPERTY_IN_ENTITY_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_values):
        self._{0} = property_values

    def add_to_{0}(self, property_value):
        if self._{0} is None:
            self._{0} = []
        self._{0}.append(property_value)

    def _get_{0}_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._{0} = []
        for odata_value in property_collection_value.get_collection_values():
            complex_value = odata_client_python.to_complex_value(odata_value)
            if complex_value is None:
                continue
            self._{0}.append({2}.create_instance_from_complex(complex_value, self._service_context))

    def _set_{0}_to_entity(self, entity):
        if self._{0} is None:
            return
        if entity is None or entity.get_value_type() is None:
            return
        entity_type = odata_client_python.to_entity_type(entity.get_value_type())
        if entity_type is None:
            return
        edm_property = entity_type.find_property("{1}")
        if edm_property is None:
            return
        property_type = edm_property.get_property_type()
        collection_value_type = odata_client_python.to_collection_type(property_type)
        if collection_value_type is None:
            return
        collection_value = odata_client_python.odata_collection_value(collection_value_type)
        for property in self._{0}:
            if property is not None:
                collection_value.add_collection_value(property.to_value())
        entity.set_value("{1}", collection_value)
"""

# class_member_name, edm_name, class_member_type
COLLECTION_NAVIGATION_PROPERTY_IN_ENTITY_MAPPING = r"""
    def get_{0}(self):
        return self._{0}

    def set_{0}(self, property_values):
        self._{0} = property_values

    def add_to_{0}(self, property_value):
        if self._{0} is None:
            self._{0} = []
        self._{0}.append(property_value)

    def load_{0}(self):
        if self._service_context is None:
            return
        path = self._service_context.get_relative_path(self._edit_link) + '/' + "{1}"
        values = self._service_context.query(path)
        if values is None:
            return
        self._{0} = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                return
            self._{0}.append({2}.create_instance_from_entity(entity_value, self._service_context))

    def _get_{0}_from_entity(self, entity):
        if entity is None:
            return
        property_value = odata_client_python.odata_value()
        if not entity.get_property_value("{1}", property_value):
            return
        if odata_client_python.is_nullptr(property_value):
            property_value = None
        if property_value is None:
            return
        property_collection_value = odata_client_python.to_collection_value(property_value)
        if property_collection_value is None:
            return
        self._{0} = []
        for odata_value in property_collection_value.get_collection_values():
            entity_value = odata_client_python.to_entity_value(odata_value)
            if entity_value is None:
                continue
            self._{0}.append({2}.create_instance_from_entity(entity_value, self._service_context))
"""

# class_name, base_class_name
BEGIN_ENTITY_INSTANCE_CREATOR = r"""
    @staticmethod
    def create_instance_from_entity(entity_value, service_context):
        if entity_value is None:
            return None
        real_type_name = entity_value.get_value_type().get_name()
        if real_type_name != "{0}":
            if real_type_name in {0}._derived_creator_map:
                instance = {0}._derived_creator_map[real_type_name](service_context)
            else:
                return None
        else:
            instance = {0}(service_context)
        instance.from_value(entity_value)
        return instance

    def from_value(self, entity_value):
        self._{1}__from_value(entity_value)
        self._edit_link = odata_client_python.odata_entity_model_builder.compute_edit_link(self.get_root_url(), entity_value, "", False)"""

# class_member_name
ON_PROPERTY_IN_ENTITY_INSTANCE_CREATOR = r"""
        self._get_{0}_from_entity(entity_value)"""

END_ENTITY_INSTANCE_CREATOR = r"""

    __from_value = from_value
"""

BEGIN_TO_ENTITY_VALUE = r"""
    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = odata_client_python.odata_entity_value(entity_type)"""

# base_class_name
BEGIN_TO_ENTITY_VALUE_WITH_BASE_CLASS = r"""
    def to_value(self):
        if self._service_context is None or self._service_context.get_edm_model() is None:
            return None
        entity_type = self._service_context.get_edm_model().find_entity_type(self._typename)
        entity_value = self._{0}__to_value()
        entity_value.set_value_type(entity_type)"""

# class_member_name
ON_TO_ENTITY_VALUE = r"""
        self._set_{0}_to_entity(entity_value)"""

END_TO_ENTITY_VALUE = r"""
        if self._namespace != "" and self._typename != "":
            entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, odata_client_python.odata_primitive_value(odata_client_python.edm_payload_annotation_type(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE), "#" + self._namespace + "." + self._typename))
        return entity_value 

    __to_value = to_value
"""

ENTITY_CONTAINER_CONSTRUCTOR = r"""
    def __init__(self, baseAddress, options=odata_client_python.client_options()):
        odata_service_context.__init__(self, baseAddress, options)
"""

# class_member_name, edm_name, strong_type_name 
QUERY_ENTITY_SET_IN_ENTITY_CONTAINER = r"""
    def {0}(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("{1}", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        ret = []
        for value in values:
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append({2}.create_instance_from_entity(entity_value, self))
        return ret
"""

# class_member_name, edm_name, strong_type_name 
QUERY_SINGLETON_IN_ENTITY_CONTAINER = r"""
    def {0}(self, key=None, filter=None, top=None, skip=None, orderby=None, select=None, expand=None):
        if self._client is None:
            return
        query_ex = self.get_query_expression("{1}", key=key, filter=filter, top=top, skip=skip, orderby=orderby, select=select, expand=expand)
        values = self._client.get_data_from_server(query_ex).get()
        if values is None:
            return
        if len(values) == 1:
            entity_value = odata_client_python.to_entity_value(values[0])
            if entity_value is None:
                return None
            return {2}.create_instance_from_entity(entity_value, self)
        else:
            return None
"""

# class_member_name, arguments
BEGIN_OPERATION = r"""
    def {0}({1}):
        if self._service_context is None:
            return None
        function_query_url = self._service_context.get_relative_path(self._edit_link) + '/'
        function_query_url += self._namespace + '.' + "{0}"
        parameters = odata_client_python.vector_odata_parameter()"""

# class_member_name, arguments
BEGIN_OPERATION_IMPORT = r"""
    def {0}({1}):
        function_query_url = "{0}"
        parameters = odata_client_python.vector_odata_parameter()"""

# member_name, edm_name
ON_PRIMITIVE_PARAMETER_IN_OPERATION = r"""
        if {0} is not None:
            primitive_value = odata_client_python.odata_primitive_value.make_primitive_value({0})
            if primitive_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("{1}", primitive_value))"""

# member_name, edm_name, member_strong_type_name
ON_CLASS_PARAMETER_IN_OPERATION = r"""
        if isinstance({0}, {2}):
            value = {0}.to_value()
            if value is not None:
                parameters.push_back(odata_client_python.odata_parameter("{1}", value))"""

# member_name, edm_name, member_strong_type_name
ON_ENUM_PARAMETER_IN_OPERATION = r"""
        if {0} is not None:
            enum_string = {2}.get_string_from_enum_value({0})
            enum_type = odata_client_python.edm_enum_type("", "", "", False)
            enum_value = odata_client_python.odata_enum_value(enum_type, enum_string)
            if enum_value is not None:
                parameters.push_back(odata_client_python.odata_parameter("{1}", enum_value))"""

# member_name, edm_name
ON_COLLECTION_PRIMITIVE_PARAMETER_IN_OPERATION = r"""
        if isinstance({0}, (list, tuple)):
            collection_value = odata_client_python.odata_collection_value(odata_client_python.edm_collection_type("action parameter"))
            for value in {0}:
                if value is None:
                    continue
                primitive_value = odata_client_python.odata_primitive_value.make_primitive_value(value)
                if primitive_value is not None:
                    collection_value.add_collection_value(primitive_value)
            parameters.push_back(odata_client_python.odata_parameter("{1}", collection_value))"""

# member_name, edm_name, member_strong_type_name
ON_COLLECTION_CLASS_PARAMETER_IN_OPERATION = r"""
        if isinstance({0}, (list, tuple)):
            collection_value = odata_client_python.odata_collection_value(odata_client_python.edm_collection_type("action parameter"))
            for ins in {0}:
                if  isinstance(ins, {2}):
                    value = ins.to_value()
                    if value is not None:
                        collection_value.add_collection_value(value)
            parameters.push_back(odata_client_python.odata_parameter("{1}", collection_value))"""

# member_name, edm_name, member_strong_type_name
ON_COLLECTION_ENUM_PARAMETER_IN_OPERATION = r"""
        if isinstance({0}, (list, tuple)):
            collection_value = odata_client_python.odata_collection_value(odata_client_python.edm_collection_type("action parameter"))
            for value in {0}:
                if value is None:
                    continue
                enum_string = {2}.get_string_from_enum_value(value)
                enum_type = odata_client_python.edm_enum_type("", "", "", False)
                enum_value = odata_client_python.odata_enum_value(enum_type, enum_string)
                if enum_value is not None:
                    collection_value.add_collection_value(enum_value)
            parameters.push_back(odata_client_python.odata_parameter("{1}", collection_value))
"""

# executor_name, is_function, return_type
END_OPERATION_WITH_RETURN_VALUE = r"""
        return self._service_context.{0}(function_query_url, parameters, {1}, {2})
"""

# executor_name, is_function
END_OPERATION_VOID = r"""
        return self._service_context.{0}(function_query_url, parameters, {1})
"""

# executor_name, is_function, return_type
END_OPERATION_IMPORT_WITH_RETURN_VALUE = r"""
        return self.{0}(function_query_url, parameters, {1}, {2})
"""

# executor_name, is_function
END_OPERATION_IMPORT_VOID = r"""
        return self.{0}(function_query_url, parameters, {1})
"""
