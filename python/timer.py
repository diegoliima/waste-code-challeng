from contextlib import ContextDecorator
from dataclasses import dataclass, field
from typing import Any, Callable, ClassVar, Dict, Optional
import pendulum

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

@dataclass
class Timer(ContextDecorator):
    timers: ClassVar[Dict[str, float]] = dict()
    name: Optional[str] = None
    _start_time: Optional[float] = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        if self.name:
            self.timers.setdefault(self.name, 0)

    def start(self) -> None:
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = pendulum.now()

    def stop(self) -> float:
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        # Calculate elapsed time
        final_time = pendulum.now()
        difference_time = final_time - self._start_time

        print(difference_time.in_words(locale='en'))

        return difference_time

    def __enter__(self) -> "Timer":
        self.start()
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.stop()