from datetime import datetime, timedelta
today = datetime.now()
five_d_ago = today - timedelta(days=5)
print(five_d_ago)