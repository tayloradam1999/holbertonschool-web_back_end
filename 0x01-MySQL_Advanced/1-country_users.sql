-- creates a table <users>. if it already exists, does not fail.
-- can be executed on any database
CREATE TABLE if NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US'
);
