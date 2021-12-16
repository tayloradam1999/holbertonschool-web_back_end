-- Creates an index <idx_name_first_score> on the table <names> and the first letter of <name> and the score.

-- Only the first letter of <name> AND the score is indexed.
CREATE INDEX idx_name_first_score ON names (name(1), score);
