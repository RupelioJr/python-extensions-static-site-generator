from ssg import hooks
import times

start_time = None
total_written = 0

@hooks.register("start_build")
def start_build():
    global start_time
    start_time = times.ctime