-- Function that divdes and returns the first number by the second number or 0 if the second number is 0
-- @param a: first number
-- @param b: second number
-- @return: the first number divided by the second number or 0 if the second number is 0
DELIMITER |
CREATE FUNCTION SafeDiv (
	a INT,
	b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END |

DELIMITER ;
