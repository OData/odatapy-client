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

BASE_TYPE_NAME = "type_base"
DATA_SERVICE_CONTEXT_NAME = "odata_service_context"

class PROPERTY_TYPE:
    E_PRIMITIVE = 0
    E_COMPLEX = 1
    E_ENTITY = 2
    E_ENUM = 3
    E_COLLECTION_PRIMITIVE = 4
    E_COLLECTION_COMPLEX = 5
    E_COLLECTION_ENTITY = 6
    E_COLLECTION_ENUM = 7
    E_FUNCTION = 8
    E_FUNCTION_IMPORT = 9
    E_ACTION = 10
    E_ACTION_IMPORT = 11
    E_CONTAINER_ENTITY_SET = 12
    E_CONTAINER_SINGLETON = 13
    E_KNOWN = 14

class CLASS_TYPE:
    E_CLASS_COMPLEX = 0
    E_CLASS_ENTITY = 1
    E_CLASS_ENUM = 2
    E_CLASS_CONTAINER = 3
    E_CLASS_KNOWN = 4

class edm_type_kind_t:
    _None = 0
    Primitive = 1
    Entity = 2
    Complex = 3
    Collection = 4
    Enum = 5
    Link = 6
    Navigation = 7
    Operation = 8
    PayloadAnnotation = 9
    Unknown = 10

class class_info:
    def __init__(self):
        self.edm_name = ""
        self.edm_namespace = ""
        self.class_name = ""
        self.base_class_name = ""
        self.type = CLASS_TYPE.E_CLASS_KNOWN

class operation_param:
    def __init__(self):
        self.edm_name = ""
        self.member_name = ""
        self.member_type = PROPERTY_TYPE.E_KNOWN
        self.member_strong_type_name = ""

class operation_info:
    def __init__(self):
        self.params = []
        self.return_type = ""
        self.executor_name = ""

class property_info:
    def __init__(self):
        self.edm_name = ""
        self.class_member_name = ""
        self.class_member_type = ""
        self.strong_type_name = ""
        self.type = PROPERTY_TYPE.E_KNOWN
        self.default_value = ""
        self.is_nullable = False
        self.is_key = False
        self.operation_info = None

class code_gen_configuration:
    def __init__(self):
        self.metadata_url = ''
        self.namespace = ''
        self.user_name = ''
        self.password = ''
        self.file_name = ''

class schema_info:
    def __init__(self):
        self.clear()

    def clear(self):
        self.class_property_map = {}
        self.class_map = {}
        self.class_list = []
        self.derived_classes = {}

class codegen_initializer:
    def __init__(self):
        self._model = None
        self._config = code_gen_configuration()
        self._code_gen_map = {}

    def get_config(self):
        return self._config

    def begin_initialize(self, metadata_url, file_name, user_name, password):
        self._config = code_gen_configuration()
        self._config.metadata_url = metadata_url
        self._config.file_name = file_name
        self._config.user_name = user_name
        self._config.password = password
        return self.begin_initialize_code_gen_info(self._config.metadata_url, self._config.user_name, self._config.password)

    def begin_initialize_code_gen_info(self, metadata_url, user_name='', password=''):
        self._reset_class_info()
        parser = None
        if user_name and password:
            options = odata_client_python.client_options()
            options.enable_client_credential(user_name, password)
            client = odata_client_python.odata_client(metadata_url, options)
        else:
            client = odata_client_python.odata_client(metadata_url)
        if client is None:
            return False

        self._model = client.get_model().get()
        if self._model is None:
            return False

        entity_container = self._model.find_container()
        if entity_container is None:
            print("must have an entity container in model!")
            exit(-1)

        ns_entity_container = ''
        for schema in self._model.get_schema():
            if schema.find_container() is not None:
                ns_entity_container = schema.get_name()

        for schema in self._model.get_schema():
            _schema_info = schema_info()
            self._initialize_class_info(schema, _schema_info)
            self._initialize_property_info_of_class(schema, _schema_info)
            self._code_gen_map[schema.get_name()] = _schema_info

        total = schema_info()
        for schema in self._code_gen_map:
            _schema_info = self._code_gen_map[schema]
            total.class_property_map.update(_schema_info.class_property_map)
            total.class_map.update(_schema_info.class_map)
            total.class_list += _schema_info.class_list
            total.derived_classes.update(_schema_info.derived_classes)
        self._code_gen_map = {}
        self._code_gen_map[ns_entity_container] = total

    def _reset_class_info(self):
        self._code_gen_map = {}

    def _initialize_class_info(self, schema, _schema_info):
        if schema is None:
            return
        enum_types = schema.get_enum_types_vector()
        for enum_type in enum_types:
            _info = class_info()
            _info.edm_name = enum_type.get_name()
            _info.class_name = enum_type.get_name()
            _info.edm_namespace = schema.get_name()
            _info.type = CLASS_TYPE.E_CLASS_ENUM
            _schema_info.class_map[enum_type.get_name()] = _info
            _schema_info.class_list.append(_info)

        complex_types = schema.get_complex_types_vector()
        for complex_type in complex_types:
            _info = class_info()
            _info.edm_name = complex_type.get_name()
            _info.class_name = complex_type.get_name()
            _info.edm_namespace = schema.get_name()
            _info.type = CLASS_TYPE.E_CLASS_COMPLEX
            _info.base_class_name = complex_type.get_base_type_name()
            if _info.base_class_name == "":
                _info.base_class_name = BASE_TYPE_NAME
            else:
                if _info.base_class_name.startswith(complex_type.get_namespace()):
                    _info.base_class_name = _info.base_class_name[len(complex_type.get_namespace()) + 1:]
            _schema_info.class_map[complex_type.get_name()] = _info

        entity_types = schema.get_entity_types_vector()
        for entity_type in entity_types:
            _info = class_info()
            _info.edm_name = entity_type.get_name()
            _info.class_name = entity_type.get_name()
            _info.edm_namespace = schema.get_name()
            _info.type = CLASS_TYPE.E_CLASS_ENTITY
            _info.base_class_name = entity_type.get_base_type_name()
            if _info.base_class_name == "":
                _info.base_class_name = BASE_TYPE_NAME
            else:
                if _info.base_class_name.startswith(entity_type.get_namespace()):
                    _info.base_class_name = _info.base_class_name[len(entity_type.get_namespace()) + 1:]
            _schema_info.class_map[entity_type.get_name()] = _info

        entity_containers = schema.get_containers_vector()
        if len(entity_containers) > 1:
            print("only support model with one entity container!")
            exit()
        for container_type in entity_containers:
            _info = class_info()
            _info.edm_name = container_type.get_name()
            _info.class_name = container_type.get_name()
            _info.edm_namespace = schema.get_name()
            _info.base_class_name = DATA_SERVICE_CONTEXT_NAME
            _info.type = CLASS_TYPE.E_CLASS_CONTAINER
            _schema_info.class_map[container_type.get_name()] = _info
            
        # sort the classes
        types_to_be_added = {}
        types_to_be_added[BASE_TYPE_NAME] = BASE_TYPE_NAME
        types_to_be_added[DATA_SERVICE_CONTEXT_NAME] = DATA_SERVICE_CONTEXT_NAME

        flag_continue = True
        while flag_continue:
            flag_continue = False
            for cls_name in _schema_info.class_map:
                _info = _schema_info.class_map[cls_name]
                if _info.base_class_name in types_to_be_added and _info.class_name not in types_to_be_added:
                    types_to_be_added[_info.class_name] = _info.class_name
                    _schema_info.class_list.append(_info)
                    flag_continue = True

        for _info in _schema_info.class_list:
            if (_info.type == CLASS_TYPE.E_CLASS_COMPLEX or _info.type == CLASS_TYPE.E_CLASS_ENTITY) and _info.base_class_name != BASE_TYPE_NAME:
                if _info.base_class_name not in _schema_info.derived_classes:
                    _schema_info.derived_classes[_info.base_class_name] = []
                _schema_info.derived_classes[_info.base_class_name].append(_info.class_name)

    def _initialize_property_info_of_class(self, schema, _schema_info):
        if schema is None:
            return

        entity_types = schema.get_entity_types_vector()
        for entity_type in entity_types:
            class_property_map = {}
            properties = entity_type.get_properties_vector()
            for property_type in properties:
                if property_type.get_property_type().get_type_kind() == edm_type_kind_t.Unknown:
                    continue
                _info = property_info()
                _info.edm_name = property_type.get_name()
                _info.class_member_name = property_type.get_name().lower()
                _info.is_nullable = property_type.is_nullable()
                _info.is_key = _info.edm_name in entity_type.key()

                type_kind = property_type.get_property_type().get_type_kind()
                if type_kind == edm_type_kind_t.Primitive:
                    _info.strong_type_name = odata_client_python.edm_model_utility.get_strong_type_name_from_edm_type_name(odata_client_python.to_primitive_type(property_type.get_property_type()))
                    _info.type = PROPERTY_TYPE.E_PRIMITIVE
                elif type_kind == edm_type_kind_t.Complex:
                    _info.strong_type_name = _schema_info.class_map[property_type.get_property_type().get_name()].class_name
                    _info.type = PROPERTY_TYPE.E_COMPLEX
                elif type_kind == edm_type_kind_t.Navigation:
                    navigation_type = odata_client_python.to_navigation_type(property_type.get_property_type())
                    if navigation_type.get_navigation_type().get_type_kind() == edm_type_kind_t.Entity:
                        _info.strong_type_name = _schema_info.class_map[navigation_type.get_navigation_type().get_name()].class_name
                        _info.type = PROPERTY_TYPE.E_ENTITY
                    elif navigation_type.get_navigation_type().get_type_kind() == edm_type_kind_t.Collection:
                        collection_entity_type = odata_client_python.to_collection_type(navigation_type.get_navigation_type())
                        _info.strong_type_name = _schema_info.class_map[collection_entity_type.get_element_type().get_name()].class_name
                        _info.type = PROPERTY_TYPE.E_COLLECTION_ENTITY
                elif type_kind == edm_type_kind_t.Enum:
                    if property_type.get_property_type().get_name() not in _schema_info.class_map:
                        _info.strong_type_name = property_type.get_property_type().get_name()
                    else:
                        _info.strong_type_name = _schema_info.class_map[property_type.get_property_type().get_name()].class_name
                    _info.type = PROPERTY_TYPE.E_ENUM
                elif type_kind == edm_type_kind_t.Collection:
                    collection_type = odata_client_python.to_collection_type(property_type.get_property_type())
                    element_type = collection_type.get_element_type()
                    if element_type.get_type_kind() == edm_type_kind_t.Complex:
                        _info.strong_type_name = _schema_info.class_map[element_type.get_name()].class_name
                        _info.type = PROPERTY_TYPE.E_COLLECTION_COMPLEX
                    elif element_type.get_type_kind() == edm_type_kind_t.Primitive:
                        _info.strong_type_name = odata_client_python.edm_model_utility.get_strong_type_name_from_edm_type_name(odata_client_python.to_primitive_type(element_type))
                        _info.type = PROPERTY_TYPE.E_COLLECTION_PRIMITIVE
                    elif element_type.get_type_kind() == edm_type_kind_t.Enum:
                        if element_type.get_name() not in _schema_info.class_map:
                            _info.strong_type_name = element_type.get_name()
                        else:
                            _info.strong_type_name = _schema_info.class_map[element_type.get_name()].class_name
                        _info.type = PROPERTY_TYPE.E_COLLECTION_ENUM

                self._set_default_value(_info, property_type)
                self._set_strong_type_name(_info)
                class_property_map[property_type.get_name()] = _info

            _schema_info.class_property_map[entity_type.get_name()] = class_property_map

        complex_types = schema.get_complex_types_vector()
        for complex_type in complex_types:
            class_property_map = {}
            for property_type in complex_type.get_properties_vector():
                if property_type.get_property_type().get_type_kind() == edm_type_kind_t.Unknown:
                    continue
                _info = property_info()
                _info.edm_name = property_type.get_name()
                _info.class_member_name = property_type.get_name().lower()
                _info.is_nullable = property_type.is_nullable()
                _info.default_value = property_type.default_value()
                
                type_kind = property_type.get_property_type().get_type_kind()
                if type_kind == edm_type_kind_t.Primitive:
                    _info.strong_type_name = odata_client_python.edm_model_utility.get_strong_type_name_from_edm_type_name(odata_client_python.to_primitive_type(property_type.get_property_type()))
                    _info.type = PROPERTY_TYPE.E_PRIMITIVE
                elif type_kind == edm_type_kind_t.Complex:
                    _info.strong_type_name = _schema_info.class_map[property_type.get_property_type().get_name()].class_name
                    _info.type = PROPERTY_TYPE.E_COMPLEX
                elif type_kind == edm_type_kind_t.Enum:
                    if property_type.get_property_type().get_name() not in _schema_info.class_map:
                        _info.strong_type_name = property_type.get_property_type().get_name()
                    else:
                        _info.strong_type_name = _schema_info.class_map[property_type.get_property_type().get_name()].class_name
                    _info.type = PROPERTY_TYPE.E_ENUM
                elif type_kind == edm_type_kind_t.Collection:
                    collection_type = odata_client_python.to_collection_type(property_type.get_property_type())
                    element_type = collection_type.get_element_type()
                    if element_type.get_type_kind() == edm_type_kind_t.Complex:
                        _info.strong_type_name = _schema_info.class_map[element_type.get_name()].class_name
                        _info.type = PROPERTY_TYPE.E_COLLECTION_COMPLEX
                    elif element_type.get_type_kind() == edm_type_kind_t.Primitive:
                        _info.strong_type_name = odata_client_python.edm_model_utility.get_strong_type_name_from_edm_type_name(odata_client_python.to_primitive_type(element_type))
                        _info.type = PROPERTY_TYPE.E_COLLECTION_PRIMITIVE
                    elif element_type.get_type_kind() == edm_type_kind_t.Enum:
                        if element_type.get_name() not in _schema_info.class_map:
                            _info.strong_type_name = element_type.get_name()
                        else:
                            _info.strong_type_name = _schema_info.class_map[element_type.get_name()].class_name
                        _info.type = PROPERTY_TYPE.E_COLLECTION_ENUM
                self._set_default_value(_info, property_type)
                self._set_strong_type_name(_info)
                class_property_map[property_type.get_name()] = _info

            _schema_info.class_property_map[complex_type.get_name()] = class_property_map

        operation_types = schema.get_operation_types_vector()
        for operation_type in operation_types:
            if operation_type.is_bound() and len(operation_type.get_operation_parameters()) > 0:
                bounded_type = operation_type.get_operation_parameters()[0].get_param_type()
                if bounded_type is None:
                    continue
                if bounded_type.get_type_kind() != edm_type_kind_t.Entity:
                    continue
                if bounded_type.get_name() not in _schema_info.class_property_map:
                    continue
                class_property_map = _schema_info.class_property_map[bounded_type.get_name()]

                function_property_info = property_info()
                function_property_info.edm_name = operation_type.get_name()
                function_property_info.class_member_name = operation_type.get_name()
                self._set_operation_info(function_property_info, operation_type, _schema_info)

                class_property_map[operation_type.get_name()] = function_property_info
                _schema_info.class_property_map[bounded_type.get_name()] = class_property_map

        enum_member_name = {}
        enum_types = schema.get_enum_types_vector()
        for enum_type in enum_types:
            class_property_map = {}
            enum_members = enum_type.get_enum_members()
            for enum_member in enum_members:
                _info = property_info()
                _info.edm_name = enum_member.get_enum_member_name()
                member_name = enum_member.get_enum_member_name()
                # TODO: other key words
                if member_name == "None":
                    member_name = '_' + member_name
                if member_name not in enum_member_name:
                    _info.class_member_name = member_name
                else:
                    _info.class_member_name = enum_type.get_name() + "_" + member_name
                enum_member_name[_info.class_member_name] = _info.class_member_name
                _info.default_value = str(enum_member.get_enum_member_value())

                class_property_map[enum_member.get_enum_member_name()] = _info

            _schema_info.class_property_map[enum_type.get_name()] = class_property_map

        if (len(schema.get_containers_vector()) == 1):
            entity_container = schema.find_container()
            class_property_map = {}
            for entity_set in entity_container.get_entity_set_vector():
                _info = property_info()
                _info.edm_name = entity_set.get_name()
                _info.strong_type_name = entity_set.get_entity_type().get_name()
                _info.class_member_name = "query_" + entity_set.get_name().lower()
                _info.type = PROPERTY_TYPE.E_CONTAINER_ENTITY_SET
                class_property_map[_info.class_member_name] = _info

            for singleton in entity_container.get_singleton_vector():
                _info = property_info()
                _info.edm_name = singleton.get_name()
                _info.strong_type_name = singleton.get_entity_type().get_name()
                _info.class_member_name = "query_" + singleton.get_name().lower()
                _info.type = PROPERTY_TYPE.E_CONTAINER_SINGLETON
                class_property_map[_info.class_member_name] = _info

            for operation_import in entity_container.get_operation_import_vector():
                if operation_import is None:
                    continue
                operation_type = operation_import.get_operation_type()
                if operation_type is None:
                    continue
                function_property_info = property_info()
                function_property_info.edm_name = operation_type.get_name()
                function_property_info.class_member_name = operation_type.get_name()
                self._set_operation_info(function_property_info, operation_type, _schema_info)
                class_property_map[operation_import.get_name()] = function_property_info

            _schema_info.class_property_map[entity_container.get_name()] = class_property_map

    def _get_executor_name_from_edm_type(self, _type):
        ret = ""
        if _type is not None:
            if _type.get_type_kind() == edm_type_kind_t.Entity:
                ret = "operation_query_entityset"
            elif _type.get_type_kind() == edm_type_kind_t.Complex:
                ret = "operation_query_complex"
            elif _type.get_type_kind() == edm_type_kind_t.Enum:
                ret = "operation_query_enum"
            elif _type.get_type_kind() == edm_type_kind_t.Primitive:
                ret = "operation_query_primitive"
        return ret

    def _set_default_value(self, _info, property_type):
        if property_type is None:
            return
        if _info.default_value != "":
            return
        if property_type.get_property_type().get_type_kind() == edm_type_kind_t.Primitive:
            if _info.is_nullable == True:
                _info.default_value = "None"
            else:
                _info.default_value = odata_client_python.edm_model_utility.get_strong_type_default_value_from_edm_type_name(odata_client_python.to_primitive_type(property_type.get_property_type()))
                if _info.default_value == "false":
                    _info.default_value = "False"
        elif property_type.get_property_type().get_type_kind() == edm_type_kind_t.Complex:
            if _info.is_nullable == True:
                _info.default_value = "None"
        elif property_type.get_property_type().get_type_kind() == edm_type_kind_t.Navigation:
            if _info.type == PROPERTY_TYPE.E_ENTITY:
                if _info.is_nullable == True:
                    _info.default_value = "None"
        elif property_type.get_property_type().get_type_kind() == edm_type_kind_t.Enum:
            if _info.is_nullable == True:
                _info.default_value = "None"
        elif property_type.get_property_type().get_type_kind() == edm_type_kind_t.Collection:
            _info.default_value = "[]"
        if _info.default_value == "":
            _info.default_value = "None"

    def _set_strong_type_name(self, _info):
        _info.class_member_type = _info.strong_type_name

    def _set_operation_info(self, _info, operation_type, _schema_info):
        if operation_type is None:
            return
        if operation_type.is_function():
            _info.type = PROPERTY_TYPE.E_FUNCTION
        else:
            _info.type = PROPERTY_TYPE.E_ACTION
        _operation_info = operation_info()
        ret_type = operation_type.get_operation_return_type()
        if ret_type is None:
            _operation_info.return_type = "void"
            _operation_info.executor_name = "operation_query_void"
        else:
            if ret_type.get_type_kind() == edm_type_kind_t.Collection:
                element_type = odata_client_python.to_collection_type(ret_type).get_element_type()
                if element_type is None:
                    return
                _operation_info.return_type = element_type.get_name()
                if element_type.get_type_kind() == edm_type_kind_t.Primitive:
                    _operation_info.return_type = odata_client_python.edm_model_utility.get_strong_type_name_from_edm_type_name(odata_client_python.to_primitive_type(element_type))
                elif element_type.get_type_kind() in (edm_type_kind_t.Complex,
                        edm_type_kind_t.Entity,
                        edm_type_kind_t.Enum):
                    _operation_info.return_type = _schema_info.class_map[element_type.get_name()].class_name
                _operation_info.executor_name = self._get_executor_name_from_edm_type(element_type)
            else:
                if ret_type.get_type_kind() == edm_type_kind_t.Primitive:
                    _operation_info.return_type = odata_client_python.edm_model_utility.get_strong_type_name_from_edm_type_name(odata_client_python.to_primitive_type(ret_type))
                elif ret_type.get_type_kind() in (edm_type_kind_t.Complex,
                        edm_type_kind_t.Entity,
                        edm_type_kind_t.Enum):
                    _operation_info.return_type = _schema_info.class_map[ret_type.get_name()].class_name
                _operation_info.executor_name = self._get_executor_name_from_edm_type(ret_type)

        first = True
        for param_iter in operation_type.get_operation_parameters():
            if first and operation_type.is_bound():
                first = False
                continue
            param = operation_param()
            param_type = param_iter.get_param_type()
            if param_type is None:
                continue
            param.edm_name = param_iter.get_param_name()
            if param_type.get_type_kind() == edm_type_kind_t.Primitive:
                param.member_strong_type_name = odata_client_python.edm_model_utility.get_strong_type_name_from_edm_type_name(odata_client_python.to_primitive_type(param_type))
                param.member_type = PROPERTY_TYPE.E_PRIMITIVE
            elif param_type.get_type_kind() == edm_type_kind_t.Complex:
                param.member_strong_type_name = _schema_info.class_map[param_type.get_name()].class_name
                param.member_type = PROPERTY_TYPE.E_COMPLEX
            elif param_type.get_type_kind() == edm_type_kind_t.Entity:
                param.member_strong_type_name = _schema_info.class_map[param_type.get_name()].class_name
                param.member_type = PROPERTY_TYPE.E_ENTITY
            elif param_type.get_type_kind() == edm_type_kind_t.Enum:
                param.member_strong_type_name = _schema_info.class_map[param_type.get_name()].class_name
                param.member_type = PROPERTY_TYPE.E_ENUM
            elif param_type.get_type_kind() == edm_type_kind_t.Collection:
                collection_type = odata_client_python.to_collection_type(param_type)
                element_type = collection_type.get_element_type()
                if element_type.get_type_kind() == edm_type_kind_t.Complex:
                    param.member_strong_type_name = _schema_info.class_map[element_type.get_name()].class_name
                    param.member_type = PROPERTY_TYPE.E_COLLECTION_COMPLEX
                elif element_type.get_type_kind() == edm_type_kind_t.Entity:
                    param.member_strong_type_name = _schema_info.class_map[element_type.get_name()].class_name
                    param.member_type = PROPERTY_TYPE.E_COLLECTION_ENTITY
                elif element_type.get_type_kind() == edm_type_kind_t.Primitive:
                    param.member_strong_type_name = odata_client_python.edm_model_utility.get_strong_type_name_from_edm_type_name(odata_client_python.to_primitive_type(element_type))
                    param.member_type = PROPERTY_TYPE.E_COLLECTION_PRIMITIVE
                elif element_type.get_type_kind() == edm_type_kind_t.Enum:
                    param.member_strong_type_name = _schema_info.class_map[element_type.get_name()].class_name
                    param.member_type = PROPERTY_TYPE.E_COLLECTION_ENUM
            param.member_name = param_iter.get_param_name()
            _operation_info.params.append(param)

        _info.operation_info = _operation_info
