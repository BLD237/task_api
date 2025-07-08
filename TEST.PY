from datetime import datetime, timedelta

expire = datetime.now() + timedelta(minutes=1)
print(expire)