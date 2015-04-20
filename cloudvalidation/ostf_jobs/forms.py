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

from horizon import forms

from cloudvalidation.api import cloudv


class CreateForm(forms.SelfHandlingForm):
    name = forms.CharField(max_length=255, label="Job Name",
                           required=True)
    description = forms.CharField(max_length=255, widget=forms.Textarea(
        attrs={'class': 'modal-body-fixed-width', 'rows': 4}),
        label="Description", required=True)

    def handle(self, request, data):
        job = cloudv.cloudvalidation_ostf_client().jobs.create(
            data['name'],
            data['description'],
            request.session.pop('tests'))
        return job
