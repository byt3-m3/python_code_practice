import typing
from enum import Enum

import attr
from boto3 import client
from boto3_practice.secret import AWS_SECRET_ACCESS_KEY_ID, AWS_ACCESS_KEY_ID


@attr.s
class DAOContext:
    data: typing.Any = attr.ib(default=None)
    status: bool = attr.ib(default=False)


class DynamoKeyTypes(Enum):
    HASH = 'HASH'
    RANGE = 'RANGE'


class DynamoAttributeTypes(Enum):
    STRING = 'S'
    NUMBER = 'N'
    BINARY = 'B'


class DynamoBillingModes(Enum):
    PAY_PER_REQUEST = 'PAY_PER_REQUEST'
    PROVISIONED = 'PROVISIONED'


class DynamoProjectionTypes(Enum):
    ALL = 'ALL'
    KEYS_ONLY = 'KEYS_ONLY'
    INCLUDE = 'INCLUDE'


class AWSRegions(Enum):
    north_virginia = 'us-east-1'
    ohio = 'us-east-2'
    north_california = 'us-west-1'
    oregon = 'us-west-2'


class TableStatues(Enum):
    """
    'CREATING'|'UPDATING'|'DELETING'|'ACTIVE'|'INACCESSIBLE_ENCRYPTION_CREDENTIALS'|'ARCHIVING'|'ARCHIVED',
        'CreationDateTime': datetime(2015, 1, 1),
    """
    CREATING = 'CREATING'
    UPDATING = 'UPDATING'
    DELETING = 'DELETING'
    ACTIVE = 'ACTIVE'
    INACCESSIBLE_ENCRYPTION_CREDENTIALS = 'INACCESSIBLE_ENCRYPTION_CREDENTIALS'
    ARCHIVING = 'ARCHIVING'
    ARCHIVED = 'ARCHIVED'
    CreationDateTime = 'CreationDateTime'


@attr.s
class AWSDynamoDAO:
    client: client = attr.ib(default=client(
        'dynamodb',
        region_name=AWSRegions.north_virginia.value,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY_ID
    )
    )
    _creation_requests: typing.List[dict] = attr.ib(default=[])

    def create_table(self,
                     AttributeDefinitions: typing.List[dict] = None,
                     KeySchema: typing.List[dict] = list,
                     TableName: str = '',
                     LocalSecondaryIndexes=None,
                     GlobalSecondaryIndexes: typing.List[dict] = None,
                     BillingMode: DynamoBillingModes = DynamoBillingModes.PAY_PER_REQUEST,
                     Tags=None,
                     ) -> DAOContext:
        request_data = {}

        request_data['TableName'] = TableName
        request_data['KeySchema'] = KeySchema
        request_data['AttributeDefinitions'] = AttributeDefinitions
        request_data['GlobalSecondaryIndexes'] = GlobalSecondaryIndexes
        request_data['BillingMode'] = BillingMode.value

        try:
            response = self.client.create_table(**request_data)
            self._self_log_table_create_request(request_data)
            return DAOContext(status=True, data=response)

        except self.client.exceptions.ResourceInUseException:
            print("Duplicate Table Detected")
            return DAOContext(status=False, data={})

        except Exception as err:
            print(type(err))
            raise

    def delete_table(self, TableName: str) -> DAOContext:
        try:
            response = self.client.delete_table(TableName=TableName)

            table_status = response['TableDescription']['TableStatus']
            if table_status == 'DELETING':
                return DAOContext(status=True, data=response)

            return DAOContext(status=False, data=None)

        except self.client.exceptions.ResourceInUseException:
            return DAOContext(status=False, data=None)

        except self.client.exceptions.ResourceNotFoundException:
            return DAOContext(status=False, data=None)

    def is_table_present(self, TableName: str) -> bool:
        """Checks if the TableName is present in dynamodb"""
        try:
            self.client.describe_table(TableName=TableName)

            return True
        except self.client.exceptions.ResourceNotFoundException:
            # do something here as you require
            return False

    def get_table_status(self, TableName: str) -> DAOContext:
        try:
            response = self.client.describe_table(TableName=TableName)

            table_status = response['Table']['TableStatus']

            return DAOContext(status=True, data=table_status)

        except self.client.exceptions.ResourceNotFoundException:
            # do something here as you require
            return DAOContext(status=False, data=None)

    def _self_log_table_create_request(self, data: dict):
        self._creation_requests.append(data)


if __name__ == '__main__':
    dao = AWSDynamoDAO()

    dao.create_table(
        TableName='test_table',
        KeySchema=[
            {
                "AttributeName": "first_name",
                "KeyType": DynamoKeyTypes.HASH.value
            },
            {
                "AttributeName": "last_name",
                "KeyType": DynamoKeyTypes.RANGE.value
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "first_name",
                "AttributeType": DynamoAttributeTypes.STRING.value
            },
            {
                "AttributeName": "last_name",
                "AttributeType": DynamoAttributeTypes.STRING.value
            }
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'first_name-last_name-index',
                'KeySchema': [
                    {
                        'AttributeName': 'first_name',
                        'KeyType': DynamoKeyTypes.HASH.value
                    },

                ],
                'Projection': {
                    'ProjectionType': DynamoProjectionTypes.ALL.value,

                },
            }
        ],
        BillingMode=DynamoBillingModes.PAY_PER_REQUEST
    )
