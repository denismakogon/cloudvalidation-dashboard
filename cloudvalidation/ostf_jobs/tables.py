from django import shortcuts
from django import http

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables
from horizon import messages

from cloudvalidation.api import cloudv


class ExecuteJob(tables.BatchAction):
    name = "execute"
    classes = ('btn-launch',)
    help_text = _("Execute job.")

    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Execute job",
            u"Execute jobs",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Executed job",
            u"Executed jobs",
            count
        )

    def action(self, request, datum_id):
        report = (cloudv.cloudvalidation_ostf_client().
                  jobs.execute(datum_id))


class ViewJob(tables.LinkAction):
    name = "view"
    verbose_name = "View report"
    classes = ("ajax-modal",)

    def get_link_url(self, datum):
        return datum.id


class DeleteJob(tables.DeleteAction):
    name = "delete"
    classes = ('btn-launch',)
    help_text = _("Delete job.")

    @staticmethod
    def action_present(count):
        return ungettext_lazy(
            u"Delete job",
            u"Delete jobs",
            count
        )

    @staticmethod
    def action_past(count):
        return ungettext_lazy(
            u"Deleted job",
            u"Deleted jobs",
            count
        )

    def delete(self, request, datum_id):
        report = (cloudv.cloudvalidation_ostf_client().
                  jobs.delete(datum_id))
        return report


class OSTFJobTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"))
    description = tables.Column("description",
                                verbose_name=_("Descripton"))
    status = tables.Column("status", verbose_name=_("Status"))
    report = tables.Column("report_status", verbose_name=_("Report"))

    def get_object_id(self, datum):
        return datum.id

    class Meta(object):
        name = "jobs"
        verbose_name = _("jobs")
        table_actions = (ExecuteJob, DeleteJob)
        row_actions = (ExecuteJob, ViewJob, DeleteJob)
