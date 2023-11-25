import requests
import json

class Rest:

    def make_delete_request(self, url="", status_code=204):
        response = requests.delete(url)
        assert response.status_code == status_code
        return response.text

    def make_get_request(self, url="", status_code=200):
        response = requests.get(url)
        assert response.status_code == status_code
        return json.loads(response.text)

    def make_post_request_all_statuses(self, url="", header="", json_body="", status_code=201):
        try:
            given_json_body = json.dumps(json_body)
            response = requests.post(url, json=given_json_body, headers=header)
            assert response.status_code == status_code
            return json.loads(response.text)
        except Exception:
            print(f"Not correct status expected {status_code} getting {response.status_code}")

    def make_post_request_success_status(self, url="", header="", json_body="", status_code=201):
        given_json_body = json.dumps(json_body)
        response = requests.post(url, json=given_json_body, headers=header)
        assert response.status_code == status_code
        return json.loads(response.text)

    def make_post_request_with_auth(self, url="", bearer="", json_body="", status_code=200):
        headers = {
            'Accept': 'application/json, text/plain',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json;charset=UTF-8',
            'authorization': 'Bearer ' + bearer
        }
        json.dumps(json_body)
        response = requests.post(url, headers, json_body)
        assert response.status_code == status_code
        return json.loads(response.text)

    def make_put_request(self, url="", header="", json_body="", status_code=200):
        json.dumps(json_body)
        response = requests.put(url, json=json_body, headers=header)
        assert response.status_code == status_code
        return json.loads(response.text)

    def make_put_request_with_auth(self, url="", bearer="", json_body="", status_code=200):
        headers = {
            'Accept': 'application/json, text/plain',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json;charset=UTF-8',
            'authorization': 'Bearer ' + bearer
        }
        json.dumps(json_body)
        response = requests.put(url, json_body, headers=headers)
        assert response.status_code == status_code
        return json.loads(response.text)