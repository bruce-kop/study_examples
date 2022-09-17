"""控制爱奇艺的使用时间"""
import psutil
import threading
import time
from interval import Interval

def check_process(pname):
    process = psutil.process_iter()
    for p in process:
        if p.name() == "QyClient.exe":
            return p
    return None

def timer_check(**kwargs):
    pname = 'pname' in kwargs and kwargs['pname'] or ""
    start = "start" in kwargs and kwargs["start"] or ""
    end = "end" in kwargs and kwargs["end"] or ""

    now_local_time = time.strftime("%H:%M:%S",time.localtime())
    now_time = Interval(now_local_time,now_local_time)
    time_interval = Interval(start,end)

    if now_time not in time_interval:
        p = check_process(pname)
        if p:
            p.kill()
            print(p.pid, "killed")

    global timer
    timer = threading.Timer(10, timer_check, kwargs ={"pname":pname})
    timer.start()
import sys
import argparse

def main(args = sys.argv[1:]):

    parser = argparse.ArgumentParser(description="manul this script")
    parser.add_argument("--client", help='client name', type=str, default="QyClient.exe")
    parser.add_argument("--start", help='start time', type=str, default="13:00:00")
    parser.add_argument("--end", help='end time', type=str, default="14:00:00")
    _args = parser.parse_args(args=args)
    print(_args.client,_args.start,_args.end)
    pname = "QyClient.exe"
    timer = threading.Timer(1, timer_check, kwargs={"pname": _args.client,
                                                    "start":_args.start,
                                                    "end":_args.end})
    timer.start()


if __name__ == '__main__':
    main()
    print("end")

