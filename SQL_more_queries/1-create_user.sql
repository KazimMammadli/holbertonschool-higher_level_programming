-- Root user
-- Create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges
GRANT ALL PRIVILEGES on *.* TO 'user_0d_1'@'localhost';
