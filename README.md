# LA

Welcome! Follow the steps below to get the app up and running:

1.) Use the following commands to install the requirements:
    * pip install flask 
    * pip install flask_sqlalchemy

2.) in your local postgres, create a db named "transactiondb" and a table in the db named "transactions" using the following commands:

    CREATE DATABASE transactiondb;

    CREATE TABLE transactions (
      created_at timestamp,
      updated_at timestamp,
      deleted_at timestamp,
      id bigint PRIMARY KEY,
      amount decimal,
      type VARCHAR ( 64 ),
      parent_id bigint
    );

3.) That's it! Finally just use "python3 app.py" to get the app running and hit the APIs using the base url as : "http://127.0.0.1:5000/"
