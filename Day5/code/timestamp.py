from datetime import datetime
import time
timestamp = 1696147200
# 转换为本地时间
local_time = datetime.fromtimestamp(timestamp)
# 格式化为字符串
formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)  # 输出：2023-10-01 00:00:00

# 反向转换（字符串转时间戳）
date_str = "2023-10-01 08:00:00"
struct_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").timetuple()
timestamp = int(time.mktime(struct_time))
print(timestamp+28800)  # 输出：1696147200（假设时区正确）