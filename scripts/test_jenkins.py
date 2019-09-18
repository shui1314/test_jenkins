import allure


class TestJen:

    @allure.step("测试步骤")
    def test_001(self):
        allure.attach("附件名称", "附件内容")
        assert True