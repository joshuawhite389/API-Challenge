import JSON_Placeholder_API

baseUrl = 'https://jsonplaceholder.typicode.com/todos/'

jsonObject = JSON_Placeholder_API.JSON_Placeholder_API(baseUrl)

# just to test
jsonObject.getJsonObject('99')

jsonObject.getTitle('99')

jsonObject.injectTime('100')
