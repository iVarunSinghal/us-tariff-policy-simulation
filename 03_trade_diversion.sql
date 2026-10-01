WITH annual_totals AS (
    SELECT year, hs_code AS hs_chapter, SUM(trade_value_usd) AS total_import_value
    FROM trade_flows
    WHERE flow_type = 'M'
    GROUP BY year, hs_code
)
SELECT 
    tf.year,
    c.country_name,
    tf.hs_code AS hs_chapter,
    tf.trade_value_usd AS import_value,
    ROUND((tf.trade_value_usd / at.total_import_value) * 100, 2) AS market_share_pct
FROM trade_flows tf
JOIN countries c ON tf.partner_code = c.country_code
JOIN annual_totals at ON tf.year = at.year AND tf.hs_code = at.hs_chapter
WHERE tf.flow_type = 'M'
ORDER BY tf.hs_code, tf.year, import_value DESC;