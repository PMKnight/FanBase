-- settings.sql
CREATE DATABASE fanbase;
CREATE USER fanbaseuser WITH PASSWORD 'fanbase';
GRANT ALL PRIVILEGES ON DATABASE fanbase TO fanbaseuser;