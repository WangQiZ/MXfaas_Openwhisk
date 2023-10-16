FROM wangqz111/mxc:vPython

RUN pip install azure.storage.blob

CMD cd pythonAction && python3 -u init.py
