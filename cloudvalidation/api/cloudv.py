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

from cloudv_client import client as mcvclient
from cloudvalidation import cfg
from horizon.utils.memoized import memoized

CONF = cfg.CONF


@memoized
def cloudvalidation_ostf_client():
    host = CONF.cloudv_host
    port = CONF.cloudv_port
    api_version = CONF.cloudv_api_version
    return mcvclient.Client(host, port, api_version)
