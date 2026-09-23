from typing import Callable, Dict, List

Loader = Callable[[], List[Dict]]
Saver = Callable[[List[Dict]], None]
