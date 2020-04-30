import threading
import time
import traceback
from lib.data import th,poc_array


def initEngine():
    th.thread_mode = False
    th.s_flag = 1
    th.thread_count = th.threads_num = th.THREADS_NUM = 4
    th.scan_count = th.found_count = 0
    th.is_continue = True
    th.found_single = False
    th.start_time = time.time()
    setThreadLock()
    msg = 'Set the number of threads: %d' % th.threads_num
    print(msg)


def singleMode():
    th.is_continue = False
    th.found_single = True


def scan():
    while 1:
        if th.thread_mode: th.load_lock.acquire()
        if th.queue.qsize() > 0 and th.is_continue:
            payload = str(th.queue.get(timeout=1.0))
            if th.thread_mode: th.load_lock.release()
        else:
            if th.thread_mode: th.load_lock.release()
            break
        try:
            status = poc_array[0].poc(payload)
            resultHandler(status, payload)
            del poc_array[0]
        except Exception:
            th.errmsg = traceback.format_exc()
            th.is_continue = False
        changeScanCount(1)

    changeThreadCount(-1)


def run():
    initEngine()
    if True:
        from gevent import monkey
        monkey.patch_all()
        import gevent
        while th.queue.qsize() > 0 and th.is_continue:
            gevent.joinall([gevent.spawn(scan) for i in range(0, th.threads_num) if
                            th.queue.qsize() > 0])

    if 'errmsg' in th:
        print(th.errmsg)

    if th.found_single:
        msg = "[single-mode] found!"
        print(msg)


def resultHandler(status, payload):
    if not status:
        return
    # elif status is POC_RESULT_STATUS.RETRAY:
    #     changeScanCount(-1)
    #     th.queue.put(payload)
    #     return
    elif status is True:
        msg = payload
    else:
        msg = "failed"
    #changeFoundCount(1)
    if th.s_flag:
        print(msg)

def setThreadLock():
    if th.thread_mode:
        th.found_count_lock = threading.Lock()
        th.scan_count_lock = threading.Lock()
        th.thread_count_lock = threading.Lock()
        th.file_lock = threading.Lock()
        th.load_lock = threading.Lock()


def setThreadDaemon(thread):
    thread.daemon = True


def changeFoundCount(num):
    if th.thread_mode: th.found_count_lock.acquire()
    th.found_count += num
    if th.thread_mode: th.found_count_lock.release()


def changeScanCount(num):
    if th.thread_mode: th.scan_count_lock.acquire()
    th.scan_count += num
    if th.thread_mode: th.scan_count_lock.release()


def changeThreadCount(num):
    if th.thread_mode: th.thread_count_lock.acquire()
    th.thread_count += num
    if th.thread_mode: th.thread_count_lock.release()


def output2file(msg):
    if th.thread_mode: th.file_lock.acquire()
    f = open(th.output, 'a')
    f.write(msg + '\n')
    f.close()
    if th.thread_mode: th.file_lock.release()
