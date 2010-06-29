

#
# soaplib - Copyright (C) 2009 Aaron Bickell, Jamie Kirkpatrick
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

import unittest
import soaplib
_ns_xs = soaplib.nsmap['xs']
_ns_xsi = soaplib.nsmap['xsi']

from soaplib.service import ServiceBase
from soaplib.service import rpc

from soaplib.serializers.enum import Enum

DaysOfWeekEnum = Enum(
    'Monday',
    'Tuesday',
    'Wednesday',
    'Friday',
    'Saturday',
    'Sunday',
    type_name = 'DaysOfWeekEnum'
)

class TestService(ServiceBase):
    @rpc(DaysOfWeekEnum, _returns=DaysOfWeekEnum)
    def remote_call(self, day):
        return DaysOfWeekEnum.Sunday

class TestEnum(unittest.TestCase):
    def test_wsdl(self):
        TestService().wsdl('punk')

    def test_serialize(self):
        mo = DaysOfWeekEnum.Monday

        elt = DaysOfWeekEnum.to_xml(mo)

        raise Exception("test something :)")

def suite():
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(TestEnum)

if __name__== '__main__':
    unittest.TextTestRunner().run(suite())
