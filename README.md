# LogByPercent
- helper to log time by task estimation in percentage

# How it works
- Instead of having 8 work hours, You have 100% work hours. Give each task a percentage. 
Percentage represent the time you spent in the task on that day in percent. 
This helper converts a task percentage to work hours in "hour:minute:seconds" format, Assuming sum of all task percentage is 100%

# Getting Started
1) execute "logbypercent.py"
2) input total task on that day
3) give each task a percent
4) execute "logbypercent.py -h" for more information

# Note
- All percentage must be divisible by 5 to avoid data loss when convert from percentage to actual work hours.
- Sum of percentage in all tasks must be 100%.

# Dependencies
- python3

