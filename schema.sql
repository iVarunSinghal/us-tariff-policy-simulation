DROP TABLE IF EXISTS scenario_overrides CASCADE;
DROP TABLE IF EXISTS scenarios CASCADE;
DROP TABLE IF EXISTS tariff_events CASCADE;
DROP TABLE IF EXISTS tariff_schedule CASCADE;
DROP TABLE IF EXISTS trade_flows CASCADE;
DROP TABLE IF EXISTS countries CASCADE;

CREATE TABLE countries (
    country_code VARCHAR(3) PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    region VARCHAR(50),
    is_key_partner BOOLEAN DEFAULT FALSE
);

CREATE TABLE trade_flows (
    id SERIAL PRIMARY KEY,
    reporter_code VARCHAR(3) DEFAULT '842',
    partner_code VARCHAR(3) REFERENCES countries(country_code),
    hs_code VARCHAR(10) NOT NULL,
    year INTEGER NOT NULL,
    flow_type CHAR(1) DEFAULT 'M',
    trade_value_usd NUMERIC(20, 2),
    net_weight_kg NUMERIC(20, 2),
    UNIQUE (reporter_code, partner_code, hs_code, year, flow_type)
);

CREATE TABLE tariff_schedule (
    id SERIAL PRIMARY KEY,
    hts_code VARCHAR(12) UNIQUE,
    description TEXT,
    hts_chapter CHAR(2),
    mfn_rate NUMERIC(8, 4),
    special_rate TEXT,
    column2_rate NUMERIC(8, 4)
);

CREATE TABLE tariff_events (
    id SERIAL PRIMARY KEY,
    event_name VARCHAR(200),
    legal_authority VARCHAR(100),
    country_code VARCHAR(10),
    hs_chapters VARCHAR(100),
    additional_rate NUMERIC(8, 4),
    effective_date DATE,
    end_date DATE,
    note TEXT
);

CREATE TABLE scenarios (
    scenario_id SERIAL PRIMARY KEY,
    scenario_name VARCHAR(200) UNIQUE,
    description TEXT,
    is_baseline BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE scenario_overrides (
    override_id SERIAL PRIMARY KEY,
    scenario_id INTEGER REFERENCES scenarios(scenario_id) ON DELETE CASCADE,
    country_code VARCHAR(10),
    hs_chapter VARCHAR(10),
    tariff_rate NUMERIC(8, 4),
    note TEXT
);

CREATE INDEX idx_trade_flows_year ON trade_flows(year);
CREATE INDEX idx_trade_flows_partner ON trade_flows(partner_code);
CREATE INDEX idx_trade_flows_hs ON trade_flows(hs_code);
CREATE INDEX idx_tariff_events_country ON tariff_events(country_code);