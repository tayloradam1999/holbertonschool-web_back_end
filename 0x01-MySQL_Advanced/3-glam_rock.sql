-- Lists all bands with `Glam rock` as their main style, ranked by their longevity.
-- Column names are <band_name> and <lifespan> (in years).
-- Uses formed and split for computing lifespan
-- Can execute on any database.
SELECT
	band_name,
	IFNULL(split, 2020) - formed AS lifespan
FROM
	metal_bands
WHERE
	FIND_IN_SET('Glam rock', style)
ORDER BY
	lifespan DESC;
