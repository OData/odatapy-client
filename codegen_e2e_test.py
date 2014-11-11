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

from WCFService import *
service_context = InMemoryEntities(r'http://odatae2etest.azurewebsites.net/cpptest/DefaultService')
service_context.ResetDataSource()

def query_entityset():
    print "==query_entityset=="
    service_context.ResetDataSource()
    people = service_context.query_people()
    print len(people) == 5
    print people[4].get_firstname() == "Peter"

def query_entity():
    print "==query_entity=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="4")
    print len(people) == 1
    print people[0].get_firstname() == "Elmo"

def top_level_query():
    print "==top_level_query=="
    service_context.ResetDataSource()
    price = service_context.query_primitive(r"Products(5)/UnitPrice", float)
    print len(price) == 1
    print price[0] == 3.24

    acct_info = service_context.query_complex(r"Accounts(101)/AccountInfo", AccountInfo)
    print len(acct_info) == 1
    print acct_info[0].get_firstname() == "Alex"

    numbers = service_context.query_primitive(r"People(4)/Numbers", unicode)
    print len(numbers) == 3
    print numbers[0] == "444-444-4444"

def create_entity():
    print "==create_entity=="
    service_context.ResetDataSource()
    new_account = Account(service_context)
    new_account.set_accountid(140)
    new_account.set_countryregion("DE")
    acinfo = AccountInfo(service_context)
    acinfo.set_firstname("cpp")
    acinfo.set_lastname("test")
    new_account.set_accountinfo(acinfo)

    status_code = service_context.add_object("Accounts", new_account)
    print status_code == 201

    account = service_context.query_accounts(key="140")
    print account[0].get_countryregion() == "DE"
    info = account[0].get_accountinfo()
    print info.get_firstname() == "cpp"
    print info.get_lastname() == "test"

def update_entity():
    print "==update_entity=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="5")
    print len(people) == 1

    people[0].set_firstname("cpp test updated")
    status_code = service_context.update_object(people[0])
    print status_code == 204

    people_new = service_context.query_people(key="5")
    print people_new[0].get_firstname() == "cpp test updated"

def delete_entity():
    print "==delete_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="107")
    print len(accounts) == 1

    status_code = service_context.delete_object(accounts[0])
    print status_code == 204

def query_contained_entity():
    print "==query_contained_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="101", expand="MyGiftCard,MyPaymentInstruments")
    print len(accounts) == 1
    account101 = accounts[0]
    print account101.get_mygiftcard().get_amount() == 19.9
    print account101.get_mypaymentinstruments()[0].get_friendlyname() == "101 first PI"
    print account101.get_mygiftcard().get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(101)/MyGiftCard"
    print account101.get_mypaymentinstruments()[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(101)/MyPaymentInstruments(101901)"

    accounts = service_context.query_accounts(key="103")
    print len(accounts) == 1
    account103 = accounts[0]
    account103.load_mygiftcard()
    account103.load_mypaymentinstruments()
    print account103.get_mygiftcard().get_amount() == 1.9
    print account103.get_mypaymentinstruments()[0].get_friendlyname() == "103 frist PI"
    print account103.get_mygiftcard().get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(103)/MyGiftCard"
    print account103.get_mypaymentinstruments()[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(103)/MyPaymentInstruments(103901)"

def create_contained_entity():
    print "==create_contained_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="101")
    print len(accounts) == 1
    account = accounts[0]

    new_pi = CreditCardPI(service_context)
    new_pi.set_paymentinstrumentid(101920)
    new_pi.set_friendlyname("cpp test containment creation")
    new_pi.set_createddate(odata_client_python.datetime.utc_now())
    new_pi.set_cardnumber("9200000000000000")
    new_pi.set_cvv("801")
    new_pi.set_holdername("cpp")
    new_pi.set_balance(32.0)
    new_pi.set_experationdate(odata_client_python.datetime.utc_now())
    status_code = service_context.add_related_object(account, "MyPaymentInstruments", new_pi)
    print status_code == 201
    print new_pi.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(101)/MyPaymentInstruments(101920)"

    pi = service_context.query_singleton(r"Accounts(101)/MyPaymentInstruments(101920)", PaymentInstrument)
    print pi.get_friendlyname() == "cpp test containment creation"

def create_contained_single_valued_entity():
    print "==create_contained_single_valued_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="101")
    print len(accounts) == 1
    account = accounts[0]

    new_giftcard = GiftCard(service_context)
    new_giftcard.set_giftcardid(304)
    new_giftcard.set_giftcardno("AAB999A")
    new_giftcard.set_amount(30.0)
    new_giftcard.set_experationdate(odata_client_python.datetime.utc_now())
    status_code = service_context.update_related_object(account, "MyGiftCard", new_giftcard)

    print status_code == 204
    print new_giftcard.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(101)/MyGiftCard"

    account.load_mygiftcard()
    giftcard = account.get_mygiftcard()
    print giftcard.get_giftcardid() == 304
    print giftcard.get_amount() == 30.0

def update_contained_entity():
    print "==update_contained_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="101")
    print len(accounts) == 1
    account = accounts[0]

    account.load_mygiftcard()
    giftcard = account.get_mygiftcard()
    print giftcard.get_amount() == 19.9

    # precision issue here
    giftcard.set_amount(91.5)
    status_code = service_context.update_object(giftcard)
    print status_code == 204

    account.load_mygiftcard()
    new_giftcard = account.get_mygiftcard()
    print new_giftcard.get_amount() == 91.5

def delete_contained_entity():
    print "==delete_contained_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="101", expand="MyPaymentInstruments")
    print len(accounts) == 1
    account = accounts[0]

    print len(account.get_mypaymentinstruments()) == 3
    cc = account.get_mypaymentinstruments()[1]
    print cc.get_friendlyname() == "101 frist credit PI"

    status_code = service_context.delete_object(cc)
    print status_code == 204

    account.load_mypaymentinstruments()
    print len(account.get_mypaymentinstruments()) == 2

def query_contained_entities_with_query_options():
    print "==query_contained_entities_with_query_options=="
    service_context.ResetDataSource()
    query_ex = service_context.get_query_expression(r"Accounts(101)/MyPaymentInstruments", filter=r"PaymentInstrumentID gt 101901")
    pis = service_context.query_entityset(query_ex, PaymentInstrument)
    print len(pis) == 2
    print pis[0].get_paymentinstrumentid() == 101902
    print pis[1].get_paymentinstrumentid() == 101903

def level2_contained_entity():
    print "==level2_contained_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="103")
    print len(accounts) == 1
    print accounts[0].get_accountid() == 103

    account = accounts[0]
    account.load_mypaymentinstruments()
    pis = account.get_mypaymentinstruments()
    print len(pis) == 4
    print pis[0].get_paymentinstrumentid() == 103901

    pi = pis[0]
    pi.load_billingstatements()
    statements = pi.get_billingstatements()
    print len(statements) == 2
    print statements[1].get_statementid() == 103901002
    print statements[1].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(103)/MyPaymentInstruments(103901)/BillingStatements(103901002)"

    single_statement = service_context.query_singleton(r"Accounts(103)/MyPaymentInstruments(103901)/BillingStatements(103901001)", Statement)
    print single_statement.get_statementid() == 103901001
    print single_statement.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(103)/MyPaymentInstruments(103901)/BillingStatements(103901001)"

def level2_noncontained_entity():
    print "==level2_noncontained_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="103")
    print len(accounts) == 1
    print accounts[0].get_accountid() == 103

    account = accounts[0]
    account.load_mypaymentinstruments()
    pis = account.get_mypaymentinstruments()
    print len(pis) == 4
    print pis[0].get_paymentinstrumentid() == 103901

    pi = pis[0]
    pi.load_thestoredpi()
    the_stored_pi = pi.get_thestoredpi()
    print the_stored_pi is not None
    print the_stored_pi.get_storedpiid() == 802
    print the_stored_pi.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/StoredPIs(802)"

def derived_type_contained_entity():
    print "==derived_type_contained_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="101")
    print len(accounts) == 1
    print accounts[0].get_accountid() == 101

    account = accounts[0]
    account.load_mypaymentinstruments()
    pis = account.get_mypaymentinstruments()
    print len(pis) == 3

    print pis[0].get_paymentinstrumentid() == 101901
    cc1 = pis[1]
    print cc1 is not None
    print cc1.get_cvv() == "234"

    print cc1.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(101)/MyPaymentInstruments(101902)/Microsoft.Test.OData.Services.ODataWCFService.CreditCardPI"
    cc2 = pis[2]
    print cc2 is not None
    print cc2.get_cvv() == "012"
    print cc2.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(101)/MyPaymentInstruments(101903)/Microsoft.Test.OData.Services.ODataWCFService.CreditCardPI"

    cc1.load_creditrecords()
    credit_records = cc1.get_creditrecords()
    print len(credit_records) == 2

    credit_record = credit_records[0]
    print credit_record.get_reason() == "Shopping"
    print credit_record.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Accounts(101)/MyPaymentInstruments(101902)/Microsoft.Test.OData.Services.ODataWCFService.CreditCardPI/CreditRecords(1)"

def query_entity_collection():
    print "==query_entity_collection=="
    service_context.ResetDataSource()
    people = service_context.query_people()
    print len(people) == 5

    customer = people[0]
    print customer.get_city() == "London"

def create_derived_type_entity():
    print "==create_derived_type_in_entity=="
    service_context.ResetDataSource()
    new_customer = Customer(service_context)
    new_customer.set_personid(10)
    new_customer.set_firstname("cpp")
    new_customer.set_lastname("test")
    numbers = []
    numbers.append("111-111-1112")
    numbers.append("111-222-2222")
    new_customer.set_numbers(numbers)
    emails = []
    emails.append(r"abc@mail.com")
    new_customer.set_emails(emails)
    new_customer.set_birthday(odata_client_python.datetime.utc_now())
    new_customer.set_city("Shanghai")
    new_customer.set_timebetweenlasttwoorders(odata_client_python.to_duration(123))

    status_code = service_context.add_object("People", new_customer)
    print status_code == 201
    print new_customer.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/People(10)"

    check_result = service_context.query_singleton(r"People(10)/Microsoft.Test.OData.Services.ODataWCFService.Customer", Customer)
    print check_result.get_city() == "Shanghai"

    new_customer.set_city("Beijing")
    status_code = service_context.update_object(new_customer)
    print status_code == 204
    check_result = service_context.query_singleton(r"People(10)/Microsoft.Test.OData.Services.ODataWCFService.Customer", Customer)
    print check_result.get_city() == "Beijing"

def update_derived_type_entity():
    print "==update_derived_type_entity=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="2")
    print len(people) == 1
    customer = people[0]
    print customer.get_city() == "Sydney"

    customer.set_city("Beijing")
    customer.set_timebetweenlasttwoorders(odata_client_python.to_duration(600))
    status_code = service_context.update_object(customer)
    print status_code == 204

    new_people = service_context.query_people(key="2")
    print len(new_people) == 1
    new_customer = new_people[0]
    print new_customer.get_city() == "Beijing"

def delete_derived_type_entity():
    print "==delete_derived_type_entity=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="2")
    print len(people) == 1
    customer = people[0]
    print customer.get_city() == "Sydney"

    status_code = service_context.delete_object(customer)
    print status_code == 204

def query_derived_type_complex():
    print "==query_derived_type_complex=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="1")
    print len(people) == 1

    address = people[0].get_homeaddress()
    print address.get_city() == "Tokyo"
    print address.get_street() == "1 Microsoft Way"
    print address.get_postalcode() == "98052"

    home = address
    print home.get_familyname() == "Cats"

def update_derived_type_complex():
    print "==update_derived_type_complex=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="1")
    print len(people) == 1
    customer = people[0]
    customer.set_timebetweenlasttwoorders(odata_client_python.to_duration(600))

    home = customer.get_homeaddress()
    home.set_city("Shang Hai")
    home.set_street("Zi Zhu")
    home.set_postalcode("120012")
    home.set_familyname("Panda")
    status_code = service_context.update_object(customer)
    print status_code == 204

    people = service_context.query_people(key="1")
    home = people[0].get_homeaddress()
    print home.get_city() == "Shang Hai"
    print home.get_street() == "Zi Zhu"
    print home.get_postalcode() == "120012"
    print home.get_familyname() == "Panda"

def create_derived_type_complex_in_entity():
    print "==create_derived_type_complex_in_entity=="
    service_context.ResetDataSource()
    new_customer = Customer(service_context)
    new_customer.set_personid(10)
    new_customer.set_firstname("cpp")
    new_customer.set_lastname("test")
    numbers = []
    numbers.append("111-111-1112")
    numbers.append("111-222-2222")
    new_customer.set_numbers(numbers)
    emails = []
    emails.append("abc@mail.com")
    new_customer.set_emails(emails)
    new_customer.set_birthday(odata_client_python.datetime.utc_now())
    new_customer.set_city("Shanghai")
    new_customer.set_timebetweenlasttwoorders(odata_client_python.to_duration(123))

    homeaddress = HomeAddress(service_context)
    homeaddress.set_city("Shang Hai")
    homeaddress.set_street("Zi Zhu")
    homeaddress.set_postalcode("120012")
    homeaddress.set_familyname("Panda")
    new_customer.set_homeaddress(homeaddress)

    status_code = service_context.add_object("People", new_customer)
    print status_code == 201
    print new_customer.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/People(10)"

    check_result = service_context.query_singleton(r"People(10)/Microsoft.Test.OData.Services.ODataWCFService.Customer", Customer)
    print check_result.get_city() == "Shanghai"
    homeaddress = check_result.get_homeaddress()
    print homeaddress.get_city() == "Shang Hai"

    new_customer.set_city("Beijing")
    status_code = service_context.update_object(new_customer)
    print status_code == 204
    check_result = service_context.query_singleton(r"People(10)/Microsoft.Test.OData.Services.ODataWCFService.Customer", Customer)
    print check_result.get_city() == "Beijing"

def query_with_enum():
    print "==query_with_enum=="
    service_context.ResetDataSource()
    products = service_context.query_products(key="5")
    print len(products) == 1

    product = products[0]
    print product.get_skincolor() == Color.Red
    print product.get_useraccess() == AccessLevel._None
    print len(product.get_covercolors()) == 3
    print product.get_covercolors()[2] == Color.Blue

    skin_color = service_context.query_enum(r"Products(5)/SkinColor", Color)
    print len(skin_color) == 1
    print skin_color[0] == Color.Red
    user_access = service_context.query_enum(r"Products(5)/UserAccess", AccessLevel)
    print len(user_access) == 1
    print user_access[0] == AccessLevel._None
    cover_colors = service_context.query_enum(r"Products(5)/CoverColors", Color)
    print len(cover_colors) == 3
    print cover_colors[2] == Color.Blue

def update_with_enum():
    print "==update_with_enum=="
    service_context.ResetDataSource()
    products = service_context.query_products(key="5")
    print len(products) == 1

    product = products[0]
    product.set_skincolor(Color.Green)
    product.set_useraccess(AccessLevel.ReadWrite)
    new_cover_colors = []
    new_cover_colors.append(Color.Green)
    new_cover_colors.append(Color.Blue)
    product.set_covercolors(new_cover_colors)

    status_code = service_context.update_object(product)
    print status_code == 204

    new_product = service_context.query_products(key="5")[0]
    print new_product.get_skincolor() == Color.Green
    print new_product.get_useraccess() == AccessLevel.ReadWrite
    cover_colors = new_product.get_covercolors()
    print len(cover_colors) == 2
    print cover_colors[1] == Color.Blue

def function_no_param_return_int():
    print "==function_no_param_return_int=="
    service_context.ResetDataSource()
    company_obj = service_context.query_company()
    ret = company_obj.GetEmployeesCount()
    print len(ret) == 1
    print ret[0] == 2

def function_one_param_return_collection_entity():
    print "==function_one_param_return_collection_entity=="
    service_context.ResetDataSource()
    products = service_context.query_products()
    ret = products[0].GetProductDetails(10)
    print len(ret) == 5

    print ret[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/ProductDetails(ProductID=5,ProductDetailID=2)"
    print ret[0].get_productid() == 5
    print ret[0].get_productdetailid() == 2
    print ret[0].get_productname() == "CheeseCake"
    print ret[0].get_description() == "Cheese-flavored snack"

    print ret[4].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/ProductDetails(ProductID=5,ProductDetailID=6)"
    print ret[4].get_productid() == 5
    print ret[4].get_productdetailid() == 6
    print ret[4].get_productname() == "Gatorade"
    print ret[4].get_description() == "fitness drink!"

    products_ret = ret[0].GetRelatedProduct()
    print len(products_ret) == 1

    print products_ret[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Products(5)"
    print products_ret[0].get_productid() == 5
    print products_ret[0].get_name() == "Cheetos"
    print products_ret[0].get_quantityperunit() == "100g Bag"
    print len(products_ret[0].get_covercolors()) == 3
    print products_ret[0].get_covercolors()[0] == Color.Green


def function_no_param_return_complex():
    print "==function_no_param_return_complex=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="1")
    print len(people) == 1
    home_address_obj = people[0].GetHomeAddress()
    print len(home_address_obj) == 1
    print home_address_obj[0].get_familyname() == "Cats"
    print home_address_obj[0].get_city() == "Tokyo"
    print home_address_obj[0].get_postalcode() == "98052"
    print home_address_obj[0].get_street() == "1 Microsoft Way"

def function_import_no_param_return_collection_entity():
    print "==function_import_no_param_return_collection_entity=="
    service_context.ResetDataSource()
    products = service_context.GetAllProducts()
    print len(products) == 5
    print products[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Products(5)"
    print products[0].get_productid() == 5
    print products[0].get_name() == "Cheetos"
    print products[0].get_quantityperunit() == "100g Bag"
    print len(products[0].get_covercolors()) == 3
    print products[0].get_covercolors()[0] == Color.Green

def action_function_import_two_param_return_collection_primitive():
    print "==action_function_import_two_param_return_collection_primitive=="
    service_context.ResetDataSource()
    emails = []
    emails.append("email_1")
    emails.append("email_2")
    emails.append("email_3")
    action_ret = service_context.ResetBossEmail(emails)

    print len(action_ret) == 3
    print action_ret[0] == "email_1"
    print action_ret[1] == "email_2"
    print action_ret[2] == "email_3"

    function_ret = service_context.GetBossEmails(0, 5)
    print len(function_ret) == 3
    print function_ret[0] == "email_1"
    print function_ret[1] == "email_2"
    print function_ret[2] == "email_3"

def function_import_one_param_return_entity():
    print "==function_import_one_param_return_entity=="
    service_context.ResetDataSource()
    ret = service_context.GetPerson2("Tokyo")
    print len(ret) == 1
    print ret[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/People(1)/Microsoft.Test.OData.Services.ODataWCFService.Customer"
    print ret[0].get_firstname() == "Bob"
    print ret[0].get_lastname() == "Cat"

def action_one_param_return_enum():
    print "==action_one_param_return_enum=="
    service_context.ResetDataSource()
    products = service_context.query_products()
    print products[0].get_useraccess() == AccessLevel._None
    ret = products[0].AddAccessRight(AccessLevel.ReadWrite)
    print len(ret) == 1
    print ret[0] == AccessLevel.ReadWrite
    products = service_context.query_products()
    print products[0].get_useraccess() == AccessLevel.ReadWrite

def action_one_param_return_primitive():
    print "==action_one_param_return_enum=="
    service_context.ResetDataSource()
    company_obj = service_context.query_company()
    print company_obj.get_revenue() == 100000
    ret = company_obj.IncreaseRevenue(212304540)
    print len(ret) == 1
    print ret[0] == 212404540
    company_obj = service_context.query_company()
    print company_obj.get_revenue() == 212404540

def action_import_return_void():
    print "==action_import_return_void=="
    service_context.ResetDataSource()
    ret = service_context.Discount(32)
    print ret == 0

def action_import_one_param_return_complex():
    print "==action_import_one_param_return_complex=="
    service_context.ResetDataSource()
    address = Address(service_context)
    address.set_city("Shang Hai")
    address.set_postalcode("123123")
    address.set_street("ZiXing Road")
    ret = service_context.ResetBossAddress(address)
    print len(ret) == 1
    print ret[0].get_city() == "Shang Hai"
    print ret[0].get_postalcode() == "123123"
    print ret[0].get_street() == "ZiXing Road"

def action_one_param_return_entity():
    print "==action_one_param_return_entity=="
    service_context.ResetDataSource()
    addresses = []
    address1 = Address(service_context)
    address1.set_city("Shang Hai")
    address1.set_postalcode("123123")
    address1.set_street("ZiXing Road")
    addresses.append(address1)

    address2 = Address(service_context)
    address2.set_city("Bei Jing")
    address2.set_postalcode("006767")
    address2.set_street("TiananMen Road")
    addresses.append(address2)

    address3 = Address(service_context)
    address3.set_city("La Sa")
    address3.set_postalcode("221122")
    address3.set_street("LaSa Road")
    addresses.append(address3)

    people = service_context.query_people(key="1")
    ret = people[0].ResetAddress(addresses, 2)
    people = service_context.query_people(key="1")
    print len(people) == 1
    print people[0].get_homeaddress().get_city() == "La Sa"
    print people[0].get_homeaddress().get_postalcode() == "221122"
    print people[0].get_homeaddress().get_street() == "LaSa Road"

def action_one_param_datetime_return_entity():
    print "==action_one_param_datetime_return_entity=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(key="101")
    dt = odata_client_python.datetime.from_string("2014-05-19T14:05:00Z", odata_client_python.datetime.ISO_8601)
    ret = accounts[0].RefreshDefaultPI(dt)
    print ret[0].get_createddate() == r"2014-05-19T14:05:00Z"

def query_navigation_collection():
    print "==query_navigation_collection=="
    service_context.ResetDataSource()
    products = service_context.query_products(key="5")
    print len(products) == 1
    product = products[0]

    product.load_details()
    print len(product.get_details()) == 5
    detail = product.get_details()[0]
    print detail.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/ProductDetails(ProductID=5,ProductDetailID=2)"
    print detail.get_productname() == "CheeseCake"

def query_navigation_single():
    print "==query_navigation_single=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="1")
    print len(people) == 1
    person = people[0]

    person.load_parent()
    parent = person.get_parent()
    print parent.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/People(2)/Microsoft.Test.OData.Services.ODataWCFService.Customer"
    print parent.get_firstname() == "Jill"

def filter_option():
    print "==filter_option=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(filter="CountryRegion eq 'US'")
    print len(accounts) == 2
    for account in accounts:
        print account.get_countryregion() == "US"

def orderby_option():
    print "==orderby_option=="
    service_context.ResetDataSource()
    accounts = service_context.query_accounts(orderby="CountryRegion")
    print len(accounts) == 7
    print accounts[0].get_countryregion() == "CN"
    print accounts[3].get_countryregion() == "FR"
    print accounts[5].get_countryregion() == "US"

def select_option():
    print "==select_option=="
    service_context.ResetDataSource()
    products = service_context.query_products(key="5", select="Name, UserAccess")
    print len(products) == 1
    product = products[0]
    print product.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Products(5)"

    products2 = service_context.query_products(key="5", select="*")
    print len(products2) == 1
    product2 = products2[0]
    print product2.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Products(5)"

def expand_option():
    print "==expand_option=="
    service_context.ResetDataSource()
    products = service_context.query_products(key="5", expand="Details")
    print len(products) == 1
    product = products[0]

    details = product.get_details()
    print len(details) == 5
    print details[0].get_productdetailid() == 2
    print details[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/ProductDetails(ProductID=5,ProductDetailID=2)"

    people = service_context.query_people(key="1", expand="Parent")
    print len(people) == 1
    person = people[0]

    parent = person.get_parent()
    print parent.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/People(2)/Microsoft.Test.OData.Services.ODataWCFService.Customer"
    print parent.get_firstname() == "Jill"

def mixed_query_options():
    print "==mixed_query_options=="
    service_context.ResetDataSource()
    expand_option = service_context.get_expand_option_expression("MyPaymentInstruments", select="PaymentInstrumentID,FriendlyName", orderby="FriendlyName")
    accounts = service_context.query_accounts(key="103", expand=expand_option)
    print len(accounts) == 1
    account = accounts[0]
    pis = account.get_mypaymentinstruments()
    print len(pis) == 4
    print pis[0].get_paymentinstrumentid() == 101910
    print pis[0].get_friendlyname() == "103 backup PI"
    print pis[1].get_paymentinstrumentid() == 103901
    print pis[1].get_friendlyname() == "103 frist PI"

def add_reference():
    print "==add_reference=="
    service_context.ResetDataSource()
    customer = service_context.query_customers(key="1")[0]
    customer.load_orders()
    print len(customer.get_orders()) == 1

    order = service_context.query_orders(key="7")[0]
    service_context.add_reference(customer, "Orders", order)

    customer.load_orders()
    print len(customer.get_orders()) == 2

def update_reference():
    print "==update_reference=="
    service_context.ResetDataSource()
    people = service_context.query_people(key="1", expand="Parent")[0]
    print people.get_parent().get_personid() == 2

    parent = service_context.query_people(key="3")[0]
    service_context.update_reference(people, "Parent", parent)

    people.load_parent()
    print people.get_parent().get_personid() == 3

def query_update_singleton():
    print "==query_update_singleton=="
    service_context.ResetDataSource()
    vip = service_context.query_vipcustomer()
    print vip.get_personid() == 1
    print vip.get_city() == "London"

    vip.set_city("Shanghai")
    vip.set_timebetweenlasttwoorders(odata_client_python.to_duration(123))
    status_code = service_context.update_object(vip)
    print status_code == 204

    new_vip = service_context.query_vipcustomer()
    print new_vip.get_city() == "Shanghai"

def derived_type_singleton():
    print "==derived_type_singleton=="
    service_context.ResetDataSource()
    boss = service_context.query_boss()
    print boss.get_personid() == 2
    print boss.get_city() == "Sydney"

    boss.set_city("Shanghai")
    boss.set_timebetweenlasttwoorders(odata_client_python.to_duration(123))
    status_code = service_context.update_object(boss)
    print status_code == 204

    new_boss = service_context.query_boss()
    print new_boss.get_city() == "Shanghai"

def singleton_with_navigation_properties():
    print "==singleton_with_navigation_properties=="
    service_context.ResetDataSource()
    company = service_context.query_company()
    company.load_employees()

    employees = company.get_employees()
    print len(employees) == 2
    print employees[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Employees(PersonID=3)"
    print employees[0].get_firstname() == "Jacob"

    company.load_vipcustomer()
    vip = company.get_vipcustomer()
    print vip.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/VipCustomer"
    print vip.get_firstname() == "Bob"

def singleton_with_query_option():
    print "==singleton_with_query_option=="
    service_context.ResetDataSource()
    expand_option = "VipCustomer," + service_context.get_expand_option_expression("Employees", filter="PersonID eq 3")
    company = service_context.query_company(expand=expand_option)
    employees = company.get_employees()
    print len(employees) == 1
    print employees[0].get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/Employees(PersonID=3)"
    print employees[0].get_firstname() == "Jacob"
    vip = company.get_vipcustomer()
    print vip.get_edit_link() == r"http://odatae2etest.azurewebsites.net/cpptest/DefaultService/VipCustomer"
    print vip.get_firstname() == "Bob"

def main():
    query_entityset()
    query_entity()
    top_level_query()
    create_entity()
    update_entity()
    delete_entity()

    query_contained_entity()
    create_contained_entity()
    create_contained_single_valued_entity()
    update_contained_entity()
    delete_contained_entity()
    query_contained_entities_with_query_options()
    level2_contained_entity()
    level2_noncontained_entity()
    derived_type_contained_entity()

    query_entity_collection()
    create_derived_type_entity()
    update_derived_type_entity()
    delete_derived_type_entity()
    query_derived_type_complex()
    update_derived_type_complex()
    create_derived_type_complex_in_entity()

    query_with_enum()
    update_with_enum()

    function_no_param_return_int()
    function_one_param_return_collection_entity()
    function_no_param_return_complex()
    function_import_no_param_return_collection_entity()
    action_function_import_two_param_return_collection_primitive()
    function_import_one_param_return_entity()
    action_one_param_return_enum()
    action_one_param_return_primitive()
    action_import_return_void()
    action_import_one_param_return_complex()
    action_one_param_return_entity()
    action_one_param_datetime_return_entity()

    query_navigation_collection()
    query_navigation_single()

    filter_option()
    orderby_option()
    select_option()
    expand_option()
    mixed_query_options()

    add_reference()
    update_reference()

    query_update_singleton()
    derived_type_singleton()
    singleton_with_navigation_properties()
    singleton_with_query_option()

if __name__ == '__main__':
    main()
