===========================
Mirantis Cloudvalidation UI
===========================

To install this application you have to do next::

  $ git clone https://github.com/openstack/horizon.git
  $ cd horizon; virtualenv .venv; source .venv/bin/activate;
  $ wget https://raw.githubusercontent.com/denismakogon/cloudvalidation-dashboard/master/cloudvalidation/settings.py -O openstack_dashboard/settings.py
  $ python setup.py install;
  $ pip install git+https://github.com/denismakogon/cloudvalidation-dashboard.git;
  $ pip install git+https://github.com/stackforge/cloudv-ostf-adapter.git

Once installation procedure is completed you will need to set next operating system variables::

  OS_AUTH_URL=http://A:5000/v2.0/
  MCLOUDV_HOST=B
  MCLOUDV_PORT=C
  MCLOUDV_API=D

  where:
   A - OpenStack's Keystone host
   B - Cloudvalidation server host, localhost is default
   C - Cloudvalidation server port, 8777 is default
   D - Cloudvalidation server API, v1 default

Once you've installed all applications you will have available next command::

    cloudvalidation-web

NOTE: This is a wrapper for Django-based manage.py

To run server you need this::

    cloudvalidation-web runserver 0.0.0.0:8000


