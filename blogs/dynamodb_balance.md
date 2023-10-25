- want to subtract 8 from balance, before that we should check balance is greater than 8.
>```
>       DynamoDbClient ddb = DynamoDbClient.builder().region(Region.of("us-east-1"))
>				.credentialsProvider(ProfileCredentialsProvider.create("cats")).build();
>
>		HashMap<String, AttributeValue> itemKey = new HashMap<>();
>		itemKey.put("pk", AttributeValue.builder().s("1_1234").build());
>		itemKey.put("sk", AttributeValue.builder().s("FME").build());
>
>		Map<String, String> expressionAttributesNames = new HashMap<>();
>		expressionAttributesNames.put("#kn0", "balance");
>		Map<String, AttributeValue> expressionAttributeValues = new HashMap<>();
>		expressionAttributeValues.put(":kv0", AttributeValue.builder().n("8").build());
>
>		UpdateItemRequest updateItemRequest = UpdateItemRequest.builder().tableName("future_match_engine-uat")
>				.key(itemKey).updateExpression("SET #kn0 = #kn0 - :kv0").conditionExpression("balance > :kv0")
>				.expressionAttributeNames(expressionAttributesNames)
>				.expressionAttributeValues(expressionAttributeValues).returnValues(ReturnValue.UPDATED_NEW).build();
>
>		try {
>			UpdateItemResponse updateItemResponse = ddb.updateItem(updateItemRequest);
>			System.out.println(updateItemResponse);
>		} catch (ConditionalCheckFailedException e) {
>			System.out.println("fail.");
>		}
>```