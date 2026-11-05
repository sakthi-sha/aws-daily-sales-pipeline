# AWS Daily Sales Pipeline

## Project Overview
This project demonstrates a daily sales reporting pipeline using AWS services.

## AWS Services Used
- Amazon S3 – Staging and Presentation storage
- AWS Glue – Data transformation
- AWS Step Functions – Workflow orchestration
- Amazon CloudWatch – Job monitoring

## Data Flow
1. Overnight sales CSV is uploaded to the S3 staging area.
2. AWS Glue reads the sales data.
3. Total sales and average order value are calculated.
4. The transformed results are stored in the S3 presentation layer.
5. AWS Step Functions is used to orchestrate the Glue job.

## Lazy Evaluation
The Spark execution plan is analyzed using `explain(True)` before execution. The `show()` action triggers the calculation and retrieves the metrics.

## Expected Results
- Total Sales: 87300
- Average Order Value: 14550

## Project Files
- daily_sales_transformation.py
- daily_sales_workflow.json
