from datetime import datetime

now = datetime.now()
ans = now.replace(microsecond = 0)
print(ans)