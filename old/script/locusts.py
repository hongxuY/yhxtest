# -*- coding: UTF-8 -*-
import multiprocessing
import sys
import time
from locust.main import main


def debug(sys_argv):
    sys_argv.append("-f")
    sys_argv.append("yjktask.py")
    sys_argv.append("--no-web")
    sys_argv.append("-c1")
    print sys_argv
    sys.argv = sys_argv
    main()

def start(sys_argv):
    sys_argv.append("-f")
    sys_argv.append("yjktask.py")
    sys_argv.append("--no-reset-stats")
    print sys_argv
    sys.argv = sys_argv
    main()


def start_master(sys_argv):
    sys_argv.append("yjktask.py")
    sys_argv.append("--master")
    sys_argv.append("--no-reset-stats")
    sys.argv = sys_argv
    main()


def start_slave(sys_argv):
    print sys_argv
    sys_argv.append("--slave")
    sys_argv.append("--no-reset-stats")
    sys.argv = sys_argv
    main()


def run_locusts_at_full_speed(sys_argv):
    master_host=''
    if len(sys_argv) == 2:
        sys_argv.pop(1)
    elif len(sys_argv) > 2:
        sys_argv.pop(1)
        master_host=sys_argv.pop(1)
        sys_argv.append("--master-host=" + master_host)

    slaves_num = multiprocessing.cpu_count()
    new_locustfile(slaves_num)
    processes = []
    sys_argv.append("-f")
    for i in range(slaves_num):
        sys_argv.append("internal-test%d.py" %(i+1))
        p_slave = multiprocessing.Process(target=start_slave, args=(sys_argv,))
        p_slave.daemon = True
        p_slave.start()
        processes.append(p_slave)
        sys_argv.pop(sys_argv.index("internal-test%d.py" %(i+1)))
        time.sleep(1)
    try:
        if master_host == '':
            start_master(sys_argv)
        else:
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
        sys.exit(0)


def main_locust():
    if 'debug' in sys.argv:
        sys.argv.pop(sys.argv.index('debug'))
        debug(sys.argv)
    elif 'master' in sys.argv:
        sys.argv.pop(sys.argv.index('master'))
        sys.argv.append("-f")
        start_master(sys.argv)
    elif 'slave' in sys.argv:
        run_locusts_at_full_speed(sys.argv)
    elif 'all' in sys.argv:
        run_locusts_at_full_speed(sys.argv)
    else:
        start(sys.argv)


def new_locustfile(cpus):
    file_path = "internal-test"
    with open("%s.py" % file_path, 'r') as f:
        text = f.read()
        for i in range(cpus):
            new_file="%s%d.py" % (file_path, (i+1))
            with open(new_file, 'w') as fw:
                fw.write(text.replace('1431210', '143121%d' % (i+1)))


if __name__ == '__main__':
    main_locust()
