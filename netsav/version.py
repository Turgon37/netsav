# -*- coding: utf8 -*-

# This file is a part of netsav
#
# Copyright (c) 2014-2015 Pierre GINDRAUD
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This file contain the program version and release notes

versions_notes :
  version 1.2 : 2015-02-11
    +change import path dir and fix error to put netsav program in a debian package
  version 1.1 : 2015-02-08
    +add a queue for store trigger event, allow more multiple client to make event simultaneous
      it(s now the server thread who run trig one by one
    +add setuid and setgid option to downgrade service privileges
  version 1.0 : 2015-01-29
    first release
"""
version = '1.2'
