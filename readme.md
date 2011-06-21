IBD Projeto Final
=================

This is the page for the final project on the Introduction to Data Bases
at DCC/UFMG by Artur Rodrigues and Leonardo Vilela

Install Instructions
--------------------

It is recommended to install VirtualEnv to deal with your packages

    sudo easy_install virtualenv

At you home directory create a new VirtualEnv and activate it

    virtualenv IBD
    . IBD/bin/activate

Install dependency packages

    sudo apt-get install libpq-dev python-dev python-imaging

Install packages

    pip install psycopg2

Next install and configure PostgreSQL if you haven't already done so:

    sudo apt-cache install postgresql
    sudo -u postgres psql postgres
    \password postgres
    (CTRL+D to exit)

Next you want to add a new user for this Django project and give it a
database inside your PostgreSQL installation

    sudo -u postgres createuser -P <name_of_the_user>
    sudo -u postgres psql
    CREATE DATABASE <name_of_the_db> OWNER <name_of_the_user>;
    (CTRL+D to exit)

Now it's time to configure your Django project local settings. Go to its
dir and

    cp local_settings.py.template local_settings.py

Configure it according to the PostgreSQL configuration you just went
through.

That should be it. Now it's time to run your test server:

    python manage.py runserver

This command will start Django's test server on port 8000, so that you
can see your development progress at http://localhost:8000/
