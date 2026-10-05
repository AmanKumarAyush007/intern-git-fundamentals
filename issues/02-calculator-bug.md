---
title: "Bug: add() returns the wrong result"
labels: bug
---

## Summary

`app.calculator.add` subtracts instead of adding.

## Steps to reproduce

```bash
python -c "from app.calculator import add; print(add(2, 3))"
```

## Expected result

`5`

## Actual result

`-1`

## Hints

Look at `app/calculator.py`. Only `add` is wrong.
