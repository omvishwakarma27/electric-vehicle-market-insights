-- Run these against the SQLite table named ev_market.

SELECT COUNT(*) AS total_records,
       COUNT(DISTINCT manufacturer) AS unique_manufacturers,
       COUNT(DISTINCT model_name) AS unique_models
FROM ev_market;

SELECT manufacturer, COUNT(*) AS vehicle_records
FROM ev_market
GROUP BY manufacturer
ORDER BY vehicle_records DESC
LIMIT 10;

SELECT market_region,
       ROUND(SUM(annual_sales_units), 0) AS total_annual_sales_units
FROM ev_market
GROUP BY market_region
ORDER BY total_annual_sales_units DESC;

SELECT category,
       ROUND(AVG(price_usd), 2) AS average_price_usd,
       ROUND(AVG(range_km), 2) AS average_range_km,
       COUNT(*) AS records
FROM ev_market
GROUP BY category
ORDER BY records DESC;

SELECT
  SUM(CASE WHEN manufacturer IS NULL OR TRIM(manufacturer) = '' THEN 1 ELSE 0 END) AS missing_manufacturer,
  SUM(CASE WHEN price_usd IS NULL THEN 1 ELSE 0 END) AS missing_price,
  SUM(CASE WHEN range_km IS NULL THEN 1 ELSE 0 END) AS missing_range,
  SUM(CASE WHEN annual_sales_units IS NULL THEN 1 ELSE 0 END) AS missing_sales
FROM ev_market;
