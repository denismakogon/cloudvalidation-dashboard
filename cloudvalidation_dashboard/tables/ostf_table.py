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
from django.utils.translation import ungettext_lazy

from horizon import tables

from cloudvalidation_dashboard.external_api import cloudvalidation_ostf_adapter


class ExecuteTest(tables.BatchAction):
    name = "execute"
    classes = ('btn-confirm',)
    help_text = _("Execute single test.")

    @staticmethod
    def action_present():
        return ungettext_lazy(
            u"Execute test",
            u"Execute tests"
        )

    @staticmethod
    def action_past():
        return ungettext_lazy(
            u"Executed test",
            u"Executed tests"
        )

    def action(self, request, datum_id):
        return (cloudvalidation_ostf_adapter.
                cloudvalidation_ostf_client().tests.run(
                datum_id, 'fuel_health'))


class OSTFTable(tables.DataTable):
    name = tables.Column("test", verbose_name=_("Test"))
    report = tables.Column("report", verbose_name=_("Report"))

    class Meta(object):
        name = "OSTF tests"
        verbose_name = _("OSTF tests")
        # row_actions = (ExecuteTest, )
