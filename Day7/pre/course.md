以下是针对 **Day 7：知识复盘** 的详细学习计划，结合你已掌握的核心技能，通过系统梳理和实战强化，帮助你全面巩固爬虫基础技术栈。

---

### 📅 **今日学习目标**
1. **核心概念复盘**：HTTP协议、请求方法、数据解析原理  
2. **工具深化**：Charles抓包工具实战应用  
3. **能力验证**：独立完成爬虫全流程开发  
4. **知识体系构建**：形成结构化知识图谱  

---

### 🧠 **模块一：HTTP协议深度理解**
#### **1.1 GET vs POST 对比**
| 维度          | GET请求                          | POST请求                        |
|---------------|---------------------------------|--------------------------------|
| **数据位置**   | URL参数（明文）                  | 请求体（可加密）                |
| **安全性**     | 低（浏览器历史记录可见）          | 较高（HTTPS下安全）            |
| **数据量限制** | 较小（URL长度限制，通常<2048字符）| 较大（理论无限制）              |
| **缓存**       | 可缓存                          | 不可缓存                       |
| **典型场景**   | 搜索、翻页、资源获取             | 登录、表单提交、文件上传        |

#### **1.2 实战验证**
用Requests库发送两种请求，观察差异：
```python
import requests

# GET请求（参数在URL）
get_response = requests.get("https://httpbin.org/get", params={"key1": "value1"})
print("GET URL:", get_response.url)  # 参数附加在URL

# POST请求（参数在请求体）
post_response = requests.post("https://httpbin.org/post", data={"key2": "value2"})
print("POST Body:", post_response.json()["form"])  # 参数在form字段
```

---

### 🛠️ **模块二：Charles抓包实战**
#### **2.1 工具准备**
- **下载安装**：[Charles官网](https://www.charlesproxy.com/)（免费试用30天）  
- **配置代理**：  
  1. 打开Charles -> Proxy -> Proxy Settings -> HTTP代理端口设为8888  
  2. 手机/电脑设置代理：IP为本机地址，端口8888  
- **SSL证书安装**（抓取HTTPS流量）：  
  Help -> SSL Proxying -> Install Charles Root Certificate  

#### **2.2 实战案例：分析B站API请求**
1. 清空Charles请求记录（Edit -> Clear Session）  
2. 浏览器访问 [B站热门视频API](https://api.bilibili.com/x/web-interface/popular)  
3. 在Charles中过滤出目标请求（Filter输入`bilibili`）  
4. 分析关键信息：  
   - **请求头**：`User-Agent`、`Cookie`  
   - **响应头**：`Content-Type`、`Cache-Control`  
   - **响应体**：JSON数据结构  

#### **2.3 高级技巧**
- **断点调试**：  
  Proxy -> Breakpoints -> 添加断点条件（修改请求/响应数据）  
- **流量重发**：  
  右键请求 -> Repeat / Repeat Advanced（压力测试）  
- **Map Local**：  
  将线上请求映射到本地文件（模拟接口响应）  

---

### 🧩 **模块三：XPath表达式强化训练**
#### **3.1 编写规范**
| 场景                  | 示例XPath表达式                            | 说明                        |
|-----------------------|-------------------------------------------|---------------------------|
| **基础定位**           | `//div[@class="title"]`                   | 按class属性定位            |
| **文本匹配**           | `//a[contains(text(),"登录")]`            | 包含"登录"文本的链接        |
| **层级嵌套**           | `//ul/li[2]/span`                         | 第二个li下的span            |
| **轴(Axis)应用**       | `//div//following-sibling::p`             | div之后的所有同级p元素      |
| **组合条件**           | `//input[@type="text" and @name="user"]`  | 同时满足type和name属性      |

#### **3.2 实战训练**
用以下HTML结构编写10个XPath表达式：
```html
<!DOCTYPE html>
<html>
<body>
  <div id="container">
    <ul class="list">
      <li data-id="1"><a href="/item1">Item 1</a></li>
      <li data-id="2"><a href="/item2" class="active">Item 2</a></li>
      <li data-id="3"><a href="/item3">Item 3</a></li>
    </ul>
    <div class="footer">
      <p>Copyright © 2023</p>
      <button onclick="submit()">Submit</button>
    </div>
  </div>
</body>
</html>
```

**参考答案**：  
1. 所有li元素：`//li`  
2. 第二个li元素：`//li[2]`  
3. 带有active类的链接：`//a[@class="active"]`  
4. data-id为2的li：`//li[@data-id="2"]`  
5. footer中的按钮：`//div[@class="footer"]/button`  
6. 包含"Copyright"的文本：`//p[contains(text(),"Copyright")]`  
7. li的直接父元素：`//li/parent::ul`  
8. Submit按钮的文本：`//button/text()`  
9. 所有href属性：`//a/@href`  
10. 最后一个li元素：`//li[last()]`  

---

### 🧪 **模块四：全流程综合验证**
#### **4.1 实战项目：豆瓣电影Top250数据抓取**
**目标**：抓取电影标题、评分、短评数量，存入CSV并生成分析报告  

**技术栈整合**：  
| 步骤           | 技术点                          | 代码示例片段                    |
|----------------|--------------------------------|--------------------------------|
| **请求数据**    | Requests + 请求头伪装           | `requests.get(url, headers=headers)` |
| **解析数据**    | XPath/lxml                     | `tree.xpath('//span[@class="title"]/text()')` |
| **存储数据**    | CSV文件写入                    | `csv.writerow([title, rating])` |
| **分析报告**    | Markdown表格生成               | `| 电影 | 评分 |`                          |

**完整代码框架**：
```python
import requests
from lxml import etree
import csv
from datetime import datetime

def fetch_douban_top250():
    headers = {"User-Agent": "Mozilla/5.0"}  # 伪装浏览器
    movies = []
    
    for page in range(0, 250, 25):  # 分页处理
        url = f"https://movie.douban.com/top250?start={page}"
        response = requests.get(url, headers=headers)
        tree = etree.HTML(response.text)
        
        for item in tree.xpath('//div[@class="item"]'):
            title = item.xpath('.//span[@class="title"]/text()')[0]
            rating = item.xpath('.//span[@class="rating_num"]/text()')[0]
            comment_count = item.xpath('.//div[@class="star"]/span[last()]/text()')[0]
            movies.append([title, rating, comment_count])
    
    # 存储CSV
    with open("douban_top250.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["标题", "评分", "短评数"])
        writer.writerows(movies)
    
    # 生成报告
    report = f"# 豆瓣Top250报告 ({datetime.now().strftime('%Y-%m-%d')})\n\n"
    report += "| 排名 | 标题 | 评分 |\n|------|------|------|\n"
    for idx, movie in enumerate(movies[:10], 1):
        report += f"| {idx} | {movie[0]} | {movie[1]} |\n"
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(report)

fetch_douban_top250()
```

---

### ✅ **验收标准自查表**
1. **HTTP协议**  
   - [ ] 能准确描述GET/POST的5个以上区别点  
   - [ ] 能用Charles捕获并分析HTTPS请求  

2. **XPath能力**  
   - [ ] 能独立编写包含轴和谓语的复杂XPath  
   - [ ] 能解释`//div[@class="a"]/span[2]`的含义  

3. **全流程开发**  
   - [ ] 成功运行豆瓣爬虫并生成CSV文件  
   - [ ] Markdown报告包含前10名电影的表格  

---

### 📚 **延伸学习资源**
1. **HTTP协议**  
   - [MDN HTTP文档](https://developer.mozilla.org/zh-CN/docs/Web/HTTP)  
   - [图解HTTP（书籍）](https://book.douban.com/subject/25863515/)  

2. **Charles高级功能**  
   - [Charles官方教程](https://www.charlesproxy.com/documentation/)  
   - [移动端抓包实战指南](https://www.jianshu.com/p/4b3d64b43d5c)  

3. **XPath进阶**  
   - [XPath轴完全指南](https://www.w3schools.com/xml/xpath_axes.asp)  
   - [XPath函数手册](https://devhints.io/xpath)  

通过今日系统复盘，你将建立起完整的爬虫知识体系，为后续动态页面抓取和反爬对抗打下坚实基础！