-- Creates a view <need_meeting> that lists all students that
-- have a score under 80 (strict) and no <last_meeting> for more than 1 month.
--
-- the view <need_meeting> should return all student names when:
-- - the student has a score under 80 (strict)
-- - the student has no <last_meeting> for more than 1 month
CREATE VIEW need_meeting AS
SELECT s.name
FROM students s
WHERE s.score < 80
AND NOT EXISTS (
	SELECT s.last_meeting FROM students s
	WHERE s.last_meeting > DATE_SUB(NOW(), INTERVAL 1 MONTH)
)
