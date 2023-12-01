# Few Shot Prompting - Test Case 2

## Prompt Test Case Problem
Assume the following conditions:
- labour quality is unskilled
- back orders are high
- lead times are high
- reorder point is far
- available capital is medium
- forecasted demands are high
- current inventory is low
- safety stock is high

Will the company experience over-stocking, under-stocking or stock-out? Provide the most probable answer.

## Prompt Solution
- Since labour quality is unskilled, orders will not probably not be met on time with good accuracy without supervision.
- Since back orders are high, the company will have to first meet those orders before taking new ones.
- Lead times are high, so procurement of new inventory is tough.
- Reorder point is far and available capital is medium along with high lead times means the company might have
difficulty in obtaining new inventory.
- Forecasted demand is high means that the company will have a lot of orders to fulfil that may / may not be
before the reorder point.
- Current inventory is low means that the forecasted demands might not be met.

Considering the above factors, there is a high probability that the company will be under-stocked with low probability
for stock-out and almost no chance for over-stocking.

## New Test Case
Assume the following conditions:
- labour quality is unskilled
- back orders are low
- lead times are high
- reorder point is near
- available capital is low
- forecasted demands are high
- current inventory is high
- safety stock is medium

Will the company experience over-stocking, under-stocking or stock-out? Provide the most probable answer.

## Expected Solution
A mix of under-stocking and stock-out with stock-out being most probable.