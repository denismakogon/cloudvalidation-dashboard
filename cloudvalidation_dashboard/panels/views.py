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

from django.utils.translation import ugettext_lazy as _
from horizon import tables

from cloudvalidation_dashboard.external_api import cloudvalidation_ostf_adapter
from cloudvalidation_dashboard.tables import ostf_table


class IndexView(tables.DataTableView):
    table_class = ostf_table.OSTFTable
    template_name = 'cloudvalidation_dashboard/panels/index.html'
    page_title = _("Tests")

    def get_data(self):
        tests = (cloudvalidation_ostf_adapter.cloudvalidation_ostf_client().
                 suites.list_tests_for_suites('fuel_health'))
        return tests
