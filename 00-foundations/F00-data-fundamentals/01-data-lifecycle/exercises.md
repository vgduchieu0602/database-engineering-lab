# F00.01 — Guided Exercise

## Dataset

| event_id | order_id | amount | status |
|---|---|---:|---|
| E01 | O101 | 500000 | completed |
| E02 | O102 | 300000 | completed |
| E03 | O101 | 500000 | completed |
| E04 | O103 | 200000 | cancelled |
| E05 | O102 | 300000 | refunded |

Assumptions: E03 is a retry of E01, not a new sale; E05 is a full refund; O103 was never completed. Ignore tax and fees.

## Guided steps
1. **Identify grain:** Each row is an order event, not a unique order.
2. **Group by order:** O101 has two events, O102 has two, O103 has one.
3. **Classify events:** E03 is a duplicate delivery; E05 is a legitimate refund event.
4. **Apply business rules:** O101 contributes 500000; O102 contributes 300000 - 300000 = 0; O103 contributes 0.
5. **Reconcile:** Total illustrative net revenue = 500000.

## Your turn
Explain in your own words why E03 and E05 must be treated differently. Then describe one data-quality check that would catch an accidental double count of E03.

## Evidence to commit
- `knowledge-summary.md` (reference concepts)
- `examples.md` (walkthrough and diagram)
- `exercises.md` (prompt, guided steps, your written answer)

## Acceptance criteria
The learner can identify the row grain, distinguish retries from valid state changes, and justify the metric under the stated assumptions. Assessment and Git commit still pending.
