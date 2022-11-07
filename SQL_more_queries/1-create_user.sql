-- creates the MySQL server user The user_0d_1 password should be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- privileges
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
FLUSH PRIVILEGES;
