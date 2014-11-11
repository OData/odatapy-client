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

from codegen_initializer import *
import codegen_template as TP

INDENT = "    "

class codegen_writer:
    def __init__(self, initializer):
        self._initializer = initializer

    def begin_generate_file(self):
        if self._initializer is None:
            print "Initialize failed"
            return
        outf = open(self._initializer.get_config().file_name + ".py", "w")

        self._generate_import_files(outf)
        for schema_name in self._initializer._code_gen_map:
            self._generate_enum_types(outf, self._initializer._code_gen_map[schema_name])
            self._generate_complex_types(outf, self._initializer._code_gen_map[schema_name])
            self._generate_entity_types(outf, self._initializer._code_gen_map[schema_name])
            self._generate_entity_container(outf, self._initializer._code_gen_map[schema_name])
            self._generate_derived_creator(outf, self._initializer._code_gen_map[schema_name])

    def _primitive_resolver(self, _info):
        ret = r"eval(primitive_value.to_string())"
        if _info.class_member_type in ("uint8_t", "int8_t", "int16_t", "int32_t", "int64_t"):
            ret = r"int(primitive_value.to_string())"
        elif _info.class_member_type in ("float", "double", "long double"):
            ret = r"float(primitive_value.to_string())"
        elif _info.class_member_type == "::utility::string_t":
            ret = r"primitive_value.to_string()"
        elif _info.class_member_type == "bool":
            ret = r"primitive_value.to_string() == 'true'"
        return ret

    def _generate_import_files(self, outf):
        outf.write(r"import odata_client_python" + '\n')
        outf.write(r"from odata_service_context import *" + '\n')
        outf.write(r"from codegen_base import *" + '\n')
        outf.write('\n')

    def _generate_class_begin(self, outf, class_info):
        if class_info.base_class_name:
            outf.write(r"class {}({}):".format(class_info.class_name, class_info.base_class_name) + "\n")
        else:
            outf.write(r"class {}:".format(class_info.class_name) + "\n")

    def _generate_derived_creator(self, outf, _schema_info):
        for class_info in _schema_info.class_list:
            if class_info.type != CLASS_TYPE.E_CLASS_COMPLEX and class_info.type != CLASS_TYPE.E_CLASS_ENTITY:
                continue
            if class_info.class_name in _schema_info.derived_classes:
                derived_classes = _schema_info.derived_classes[class_info.class_name]
                outf.write(r"{}._derived_creator_map = ".format(class_info.class_name) + '{')
                for derived_class_name in derived_classes:
                    outf.write(r'"{0}" : {0}, '.format(derived_class_name))
                outf.write('}\n')

    def _generate_enum_types(self, outf, _schema_info):
        for class_info in _schema_info.class_list:
            if class_info.type != CLASS_TYPE.E_CLASS_ENUM:
                continue
            self._generate_class_begin(outf, class_info)
            class_property_map = _schema_info.class_property_map[class_info.class_name]
            for property_name in class_property_map:
                _info = class_property_map[property_name]
                self._generate_enum_member(outf, _info)
            self._generate_common_methods_in_enum(outf, class_info, class_property_map)
            outf.write("\n")

    def _generate_common_methods_in_enum(self, outf, class_info, class_property_map):
        outf.write(TP.GET_ENUM_TYPE_NAMESPACE.format(class_info.edm_namespace))
        outf.write(TP.BEGIN_GET_ENUM_TYPE_FROM_STRING)
        for property_name in class_property_map:
            _info = class_property_map[property_name]
            outf.write(TP.ON_GET_ENUM_TYPE_FROM_STRING.format(class_info.class_name, _info.edm_name, _info.class_member_name))
        outf.write(TP.END_GET_ENUM_TYPE_FROM_STRING)
        outf.write(TP.BEGIN_GET_STRING_FROM_ENUM_TYPE)
        for property_name in class_property_map:
            _info = class_property_map[property_name]
            outf.write(TP.ON_GET_STRING_FROM_ENUM_TYPE.format(class_info.class_name, _info.edm_name, _info.class_member_name))
        outf.write(TP.END_GET_STRING_FROM_ENUM_TYPE)

    def _generate_enum_member(self, outf, _info):
        outf.write(INDENT + _info.class_member_name + " = " + _info.default_value + "\n")

    def _generate_complex_types(self, outf, _schema_info):
        for class_info in _schema_info.class_list:
            if class_info.type != CLASS_TYPE.E_CLASS_COMPLEX:
                continue
            self._generate_class_begin(outf, class_info)
            class_property_map = _schema_info.class_property_map[class_info.class_name]
            self._generate_common_methods_in_complex(outf, class_info, class_property_map)
            for property in class_property_map:
                _info = class_property_map[property]
                self._generate_property_in_complex(outf, class_info, _info)
            self._generate_complex_instance_creator(outf, class_info, class_property_map)
            self._generate_to_complex_value(outf, class_info, class_property_map)
            outf.write("\n")

    def _generate_complex_constructor(self, outf, class_info, class_property_map):
        outf.write(TP.BEGIN_COMPLEX_CONSTRUCTOR.format(class_info.base_class_name))
        for property in class_property_map:
            _info = class_property_map[property]
            if _info.type == PROPERTY_TYPE.E_FUNCTION or _info.type == PROPERTY_TYPE.E_ACTION:
                continue
            outf.write(TP.ON_PROPERTY_IN_COMPLEX_CONSTRUCTOR.format(_info.class_member_name, _info.default_value))
        outf.write('\n')

    def _generate_common_methods_in_complex(self, outf, class_info, class_property_map):
        self._generate_complex_constructor(outf, class_info, class_property_map)
        outf.write(TP.GET_ROOT_URL)
        outf.write(TP.EDM_INFO.format(class_info.class_name, class_info.edm_namespace, class_info.edm_name))

    def _generate_property_in_complex(self, outf, class_info, _info):
        if _info.type == PROPERTY_TYPE.E_PRIMITIVE:
            outf.write(TP.PRIMITIVE_PROPERTY_IN_COMPLEX_MAPPING.format(_info.class_member_name, _info.edm_name, self._primitive_resolver(_info)))
        elif _info.type == PROPERTY_TYPE.E_COMPLEX:
            outf.write(TP.COMPLEX_PROPERTY_IN_COMPLEX_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        elif _info.type == PROPERTY_TYPE.E_ENUM:
            outf.write(TP.ENUM_PROPERTY_IN_COMPLEX_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        elif _info.type == PROPERTY_TYPE.E_COLLECTION_PRIMITIVE:
            outf.write(TP.COLLECTION_PRIMITIVE_PROPERTY_IN_COMPLEX_MAPPING.format(_info.class_member_name, _info.edm_name, self._primitive_resolver(_info)))
        elif _info.type == PROPERTY_TYPE.E_COLLECTION_ENUM:
            outf.write(TP.COLLECTION_ENUM_PROPERTY_IN_COMPLEX_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        outf.write('\n')

    def _generate_complex_instance_creator(self, outf, class_info, class_property_map):
        outf.write(TP.BEGIN_COMPLEX_INSTANCE_CREATOR.format(class_info.class_name, class_info.base_class_name))
        for property in class_property_map:
            _info = class_property_map[property]
            if _info.type == PROPERTY_TYPE.E_ACTION or _info.type == PROPERTY_TYPE.E_FUNCTION:
                continue
            outf.write(TP.ON_PROPERTY_IN_COMPLEX_INSTANCE_CREATOR.format(_info.class_member_name))
        outf.write(TP.END_COMPLEX_INSTANCE_CREATOR)

    def _generate_to_complex_value(self, outf, class_info, class_property_map):
        if class_info.base_class_name == "type_base":
            outf.write(TP.BEGIN_TO_COMPLEX_VALUE)
        else:
            outf.write(TP.BEGIN_TO_COMPLEX_VALUE_WITH_BASE_CLASS.format(class_info.base_class_name))
        for property in class_property_map:
            _info = class_property_map[property]
            if _info.type in (PROPERTY_TYPE.E_ACTION, PROPERTY_TYPE.E_FUNCTION, PROPERTY_TYPE.E_ENTITY, PROPERTY_TYPE.E_COLLECTION_ENTITY):
                continue
            outf.write(TP.ON_TO_COMPLEX_VALUE.format(_info.class_member_name))
        outf.write(TP.END_TO_COMPLEX_VALUE)

    def _generate_entity_types(self, outf, _schema_info):
        for class_info in _schema_info.class_list:
            if class_info.type != CLASS_TYPE.E_CLASS_ENTITY:
                continue
            self._generate_class_begin(outf, class_info)
            class_property_map = _schema_info.class_property_map[class_info.class_name]
            self._generate_common_methods_in_entity(outf, class_info, class_property_map)
            for property in class_property_map:
                _info = class_property_map[property]
                self._generate_property_in_entity(outf, class_info, _info)
            self._generate_entity_instance_creator(outf, class_info, class_property_map)
            self._generate_to_entity_value(outf, class_info, class_property_map)
            outf.write('\n')

    def _generate_entity_constructor(self, outf, class_info, class_property_map):
        outf.write(TP.BEGIN_ENTITY_CONSTRUCTOR.format(class_info.base_class_name))
        for property in class_property_map:
            _info = class_property_map[property]
            if _info.type == PROPERTY_TYPE.E_FUNCTION or _info.type == PROPERTY_TYPE.E_ACTION:
                continue
            outf.write(TP.ON_PROPERTY_IN_ENTITY_CONSTRUCTOR.format(_info.class_member_name, _info.default_value))
        outf.write('\n')

    def _generate_common_methods_in_entity(self, outf, class_info, class_property_map):
        self._generate_entity_constructor(outf, class_info, class_property_map)
        outf.write(TP.GET_ROOT_URL)
        outf.write(TP.EDM_INFO.format(class_info.class_name, class_info.edm_namespace, class_info.edm_name))

    def _generate_property_in_entity(self, outf, class_info, _info):
        if _info.type == PROPERTY_TYPE.E_ACTION or _info.type == PROPERTY_TYPE.E_FUNCTION:
            self._generate_operation_in_entity(outf, class_info, _info)
            return
        if _info.type == PROPERTY_TYPE.E_PRIMITIVE:
            outf.write(TP.PRIMITIVE_PROPERTY_IN_ENTITY_MAPPING.format(_info.class_member_name, _info.edm_name, self._primitive_resolver(_info)))
        elif _info.type == PROPERTY_TYPE.E_ENUM:
            outf.write(TP.ENUM_PROPERTY_IN_ENTITY_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        elif _info.type == PROPERTY_TYPE.E_COMPLEX:
            outf.write(TP.COMPLEX_PROPERTY_IN_ENTITY_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        elif _info.type == PROPERTY_TYPE.E_ENTITY:
            outf.write(TP.NAVIGATION_PROPERTY_IN_ENTITY_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        elif _info.type == PROPERTY_TYPE.E_COLLECTION_PRIMITIVE:
            outf.write(TP.COLLECTION_PRIMITIVE_PROPERTY_IN_ENTITY_MAPPING.format(_info.class_member_name, _info.edm_name, self._primitive_resolver(_info)))
        elif _info.type == PROPERTY_TYPE.E_COLLECTION_ENUM:
            outf.write(TP.COLLECTION_ENUM_PROPERTY_IN_ENTITY_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        elif _info.type == PROPERTY_TYPE.E_COLLECTION_COMPLEX:
            outf.write(TP.COLLECTION_COMPLEX_PROPERTY_IN_ENTITY_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        elif _info.type == PROPERTY_TYPE.E_COLLECTION_ENTITY:
            outf.write(TP.COLLECTION_NAVIGATION_PROPERTY_IN_ENTITY_MAPPING.format(_info.class_member_name, _info.edm_name, _info.class_member_type))
        outf.write('\n')

    def _generate_operation_in_entity(self, outf, class_info, _info):
        if _info is None:
            return
        _operation_info = _info.operation_info
        if _operation_info is None:
            return
        arguments = "self"
        for param in _operation_info.params:
            arguments += ", " + param.member_name
        outf.write(TP.BEGIN_OPERATION.format(_info.class_member_name, arguments))
        for param in _operation_info.params:
            if param.member_type == PROPERTY_TYPE.E_PRIMITIVE:
                outf.write(TP.ON_PRIMITIVE_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name))
            elif param.member_type == PROPERTY_TYPE.E_COMPLEX or param.member_type == PROPERTY_TYPE.E_ENTITY:
                outf.write(TP.ON_CLASS_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name, param.member_strong_type_name))
            elif param.member_type == PROPERTY_TYPE.E_ENUM:
                outf.write(TP.ON_ENUM_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name, param.member_strong_type_name))
            elif param.member_type == PROPERTY_TYPE.E_COLLECTION_PRIMITIVE:
                outf.write(TP.ON_COLLECTION_PRIMITIVE_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name))
            elif param.member_type == PROPERTY_TYPE.E_COLLECTION_ENTITY or param.member_type == PROPERTY_TYPE.E_COLLECTION_COMPLEX:
                outf.write(TP.ON_COLLECTION_CLASS_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name, param.member_strong_type_name))
            elif param.member_type == PROPERTY_TYPE.E_COLLECTION_ENUM:
                outf.write(TP.ON_COLLECTION_ENUM_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name, param.member_strong_type_name))
        is_function = "True" if _info.type == PROPERTY_TYPE.E_FUNCTION else "False"
        if _operation_info.return_type == "void":
            outf.write(TP.END_OPERATION_VOID.format(_operation_info.executor_name, is_function))
        else:
            return_type = _operation_info.return_type
            if _operation_info.executor_name == "operation_query_primitive":
                return_type = '"' + return_type + '"'
            outf.write(TP.END_OPERATION_WITH_RETURN_VALUE.format(_operation_info.executor_name, is_function, return_type))
        outf.write('\n')

    def _generate_entity_instance_creator(self, outf, class_info, class_property_map):
        outf.write(TP.BEGIN_ENTITY_INSTANCE_CREATOR.format(class_info.class_name, class_info.base_class_name))
        for property in class_property_map:
            _info = class_property_map[property]
            if _info.type == PROPERTY_TYPE.E_ACTION or _info.type == PROPERTY_TYPE.E_FUNCTION:
                continue
            outf.write(TP.ON_PROPERTY_IN_ENTITY_INSTANCE_CREATOR.format(_info.class_member_name))
        outf.write(TP.END_ENTITY_INSTANCE_CREATOR)

    def _generate_to_entity_value(self, outf, class_info, class_property_map):
        if class_info.base_class_name == "type_base":
            outf.write(TP.BEGIN_TO_ENTITY_VALUE)
        else:
            outf.write(TP.BEGIN_TO_ENTITY_VALUE_WITH_BASE_CLASS.format(class_info.base_class_name))
        for property in class_property_map:
            _info = class_property_map[property]
            if _info.type in (PROPERTY_TYPE.E_ACTION, PROPERTY_TYPE.E_FUNCTION, PROPERTY_TYPE.E_ENTITY, PROPERTY_TYPE.E_COLLECTION_ENTITY):
                continue
            outf.write(TP.ON_TO_ENTITY_VALUE.format(_info.class_member_name))
        outf.write(TP.END_TO_ENTITY_VALUE)

    def _generate_entity_container(self, outf, _schema_info):
        for class_info in _schema_info.class_list:
            if class_info.type != CLASS_TYPE.E_CLASS_CONTAINER:
                continue
            self._generate_class_begin(outf, class_info)
            outf.write(TP.ENTITY_CONTAINER_CONSTRUCTOR)
            class_property_map = _schema_info.class_property_map[class_info.class_name]
            for property_name in class_property_map:
                _info = class_property_map[property_name]
                if _info.type == PROPERTY_TYPE.E_CONTAINER_ENTITY_SET:
                    self._generate_entity_set_in_entity_container(outf, class_info, _info)
                elif _info.type == PROPERTY_TYPE.E_CONTAINER_SINGLETON:
                    self._generate_singleton_in_entity_conatiner(outf, class_info, _info)
                elif _info.type == PROPERTY_TYPE.E_ACTION or _info.type == PROPERTY_TYPE.E_FUNCTION:
                    self._generate_operation_imports_in_entity_container(outf, class_info, _info)
                else:
                    continue

    def _generate_entity_set_in_entity_container(self, outf, class_info, _info):
        outf.write(TP.QUERY_ENTITY_SET_IN_ENTITY_CONTAINER.format(_info.class_member_name, _info.edm_name, _info.strong_type_name))

    def _generate_singleton_in_entity_conatiner(self, outf, class_info, _info):
        outf.write(TP.QUERY_SINGLETON_IN_ENTITY_CONTAINER.format(_info.class_member_name, _info.edm_name, _info.strong_type_name))

    def _generate_operation_imports_in_entity_container(self, outf, class_info, _info):
        if _info is None:
            return
        _operation_info = _info.operation_info
        if _operation_info is None:
            return
        arguments = "self"
        for param in _operation_info.params:
            arguments += ", " + param.member_name
        outf.write(TP.BEGIN_OPERATION_IMPORT.format(_info.class_member_name, arguments))
        for param in _operation_info.params:
            if param.member_type == PROPERTY_TYPE.E_PRIMITIVE:
                outf.write(TP.ON_PRIMITIVE_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name))
            elif param.member_type == PROPERTY_TYPE.E_COMPLEX or param.member_type == PROPERTY_TYPE.E_ENTITY:
                outf.write(TP.ON_CLASS_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name, param.member_strong_type_name))
            elif param.member_type == PROPERTY_TYPE.E_ENUM:
                outf.write(TP.ON_ENUM_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name, param.member_strong_type_name))
            elif param.member_type == PROPERTY_TYPE.E_COLLECTION_PRIMITIVE:
                outf.write(TP.ON_COLLECTION_PRIMITIVE_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name))
            elif param.member_type == PROPERTY_TYPE.E_COLLECTION_ENTITY or param.member_type == PROPERTY_TYPE.E_COLLECTION_COMPLEX:
                outf.write(TP.ON_COLLECTION_CLASS_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name, param.member_strong_type_name))
            elif param.member_type == PROPERTY_TYPE.E_COLLECTION_ENUM:
                outf.write(TP.ON_COLLECTION_ENUM_PARAMETER_IN_OPERATION.format(param.member_name, param.edm_name, param.member_strong_type_name))
        is_function = "True" if _info.type == PROPERTY_TYPE.E_FUNCTION else "False"
        if _operation_info.return_type == "void":
            outf.write(TP.END_OPERATION_IMPORT_VOID.format(_operation_info.executor_name, is_function))
        else:
            return_type = _operation_info.return_type
            if _operation_info.executor_name == "operation_query_primitive":
                return_type = '"' + return_type + '"'
            outf.write(TP.END_OPERATION_IMPORT_WITH_RETURN_VALUE.format(_operation_info.executor_name, is_function, return_type))
        outf.write('\n')
