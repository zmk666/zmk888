from datetime import datetime
birthday = datetime(1998,12,29)
birthday.strftime("%Y-%m-%d")
birthday.strftime('%b %d, %Y')
birthday.strftime('%d %B %Y')
birthday.strftime('%Y/%m/%d')
birthday.strftime('%m/%d/%Y')
birthday.strftime('%A/%Y/%m/%d')
print(birthday)
