class things(object):
    def __init__(self, name, function, surface):
        self.name = name
        self.function = function
        self.surface = surface

    def description(self):
        print(f"名字：{self.name},功能：{self.function}，外貌：{self.surface}")


things1 = things("桌子", "陈放东西", "有四条腿")
things2 = things("椅子", "可以坐人", "有四条腿")
things3 = things("柜子", "可以储物", "由储存空间")
things4 = things("笔记本", "可以携带", "屏幕与电脑本身为一体")
things5 = things("电视", "可以看电影", "屏幕很大")
