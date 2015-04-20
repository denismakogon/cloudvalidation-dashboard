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

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from horizon import forms
from horizon import tables as horizon_tables

from cloudvalidation.ostf_jobs import forms as ostf_forms
from cloudvalidation.ostf_jobs import tables
from cloudvalidation.api import cloudv


class JobDescriptor(object):

    def __init__(self, job):
        self.id = job['id']
        self.name = job['name']
        self.description = job['description']
        self.status = job['status']
        self.tests = job['tests']
        self.report = job.get('report', [])
        if self.report:
            self.report_status = 'SUCCEEDED'
        else:
            self.report_status = ''
        for r in self.report:
            if r['result'] == 'Failed':
                self.report_status = 'FAILED'


class IndexView(horizon_tables.DataTableView):

    table_class = tables.OSTFJobTable
    template_name = 'ostf_jobs/templates/ostf_jobs/index.html'
    page_title = "OSTF Jobs"

    def get_data(self):
        resp = []
        jobs = cloudv.cloudvalidation_ostf_client().jobs.list()
        for job in jobs:
            resp.append(JobDescriptor(job))
        return resp


class JobDetailView(forms.ModalFormMixin, generic.TemplateView):

    template_name = "ostf_jobs/templates/ostf_jobs/job.html"
    page_title = "OSTF Job"

    def get_context_data(self, job_id=None):
        context = super(JobDetailView, self).get_context_data()
        job = cloudv.cloudvalidation_ostf_client().jobs.get(job_id)
        context['object'] = JobDescriptor(job)
        return context


class CreateView(forms.ModalFormView):
    form_class = ostf_forms.CreateForm
    modal_header = "Create Job"
    template_name = 'ostf_jobs/templates/ostf_jobs/create.html'
    submit_label = "Create Job"
    submit_url = "/cloudvalidation_portal/jobs/create/"
    cancel_url = "/cloudvalidation_portal/"
    success_url = "/cloudvalidation_portal/jobs/"
