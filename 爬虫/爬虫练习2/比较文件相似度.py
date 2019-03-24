from fuzzywuzzy import fuzz


# 输出相似度
print(fuzz.ratio("我喜欢打游戏, 你呢", "我喜欢看电影, 不喜欢打游戏"))
print(fuzz.ratio("按时打卡积分哈开始介绍的划分来看", "按时打卡积分哈开始介绍的划分来看"))