# log
This is logging for projects

## Using
```py
from log import create_log, write_log

new_log = create_log("INFO", "A log was created")
write_log(new_log)
```

Result:
```
INFO: [2026-08-30 16:19:58] A log was created
```
