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

path = r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService"
client = odata_client_python.odata_client(path)

def query_entityset():
    print r"==query_entityset=="
    client.send_data_to_server(r"ResetDataSource").get()
    entity_set_name = r"Products"
    entity_set = client.get_entities(entity_set_name).get()
    print len(entity_set) == 5
    print entity_set[0].get_value_type().get_type_kind() == odata_client_python.Entity
    first_entity = entity_set[0]
    property_value = odata_client_python.odata_value()
    print first_entity.get_property_value(r"Name", property_value)
    print property_value.get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(property_value)
    name = primitive_value.to_string()
    print name == r"Cheetos"

def query_entity():
    print r"==query_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    query_result = client.get_data_from_server(r"Products(6)").get()
    print len(query_result) == 1
    print query_result[0].get_value_type().get_type_kind() == odata_client_python.Entity
    entity = odata_client_python.to_entity_value(query_result[0])
    property_value = odata_client_python.odata_value()
    print entity.get_property_value(r"UnitPrice", property_value)
    print property_value.get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(property_value)
    unit_price = eval(primitive_value.to_string())
    print unit_price == 3.24

def query_primitive_property():
    print r"==query_primitive_property=="
    client.send_data_to_server(r"ResetDataSource").get()
    query_result = client.get_data_from_server(r"Products(7)/QuantityInStock").get()
    print len(query_result) == 1
    property_value = query_result[0]
    print property_value.get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(property_value)
    quantity = eval(primitive_value.to_string())
    print quantity == 20

def query_complex_property():
    print r"==query_complex_property=="
    client.send_data_to_server(r"ResetDataSource").get()
    query_result = client.get_data_from_server(r"People(1)/HomeAddress").get()
    print len(query_result) == 1
    print query_result[0].get_value_type().get_type_kind() == odata_client_python.Complex
    property_value = odata_client_python.to_complex_value(query_result[0])
    street_field = odata_client_python.odata_value()
    print property_value.get_property_value(r"Street", street_field)
    print street_field.get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(street_field)
    street = primitive_value.to_string()
    print street == r"1 Microsoft Way"

def query_collection_property():
    print r"==query_collection_property=="
    client.send_data_to_server(r"ResetDataSource").get()
    query_result = client.get_data_from_server(r"People(4)/Numbers").get()
    print len(query_result) == 3
    print query_result[0].get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(query_result[1])
    number = primitive_value.to_string()
    print number == r"555-555-5555"

def query_basic_properties_in_entity():
    print r"==query_basic_properties_in_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    query_result = client.get_data_from_server(r"People(4)").get()
    print len(query_result) == 1
    print query_result[0].get_value_type().get_type_kind() == odata_client_python.Entity
    entity = odata_client_python.to_entity_value(query_result[0])
    collection_property = odata_client_python.odata_value()
    print entity.get_property_value(r"Numbers", collection_property)
    print collection_property.get_value_type().get_type_kind() == odata_client_python.Collection
    collection_value = odata_client_python.to_collection_value(collection_property)
    collection_vector = collection_value.get_collection_values()
    print len(collection_vector) == 3
    collection_member = odata_client_python.to_primitive_value(collection_vector[1])
    print collection_member.to_string() == r"555-555-5555"

def create_entity():
    print r"==create_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    model = client.get_model().get()
    entity_set_name = r"Accounts"
    entity = odata_client_python.odata_entity_value(model.find_container().find_entity_set(entity_set_name).get_entity_type())
    entity.set_value(r"AccountID", 130)
    entity.set_value(r"CountryRegion", "CN")
    account_info = odata_client_python.odata_complex_value(model.find_complex_type(r"AccountInfo"))
    account_firstname = r"cpp"
    account_lastname = r"client"
    account_info.set_value(r"FirstName", account_firstname)
    account_info.set_value(r"LastName", account_lastname)
    entity.set_value(r"AccountInfo", account_info)
    response_code = client.create_entity(entity_set_name, entity).get()
    print response_code == 201
    query_result = client.get_data_from_server(r"Accounts(130)").get()
    print len(query_result) == 1
    new_entity = odata_client_python.to_entity_value(query_result[0])
    property_value = odata_client_python.odata_value()
    print entity.get_property_value(r"AccountID", property_value)
    primitive_value = odata_client_python.to_primitive_value(property_value)
    new_id = eval(primitive_value.to_string())
    print new_id == 130

def update_entity_with_patch():
    print r"==update_entity_with_patch=="
    client.send_data_to_server(r"ResetDataSource").get()
    model = client.get_model().get()
    query_result = client.get_data_from_server(r"Accounts(101)").get()
    old_entity = odata_client_python.to_entity_value(query_result[0])
    old_value = odata_client_python.odata_value()
    old_entity.get_property_value(r"CountryRegion", old_value)
    old_country = odata_client_python.to_primitive_value(old_value)
    print old_country.to_string() == r"US"
    old_entity.set_value(r"CountryRegion", r"GB")
    response_code = client.patch_entity(r"Accounts", old_entity).get()
    print response_code == 204
    check_query = client.get_data_from_server(r"Accounts(101)").get()
    new_entity = odata_client_python.to_entity_value(check_query[0])
    property_value = odata_client_python.odata_value()
    print new_entity.get_property_value(r"CountryRegion", property_value)
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print primitive_value.to_string() == r"GB"

def query_contained_entityset():
    print r"==query_contained_entityset=="
    client.send_data_to_server(r"ResetDataSource").get()
    entity_set = client.get_data_from_server(r"Accounts(101)/MyPaymentInstruments").get()
    print len(entity_set) == 3
    print entity_set[0].get_value_type().get_type_kind() == odata_client_python.Entity
    first_entity = odata_client_python.to_entity_value(entity_set[0])
    property_value = odata_client_python.odata_value()
    print first_entity.get_property_value(r"PaymentInstrumentID", property_value)
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print eval(primitive_value.to_string()) == 101901
    
def query_contained_entity():
    print r"==query_contained_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    entity_set = client.get_data_from_server(r"Accounts(101)/MyPaymentInstruments(101902)").get()
    print len(entity_set) == 1
    print entity_set[0].get_value_type().get_type_kind() == odata_client_python.Entity
    first_entity = odata_client_python.to_entity_value(entity_set[0])
    property_value = odata_client_python.odata_value()
    print first_entity.get_property_value(r"PaymentInstrumentID", property_value)
    print property_value.get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print eval(primitive_value.to_string()) == 101902
    
def query_contained_single_valued_entity():
    print r"==query_contained_single_valued_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    entity_set = client.get_data_from_server(r"Accounts(101)/MyGiftCard").get()
    print len(entity_set) == 1
    print entity_set[0].get_value_type().get_type_kind() == odata_client_python.Entity
    first_entity = odata_client_python.to_entity_value(entity_set[0]);
    property_value = odata_client_python.odata_value()
    print first_entity.get_property_value(r"Amount", property_value);
    print property_value.get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print eval(primitive_value.to_string()) == 19.9

def create_contained_entity():
    print r"==create_contained_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    model = client.get_model().get()
    entity_type_name = r"PaymentInstrument"
    entity = odata_client_python.odata_entity_value(model.find_entity_type(entity_type_name))
    entity.set_value(r"PaymentInstrumentID", 101920)
    entity.set_value(r"FriendlyName", r"created by cpp test")
    now = odata_client_python.datetime.utc_now()
    entity.set_value(r"CreatedDate", now)
    response_code = client.create_entity(r"Accounts(101)/MyPaymentInstruments", entity).get()
    print response_code == 201
    query_result = client.get_data_from_server(r"Accounts(101)/MyPaymentInstruments(101920)").get()
    print len(query_result) == 1
    new_entity = odata_client_python.to_entity_value(query_result[0])
    property_value = odata_client_python.odata_value()
    print entity.get_property_value(r"FriendlyName", property_value)
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print primitive_value.to_string() == r"created by cpp test"

def create_contained_single_valued_entity():
    print r"==create_contained_single_valued_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    model = client.get_model().get()
    entity_type_name = r"GiftCard"
    entity = odata_client_python.odata_entity_value(model.find_entity_type(entity_type_name))
    entity.set_value(r"GiftCardID", 304)
    card_number = r"AAASSSDD30"
    entity.set_value(r"GiftCardNO", card_number)
    entity.set_value(r"Amount", 132.0)
    now = odata_client_python.datetime.utc_now()
    entity.set_value(r"ExperationDate", now)
    response_code = client.send_data_to_server(r"Accounts(104)/MyGiftCard", entity, r"PATCH").get()
    print response_code == 204
    query_result = client.get_data_from_server(r"Accounts(104)/MyGiftCard").get()
    print len(query_result) == 1
    new_entity = odata_client_python.to_entity_value(query_result[0])
    property_value = odata_client_python.odata_value()
    print entity.get_property_value(r"Amount", property_value)
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print eval(primitive_value.to_string()) == 132.0

def query_entity_collection():
    print r"==query_entity_collection=="
    client.send_data_to_server(r"ResetDataSource").get()
    entities = client.get_data_from_server(r"People/Microsoft.Test.OData.Services.ODataWCFService.Customer").get()
    print len(entities) == 2
    first_entity = odata_client_python.to_entity_value(entities[0])
    property_value = odata_client_python.odata_value()
    print first_entity.get_property_value(r"City", property_value)
    print property_value.get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print primitive_value.to_string() == r"London"

def query_single_entity():
    print r"==query_single_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    entities = client.get_data_from_server(r"People(3)/Microsoft.Test.OData.Services.ODataWCFService.Employee").get()
    print len(entities) == 1
    first_entity = odata_client_python.to_entity_value(entities[0])
    property_value = odata_client_python.odata_value()
    print first_entity.get_property_value(r"DateHired", property_value)
    print property_value.get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print primitive_value.to_string() == r"2010-12-13T00:00:00Z"

def query_enum_in_entity():
    print r"==query_enum_in_entity=="
    client.send_data_to_server(r"ResetDataSource").get()
    entities = client.get_entities(r"Products").get()
    firstEntity = entities[0]
    skinColor = odata_client_python.odata_value()
    firstEntity.get_property_value(r"SkinColor", skinColor)
    print skinColor.get_value_type().get_type_kind() == odata_client_python.Enum
    skinColorEnum = odata_client_python.to_enum_value(skinColor)
    print skinColorEnum.to_string() == r"Red"
    
def query_enum_property():
    print r"==query_enum_property=="
    client.send_data_to_server(r"ResetDataSource").get()
    data = client.get_data_from_server(r"Products(5)/SkinColor").get()
    print len(data) == 1
    skinColor = odata_client_python.to_enum_value(data[0])
    print skinColor.to_string() == r"Red"

def update_enum_property():
    print r"==update_enum_property=="
    client.send_data_to_server(r"ResetDataSource").get()
    model = client.get_model().get()
    old_data = client.get_data_from_server(r"Products(5)").get()
    old_entity = odata_client_python.to_entity_value(old_data[0])
    old_value = odata_client_python.odata_value()
    old_entity.get_property_value(r"UserAccess", old_value)
    old_enum = odata_client_python.to_enum_value(old_value)
    print old_enum.to_string() == r"None"
    access_level_type = model.find_enum_type(r"AccessLevel")
    new_access = odata_client_python.odata_enum_value(access_level_type, r"ReadWrite")
    old_entity.set_value(r"UserAccess", new_access)
    response_code = client.patch_entity(r"Products", old_entity).get()
    print response_code == 204
    new_data = client.get_data_from_server(r"Products(5)").get()
    new_entity = odata_client_python.to_entity_value(new_data[0])
    new_value = odata_client_python.odata_value()
    new_entity.get_property_value(r"UserAccess", new_value)
    new_enum = odata_client_python.to_enum_value(new_value)
    print new_enum.to_string() == r"ReadWrite"

def invoke_unbound_function():
    print r"==invoke_unbound_function=="
    client.send_data_to_server(r"ResetDataSource").get()
    function_ret = client.get_data_from_server(r"Company/Microsoft.Test.OData.Services.ODataWCFService.GetEmployeesCount()").get()
    print len(function_ret) == 1
    print function_ret[0].get_value_type().get_type_kind() == odata_client_python.Primitive
    primitive_value = odata_client_python.to_primitive_value(function_ret[0])
    print eval(primitive_value.to_string()) == 2

def simple_function():
    print r"==simple_function=="
    client.send_data_to_server(r"ResetDataSource").get()
    employees_count_path = r"Company/Microsoft.Test.OData.Services.ODataWCFService.GetEmployeesCount"
    parameters = odata_client_python.vector_odata_parameter()
    returned_values = odata_client_python.vector_odata_value()
    client.send_data_to_server(employees_count_path, parameters, returned_values, odata_client_python.HTTP_GET).get()
    print len(returned_values) == 1
    print eval(odata_client_python.to_primitive_value(returned_values[0]).to_string()) == 2

def function_return_collection_of_complex_value():
    print r"==function_return_collection_of_complex_value=="
    client.send_data_to_server(r"ResetDataSource").get()
    product_details_path = r"Products(5)/Microsoft.Test.OData.Services.ODataWCFService.GetProductDetails"
    parameters = odata_client_python.vector_odata_parameter()
    parameters.push_back(odata_client_python.odata_parameter(r"count", odata_client_python.odata_primitive_value.make_primitive_value(3)))
    returned_values = odata_client_python.vector_odata_value()
    client.send_data_to_server(product_details_path, parameters, returned_values, odata_client_python.HTTP_GET).get()
    print len(returned_values) == 3
    detail1 = odata_client_python.to_entity_value(returned_values[0])
    property_value = odata_client_python.odata_value()
    detail1.get_property_value(r"ProductID", property_value)
    primitive_value = odata_client_python.to_primitive_value(property_value)
    print eval(primitive_value.to_string()) == 5

def action_of_primitive_value():
    print r"==action_of_primitive_value=="
    client.send_data_to_server(r"ResetDataSource").get()
    company_revenue_path = r"Company/Revenue"
    revenue_odata_value = client.get_data_from_server(company_revenue_path).get()[0]
    revenue_primitive_value = odata_client_python.to_primitive_value(revenue_odata_value)
    revenue = eval(revenue_primitive_value.to_string())
    print revenue == 100000
    parameters = odata_client_python.vector_odata_parameter()
    parameters.push_back(odata_client_python.odata_parameter(r"IncreaseValue", odata_client_python.odata_primitive_value.make_primitive_value(100000)))
    returned_values = odata_client_python.vector_odata_value()
    client.send_data_to_server(r"Company/Microsoft.Test.OData.Services.ODataWCFService.IncreaseRevenue", parameters, returned_values).get()
    print len(returned_values) == 1
    returned_value = returned_values[0]
    revenue_odata_value = client.get_data_from_server(company_revenue_path).get()[0]
    revenue_primitive_value = odata_client_python.to_primitive_value(revenue_odata_value)
    revenue = eval(revenue_primitive_value.to_string())
    print revenue == 200000
    returned_primitive_value = odata_client_python.to_primitive_value(returned_value)
    print eval(returned_primitive_value.to_string()) == 200000
    
def action_of_enum_value():
    print r"==action_of_enum_value=="
    client.send_data_to_server(r"ResetDataSource").get()
    product_user_access = r"Products(5)/UserAccess"
    user_access_value = odata_client_python.to_enum_value(client.get_data_from_server(product_user_access).get()[0])
    print user_access_value.to_string() == r"None"
    model = client.get_model().get()
    new_access = odata_client_python.odata_enum_value(model.find_enum_type(r"AccessLevel"), r"ReadWrite")
    parameters = odata_client_python.vector_odata_parameter()
    parameters.push_back(odata_client_python.odata_parameter(r"accessRight", new_access))
    returned_values = odata_client_python.vector_odata_value()
    client.send_data_to_server(r"Products(5)/Microsoft.Test.OData.Services.ODataWCFService.AddAccessRight", parameters, returned_values).get()
    print len(returned_values) == 1
    returned_value = returned_values[0];
    user_access_value = odata_client_python.to_enum_value(client.get_data_from_server(product_user_access).get()[0])
    print user_access_value.to_string() == r"ReadWrite"
    returned_enum_value = odata_client_python.to_enum_value(returned_value)
    print returned_enum_value.to_string() == r"ReadWrite"

def action_of_complex_value():
    print r"==action_of_complex_value=="
    client.send_data_to_server(r"ResetDataSource").get()
    home_address = r"People(1)/HomeAddress"
    home_address_value = odata_client_python.to_complex_value(client.get_data_from_server(home_address).get()[0])
    property_value = odata_client_python.odata_value()
    home_address_value.get_property_value(r"City", property_value)
    print odata_client_python.to_primitive_value(property_value).to_string() == r"Tokyo"
    model = client.get_model().get()
    address_type = model.find_complex_type(r"Address")
    new_address1 = odata_client_python.odata_complex_value(address_type)
    new_address1.set_value(r"City", r"Shanghai")
    new_address1.set_value(r"PostalCode", r"200000")
    new_address1.set_value(r"Street", r"Zixing Road")
    addresses = odata_client_python.odata_collection_value(odata_client_python.edm_collection_type(r"AddressCollection", address_type))
    addresses.add_collection_value(new_address1)
    parameters = odata_client_python.vector_odata_parameter()
    parameters.push_back(odata_client_python.odata_parameter(r"addresses", addresses))
    parameters.push_back(odata_client_python.odata_parameter(r"index", odata_client_python.odata_primitive_value.make_primitive_value(0)))
    returned_values = odata_client_python.vector_odata_value()
    client.send_data_to_server(r"People(1)/Microsoft.Test.OData.Services.ODataWCFService.ResetAddress", parameters, returned_values).get()
    print len(returned_values) == 1
    returned_value = returned_values[0]
    home_address_value = odata_client_python.to_complex_value(client.get_data_from_server(home_address).get()[0])
    home_address_value.get_property_value(r"City", property_value)
    print odata_client_python.to_primitive_value(property_value).to_string() == r"Shanghai"
    returned_entity_value = odata_client_python.to_entity_value(returned_value)
    returned_entity_value.get_property_value(r"HomeAddress", property_value)
    odata_client_python.to_complex_value(property_value).get_property_value(r"City", property_value)
    print odata_client_python.to_primitive_value(property_value).to_string() == r"Shanghai"

def query_navigaton_collection():
    print r"==query_navigaton_collection=="
    client.send_data_to_server(r"ResetDataSource").get()
    entities = client.get_data_from_server(r"Products(5)/Details").get()
    print len(entities) == 5
    first_entity = odata_client_python.to_entity_value(entities[1])
    property_value = odata_client_python.odata_value()
    print first_entity.get_property_value(r"@odata.editLink", property_value)
    print property_value.get_value_type().get_type_kind() == odata_client_python.PayloadAnnotation
    primitive_value = odata_client_python.to_primitive_value(property_value)
    edit_link = primitive_value.to_string()
    print edit_link == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/ProductDetails(ProductID=5,ProductDetailID=3)"
    
def expand_option():
    print r"==expand_option=="
    client.send_data_to_server(r"ResetDataSource").get()
    entities = client.get_data_from_server(r"Accounts(101)?$expand=MyGiftCard").get()
    print len(entities) == 1

def add_reference():
    print r"==add_reference=="
    client.send_data_to_server(r"ResetDataSource").get()
    orders_of_customer1 = r"Customers(1)/Orders"
    orders = client.get_data_from_server(orders_of_customer1).get()
    print len(orders) == 1
    orderEntity = odata_client_python.to_entity_value(client.get_data_from_server(r"Orders(7)").get()[0])
    property_value = odata_client_python.odata_value()
    orderEntity.get_property_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_ID, property_value)
    orderId = odata_client_python.to_primitive_value(property_value).to_string()
    client.add_reference(orders_of_customer1, orderId).get()
    orders = client.get_data_from_server(orders_of_customer1).get()
    print len(orders) == 2

def delete_reference_in_collection_valued_navigation_property():
    print r"==delete_reference_in_collection_valued_navigation_property=="
    client.send_data_to_server(r"ResetDataSource").get()
    orders_of_customer1 = r"Customers(1)/Orders"
    orders = client.get_data_from_server(orders_of_customer1).get()
    print len(orders) == 1
    orderEntity = odata_client_python.to_entity_value(orders[0])
    property_value = odata_client_python.odata_value()
    orderEntity.get_property_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_ID, property_value)
    orderId = odata_client_python.to_primitive_value(property_value).to_string()
    client.remove_reference(orders_of_customer1, orderId).get()
    orders = client.get_data_from_server(orders_of_customer1).get()
    print len(orders) == 0

def update_reference():
    print r"==update_reference=="
    client.send_data_to_server(r"ResetDataSource").get()
    parent = r"People(1)/Parent"
    person_id_property = r"PersonID"
    parentEntity = odata_client_python.to_entity_value(client.get_data_from_server(parent).get()[0])
    property_value = odata_client_python.odata_value()
    parentEntity.get_property_value(person_id_property, property_value)
    person_id = eval(odata_client_python.to_primitive_value(property_value).to_string())
    print person_id == 2
    newParentEntity = odata_client_python.to_entity_value(client.get_data_from_server(r"People(3)").get()[0])
    newParentEntity.get_property_value(odata_client_python.odata_json_constants.PAYLOAD_ANNOTATION_ID, property_value)
    newParentId = odata_client_python.to_primitive_value(property_value).to_string()
    client.update_reference(parent, newParentId).get()
    parentEntity = odata_client_python.to_entity_value(client.get_data_from_server(parent).get()[0])
    parentEntity.get_property_value(person_id_property, property_value)
    person_id = eval(odata_client_python.to_primitive_value(property_value).to_string())
    print person_id == 3
    
def query_singleton():
    print r"==query_singleton=="
    client.send_data_to_server(r"ResetDataSource").get()
    query_result = client.get_data_from_server(r"Company").get()
    print len(query_result) == 1
    print query_result[0].get_value_type().get_type_kind() == odata_client_python.Entity

def main():
    client.send_data_to_server(r"ResetDataSource").get()
    query_entityset()
    query_entity()
    query_primitive_property()
    query_complex_property()
    query_collection_property()
    query_basic_properties_in_entity()
    create_entity()
    update_entity_with_patch()
    query_contained_entityset()
    query_contained_entity()
    query_contained_single_valued_entity()
    create_contained_entity()
    create_contained_single_valued_entity()
    query_entity_collection()
    query_single_entity()
    query_enum_in_entity()
    query_enum_property()
    update_enum_property()
    invoke_unbound_function()
    simple_function()
    function_return_collection_of_complex_value()
    action_of_primitive_value()
    action_of_enum_value()
    action_of_complex_value()
    query_navigaton_collection()
    expand_option()
    add_reference()
    delete_reference_in_collection_valued_navigation_property()
    update_reference()
    query_singleton()

if __name__ == "__main__":
    main()
