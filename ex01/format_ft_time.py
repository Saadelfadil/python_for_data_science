from datetime import datetime

now = datetime.now()
ts = now.timestamp()

print(f'Seconds since January 1, 1970: {format(ts, ",.14")} or {format(ts, ".3")} in scientific notation')
print(now.strftime("%b %d %Y"))