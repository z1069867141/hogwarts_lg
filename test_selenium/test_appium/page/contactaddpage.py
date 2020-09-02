class ContactAddPage:
    def edit_name(self,name):
        return self

    def edit_gender(self,gender):
        return self

    def edit_phonenum(self,phonenum):
        return self

    def click_save(self):
        from test_selenium.test_appium.page.memberinvitepage import MemberInvitePage #通过使用局部导入只有在用这个方法的时候才调用，防止全局导入的时候初始化代码报错提示导入循环造成问题
        return MemberInvitePage()