### 安装jupyterlab环境(conda中进行)  
**创建jupyterlab使用环境**  
`conda create -n ju_env python=3.8`

**安装jupyterlab**  
`conda install -c conda-forge jupyterlab`

**汉化(控制台安装)(亲测失败)**  
`pip install jupyterlab-language-pack-zh-CN`

**汉化(手动下载安装)**  
[下载汉化文件](https://files.pythonhosted.org/packages/a9/78/f2eed3e44db0ba62ee0ad12d475b95690db4ea04a42566c72d81c6d83c50/jupyterlab_language_pack_zh_cn-4.3.post1-py2.py3-none-any.whl)  
`jupyterlab_language_pack_zh_cn-4.3.post1-py2.py3-none-any.whl`

**导航到下载文件夹安装(在对应环境)**  
`pip install jupyterlab_language_pack_zh_cn-4.3.post1-py2.py3-none-any.whl`

**安装完成后激活jupyterlab调设置**  
`jupyter lab`  
![切换中文](https://i-blog.csdnimg.cn/blog_migrate/a64bf7e072702cdfed69761f395fcba3.png)

