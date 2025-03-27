# Python Script for Log analyzer

## How to run the log analyzer

The inputs to the python script are:
* File name 
* Start data in **%Y-%m-%d** format or **%Y-%m-%d %H:%M:%S** format
* End data in **%Y-%m-%d** format or **%Y-%m-%d %H:%M:%S** format

```
python log_analyzer app.log "2023-03-02 09:03:23" "2023-03-08 10:34:34"
                      OR
python log_analyzer app.log
```

**Note:**
The script can also be run with just the file name. If the start data and end date is not added to the command line, the logs are not filtered

## Folder Content

* app.log - Input log file
* Hiring _ Python Assignment.docx - assignment question
* log_analyzer.py - script for log analyzer
* summary.json - JSON file with summary of the log file
* test_log_analyzer.py - pytest script for log_analyzer.py