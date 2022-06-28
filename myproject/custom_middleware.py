from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
import csv
import pandas as pd

class Mymiddleware(MiddlewareMixin) :
    
    def process_request(self, request) :
        self.request_time = timezone.now()
        
    def process_response(self, request, response) :
        self.response_time = timezone.now()
        Latency_ms = (self.response_time-self.request_time).total_seconds()
        METHOD = request.method
        URL = request.META["REMOTE_ADDR"]
        Status_Code = response
        
        save_dict = {'timestamp' : self.request_time,
                     'METHOD' : METHOD,
                     "URL" : URL,
                     "Status_Code" : Status_Code.status_code,
                     "Latency_ms" : Latency_ms}
        
        df = pd.DataFrame([save_dict])
        # print(df)
        # df.to_csv('log_data.csv', index=False, encoding='cp949')
        
        with open('log_data.csv', 'a', encoding='utf8') as f:
            wr = csv.writer(f)
            wr.writerow([df])
            
        return response