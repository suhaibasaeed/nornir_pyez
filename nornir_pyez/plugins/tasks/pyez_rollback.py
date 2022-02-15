import copy
from typing import Any, Dict, List, Optional
from jnpr.junos.utils.config import Config
from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME


def pyez_rollback(task: Task,
                ) -> Result:
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    device.timeout = 300
    config = Config(device)
    config.rollback()
    config.unlock()
    return Result(host=task.host, result=f"Successfully rollbacked")
