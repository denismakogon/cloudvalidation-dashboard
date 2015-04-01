#    Copyright 2015 Mirantis, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from horizon import tables as horizon_tables

from cloudvalidation.ostf_tests import tables
from cloudvalidation.api import cloudv


class TestDescriptor(object):

    def __init__(self, test, report):
        self._report = report
        self.test = test
        self.report = report['report']
        self.duration = report['duration']
        self.result = report['result']


class IndexView(horizon_tables.DataTableView):

    table_class = tables.OSTFTable
    template_name = 'ostf_tests/templates/ostf_tests/index.html'
    page_title = "OSTF tests"

    def get_data(self):
        resp = []
        tests = (cloudv.cloudvalidation_ostf_client().
                 suites.list_tests_for_suites('fuel_health'))['tests']
        for test in tests:
            report = {
                "report": '',
                "duration": "0.0s",
                "result": "-"
            }
            resp.append(TestDescriptor(test, report))
        return resp
