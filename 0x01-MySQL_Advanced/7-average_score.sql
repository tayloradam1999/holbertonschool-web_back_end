-- Creates stored procedure <ComputeAverageScoreForUser> that computes and stores the average score for a student.
-- Note: An average can hold a decimal.

-- ComputeAverageScoreForUser takes 1 parameter:
-- user_id: a <users.id> value
DELIMITER |
CREATE PROCEDURE ComputeAverageScoreForUser (
	IN user_id INT
)
BEGIN
	DECLARE total FLOAT;
	DECLARE count INT;
	DECLARE average FLOAT;
	SELECT SUM(score) INTO total FROM corrections WHERE corrections.user_id = user_id;
	SELECT COUNT(project_id) INTO count FROM corrections WHERE corrections.user_id = user_id;
	SET average = total / count;
	UPDATE users SET average_score = average WHERE id = user_id;
END |

DELIMITER ;
