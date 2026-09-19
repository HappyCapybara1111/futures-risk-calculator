# Futures Risk Calculator (Learning project)

A simple Python command-line tool for calculating:
- Maximum dollar risk per trade
- Risk per futures contract
- Theoretical maximum number of contracts

## Formula

Maximum dollar risk:
```text
account_size × risk_percent ÷ 100
```

Risk per contract:
```text
stop_loss_points × point_value
```

Theoretical maximum contracts:

```text
maximum_risk_dollars ÷ contract_risk
```

## Example input
```text
Account size: 25000
Risk per trade (%): 0.5
Enter your symbol: ES
Stop loss points: 5
Point value: 50
```

## Important note
This is a learning project only. It does not account for commissions, slippage, tick size, contract minimums, margin requirements, or other trading risks.
