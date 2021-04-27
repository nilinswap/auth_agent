recreatedb(){


    # recreate testlhdb and make it like lhdb
    psql -h localhost -U postgres -c 'DROP DATABASE IF EXISTS template_database;'
    psql -h localhost -U postgres -c 'CREATE DATABASE template_database' template1

    # run migrations on lhdb
    pushd2 /src/backend/dbhandler/lhmodel
    python manage.py migrate
    popd2
}