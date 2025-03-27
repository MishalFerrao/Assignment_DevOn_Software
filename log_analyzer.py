import sys
import json
from datetime import datetime

def read_log_file(log_file):
    """
    Read the log file and store the logs in the dictionary
    
    Parameters:
    log_file (str): log file name
    
    Returns:
    dict: logs from the file
    """
    logs_data = {}
    metadata_from_file = ['Date_and_time', 'Service_name','log_level','log_message']

    with open(log_file) as file:
        data = file.readlines()
        for i in range(len(data)):
            # if the log does not have all the fields, print the line number of the log in the file
            if len(data[i].split(' - ')) == 4: 
                logs_data[i] = dict(zip(metadata_from_file,data[i].split(' - ')))
            else:
                print("Line {} of {} not in the required format".format(i,log_file)) 
    return logs_data

def count_entries_log_level(logs_dict):
    """
    Count the different log levels in the logs dictionary
    
    Parameters:
    logs_dict (dict): dictionary with logs from the file
    
    Returns:
    dict: count of the log levels
    """
    log_level_count_dict = {}
    for i in range(len(logs_dict)):
        if logs_dict[i]['log_level'] in log_level_count_dict:
            log_level_count_dict[logs_dict[i]['log_level']] += 1
        else:
            log_level_count_dict[logs_dict[i]['log_level']] = 1

    return log_level_count_dict


def count_entries_services(logs_dict):
    """
    Count the different services in the logs dictionary
    
    Parameters:
    logs_dict (dict): dictionary with logs from the file
    
    Returns:
    dict: count of the services
    """
    service_count_dict = {}   
    for i in range(len(logs_dict)):
        if logs_dict[i]['Service_name'] in service_count_dict:
            service_count_dict[logs_dict[i]['Service_name']] += 1
        else:
            service_count_dict[logs_dict[i]['Service_name']] = 1
    return service_count_dict


def most_common_error_messages(logs_dict):
    """
    Get the most repeated error message in the logs dictionary
    
    Parameters:
    logs_dict (dict): dictionary with logs from the file
    
    Returns:
    list: maximum repeated error message 
    """
    log_error_dict = {}
    for i in range(len(logs_dict)):
        if logs_dict[i]["log_level"] == "ERROR" and logs_dict[i]["log_message"] in log_error_dict:
            log_error_dict[logs_dict[i]["log_message"]] += 1
        else:
            log_error_dict[logs_dict[i]["log_message"]] = 1

    # get the maximum value in the dict and its corresponding key as a list in case of 
    # more than one error message is present
    maxval = max(log_error_dict.values())
    max_count_log_error_list = [k for k in log_error_dict if log_error_dict[k]==maxval]

    return max_count_log_error_list


def save_summary(data):
    """
    Dump the summary data to a json file
    
    Parameters:
    data (dict): dictionary with the summary of the log file
    
    """
    with open("summary.json", "w") as outfile:
        json.dump(data, outfile)

def filter_logs_based_on_date(start,end,logs_dict):
    """
    Filter the logs based on start date and end date
    
    Parameters:
    start (str): start date 
    end (str): end date 
    logs_dict (dict): dictionary with logs from the file

    Returns:
    dict: Logs recorded within the start date and end date
    """
    filter_logs = {}

    try:
        if bool(datetime.strptime(start,'%Y-%m-%d %H:%M:%S')):
            start_time = datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
        elif bool(datetime.strptime(start,'%Y-%m-%d')):
            start_time = datetime.strptime(start,'%Y-%m-%d')
        else:
            pass
    except ValueError:
        print("Start time not in the %Y-%m-%d format or %Y-%m-%d %H:%M:%S format")
        return 0
        

    try:
        if bool(datetime.strptime(end,'%Y-%m-%d %H:%M:%S')):
            end_time = datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
        elif bool(datetime.strptime(end,'%Y-%m-%d')):
            end_time = datetime.strptime(end,'%Y-%m-%d')
        else:
            pass
    except ValueError:
        print("End time not in the %Y-%m-%d format or %Y-%m-%d %H:%M:%S format")
        return 0
        
    #Exchange the start time and end time if start is greater than end
    if start_time > end_time:
        start_time, end_time = end_time, start_time

    for i in range(len(logs_dict)):
        try: 
            log_time = datetime.strptime(logs_dict[i]['Date_and_time'],'%Y-%m-%d %H:%M:%S')
        except ValueError:
            log_time = datetime.strptime(logs_dict[i]['Date_and_time'],'%Y-%m-%d')

        if (log_time > start_time) and (log_time < end_time):
            filter_logs[i] = logs_dict[i]
    return filter_logs          

def log_analyzer(arguments):
    """
    Analyzes the log file and summarizes and filters the logs
    
    Parameters:
    arguments (list): Input arguments

    """
    summary = {}
    logs = read_log_file(arguments[0])
    log_level_count = count_entries_log_level(logs)
    service_count = count_entries_services(logs)
    most_repeated_error_message = most_common_error_messages(logs)
 
    summary['file_name'] = arguments[0]
    summary['log_level_count'] = log_level_count
    summary['services_count'] = service_count
    summary['most_common_log'] = most_repeated_error_message
    
    save_summary(summary)


    # filters the log only if both start and end date is provided as input argument in 
    # the required format
    if len(arguments) == 3:
        filtered_logs = {}
        filtered_logs = filter_logs_based_on_date(arguments[1],arguments[2],logs)
        if filtered_logs != 0:
            print(filtered_logs)


def main(arguments):
    """
    Entry point for the log analyzer
    
    Parameters:
    arguments (list): Input arguments

    """
    if (len(arguments) == 1) or (len(arguments) == 3):
        log_analyzer(arguments)
    else:
        print("The input argument length can either be 1 or 3. Please check the input")


if '__main__' == __name__ :
    main(sys.argv[1:])