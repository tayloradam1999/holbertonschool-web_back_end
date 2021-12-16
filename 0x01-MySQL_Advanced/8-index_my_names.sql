-- Creates index <idx_name_first> on the table <names> and the first letter of <name>
--
-- Only the first letter of <name> is indexed.
CREATE INDEX idx_name_first ON names (name(1));
