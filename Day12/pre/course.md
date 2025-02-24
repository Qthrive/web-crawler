以下是针对 **Day 12：效率优化** 的详细学习计划，结合你已掌握的爬虫技能，通过多线程、缓存和增量抓取技术，显著提升爬虫性能和可靠性。

---

### 📅 **今日学习目标**
1. **多线程爬虫**：利用并发提升抓取速度  
2. **请求缓存**：减少重复请求，节省资源  
3. **增量爬取**：实现断点续爬和数据去重  

---

### 🛠️ **工具与库准备**
1. **安装依赖库**：
   ```bash
   pip install requests sqlalchemy concurrent-log-handler
   ```
2. **推荐工具**：
   - **数据库管理**：[DB Browser for SQLite](https://sqlitebrowser.org/)  
   - **性能分析**：Python内置 `cProfile` 模块  

---

### 📚 **核心学习资源**
1. **多线程编程**：
   - [Python官方文档 - concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)  
2. **缓存机制**：
   - [Python磁盘缓存最佳实践](https://realpython.com/python-data-classes/#caching)  
3. **增量爬取**：
   - [Scrapy增量爬取实现原理](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#duplicates-filter)  

---

### 🧩 **模块一：多线程爬虫实战**
#### **1.1 单线程 vs 多线程对比**
**单线程爬虫**（耗时约30秒）：
```python
import requests
from lxml import etree

def fetch_page(url):
    response = requests.get(url)
    tree = etree.HTML(response.text)
    titles = tree.xpath('//h2/text()')
    return titles

urls = [f"https://example.com/page/{i}" for i in range(1, 11)]

# 单线程执行
results = []
for url in urls:
    results.extend(fetch_page(url))
print(f"抓取完成，共{len(results)}条数据")
```

**多线程爬虫**（耗时约5秒）：
```python
from concurrent.futures import ThreadPoolExecutor

def fetch_page_concurrent(urls, max_workers=4):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_page, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            results.extend(future.result())
    return results

results = fetch_page_concurrent(urls)
print(f"多线程抓取完成，共{len(results)}条数据")
```

#### **1.2 线程安全注意事项**
- **共享资源加锁**：使用 `threading.Lock` 保护数据库写入等操作  
- **控制并发量**：避免触发目标网站反爬机制（建议5-10线程）  

---

### 🧩 **模块二：请求缓存实现**
#### **2.1 磁盘缓存方案**
使用SQLite存储已抓取数据：
```python
import sqlite3
from hashlib import md5

class DiskCache:
    def __init__(self, db_path="cache.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()
    
    def _create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                value TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    
    def get(self, url):
        key = md5(url.encode()).hexdigest()
        cursor = self.conn.execute("SELECT value FROM cache WHERE key=?", (key,))
        row = cursor.fetchone()
        return row[0] if row else None
    
    def set(self, url, data):
        key = md5(url.encode()).hexdigest()
        self.conn.execute("REPLACE INTO cache (key, value) VALUES (?, ?)", (key, data))
        self.conn.commit()

# 使用示例
cache = DiskCache()
url = "https://example.com/data"

# 优先读取缓存
cached_data = cache.get(url)
if not cached_data:
    response = requests.get(url)
    cache.set(url, response.text)
    data = response.text
else:
    data = cached_data
```

---

### 🧩 **模块三：增量爬取策略**
#### **3.1 时间戳记录法**
```python
import sqlite3
import time

class ProgressTracker:
    def __init__(self, db_path="progress.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()
    
    def _create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS progress (
                id INTEGER PRIMARY KEY,
                last_timestamp FLOAT
            )
        ''')
    
    def get_last_timestamp(self):
        cursor = self.conn.execute("SELECT last_timestamp FROM progress ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        return row[0] if row else 0
    
    def update_timestamp(self, timestamp):
        self.conn.execute("INSERT INTO progress (last_timestamp) VALUES (?)", (timestamp,))
        self.conn.commit()

# 使用示例
tracker = ProgressTracker()
last_time = tracker.get_last_timestamp()

# 抓取新数据
new_data = fetch_new_data_since(last_time)

if new_data:
    current_time = time.time()
    tracker.update_timestamp(current_time)
```

---

### ✅ **验收标准**
1. **基础能力**  
   - [ ] 多线程爬虫速度达到单线程3倍以上  
   - [ ] 实现SQLite缓存，减少重复请求50%以上  

2. **进阶能力**  
   - [ ] 增量爬取能准确跳过已处理数据  
   - [ ] 在多线程环境下安全读写数据库  

3. **扩展挑战**  
   - [ ] 添加缓存过期机制（如24小时自动清除）  
   - [ ] 实现分布式爬虫进度同步（使用Redis）  

---

### ⚠️ **常见问题与解决方案**
| 问题现象                  | 解决方案                          |
|--------------------------|---------------------------------|
| 数据库写入冲突           | 使用线程锁（`threading.Lock`）     |
| 缓存占用磁盘空间过大     | 添加LRU淘汰机制                  |
| 增量时间戳不准确         | 使用唯一ID代替时间戳             |

---

### 📚 **延伸学习资源**
1. **高级并发**：
   - [Python asyncio异步爬虫实战](https://realpython.com/async-io-python/)  
2. **分布式爬虫**：
   - [Scrapy-Redis分布式爬虫架构](https://github.com/rmax/scrapy-redis)  
3. **性能优化**：
   - [Python性能分析指南](https://docs.python.org/3/library/profile.html)  

通过今日学习，你将掌握高效爬虫的核心优化技术，为处理大规模数据采集任务奠定基础！遇到问题随时提问。