metadata_from_file = ['Date_and_time', 'Serive_name','log_level','log_message']


def read_log_file(log_file):
    logs_data = {}
    with open(log_file) as file:
        data = file.readlines()
        for i in range(len(data)):
            if len(data[i].split(' - ')) == 4:
                logs_data[i] = dict(zip(metadata_from_file,data[i].split(' - ')))
            else:
                pass 
    return logs_data

def count_entries_log_level(logs_dict):
    info_log_count = 0
    error_log_count = 0
    warn_log_count = 0
    for i in range(len(logs_dict)):
        if 


    
def main():
    log_dict = read_log_file("app.log")
    count_entries_log_level(log_dict)
    







if '__main__' == __name__ :
    main()