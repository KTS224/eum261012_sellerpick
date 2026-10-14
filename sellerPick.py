import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# 안정적인 대기를 위해 아래 두 줄을 새로 추가했습니다.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 크롬 디버깅 연결
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# 2. 첫 번째 요소(span) 클릭할 때까지 안전하게 대기 후 클릭
# (최대 10초 동안 화면에 나타나길 기다립니다)
first_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/span[1]"))
)
first_element.click()

# 3. 두 번째 버튼(button[6])이 화면에 나타나고 클릭 가능해질 때까지 대기 후 클릭
# (첫 번째 클릭 후 화면이 바뀔 때 발생하는 타이밍 에러를 완벽히 잡아줍니다)
try:
    second_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/div/button[6]"))
    )
    second_element.click()
    print("두 개의 버튼을 모두 성공적으로 클릭했습니다!")
    
except Exception as e:
    # 만약 웹사이트 반응이 느려 10초 안에 안 나타나면 자바스크립트로 강제 클릭을 시도합니다.
    print("일반 클릭 실패, 자바스크립트 강제 클릭을 시도합니다.")
    second_element = driver.find_element(By.XPATH, "//div[2]/div[1]/div/button[6]]")
    driver.execute_script("arguments[0].click();", second_element)




# 1. 이전 버튼 클릭 후 이미지가 로딩될 때까지 1초간 안전하게 대기
time.sleep(1)

# 2. 지정한 경로 '하위 전체(//)'에서 img 태그가 있는지 찾아서 리스트로 저장
# 주소 맨 끝에 //img 가 붙은 점을 확인하세요!
target_path = '//*[@id="mainCkEditorDiv"]/div[2]/div[2]/div//img'
images = driver.find_elements(By.XPATH, target_path)

# 3. 이미지 개수로 유무 판단하기
if len(images) > 0:
    print(f"★ 이미지가 존재합니다! (발견된 이미지 개수: {len(images)}개)")
    # [조건 A] 이미지가 있을 때 수행할 코드 작성 위치
    # 상품명/키워드 [상단버튼]
    first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div/div[2]/div[1]/div/button[2]"))
    )
    first_element.click()
    
    time.sleep(1)
    
    # ai 다듬기 버튼 누르기
    first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[1]/div[2]/div[1]/div[2]/button[3]"))
    )
    first_element.click()
    
    time.sleep(3)
    
    # 옵션 [상단버튼]
    first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div/div[2]/div[1]/div/button[3]"))
    )
    first_element.click()
    
    time.sleep(1)
    # Ai 옵션명 다듬기 버튼 누르기
    first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pmOptionWrap"]/div[1]/div[1]/div[2]/div/button[2]'))
    )
    first_element.click()
    
    time.sleep(5)
    
    # 판매가 관리 [상단버튼]
    first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div/div[2]/div[1]/div/button[4]"))
    )
    first_element.click()
    
    time.sleep(1)
    
    # 가격정렬 누르기
    first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pmPriceWrap"]/div[3]/div[2]/button[4]'))
    )
    first_element.click()
    
    ## TODO: 체크박스 8개만 설정하기 
    #       if 8이하면 통과
    #       8개 이상이면 8개만 체크하기
    
    ## TODO: 업로드관리상품 누르기
    
    # TODO: 우측 그룹 work_end 선택하기

    
else:
    print("☆ 하위 항목에 이미지가 없습니다.")
    # [조건 B] 삭제
    
    
    
##  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"
##  터미널에 실행 후 로그인. FOR MAC OS
    
    