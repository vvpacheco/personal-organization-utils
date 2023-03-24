import os
import sys
import pandas as pd
from datetime import datetime, timedelta


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d/%m/%Y %H:%M:%S')
    return formated_date

def list_files(path_to_list):
    file_list = []
    entries = os.scandir(path_to_list)
    for entry in entries:
        if entry.is_file():
            file_data = entry.stat()
            #print(file_data.st_mtime)
            #print(type(file_data.st_mtime))
            #print(convert_date(file_data.st_mtime))
            file_list.append((entry.name,datetime.utcfromtimestamp(file_data.st_mtime)))
    return file_list

if __name__ == '__main__':
    print(sys.argv[1:])
    directory, days = sys.argv[1:]

    arquivos = list_files(directory)
    df = pd.DataFrame(arquivos,columns=['Name','Modified'])
    #pd.to_datetime(df['Modified'], )
    target_date = datetime.today() - timedelta(days=int(days))
    print(target_date)
    print('Apenas antigos')
    print(df[df['Modified']>=target_date].sort_values('Modified'))
