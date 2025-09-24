import time

class Time:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Time, cls).__new__(cls)
            cls.instance._start_time = time.localtime()
        return cls.instance
    
    @property
    def start_time(self):
        return self._start_time

    def get_time(self):
        return time.localtime()
    
    def time_from_start(self, start_time):
        return time.mktime(time.localtime()) - time.mktime(start_time)
    
    def time_elapsed(self, start_time, end_time):
        return time.mktime(end_time) - time.mktime(start_time)
    
    def delay_condition(self, stored_time, seconds):
        """
        Returns True if the time elapsed reaches the specified seconds.

        Parameters:
            time: The time to compare with the current time.
            seconds: The time to compare with the time elapsed.
        """

        if self.time_elapsed(stored_time, self.get_time()) == seconds:
            return True
        return False

shared_time = Time()