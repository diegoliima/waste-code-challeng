from timer import Timer
import time

@Timer(name="Test Decorator")
def test_timer_decorator():
    time.sleep(0.5)

def test_times_context():
    with Timer("Context"):
        time.sleep(10)

def test_time_class():
    t = Timer("Test Class")
    t.start()
    time.sleep(30)
    t.stop()


if __name__ == "__main__":
    print("Started")
    test_timer_decorator()
    test_times_context()
    test_time_class()