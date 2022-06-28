from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
import csv
import pandas as pd
import datetime
import time

class Mymiddleware(MiddlewareMixin) :
    
    def process_request(self, request) :
        self.request_time = timezone.now()
        self.request_unix_time = datetime.datetime.now().replace(tzinfo=timezone.utc).timestamp()
        
    def process_response(self, request, response) :
        self.response_time = timezone.now()

        Latency_ms = (self.response_time-self.request_time).total_seconds()/1000
        
        METHOD = request.method
        URL = request.META["REMOTE_ADDR"]
        Status_Code = response.status_code
        
        save_dict = {'timestamp' : self.request_unix_time,
                     'METHOD' : METHOD,
                     "URL" : URL,
                     "Status_Code" : Status_Code,
                     "Latency_ms" : Latency_ms}
        
        df = pd.DataFrame([save_dict])
        
        with open('log_data.csv', 'a', encoding='utf8') as f:
            wr = csv.writer(f)
            wr.writerow(df.iloc[0])
        
        return response