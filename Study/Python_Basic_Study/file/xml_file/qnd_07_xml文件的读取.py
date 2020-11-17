# 导入模块
import xml.dom.minidom

# 定义一个变量保存文件名
file_name = "xml.xml"

# 打开xml文档
domTree = xml.dom.minidom.parse(file_name)

# 返回文档的根节点
root = domTree.documentElement

# 返回带有指定标签名的对象的集合(在集合中获取所有电影)
musics = root.getElementsByTagName("music")

# 打印每部电影的详细信息
for music in musics:

    print("------音乐------")
    # 如果元素的属性为title
    if music.hasAttribute("title"):
        print("歌名: %s" % music.getAttribute("title"))

    # 格式
    type = music.getElementsByTagName("format")[0]
    print("-格式: %s" % type.childNodes[0].data)
    year = music.getElementsByTagName("year")[0]
    print("-年份: %s" % year.childNodes[0].data)
    month = music.getElementsByTagName("month")[0]
    print("-月份: %s" % month.childNodes[0].data)
    start = music.getElementsByTagName("stars")[0]
    print("-星数: %s" % start.childNodes[0].data)
    desc = music.getElementsByTagName("description")[0]
    print("-描述:%s" % desc.childNodes[0].data)