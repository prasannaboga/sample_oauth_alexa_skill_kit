import requests

class SampleOauth:
  
  def __init__(self, access_token):
    self.base_url = 'https://glacial-retreat-51710.herokuapp.com'
    #self.base_url = 'http://192.168.6.24:5000'
    self.headers = {'Authorization': 'Bearer {}'.format(access_token), 'Content-Type': 'application/json',
               'Accept': 'application/json'}
    print(" ==== base_url ====> " + self.base_url)
    
  def get_user_info(self):
    profile_url = '{0}/api/profile'.format(self.base_url)
    response = requests.get(profile_url, params={}, headers=self.headers)
    return response
    
  def update_user_info(self):
    profile_url = '{0}/api/profile'.format(self.base_url)
    response = requests.put(profile_url, params={}, headers=self.headers)
    return response

