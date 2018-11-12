from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'INSERT-HERE'
VIEW_ID = 'INSERT-HERE'


credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)
analytics = build('analyticsreporting', 'v4', credentials=credentials)

response = analytics.reports().batchGet(
    body={
      'reportRequests': [
      {
        'viewId': VIEW_ID,
        'dateRanges': [{'startDate': '730daysAgo', 'endDate': 'today'}],
        'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:pageviews'}],
        'dimensions': [{'name': 'ga:fullReferrer'}, {'name': 'ga:country'}]
      }]
    }
).execute()

for report in response.get('reports', []):
  columnHeader = report.get('columnHeader', {})
  dimensionHeaders = columnHeader.get('dimensions', [])
  metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

  for row in report.get('data', {}).get('rows', []):
    dimensions = row.get('dimensions', [])
    dateRangeValues = row.get('metrics', [])

    for header, dimension in zip(dimensionHeaders, dimensions):
      print header + ': ' + dimension

    for i, values in enumerate(dateRangeValues):
      print 'Date range: ' + str(i)
      for metricHeader, value in zip(metricHeaders, values.get('values')):
        print metricHeader.get('name') + ': ' + value
    print '============================'

