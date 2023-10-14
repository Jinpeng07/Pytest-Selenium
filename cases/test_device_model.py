import time

import pytest
from selenium.webdriver.common.by import By

from util.webUI import smpUI
from cfg import *


@pytest.fixture(scope='module')
def inDeviceModelMgr():
    print('\n设备管理页面 setup **')
    smpUI.login_check('byhy', 'sdfsdf')
    time.sleep(1)
    smpUI.wd.get(SMP_URL_DEVICE_MODEL)
    yield
    print('\n设备管理页面 teardown **')


@pytest.fixture()
def delAddedDeviceModel():
    print('\n删除添加的设备型号 setup **')
    smpUI.del_all_devices()
    yield
    print('\n删除添加的设备型号 teardown')
    # smpUI.del_all_devices()


def test_SMP_device_model_001(inDeviceModelMgr, delAddedDeviceModel):
    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()

    smpUI.add_device_model(
        "存储柜",
        'elife-canbinlocker-g22-10-20-40',
        '南京e生活存储柜-10大20中40小')

    dms = smpUI.get_first_page_device_models()
    assert dms == [[
        "存储柜",
        'elife-canbinlocker-g22-10-20-40',
        '南京e生活存储柜-10大20中40小'
    ]]


def test_SMP_device_model_002(inDeviceModelMgr, delAddedDeviceModel):
    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_device_model(
        "存储柜",
        '韩' * 100,
        '南京e生活存储柜-10大20中40小')
    dms = smpUI.get_first_page_device_models()
    assert dms == [[
        "存储柜",
        '韩' * 100,
        '南京e生活存储柜-10大20中40小'
    ]]

def test_SMP_device_model_003(inDeviceModelMgr, delAddedDeviceModel):
    # 点击添加按钮
    topBtn = smpUI.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span')
    if topBtn.text == '添加':
        topBtn.click()
    smpUI.add_device_model(
        "存储柜",
        '111',
        '南京e生活存储柜-10大20中40小')
    smpUI.add_device_model(
        "存储柜",
        '2222',
        '南京e生活存储柜-10大20中40小')
    smpUI.add_device_model(
        "存储柜",
        '333',
        '南京e生活存储柜-10大20中40小')
    dms = smpUI.get_first_page_device_models()
    assert dms == [
        ['存储柜', '333', '南京e生活存储柜-10大20中40小'],
        ['存储柜', '2222', '南京e生活存储柜-10大20中40小'],
        ['存储柜', '111', '南京e生活存储柜-10大20中40小']
    ]
