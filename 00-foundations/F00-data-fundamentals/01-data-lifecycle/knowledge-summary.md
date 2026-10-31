# F00.01 — Data Lifecycle: Knowledge Summary

## Learning objectives
- Explain the stages of a data lifecycle.
- Distinguish event-level records from order-level records.
- Explain raw versus curated datasets and basic quality controls.
- Separate Data Engineering responsibilities from Data Analytics responsibilities.

## Core concepts
**Data lifecycle** describes how data is generated, ingested, stored, processed, served/analyzed, and retained, archived, or deleted. The order varies by architecture: transformation can occur before or after storage.

**Data Engineering** builds and operates reliable ingestion, storage, transformation, and serving systems. **Data Analytics** defines business questions and metrics, analyzes datasets, and communicates findings with appropriate caveats.

**Raw data** preserves source records and useful metadata for auditing/reprocessing, subject to access controls and retention rules. **Curated data** is validated and transformed for specific consumers and documented business definitions.

**Data grain** is what one row represents. One row per order event differs from one row per order. Multiple events with the same order ID may be valid; deduplication requires an event identity or clear source/business rules.

**Data quality** includes completeness, validity, uniqueness (at the defined grain), consistency, timeliness, and accuracy. Tests and monitoring should cover important assumptions.

## Worked example
An order O101 has `completed` event E01 for 500,000 VND and a retried copy E03; O102 has `completed` for 300,000 VND then `refunded` for 300,000 VND; O103 is `cancelled` before completion. If E03 is confirmed to be a retry and refunds are full, illustrative net revenue is **500,000 VND**. Never simply sum all event amounts. Actual revenue reporting depends on agreed accounting and business definitions.

## Design questions before writing SQL
1. What does each row represent (grain)?
2. What is the source and event identity?
3. Which timestamps or versions determine ordering?
4. What business rules define the metric?
5. What quality, security, and retention requirements apply?

## Common pitfalls
- Assuming repeated `order_id` always means duplicate.
- Assuming larger event IDs imply later event time.
- Deleting raw data without retention/recovery considerations.
- Summing event amounts as if every event were a sale.
- Defining revenue without specifying refunds and reporting period.

## Completion criteria
Theory assessment ≥8/10, guided exercise checked, artifacts reviewed, commit pushed.
