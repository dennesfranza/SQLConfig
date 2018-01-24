# SQLConfig
Create SQL config file

This simple program creates sql configuration string.
I am working on a python base project and it requires me to connect to multiple database.
(MariaDB and MSSQL)

And I need an SQL connection string to configure database connection base on DB credentials.

How to use:

$ chmod u+x createSQLConfig.py

$ sudo cp createSQLConfig.py /usr/local/bin

$ createSQLConfig.py -h

Usage: createSQLconfig.py [options]

Options:
  
  -h, --help            show this help message and exit

  -d DRIVER, --driver=DRIVER

  -b DATABASE, --db=DATABASE

  -o HOST, --host=HOST  

  -u USER, --user=USER  

  -p PASSWORD, --pass=PASSWORD

  -f FILENAME, --file=FILENAME

Outputs config.json file with values encrypted using Fernet.
Store key somewhere else.
