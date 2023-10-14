import time

import pytest
from selenium.webdriver.common.by import By

from lib.webUI import smpUI
from cfg import *


@pytest.fixture(scope='module')
def inServiceRuleMgr():
    smpUI.login_check('byhy', 'sdfsdf')
    time.sleep(1)
    smpUI.wd.get(SMP_URL_SERVICE_RULE)
    yield


@pytest.fixture()
def delAddedServiceRule():
    print('\n删除添加的ServiceRule setup **')
    smpUI.del_all_devices()
    yield
    print('\n删除添加的ServiceRule teardown')
    # smpUI.del_all_devices()


def test_SMP_device_model_001(inServiceRuleMgr, delAddedServiceRule):
    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_svc_rule(
        "全国-电瓶车充电费率1",
        "预付费-下发业务量",
        "0.1",
        "2",
        ['千瓦时', '1'],
        "")

    dms = smpUI.get_first_page_svc_rules()
    assert dms == [["全国-电瓶车充电费率1",
                    "预付费-下发业务量",
                    {'最小消费': '0.1', '预估消费': '2', '费率': '单位：千瓦时 \n单价：1'},
                    ''
                    ]
                   ]


