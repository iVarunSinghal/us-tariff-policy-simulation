SELECT 
    tf.year,
    c.country_name,
    tf.hs_code AS hs_chapter,
    s.scenario_name,
    so.tariff_rate,
    (tf.trade_value_usd / NULLIF(tf.net_weight_kg, 0)) AS fob_value_per_kg,
    -- CIF = FOB * 1.04 (Estimated 3.5% freight + 0.5% insurance)
    ((tf.trade_value_usd / NULLIF(tf.net_weight_kg, 0)) * 1.04) AS cif_value_per_kg,
    -- Calculate MPF (0.3464%) and HMF (0.125%)
    (((tf.trade_value_usd / NULLIF(tf.net_weight_kg, 0)) * 1.04) * (so.tariff_rate + 0.003464 + 0.00125)) AS duties_and_fees_per_kg
FROM trade_flows tf
JOIN countries c ON tf.partner_code = c.country_code
CROSS JOIN scenarios s
JOIN scenario_overrides so ON s.scenario_id = so.scenario_id 
    AND (so.country_code = c.country_code OR so.country_code = 'ALL')
    AND (so.hs_chapter = tf.hs_code OR so.hs_chapter = 'ALL')
WHERE tf.year = 2024 AND tf.flow_type = 'M'
ORDER BY tf.hs_code, c.country_name, s.scenario_id;