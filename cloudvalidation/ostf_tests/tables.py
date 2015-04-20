from django import shortcuts
from django import http

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables
from horizon import messages

from cloudvalidation.api import cloudv


class CreateJob(tables.BatchAction):
    name = "create"
    verbose_name = "Create Job"
    classes = ("btn-launch",)
    icon = "plus"

    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Create job",
            u"Create jobs",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Create job",
            u"Created jobs",
            count
        )

    def handle(self, table, request, obj_ids):
        request.session['tests'] = obj_ids
        return shortcuts.redirect('/cloudvalidation_portal/jobs/create')


class ExecuteTest(tables.BatchAction):
    name = "execute"
    classes = ('btn-launch',)
    help_text = _("Execute test.")

    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Execute test",
            u"Execute tests",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Executed test",
            u"Executed tests",
            count
        )

    def action(self, request, datum_id):
        report = (cloudv.cloudvalidation_ostf_client().
                  tests.run(datum_id, "fuel_health"))[0]
        return report

    def handle(self, table, request, obj_ids):
        reports = []
        for id in obj_ids:
            report = self.action(reports, id)
            self.update(request, id)
            _test = ("Test %(test)s.\n"
                     "Duration: %(duration)s.\n"
                     "Result: %(result)s.\n"
                     "Report: %(report)s.\n" % report)
            reports.append(_test)
        response = http.HttpResponse(status=200, reason="OK")
        response['Content-Disposition'] = 'attachment; filename="reports"'
        response['Content-Type'] = 'application/octet-stream'

        view = ('Executed tests:'
                '\n%(tests)s\n'
                '\n%(reports)s\n')

        response.write(view % {"tests": "\n".join(obj_ids),
                               "reports": "\n".join(reports)})
        response.close()
        return response


class OSTFTable(tables.DataTable):
    test = tables.Column("test", verbose_name=_("Test"))

    def get_object_id(self, datum):
        return datum.test

    class Meta(object):
        name = "OSTF tests"
        verbose_name = _("OSTF tests")
        table_actions = (ExecuteTest, CreateJob)
        row_actions = (ExecuteTest, )
