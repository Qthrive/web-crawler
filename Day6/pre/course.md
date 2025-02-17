以下是针对 **Day 6：综合训练** 的详细学习计划，结合你已掌握的核心技能（Requests、XPath、JSON、文件操作等），通过实战项目系统巩固爬虫全流程能力。

---

### 📅 **今日学习目标**
1. **完整爬虫项目开发**：从数据抓取到存储的全流程实现  
2. **SQLite数据库实战**：掌握结构化数据持久化方法  
3. **自动化报告生成**：用Markdown输出结构化日报  
4. **PyCharm调试技巧**：提升代码排错效率  

---

### 🛠️ **工具与环境准备**
1. **PyCharm调试功能**：  
   - 设置断点：点击代码行号左侧灰色区域  
   - 快捷键：`F8`（单步执行），`F9`（恢复执行）  
   - 查看变量：调试面板的「Variables」窗口  

2. **SQLite可视化工具**（可选）：  
   - [DB Browser for SQLite](https://sqlitebrowser.org/)  
   - 查看数据库结构和数据  

---

### 🧩 **任务1：开发天气爬虫（中国天气网）**
#### **步骤详解**
**1. 目标分析**  
访问 [中国天气网](http://www.weather.com.cn/)，抓取指定城市（如北京）的实时天气数据，包括：  
- 温度  
- 天气状况  
- 湿度  
- 风力  

**2. 页面结构分析**  
使用Chrome开发者工具（F12）分析北京天气页面：  
- 页面URL：`http://www.weather.com.cn/weather1d/101010100.shtml`  
- 目标数据位置（XPath）：  
  ```xpath
  //div[@class="today"]//div[@class="tem"]/text()                # 温度
  //div[@class="today"]//p[@class="wea"]/text()                 # 天气状况
  //div[@class="today"]//li[@class="hum"]/span/text()           # 湿度
  //div[@class="today"]//li[@class="win"]/span/text()           # 风力
  ```

**3. 完整代码实现**  
```python
import requests
from lxml import etree
import sqlite3

def fetch_weather(city_code="101010100"):
    url = f"http://www.weather.com.cn/weather1d/{city_code}.shtml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"  # 解决中文乱码
    tree = etree.HTML(response.text)
    
    weather_data = {
        "temperature": tree.xpath('//div[@class="today"]//div[@class="tem"]/text()')[0].strip(),
        "condition": tree.xpath('//div[@class="today"]//p[@class="wea"]/text()')[0],
        "humidity": tree.xpath('//div[@class="today"]//li[@class="hum"]/span/text()')[0],
        "wind": tree.xpath('//div[@class="today"]//li[@class="win"]/span/text()')[0]
    }
    return weather_data

# 测试
print(fetch_weather())
```

---

### 🧩 **任务2：数据持久化（SQLite存储）**
#### **步骤详解**
**1. 数据库设计**  
创建表结构：  
```sql
CREATE TABLE weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    temperature TEXT,
    condition TEXT,
    humidity TEXT,
    wind TEXT,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**2. 数据库操作代码**  
```python
def save_to_db(data, city="北京"):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    
    # 建表（如果不存在）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature TEXT,
            condition TEXT,
            humidity TEXT,
            wind TEXT,
            update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 插入数据
    cursor.execute('''
        INSERT INTO weather (city, temperature, condition, humidity, wind)
        VALUES (?, ?, ?, ?, ?)
    ''', (city, data["temperature"], data["condition"], data["humidity"], data["wind"]))
    
    conn.commit()
    conn.close()

# 结合爬虫使用
weather_data = fetch_weather()
save_to_db(weather_data)
```

---

### 🧩 **任务3：编写Markdown日报**
#### **步骤详解**
**1. 从数据库读取最新数据**  
```python
def get_latest_weather():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather ORDER BY update_time DESC LIMIT 1")
    latest = cursor.fetchone()
    conn.close()
    return latest

# 返回结果示例：(1, '北京', '25℃', '晴', '45%', '3级', '2023-10-05 14:30:00')
```

**2. 生成Markdown文件**  
```python
def generate_md_report():
    data = get_latest_weather()
    report = f"""# 天气日报 ({data[5]})

| 城市 | 温度 | 天气状况 | 湿度 | 风力 |
|------|------|----------|------|------|
| {data[1]} | {data[2]} | {data[3]} | {data[4]} | {data[5]} |

**数据来源**：中国天气网
"""
    with open("weather_report.md", "w", encoding="utf-8") as f:
        f.write(report)

# 执行生成
generate_md_report()
```

---

### 🔍 **调试技巧与常见问题**
#### **PyCharm调试重点**
1. **变量监控**：  
   - 在「Variables」面板查看爬取到的原始HTML  
   - 检查XPath解析后的数据格式  

2. **数据库事务调试**：  
   - 在插入数据前后设置断点  
   - 使用DB Browser验证数据是否写入  

#### **常见问题解决方案**
| 问题现象                  | 可能原因                | 解决方案                          |
|--------------------------|-----------------------|---------------------------------|
| 爬取数据为空              | XPath路径错误          | 用Chrome开发者工具重新验证XPath    |
| 中文乱码                 | 编码未正确设置          | 添加 `response.encoding = "utf-8"` |
| 数据库写入失败           | 表结构不匹配           | 删除旧数据库文件后重新运行          |
| Markdown表格不对齐       | 缺失对齐符号           | 确保第二行包含 `|---|` 对齐标记     |

---

### ✅ **验收标准**
1. **基础功能**  
   - [ ] 成功运行天气爬虫并打印数据  
   - [ ] 数据库中出现至少3条不同时间点的记录  

2. **高级要求**  
   - [ ] Markdown日报包含完整表格和时间戳  
   - [ ] 使用PyCharm调试解决至少一个实际问题  

3. **扩展挑战**  
   - [ ] 实现多城市抓取（如上海：`101020100`）  
   - [ ] 在日报中添加折线图（需转存为HTML+Matplotlib）  

---

### 📚 **延伸学习资源**
1. **SQLite官方文档**：  
   - [Python SQLite3模块指南](https://docs.python.org/3/library/sqlite3.html)  

2. **Markdown高级语法**：  
   - [Markdown表格生成器](https://www.tablesgenerator.com/markdown_tables)  

3. **可视化扩展**：  
   - [Matplotlib入门教程](https://matplotlib.org/stable/tutorials/index.html)  

通过今日综合训练，你将完成首个完整的爬虫项目，掌握数据采集-存储-展示的全流程技能！遇到问题随时提问。