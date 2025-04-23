#
# Author: Rohtash Lakra
#

import json
import logging
import os
import time
from threading import Thread

import boto3

logger = logging.getLogger(__name__)


class SQSListener:

    def __init__(self, app):
        self.app = app
        self.sqsClient = boto3.client('sqs')  # a sqs client
        self.queue_name = os.getenv('SQS_QUEUE_NAME')  # get the queue name from environment variable
        # self.queue_url = os.getenv('SQS_QUEUE_URL')  # get the queue URL from environment variable

        with self.app.app_context():
            try:
                # Get URL for SQS queue
                self.queue_url = self.sqsClient.get_queue_url(QueueName=self.queue_name)
            except Exception as e:
                logger.error(f"Failed while getting SQS Queue URL! Error={str(e)}")

        self.maxNumberOfMessages = 10
        self.waitTimeSeconds = 30

    def handler(self):
        with self.app.app_context():
            try:
                logger.info("handler() => Waiting for sqs message")
                #  the message configs can be set as required
                response = self.sqsClient.receive_message(
                    QueueUrl=self.queue_url,
                    AttributeNames=['All'],
                    MaxNumberOfMessages=self.maxNumberOfMessages,
                    WaitTimeSeconds=self.waitTimeSeconds
                )

                if 'Messages' in response:
                    logger.info(f"response={response}")
                    message_receipt_handle = ''
                    message_body = ''
                    messages = response['Messages']
                    for value in messages:
                        message_receipt_handle = value['ReceiptHandle']
                        message_body = value['Body']
                        logger.info(f"Read from SQS message_body={message_body}")
                        message = json.loads(message_body)
                        # process the message as needed

                        # and finally delete the message to avoid reprocessing of it
                        self.sqsClient.delete_message(
                            QueueUrl=self.queue_url,
                            ReceiptHandle=message_receipt_handle
                        )
            except Exception as e:
                logger.error(f"Failed while reading from sqs! Error={str(e)}")

            # make the loop for 10 seconds
            time.sleep(10)


class SQSTask(Thread):

    def __init__(self, app=None):
        super().__init__(name="SQSTask", daemon=True)
        self.listener = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.listener = SQSListener(app)
        self.start()

    def run(self, *args, **kwargs):
        while True:  # an infinite loop acting as a listener for SQS
            self.listener.handler()
