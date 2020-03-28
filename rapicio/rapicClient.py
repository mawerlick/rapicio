import json
import time

import requests


class Rapic:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.access_t = ""
        self.refresh_t = ""
        self.start_time = 0
        self.stop_time = 0

    def login(self):
        try:
            self.start_time = time.time()
            url = "https://rapicapi.herokuapp.com/api/token/"
            h = {
                "Content-Type": "application/json"
            }
            data = {
                'username': self.username,
                'password': self.password
            }
            r = requests.post(url=url, headers=h, data=json.dumps(data))
            r1 = r.json()
            if r.status_code >= 200 and r.status_code <= 299:
                self.access_t = r1.get("access")
                self.refresh_t = r1.get("refresh")
            else:
                print("rapicio login failed")
        except Exception as e:
            print("Login error:{}".format(e))

    def post_data(self, projectName, objectName, data):
        try:
            self.stop_time = time.time()
            if (self.start_time - self.stop_time) >= 60:
                self.access_t = self.refresh_token()
                self.start_time = time.time()
            head = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(self.access_t)
            }
            url = "http://{0}.rapic.io/{1}/{2}/".format(self.username, projectName, objectName)
            r = requests.post(url, headers=head, data=json.dumps(data))
            return r.json()
        except Exception as e:
            print("Posting data error:{}".format(e))

    def update_data(self, projectName, objectName, id, data):
        try:
            self.stop_time = time.time()
            if (self.start_time - self.stop_time) >= 60:
                self.access_t = self.refresh_token()
                self.start_time = time.time()
            head = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(self.access_t)
            }
            url = "http://{0}.rapic.io/{1}/{2}/{3}".format(self.username, projectName, objectName, id)
            r = requests.post(url, headers=head, data=json.dumps(data))
            return r.json()
        except Exception as e:
            print("Updating data error:{}".format(e))

    def get_data(self, projectName, objectName, filter=None):
        try:
            self.stop_time = time.time()
            if (self.start_time - self.stop_time) >= 60:
                self.access_t = self.refresh_token()
                self.start_time = time.time()
            head = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(self.access_t)
            }
            url = "http://{0}.rapic.io/{1}/{2}/".format(self.username, projectName, objectName)
            r = requests.get(url, headers=head)
            return r.json()
        except Exception as e:
            print("Getting data error:{}".format(e))

    def delete_data(self, projectName, objectName, id):
        try:
            self.stop_time = time.time()
            if (self.start_time - self.stop_time) >= 60:
                self.access_t = self.refresh_token()
                self.start_time = time.time()
            head = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {0}".format(self.access_t)
            }
            url = "http://{0}.rapic.io/{1}/{2}/{3}".format(self.username, projectName, objectName, id)
            r = requests.delete(url, headers=head)
            return r.json()
        except Exception as e:
            print("Deleting data error:{}".format(e))

    def refresh_token(self):
        try:
            h = {
                "Content-Type": "application/json"
            }
            url_time = "https://rapicapi.herokuapp.com/api/token/refresh/ "
            params = {
                "refresh": self.refresh_t
            }
            r_time = requests.post(url_time, headers=h, data=json.dumps(params))
            if r_time.status_code >= 200 and r_time.status_code <= 299:
                r1 = r_time.json()
                return r1.get("access")
        except Exception as e:
            print("Refresh error:{}".format(e))
