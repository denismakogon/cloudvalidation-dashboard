from django.utils.translation import ugettext_lazy as _

import horizon

from cloudvalidation.ostf_tests import panel_group


class Cloudvalidation(horizon.Dashboard):
    name = _("Cloudvalidation Portal")
    slug = "cloudvalidation_portal"
    panels = (panel_group.CloudvalidationGroup, )
    default_panel = 'OSTF Tests'


horizon.register(Cloudvalidation)
