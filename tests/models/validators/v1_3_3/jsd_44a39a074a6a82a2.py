# -*- coding: utf-8 -*-
"""DNA Center Get Events data model.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidator44A39A074A6A82A2(object):
    """Get Events request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator44A39A074A6A82A2, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "items": {
                "properties": {
                "category": {
                "description":
                "Category",
                "type": [
                "string",
                "null"
                ]
                },
                "description":
                 {
                "description":
                "Description",
                "type": [
                "string",
                "null"
                ]
                },
                "details": {
                "description":
                "Details",
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "domain": {
                "description":
                "Domain",
                "type": [
                "string",
                "null"
                ]
                },
                "eventId": {
                "description":
                "Event Id",
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "description":
                "Name",
                "type": [
                "string",
                "null"
                ]
                },
                "nameSpace": {
                "description":
                "Name Space",
                "type": [
                "string",
                "null"
                ]
                },
                "severity": {
                "type": [
                "number",
                "null"
                ]
                },
                "subDomain": {
                "description":
                "Sub Domain",
                "type": [
                "string",
                "null"
                ]
                },
                "subscriptionTypes": {
                "description":
                "Subscription Types",
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "tags": {
                "description":
                "Tags",
                "items": {
                "type": [
                "string",
                "null",
                "object"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "type": {
                "description":
                "Type",
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
                "description":
                "Version",
                "type": [
                "string",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": "array"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )