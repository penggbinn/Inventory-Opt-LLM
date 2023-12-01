# Few Shot Prompting - Test Case 1

## Prompt Test Case Problem
Assume the following conditions:
- labour quality is skilled
- back orders are high
- lead times are low
- reorder point is near
- available capital is high
- forecasted demands are low
- current inventory is high
- safety stock is low

Will the company experience over-stocking, under-stocking or stock-out? Provide the most probable answer.

## Prompt Solution
- Since labour quality is skilled, orders will be met on time with great accuracy.
- Since back orders are high, the company will have to first meet those orders before taking new ones.
- Lead times are low, so procurement of new inventory is easy.
- Current inventory is high
- Reorder point is low and the available capital is high along with low lead times means the company can easily stock
new inventory if need be.
- Forecasted demand is low meaning the company does not have to worry about new orders being requested.

Considering these factors there is a greater possibility of the company being overstocked with some chance of stock-out
and almost no chance of under-stock.

## New Test Case
Assume the following conditions:
- labour quality is semi-skilled
- back orders are medium
- lead times are low
- reorder point is near
- available capital is medium
- forecasted demands are medium
- current inventory is high
- safety stock is medium

Will the company experience over-stocking, under-stocking or stock-out? Provide the most probable answer.

## Expected Solution
A mix of stock-out and balanced with stock-out being the most probable.