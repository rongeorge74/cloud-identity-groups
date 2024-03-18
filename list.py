# Detailed Python Client setup for Cloud Identity APIs can be found here:
# https://cloud.google.com/identity/docs/how-to/setup

from oauth2client.client import GoogleCredentials
import googleapiclient.discovery
from urllib.parse import urlencode


SCOPES = ['https://www.googleapis.com/auth/cloud-identity.groups']
SERVICE_ACCOUNT_FILE = './identity-groups-admin.json'

CUSTOMER_ID = "C03j0o317"


def search_google_groups(service, customer_id):
  search_query = urlencode({
          "query": "parent=='customerId/{}' && 'cloudidentity.googleapis.com/groups.discussion_forum' in labels".format(customer_id)
  })
  search_group_request = service.groups().search()
  param = "&" + search_query
  search_group_request.uri += param
  response = search_group_request.execute()

  return response

def create_service():
  credentials = GoogleCredentials.get_application_default()
  service_name = 'cloudidentity'
  api_version = 'v1'
  service = googleapiclient.discovery.build(
    service_name,
    api_version,
    credentials=credentials)

  return service


def filter(filterString, groups):
  groups = {
      "groups": []
    }
  group = {
    "id": "",
    "email": "",
    "name": ""
  }
  for g in search_response['groups']:
    if g['groupKey']['id'].startswith(filterString):
      group['id'] = g['name']
      group['email'] = g['groupKey']['id']
      group['name'] = g['displayName']
      groups['groups'].append(group)
  return(groups)


if __name__=="__main__":
    service = create_service()
    search_response = search_google_groups(service=service, customer_id=CUSTOMER_ID)
    print(filter('bms', search_response))