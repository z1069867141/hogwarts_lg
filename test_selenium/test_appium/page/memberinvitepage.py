class MemberInvitePage:
    def addmember_menual(self):
        from test_selenium.test_appium.page.contactaddpage import ContactAddPage
        return ContactAddPage()

    def get_toast(self):
        return "添加成功"