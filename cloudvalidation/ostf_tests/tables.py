from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy

from horizon import tables


class ExecuteTest(tables.BatchAction):
    name = "execute"
    classes = ('btn-launch',)
    help_text = _("Execute set of tests.")

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


class OSTFTable(tables.DataTable):
    test = tables.Column("test", verbose_name=_("Test"))
    duration = tables.Column("duration", verbose_name=_("Duration"))
    result = tables.Column("result", verbose_name=_("Result"))
    report = tables.Column("report", verbose_name=_("Report"))

    def get_object_id(self, datum):
        return datum.test

    class Meta(object):
        name = "OSTF tests"
        verbose_name = _("OSTF tests")
        table_actions = (ExecuteTest, )
        raw_actions = (ExecuteTest, )
