===========================
Mirantis Cloudvalidation UI
===========================

To install this application you have to do next::

   $ git clone https://github.com/openstack/horizon.git

   Once you do have cloned Horizon you need to do edit next lines in openstack_dashboard/setting.py:

   OPENSTACK_KEYSTONE_URL = "http://A:5000/v2.0/"

   where A is your cloud Keystone public IP endpoint

   Add next line into TEMPLATE_DIRS

   os.path.join(ROOT_PATH, '../cloudvalidation')

   Edit next lines

    import cloudvalidation.enabled
    from openstack_dashboard.utils import settings

    INSTALLED_APPS = list(INSTALLED_APPS)  # Make sure it's mutable
    settings.update_dashboards(
        [
            cloudvalidation.enabled,
        ],
        HORIZON_CONFIG,
        INSTALLED_APPS,
    )
    INSTALLED_APPS[0:0] = ADD_INSTALLED_APPS

    Also please add:

    ALLOWED_HOST = "0.0.0.0"

    or

    DEBUG = True


Once you have done this, please proceed with next commands:

   $ pip install git+https://github.com/stackforge/cloudv-ostf-adapter.git
   $ pip install git+https://github.com/denismakogon/cloudvalidation-dashboard.git


Once you've installed all applications you will have available next command:

    cloudvalidation-web

NOTE: This is a wrapper for Django-based manage.py

To run server you need this:

    cloudvalidation-web runserver 0.0.0.0:8000
