-- 1. View of trade exposure by country and chapter
CREATE OR REPLACE VIEW vw_trade_exposure AS
SELECT 
    c.country_name,
    c.region,
    tf.hs_code AS hs_chapter,
    tf.year,
    tf.trade_value_usd,
    ROUND(tf.trade_value_usd / 1e9, 2) AS trade_value_billions_usd
FROM trade_flows tf
JOIN countries c ON tf.partner_code = c.country_code;

-- 2. View showing scenario tariff rates per country and product
CREATE OR REPLACE VIEW vw_scenario_tariffs AS
SELECT 
    s.scenario_name,
    s.is_baseline,
    so.country_code,
    COALESCE(c.country_name, 'All Partners') AS country_name,
    so.hs_chapter,
    so.tariff_rate,
    ROUND(so.tariff_rate * 100, 2) AS tariff_rate_pct
FROM scenarios s
JOIN scenario_overrides so ON s.scenario_id = so.scenario_id
LEFT JOIN countries c ON so.country_code = c.country_code;