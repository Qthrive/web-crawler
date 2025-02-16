以下是针对 **Day 5：JSON数据处理** 的详细学习计划，结合你已掌握的内容（Requests库、XPath解析等），系统掌握JSON数据处理核心技能。

---

### 📅 **今日学习目标**
1. **理解JSON数据结构**：掌握嵌套JSON的解析技巧  
2. **掌握JSONPath表达式**：快速定位复杂JSON数据  
3. **实战处理时间戳与编码问题**  
4. **综合应用**：将B站热门视频数据转为结构化CSV文件  

---

### 🧠 **核心知识体系**
#### **1. JSON基础与进阶（1小时）**
**学习资源**：  
- **[JSON官方文档](https://www.json.org/json-en.html)**（快速理解语法规范）  
- **[JSONPath在线测试工具](https://jsonpath.com/)**（实时验证表达式）  

**核心知识点**：  
| 概念                | 说明                                                                 | 示例（B站API数据片段）                            |
|---------------------|---------------------------------------------------------------------|-------------------------------------------------|
| **JSON结构**         | 键值对集合，支持对象（`{}`）和数组（`[]`）嵌套                         | `{"data": [{"aid": 123, "title": "视频标题"}]}` |
| **JSONPath表达式**   | 类似XPath，用于快速定位JSON节点                                      | `$.data[*].title`（提取所有标题）               |
| **时间戳处理**       | 将Unix时间戳（如`1696147200`）转为可读日期                           | `datetime.fromtimestamp(1696147200)` → `2023-10-01` |
| **Unicode编码**      | 处理中文等非ASCII字符（`ensure_ascii=False`）                       | `json.dumps(data, ensure_ascii=False)`          |

---

#### **2. 工具准备：JSON Viewer（0.5小时）**
**Chrome插件安装**：  
1. 访问 [Chrome应用商店-JSON Viewer](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh)  
2. 点击「添加至Chrome」安装  
3. 打开B站API链接（https://api.bilibili.com/x/web-interface/popular），自动格式化JSON  

**功能亮点**：  
- 折叠/展开JSON层级  
- 搜索关键词快速定位节点  

---

#### **3. JSONPath实战（1.5小时）**
**语法对照表**：  
| 表达式             | 说明                          | 示例（B站API数据）                  |
|-------------------|-----------------------------|------------------------------------|
| `$`               | 根节点                       | `$`                               |
| `.key` 或 `['key']` | 获取子节点                   | `$.data[*].title`                 |
| `*`               | 通配符（匹配所有元素）         | `$.data[*].owner.name`            |
| `..`              | 递归搜索                     | `$..name`（搜索所有name字段）       |
| `[start:end]`     | 数组切片                     | `$.data[0:5]`（前5条数据）         |
| `?(表达式)`         | 过滤条件                     | `$.data[?(@.view > 1000000)]`     |

**练习任务**：  
使用 [JSONPath在线测试工具](https://jsonpath.com/) 解析以下数据：  
```json
{
  "data": [
    {
      "aid": 123,
      "title": "Python入门教程",
      "owner": {"mid": 1001, "name": "教育频道"},
      "stat": {"view": 1500000, "like": 50000},
      "pubdate": 1696147200
    },
    {
      "aid": 456,
      "title": "机器学习实战",
      "owner": {"mid": 2002, "name": "科技频道"},
      "stat": {"view": 800000, "like": 30000},
      "pubdate": 1696060800
    }
  ]
}
```
- 任务1：提取所有视频标题 → `$.data[*].title`  
- 任务2：提取播放量超过100万的视频 → `$.data[?(@.stat.view > 1000000)]`  
- 任务3：提取所有UP主名称 → `$.data[*].owner.name`  

---

#### **4. 时间戳转换（0.5小时）**
**核心代码**：  
```python
from datetime import datetime

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
print(timestamp)  # 输出：1696147200（假设时区正确）
```

---

### 🛠️ **综合实战：B站热门视频数据处理**
#### **任务目标**  
1. 调用B站热门视频API获取数据  
2. 解析嵌套JSON并提取关键字段  
3. 处理时间戳和Unicode字符  
4. 保存为CSV文件  

---

#### **步骤详解**
**1. 获取API数据**  
```python
import requests

url = "https://api.bilibili.com/x/web-interface/popular"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)
data = response.json()  # 自动将响应内容解析为字典
```

**2. 解析嵌套JSON结构**  
观察B站API返回的数据结构（使用JSON Viewer）：  
```json
{
  "code": 0,
  "data": [
    {
      "aid": 123,
      "bvid": "BV1Ab4y1q7xx",
      "title": "视频标题",
      "owner": {"name": "UP主名称"},
      "stat": {"view": 1000000, "like": 50000},
      "pubdate": 1696147200
    }
  ]
}
```

**3. 提取数据并转换时间戳**  
```python
from datetime import datetime
import csv

# 提取关键字段
videos = []
for video in data["data"]:
    pubdate = datetime.fromtimestamp(video["pubdate"]).strftime("%Y-%m-%d %H:%M:%S")
    videos.append({
        "aid": video["aid"],
        "bvid": video["bvid"],
        "title": video["title"],
        "up主": video["owner"]["name"],
        "播放量": video["stat"]["view"],
        "点赞数": video["stat"]["like"],
        "发布时间": pubdate
    })

# 保存为CSV（处理Unicode）
with open("bilibili_hot.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["aid", "bvid", "title", "up主", "播放量", "点赞数", "发布时间"])
    writer.writeheader()
    writer.writerows(videos)
```

**关键点**：  
- `encoding="utf-8-sig"`：解决Excel打开CSV文件乱码问题  
- `csv.DictWriter`：自动处理字段对齐  

---

### ⚠️ **常见问题与解决方案**
#### **问题1：嵌套层级过深**  
**场景**：  
```json
{
  "user": {
    "profile": {
      "social": {"weibo": "https://weibo.com/xxx"}
    }
  }
}
```
**解决**：  
- 使用JSONPath：`$..weibo`  
- 防御性编程：  
  ```python
  weibo_url = data.get("user", {}).get("profile", {}).get("social", {}).get("weibo", "")
  ```

#### **问题2：性能优化**  
**场景**：处理超大规模JSON文件（>1GB）  
**解决**：  
- 使用流式解析库：`ijson`  
  ```python
  import ijson
  with open("large.json", "r") as f:
      for item in ijson.items(f, "data.item"):
          process(item)
  ```

---

### ✅ **验收标准**
1. **基础能力**  
   - [ ] 能使用JSONPath表达式提取嵌套数据  
   - [ ] 能正确转换Unix时间戳为可读格式  

2. **实战成果**  
   - [ ] 成功运行B站数据处理代码，生成有效CSV文件  
   - [ ] CSV文件在Excel中打开无乱码  

3. **扩展挑战**  
   - [ ] 尝试解析更复杂的API（如微博热搜榜）  
   - [ ] 将数据存入SQLite数据库（使用`sqlite3`模块）  

---

### 📚 **扩展资源**
1. **书籍推荐**：  
   - 《Python数据科学手册》第2章 - 数据清洗与预处理  
2. **在线工具**：  
   - [JSON转CSV在线工具](https://www.convertcsv.com/json-to-csv.htm)（对比手动实现差异）  
3. **API资源**：  
   - [公开API集合](https://public-apis.io/)（寻找练习项目）  

通过今日学习，你将掌握JSON数据处理的核心技能，为后续动态页面抓取和数据分析打下坚实基础！遇到问题随时提问。