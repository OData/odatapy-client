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
import urllib

class odata_service_context(object):
    def __init__(self, base_address, options=odata_client_python.client_options()):
        self._client = odata_client_python.odata_client(base_address, options)
        self._model = None

    def get_edm_model(self):
        if self._model is None:
            self._model = self._client.get_model().get()
        return self._model

    def get_client(self):
        return self._client

    def get_root_url(self):
        return self._client.get_service_root_url()

    def get_relative_path(self, full_path):
        return self._client.get_relative_path(full_path)

    def get_expand_option_expression(self, path, filter=None, top=None, skip=None, select=None, orderby=None, expand=None):
        query_ex = path
        is_first = True
        if filter is not None:
            if is_first:
                query_ex += '('
                is_first = False
            else:
                query_ex += ';'
            query_ex += "$filter=" + filter
        if top is not None:
            if is_first:
                query_ex += '('
                is_first = False
            else:
                query_ex += ';'
            query_ex += "$top=" + str(top)
        if skip is not None:
            if is_first:
                query_ex += '('
                is_first = False
            else:
                query_ex += ';'
            query_ex += "$skip=" + str(skip)
        if select is not None:
            if is_first:
                query_ex += '('
                is_first = False
            else:
                query_ex += ';'
            query_ex += "$select=" + select
        if orderby is not None:
            if is_first:
                query_ex += '('
                is_first = False
            else:
                query_ex += ';'
            query_ex += "$orderby=" + orderby
        if expand is not None:
            if is_first:
                query_ex += '('
                is_first = False
            else:
                query_ex += ';'
            query_ex += "$expand=" + expand
        if not is_first:
            query_ex += ')'
        return query_ex
 
    def get_query_expression(self, path, key=None, filter=None, top=None, skip=None, select=None, orderby=None, expand=None):
        query_ex = path
        if key is not None:
            query_ex += '(' + key + ')'
        is_first = True
        if filter is not None:
            if is_first:
                query_ex += '?'
                is_first = False
            else:
                query_ex += '&'
            query_ex += "$filter=" + filter
        if top is not None:
            if is_first:
                query_ex += '?'
                is_first = False
            else:
                query_ex += '&'
            query_ex += "$top=" + str(top)
        if skip is not None:
            if is_first:
                query_ex += '?'
                is_first = False
            else:
                query_ex += '&'
            query_ex += "$skip=" + str(skip)
        if select is not None:
            if is_first:
                query_ex += '?'
                is_first = False
            else:
                query_ex += '&'
            query_ex += "$select=" + select
        if orderby is not None:
            if is_first:
                query_ex += '?'
                is_first = False
            else:
                query_ex += '&'
            query_ex += "$orderby=" + orderby
        if expand is not None:
            if is_first:
                query_ex += '?'
                is_first = False
            else:
                query_ex += '&'
            query_ex += "$expand=" + expand
        return urllib.quote(query_ex, '?$&,;=()/')

    def query(self, query_ex):
        return self._client.get_data_from_server(query_ex).get()

    def query_primitive(self, query_ex, ret_type):
        if self._client is None:
            return []
        values = self._client.get_data_from_server(query_ex).get()
        ret = []
        for value in values:
            if value is None:
                continue
            primitive_value = odata_client_python.to_primitive_value(value)
            if primitive_value is None:
                continue
            try:
                if ret_type is int:
                    val = int(primitive_value.to_string())
                elif ret_type is float:
                    val = float(primitive_value.to_string())
                elif ret_type is bool:
                    val = primitive_value.to_string() == "true"
                elif ret_type is str or ret_type is unicode:
                    val = primitive_value.to_string()
                else:
                    val = eval(primitive_value.to_string())
            except:
                val = primitive_value.to_string()
            ret.append(val)
        return ret

    def query_enum(self, query_ex, ret_type):
        if self._client is None:
            return []
        values = self._client.get_data_from_server(query_ex).get()
        ret = []
        for value in values:
            if value is None:
                continue
            enum_value = odata_client_python.to_enum_value(value)
            if enum_value is None:
                continue
            val = ret_type.get_enum_value_from_string(enum_value.to_string())
            ret.append(val)
        return ret

    def query_complex(self, query_ex, ret_type):
        if self._client is None:
            return []
        values = self._client.get_data_from_server(query_ex).get()
        ret = []
        for value in values:
            if value is None:
                continue
            complex_value = odata_client_python.to_complex_value(value)
            if complex_value is None:
                continue
            ret.append(ret_type.create_instance_from_complex(complex_value, self))
        return ret

    def query_entityset(self, query_ex, ret_type):
        if self._client is None:
            return []
        values = self._client.get_data_from_server(query_ex).get()
        ret = []
        for value in values:
            if value is None:
                continue
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(ret_type.create_instance_from_entity(entity_value, self))
        return ret

    def query_singleton(self, query_ex, ret_type):
        if self._client is None:
            return None
        values = self._client.get_data_from_server(query_ex).get()
        if len(values) != 1:
            return None
        entity_value = odata_client_python.to_entity_value(values[0])
        return ret_type.create_instance_from_entity(entity_value, self)

    def operation_query_primitive(self, query_ex, parameters, is_function, ret_type):
        if self._client is None:
            return None
        ret_values = odata_client_python.vector_odata_value()
        self._client.send_data_to_server(query_ex, parameters, ret_values, odata_client_python.HTTP_GET if is_function else odata_client_python.HTTP_POST).get()
        ret = []
        for value in ret_values:
            if value is None:
                continue
            primitive_value = odata_client_python.to_primitive_value(value)
            if primitive_value is None:
                continue
            try:
                if ret_type in ("uint8_t", "int8_t", "int16_t", "int32_t", "int64_t") or ret_type is int:
                    val = int(primitive_value.to_string())
                elif ret_type in ("float", "double", "long double") or ret_type is float:
                    val = float(primitive_value.to_string())
                elif ret_type == "bool" or ret_type is bool:
                    val = primitive_value.to_string() == "true"
                elif ret_type == "::utility::string_t" or ret_type is str or ret_type is unicode:
                    val = primitive_value.to_string()
                else:
                    val = eval(primitive_value.to_string())
            except:
                val = primitive_value.to_string()
            ret.append(val)
        return ret

    def operation_query_enum(self, query_ex, parameters, is_function, ret_type):
        if self._client is None:
            return None
        ret_values = odata_client_python.vector_odata_value()
        self._client.send_data_to_server(query_ex, parameters, ret_values, odata_client_python.HTTP_GET if is_function else odata_client_python.HTTP_POST).get()
        ret = []
        for value in ret_values:
            if value is None:
                continue
            enum_value = odata_client_python.to_enum_value(value)
            if enum_value is None:
                continue
            val = ret_type.get_enum_value_from_string(enum_value.to_string())
            ret.append(val)
        return ret

    def operation_query_complex(self, query_ex, parameters, is_function, ret_type):
        if self._client is None:
            return None
        ret_values = odata_client_python.vector_odata_value()
        self._client.send_data_to_server(query_ex, parameters, ret_values, odata_client_python.HTTP_GET if is_function else odata_client_python.HTTP_POST).get()
        ret = []
        for value in ret_values:
            if value is None:
                continue
            complex_value = odata_client_python.to_complex_value(value)
            if complex_value is None:
                continue
            ret.append(ret_type.create_instance_from_complex(complex_value, self))
        return ret

    def operation_query_entityset(self, query_ex, parameters, is_function, ret_type):
        if self._client is None:
            return None
        ret_values = odata_client_python.vector_odata_value()
        self._client.send_data_to_server(query_ex, parameters, ret_values, odata_client_python.HTTP_GET if is_function else odata_client_python.HTTP_POST).get()
        ret = []
        for value in ret_values:
            if value is None:
                continue
            entity_value = odata_client_python.to_entity_value(value)
            if entity_value is None:
                continue
            ret.append(ret_type.create_instance_from_entity(entity_value, self))
        return ret

    def operation_query_singleton(self, query_ex, parameters, is_function, ret_type):
        if self._client is None:
            return None
        ret_values = odata_client_python.vector_odata_value()
        self._client.send_data_to_server(query_ex, parameters, ret_values, odata_client_python.HTTP_GET if is_function else odata_client_python.HTTP_POST).get()
        ret = None
        if len(ret_values) != 1:
            return None
        entity_value = odata_client_python.to_entity_value(ret_values[0])
        return ret_type.create_instance_from_entity(entity_value, self)

    def operation_query_void(self, query_ex, parameters, is_function):
        if self._client is None:
            return -1
        ret_values = odata_client_python.vector_odata_value()
        self._client.send_data_to_server(query_ex, parameters, ret_values, odata_client_python.HTTP_GET if is_function else odata_client_python.HTTP_POST).get()
        return 0

    def add_object(self, path, _object):
        if self._client is None or _object is None:
            return -1
        model = self._client.get_model().get()
        if model is None:
            return -1
        entity_value = odata_client_python.to_entity_value(_object.to_value())
        if entity_value is None:
            return -1
        entity_value.set_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_TYPE, _object.get_full_name())
        ret_code = self._client.create_entity(path, entity_value).get()
        edit_link = entity_value.get_edit_link()
        if edit_link != "":
            _object.set_edit_link(edit_link)
        return ret_code

    def update_object(self, _object):
        if self._client is None or _object is None:
            return -1
        return self._client.send_data_to_server(self.get_relative_path(_object.get_edit_link()), _object.to_value(), odata_client_python.HTTP_PATCH).get()

    def delete_object(self, _object):
        if self._client is None or _object is None:
            return -1
        return self._client.send_data_to_server(self.get_relative_path(_object.get_edit_link()), odata_client_python.HTTP_DELETE).get()

    def add_related_object(self, _parent, path, _object):
        model = self.get_edm_model()
        if _parent is None or model is None or _object is None:
            return -1
        return self.add_object(self.get_relative_path(_parent.get_edit_link() + '/' + path), _object)

    def update_related_object(self, _parent, path, _object):
        if _parent is None or _object is None or self._client is None:
            return -1
        full_navigation_path = _parent.get_edit_link() + "/" + path
        navigation_path = self.get_relative_path(full_navigation_path)
        ret_code = self._client.send_data_to_server(self.get_relative_path(navigation_path), _object.to_value(), odata_client_python.HTTP_PATCH).get()
        if _object is not None:
            _object.set_edit_link(full_navigation_path)
        return ret_code

    def add_reference(self, _parent, path, _object):
        if self._client is None or _parent is None or _object is None:
            return -1
        return self._client.add_reference(self.get_relative_path(_parent.get_edit_link() + "/" + path), _object.get_edit_link()).get()

    def update_reference(self, _parent, path, _object):
        if self._client is None or _parent is None or _object is None:
            return -1
        return self._client.update_reference(self.get_relative_path(_parent.get_edit_link() + "/" + path), _object.get_edit_link()).get()

    def delete_reference(self, _parent, path, _object):
        if self._client is None or _parent is None or _object is None:
            return -1
        return self._client.remove_reference(self.get_relative_path(_parent.get_edit_link() + "/" + path), _object.get_edit_link()).get()
