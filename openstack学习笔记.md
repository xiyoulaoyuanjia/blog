**How to generate po files**

[原文](https://groups.google.com/forum/?fromgroups#!topic/django-users/z0CkpD6nnMU)

    apt-get install gettext
    set DJANGO_SETTINGS_MODULE=settings.py
    cd /opt/stack/horizon/openstack_dashboard
    django_admin.py makemessages
