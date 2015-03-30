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

import uuid

from horizon import tables as horizon_tables

from cloudvalidation.ostf_tests import tables
from cloudvalidation.api import cloudv


class TestDescriptor(object):

    def __init__(self, test, report):
        self._report = report
        self.id = str(uuid.uuid4())
        self.test = test
        self.report = report['report']
        self.duration = report['duration']
        self.result = report['result']


class IndexView(horizon_tables.DataTableView):

    table_class = tables.OSTFTable
    template_name = 'ostf_tests/templates/ostf_tests/index.html'
    page_title = "OSTF tests"
    reports = []

    def build_view_for_executed(self, reports):
        tests = []
        for report in reports:
            _report = TestDescriptor(report['test'], report)
            tests.append(_report)
        return tests

    def get_request_action(self):
        action = [a for a in self.request.body.split("&")
                  if a.startswith("action")]
        return action[0] if action else ""

    def execute_and_report(self):
        reports = []
        tests = [a.split("=")[-1].replace("%3A", ":")
                 for a in self.request.body.split("&")
                 if a.startswith("object_id")]
        for test in tests:
            report = (cloudv.cloudvalidation_ostf_client().
                      tests.run(test, "fuel_health"))[0]
            reports.append(report)
        return self.build_view_for_executed(reports)

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

    def post(self, request, *args, **kwargs):
        self._data = {self.get_table()._meta.name:
                      self.execute_and_report()}
        return self.get(request, *args, **kwargs)
