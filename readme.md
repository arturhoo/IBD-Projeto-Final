IBD Projeto Final
=================

Install Instructions
--------------------

It is recommended to install VirtualEnv to deal with your packages

    sudo easy_install virtualenv

At you home directory create a new VirtualEnv

    virtualenv IBD
    . IBD/bin/activate

Install dependency packages

    sudo apt-get install libpq-dev python-dev

Install packages

    pip install psycopg2
