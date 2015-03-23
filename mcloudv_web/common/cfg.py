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

import os

from oslo_config import cfg

cloudvalidation_ostf_client_opts = [
    cfg.StrOpt("host", default=os.environ.get("MCLOUDV_HOST", "localhost")),
    cfg.IntOpt("port", default=os.environ.get("MCLOUDV_PORT", 8777)),
    cfg.StrOpt("api_version", default=os.environ.get("MCLOUDV_API", "v1"))
]

CONF = cfg.CONF

cloudvalidation_ostf_client = cfg.OptGroup("cloudvalidation_ostf_client",
                                           "Cloudvalidation OSTF client.")

CONF.register_group(cloudvalidation_ostf_client)
CONF.register_opts(cloudvalidation_ostf_client_opts,
                   cloudvalidation_ostf_client)
