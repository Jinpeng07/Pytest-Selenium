import pytest
from util.webUI import smpUI


def test_login_success():
    smpUI.login_check('byhy', 'sdfsdf')
    title = smpUI.wd.title
    assert title == 'E生活'


# @pytest.fixture(scope='function')
# def clear_alert():
#     yield
#     try:
#         login_page.wd.switch_to.alert.accept()
#     except Exception as e:
#         print(e)


@pytest.mark.parametrize('username, password, expected',
                         [
                             (None, 'sdfsdf', '请输入用户名'),
                             ('byhy', None, '请输入密码'),
                             ('byhy', 'sdfsd', '登录失败： 用户名或者密码错误'),
                             ('byhy', 'sdfsdff', '登录失败： 用户名或者密码错误'),
                             ('byh', 'sdfsdf', '登录失败： 用户名不存在'),
                             ('byhyy', 'sdfsdf', '登录失败： 用户名不存在'),
                         ]
                         )
def test_login_failed(username, password, expected):
    smpUI.login_check(username, password, expected)
