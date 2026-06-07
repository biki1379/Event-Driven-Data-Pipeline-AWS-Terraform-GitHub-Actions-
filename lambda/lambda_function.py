import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    try:
        report = {
            "status": "Report generated successfully",
            "requestId": context.aws_request_id
        }
        logger.info("Report generated: %s", report)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(report)
        }
    except Exception as e:
        logger.error("Error processing event: %s", str(e))
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"status": "error", "message": str(e)})
        }
