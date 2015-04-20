from django.utils.translation import ugettext_lazy as _

import horizon


class CloudvalidationGroup(horizon.PanelGroup):
    slug = "Cloudvalidation Center"
    name = _("Cloudvalidation Center")
    panels = ('ostf_tests', 'ostf_jobs')


class Cloudvalidation(horizon.Dashboard):
    name = _("Cloudvalidation Portal")
    slug = "cloudvalidation_portal"
    panels = (CloudvalidationGroup, )
    default_panel = 'OSTF Tests'


horizon.register(Cloudvalidation)
