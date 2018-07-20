# ezproxy-logs
EZproxy log files are created with the following format:
```
ezproxy-20180707.zip
ezproxy-20180708.zip
...
ezproxy-20180731.zip
```
This Python script will unzip all the previous month's EZproxy log files from source to directory.

To use, simply execute the below command:
```
python unpack.py <source> <destination> 
```
