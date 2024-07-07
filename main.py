# %%
import requests
from bs4 import BeautifulSoup
import pickle
import hashlib
import sys
import os 



def hash_str(s: str) -> int:
    input_bytes = s.encode('utf-8')
    
    hash_object = hashlib.sha256()
    hash_object.update(input_bytes)
    return int(hash_object.hexdigest(), 16)

def get_content() -> int: #set the content which will be listen here.
    pass
    # url = ''
    # res = requests.get(url)
    # soup = BeautifulSoup(res.text, 'lxml')
    
    # titles = [i.text.strip() for i in soup.find_all('div', {'class' : 'col-md-auto'})][:-2]
    
    # return hash_str(str(titles))

class Storge:
    def __init__(self, url: str):
        self.url = url
    
    def __check_file(self, url: str) -> bool:
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, url)
        return os.path.exists(file_path)
    
    def store(self, v: any):
        with open(self.url, 'wb') as f:
            pickle.dump(v, f)
            
    def load(self) -> any:
        if not self.__check_file(self.url):
            return None
        with open(self.url, 'rb') as f:
            self.variable = pickle.load(f)
        return self.variable

def lineNotifyMessage(msg):
    headers = {
      "Authorization": "Bearer " + line_token, 
      "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

try:
    line_token = str(sys.argv[1])
    f = Storge('hash_v.pkl')
    old_v = f.load()
    new_v = get_content()
    if old_v == new_v:
        print("nothing updated")
    else: #set notify message here.
        lineNotifyMessage("[公告監控通知] Url_1 有新公告")
    f.store(new_v)
except Exception as err: #set script error message here.
    lineNotifyMessage("[自動執行發生錯誤] 監控 Url_1 意外終止")
    print(err)
# %%