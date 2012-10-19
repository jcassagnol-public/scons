#!/usr/bin/env python
#
# __COPYRIGHT__
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__revision__ = "__FILE__ __REVISION__ __DATE__ __DEVELOPER__"

"""
Test the ability to configure the $TARGET_ARCH construction variable.
"""

import TestSCons
import sys

_python_ = TestSCons._python_

test = TestSCons.TestSCons()

if sys.platform != 'win32':
    msg = "Skipping Visual C/C++ test on non-Windows platform '%s'\n" % sys.platform
    test.skip_test(msg)

test.write('SConstruct', """
env_64 = Environment(tools=['default', 'msvc'],
                  TARGET_ARCH = 'amd64')
env_32 = Environment(tools=['default', 'msvc'],
                  TARGET_ARCH = 'x86')
""" % locals())

test.run(arguments = ".")

# test.pass_test()

test.write('SConstruct', """
env_xx = Environment(tools=['default', 'msvc'],
                  TARGET_ARCH = 'nosucharch')
""" % locals())

test.run(arguments = ".", status=2, stderr=None)
test.must_contain_any_line(test.stderr(), "Unrecognized target architecture")
test.must_contain_any_line(test.stderr(), "Valid architectures")

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
