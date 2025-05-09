import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # 配置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # 从环境变量获取token
    token = os.getenv("DUODUO_TOKEN")
    if not token:
        raise ValueError("DUODUO_TOKEN环境变量未设置")
    
    # 初始化WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    try:
        driver.get("https://www.duoduo.link/")
        
        # 注入token
        driver.execute_script(
            f'window.localStorage.setItem("auth-store", \'{{"token":"Bearer {token}"}}\');'
        )
        driver.refresh()
        time.sleep(3)  # 等待页面加载
        
        # 尝试签到
        try:
            button = driver.find_element(
                By.XPATH,
                '//*[@id="app"]//div[contains(@class,"font-num") and contains(., "签到")]'
            )
            button.click()
            print("签到成功！")
        except Exception as e:
            print(f"签到按钮未找到或点击失败: {str(e)}")
            
        time.sleep(5)  # 等待操作完成
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
