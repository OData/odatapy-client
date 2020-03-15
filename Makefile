all: _odata_client_python.so

# python3x below

odata_client_python_wrap.o: odata_client_python_linux_wrap.cxx
	$(CXX) $< -o $@ -c -g -fPIC -shared -std=c++11 -fno-strict-aliasing -O2 -I/usr/include/python3.6 -Iodatacpp/include -I/usr/include/openssl -I/usr/include/libxml2 

_odata_client_python.so: odata_client_python_wrap.o
	$(CXX) $< -o $@ -g -shared -Lodatacpp/output -L/usr/lib/x86_64-linux-gnu -lodata-client -lpython3.6m -lcpprest -lboost_system -lssl -lcrypto

clean:
	rm -f _odata_client_python.so odata_client_python_wrap.o

# to test: 
# 1.	get a proper url go to https://services.odata.org/v4/TripPinServiceRW
# 2. 	replace the url in the below call
test:
	LD_LIBRARY_PATH=${PWD}/odatacpp/output python3.6 codegen_tools.py 'https://services.odata.org/v4/(S(sbe2f21zvvhp33ytwqndereb))/TripPinServiceRW/' TripPin

## pyhon3.x

# python2.7 below

#odata_client_python_wrap.o: odata_client_python_linux_wrap.cxx
#	$(CXX) $< -o $@ -c -g -fPIC -shared -std=c++11 -fno-strict-aliasing -O2 -I/usr/include/python2.7 -Iodatacpp/include -I/usr/include/openssl -I/usr/include/libxml2 

#_odata_client_python.so: odata_client_python_wrap.o
#	$(CXX) $< -o $@ -g -shared -Lodatacpp/output -L/usr/lib/x86_64-linux-gnu -lodata-client -lpython2.7 -lcpprest -lboost_system -lssl -lcrypto

#clean:
#	rm -f _odata_client_python.so odata_client_python_wrap.o

# to test: 
# 1.    get a proper url go to https://services.odata.org/v4/TripPinServiceRW
# 2.    replace the url in the below call
#test:
#	LD_LIBRARY_PATH=${PWD}/odatacpp/output python2.7 codegen_tools.py 'https://services.odata.org/v4/(S(sbe2f21zvvhp33ytwqndereb))/TripPinServiceRW/' TripPin

## python2.7
