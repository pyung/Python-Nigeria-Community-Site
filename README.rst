python_nigeria_site
===================

A short description of the project.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: GPLv3


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Setting up the repo for development
-----------------------------------
1. Ensure that you have Postgres installed on your system. Visit [Postgres Download Section](https://www.postgresql.org/download/) to download postgres for your respective operating system.
2. Ensure you have `Python 3.6` installed by running the following in your terminal::
    
    $ python3 --version
    
3. Install [docker](https://www.docker.com/get-docker) _(though optional, it is essential for ease in setting up the mail server)_ for your respective operating system
4. Open a new directory and clone the project::
    
    $ git clone https://github.com/pyung/Python-Nigeria-Community-Site.git pncs
    # Ensure you switch to the `develop` branch
    $ git checkout develop
    
5. Create a virtual environment in the same directory as the root of the project::
    
    $ virtualenv -p `which python3.6` venv $ source venv/Scripts/activate # on Linux or Mac **source venv/bin/activate**
    $ pip install -r requirements/local.txt
    
6. Create a database for the application::
    
    $ docker-compose -f local.yml up -d postgres mailhog

    # Create a startup script file to load up all the environment variables that would be used
    $ nano .env # for Linux or Mac Users

    # Run the .env script $ source .env

    # Migrate all the settings $ python manage.py migrate
    
7. Start the application::
    
    $ python manage.py runserver
    


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

.. _mailhog: https://github.com/mailhog/MailHog

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``




Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



