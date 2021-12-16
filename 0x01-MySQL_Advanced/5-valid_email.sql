-- Creates a trigger that resets the attribute <valid_email> when then <email> has been changed.
CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users.email
FOR EACH ROW UPDATE users
SET valid_email = 0
WHERE email != NEW.email;
