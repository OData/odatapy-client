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

import sys
from codegen_initializer import *
from codegen_writer import *

def main():
    if len(sys.argv) != 3 and len(sys.argv) != 5:
        print "Usage: python codegen_tools.py <ServiceURL> <ProxyFileName> [<Username> <Password>]"
        exit(-1)

    metadata_url = sys.argv[1]
    file_name = sys.argv[2]
    user_name = ''
    password = ''
    if len(sys.argv) > 3:
        user_name = sys.argv[3]
        password = sys.argv[4]

    initializer = codegen_initializer()
    initializer.begin_initialize(metadata_url, file_name, user_name, password)
    writer = codegen_writer(initializer)
    writer.begin_generate_file()

if __name__ == "__main__":
    main()
