# Welcome to ODataPy
ODataPy is an open-source Python library that implements the Open Data Protocol (OData). It supports the [OData protocol version 4.0](http://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html). It is built on top of ODataCpp using language binding. It is under development and currently serves only parts of client and client side proxy generation (code gen) aspects of OData.

# Getting started

## Getting the source

    git clone https://odatateam.visualstudio.com/DefaultCollection/_git/odatapy

## Getting ODataCpp and building

1.Download the source code of [ODataCpp](https://github.com/OData/odatacpp) and save it at 'odatacpp\' under the ODataPy folder.

2.Build the Win32 Release version of ODataCpp.

3.Set the following environment variables to your Python install location, such as:

    SET PYTHON_INCLUDE=C:\python27\include
    SET PYTHON_LIB=C:\python27\libs\python27.lib

4.Run buildall.bat in VS2012 Command Prompt to build the library for ODataPy

## Running tests

After building the library, you can run the end-to-end tests to check the basic functionality.

1.Test the raw client:

    python raw_client_e2e_test.py

2.Test the generated client:

    python codegen_e2e_test.py

# Your first ODataPy app

## Generate the client side proxy of the target service

Navigate to the folder of ODataPy and run the code generation tool to generate the proxy.

    python codegen_tools.py <ServiceURL> <ProxyFileName> [<Username> <Password>]

<ServiceURL> is the URL of the service document of the target OData service.
<ProxyFileName> is the name you want for the .py file of the proxy code.
<Username> and <Password> are the credential for accessing the service in case it requires authentication.

In this tutorial, we want to build a client application for the TripPin service published on [www.odata.org](http://www.odata.org/odata-services/) and it doesn't require authentication, so the command is:

    python codegen_tools.py http://services.odata.org/v4/TripPinServiceRW TripPin

and we get TripPin.py.

## Create a client app in Python

Type in the following code:

    import TripPin

    path = r"http://services.odata.org/V4/(S(b4zxbbluog0mjnooyavzfcim))/TripPinServiceRW/"
    context = TripPin.DefaultContainer(path)
    context.ResetDataSource()
    airports = context.query_airports()
    for airport in airports:
        print airport.get_name()

Save it as "sample.py", and run it!
