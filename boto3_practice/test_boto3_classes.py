from boto3_practice.boto3_utils import AWSDynamoDAO, DynamoKeyTypes, DynamoAttributeTypes, DynamoProjectionTypes, \
    DynamoBillingModes, DAOContext
from pytest_mock import mocker


def test_dao_case_1(mocker):



    dao = AWSDynamoDAO()
    if dao.is_table_present(TableName='test_table'):
        d_context = dao.delete_table(TableName='test_table')
        assert isinstance(d_context, DAOContext)

    result_context = dao.create_table(
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
    assert isinstance(result_context, DAOContext)
    assert isinstance(result_context.data, dict)
    assert isinstance(result_context.status, bool)


def test_dao_case_2():
    dao = AWSDynamoDAO()
    assert dao.is_table_present(TableName='test_table') is True


def test_das_case_3():
    dao = AWSDynamoDAO()
    context = dao.get_table_status(TableName='test_table')
    assert isinstance(context, DAOContext)
    assert isinstance(context.data, str)

