import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

    
    ##  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"
    ##  터미널에 실행 후 로그인. FOR MAC OS
    
# 1. 메인 실행 로직 (맨 위에 위치하여 가독성이 좋음)
def main():
    print("프로그램을 시작합니다.")
    


    count = int(input("반복할 횟수를 입력하세요: "))
    for i in range(count):
        print(f"===================={i + 1}번째 시작=============={i + 1} / {count} ======")
        doWork()
        time.sleep(2)
        print(f"===================={i + 1}번째 작업 완료====================")

def doWork():
    changeGruopTo("work_work")
    
    try:
        # 1. 해당 요소가 화면에 나타나고 글자가 보일 때까지 최대 15초 대기합니다.
        toolbar_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="pdToolbar"]/span[2]/b'))
        )
        
        # 2. .text 속성을 사용해 태그 사이에 있는 글자를 가져옵니다.
        toolbar_text = toolbar_element.text
        
        # 3. 콘솔 창에 출력합니다.
        print(f"📊 현재 아이템 개수: {toolbar_text}")

    except Exception as e:
        print("❌ 아이탬개수 출력중 오류가 발생했습니다:", e)
        
        
        
        
    # 2. 첫 번째 요소(span) 클릭할 때까지 안전하게 대기 후 클릭
    # (최대 10초 동안 화면에 나타나길 기다립니다)
    ## ++++++상품번호 누름 시작++++++
    first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/span[1]"))
    )
    first_element.click()

    # 3. 두 번째 버튼(button[6])이 화면에 나타나고 클릭 가능해질 때까지 대기 후 클릭
    # (첫 번째 클릭 후 화면이 바뀔 때 발생하는 타이밍 에러를 완벽히 잡아줍니다)
    ## ++++++ [썸네일/상품설명]누름 ++++++++++
    try:
        second_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[2]/div[1]/div/button[6]"))
        )
        second_element.click()
        print("[썸네일/상품설명] 누름")
        
    except Exception as e:
        # 만약 웹사이트 반응이 느려 10초 안에 안 나타나면 자바스크립트로 강제 클릭을 시도합니다.
        print("일반 클릭 실패, 자바스크립트 강제 클릭을 시도합니다.")
        second_element = driver.find_element(By.XPATH, "//div[2]/div[1]/div/button[6]]")
        driver.execute_script("arguments[0].click();", second_element)

    try:
        print("⏳ 동영상 라디오 박스 상태 확인 중...")
        
        # 1. 요소가 화면에 로드될 때까지 최대 15초 대기합니다.
        video_radio = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="deVideo"]'))
        )
        
        # 2. .is_selected()로 현재 체크 상태를 확인합니다.
        if video_radio.is_selected():
            print("💡 [체크 상태 발견] 동영상 라디오 박스가 켜져 있습니다. 해제를 시도합니다.")
            
            # 3. 켜져 있으므로 자바스크립트로 정확히 강제 클릭(해제)을 수행합니다.
            driver.execute_script("arguments[0].click();", video_radio)
            print("🎯 동영상 라디오 박스 해제 완료!")
            
            # 반영을 위한 아주 짧은 대기
            time.sleep(1)
        else:
            print("➡️ [미체크 상태] 동영상 라디오 박스가 이미 꺼져 있으므로 아무것도 하지 않고 넘어갑니다.")

    except Exception as e:
        print("❌ 동영상 라디오 박스를 판단/조작하는 중 오류가 발생했습니다:", e)



    # 1. 이전 버튼 클릭 후 이미지가 로딩될 때까지 1초간 안전하게 대기
    time.sleep(1)

    # 2. 지정한 경로 '하위 전체(//)'에서 img 태그가 있는지 찾아서 리스트로 저장
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
        
        # AI 키워드추천 버튼 누르기
        first_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[1]/div[2]/div[1]/div[2]/button[3]"))
        )
        first_element.click()
        print("AI 키워드추천 버튼 누르기 완료!")
        
        time.sleep(5)
        
        # 옵션 [상단버튼]
        first_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div/div[2]/div[1]/div/button[3]"))
        )
        first_element.click()
        print("옵션 [상단버튼] 누르기 완료!")
        
        time.sleep(1)
        # AI 옵션명 다듬기 버튼 누르기
        first_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="pmOptionWrap"]/div[1]/div[1]/div[2]/div/button[2]'))
        )
        first_element.click()
        print("AI 옵션명 다듬기 버튼 누르기 완료!")
        
        time.sleep(5)
        
        # 판매가 관리 [상단버튼]
        first_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div/div[2]/div[1]/div/button[4]"))
        )
        first_element.click()
        print("판매가 관리 [상단버튼] 버튼 누르기 완료!")
        
        time.sleep(1)
        
        # 가격정렬 누르기
        first_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="pmPriceWrap"]/div[3]/div[2]/button[4]'))
        )
        first_element.click()
        print("가격정렬 버튼 누르기 완료 ##")
        
        
        # 1. 15개의 큰 줄(div) 주소 모으기
        item_row_xpath = '//*[@id="spList"]/div'
        all_rows = driver.find_elements(By.XPATH, item_row_xpath)
        print(f"★ 전체 항목 개수: {len(all_rows)}개")

        # 2. 현재 체크박스가 켜져 있는 항목들만 골라내기
        checked_inputs = []  # 이미 체크된 인풋들을 담을 리스트

        for row in all_rows:
            try:
                actual_input = row.find_element(By.XPATH, "./span/input")
                
                # .is_selected()는 체크박스가 선택되어 있으면 True, 안 되어있으면 False를 반환합니다.
                if actual_input.is_selected():
                    checked_inputs.append(actual_input)
            except:
                pass

        current_checked_count = len(checked_inputs)
        print(f"📊 현재 체크되어 있는 개수: {current_checked_count}개")

        ##### Q1. 만약 체크박스 아이템 수가 7개 인데 현재 체크된 아이템수가 5개 일 경우는 나머지를 체크해서 7를 누른 후 통과하는지 // 그냥 통과하는지.

        # [상황 1] 체크된 개수가 8개 미만(적다면) -> 최대 8개까지 모자란 만큼 추가로 체크하기
        if current_checked_count < 8:
            print(f"⚠️ 현재 {current_checked_count}개만 체크되어 있습니다. 최대 8개까지 추가 체크를 시작합니다.")
            
            # 전체 항목(all_rows) 중 최대 앞의 8개까지만 타겟으로 잡습니다.
            # 만약 전체 항목이 5개뿐이라면 5개까지만 잡힙니다.
            target_rows = all_rows[:8]
            
            for index, row in enumerate(target_rows, start=1):
                try:
                    actual_input = row.find_element(By.XPATH, "./span/input")
                    
                    # 💡 핵심: 아직 체크가 안 되어 있는(False) 항목만 찾아서 클릭합니다.
                    if not actual_input.is_selected():
                        driver.execute_script("arguments[0].click();", actual_input)
                        # print(f"[{index}번째 항목] 미체크 상태 확인 -> 추가 체크 완료")
                        time.sleep(0.2)
                    else:
                        # print(f"[{index}번째 항목] 이미 체크되어 있음 -> 패스")
                        
                except Exception as e:
                    print(f"{index}번째 항목 추가 체크 중 오류 발생:", e)
                    
            print("✨ 8개 미만일 때의 모자란 체크 채우기 작업을 완료했습니다!")


        # [상황 2] 체크된 개수가 8개 이상인 경우 -> 앞의 8개만 남기고 9번째부터는 체크 해제
        else:
            print("🧹 8개보다 많이 체크되어 있습니다. 9번째 항목부터 체크 해제를 시작합니다.")
            
            # 9번째(인덱스 8) 항목부터 끝까지 순회
            for index, target_input in enumerate(checked_inputs[8:], start=9):
                try:
                    # [진짜 수정] arguments 뒤에 [0]을 붙여 정확한 자바스크립트 클릭 명령을 내립니다.
                    driver.execute_script("arguments[0].click();", target_input)
                    # print(f"[{index}번째 항목] 체크 해제 완료")
                    
                    # 안정적인 반영을 위한 짧은 대기
                    time.sleep(0.2)
                except Exception as e:
                    print(f"{index}번째 항목 해제 중 오류 발생:", e)
                    
            print("✨ 앞의 8개만 남기고 나머지 항목의 체크 해제를 완료했습니다!")
            
        time.sleep(2)



        ## 업로드관리상품 누르기 
        
        try:
            # 1. 존재 여부만 체크 (clickable 조건보다 훨씬 안정적입니다)
            print("⏳ 업로드관리상품 버튼이 로딩되기를 기다리는 중...")
            first_element = WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pmMove"]'))
            )
            
            # 2. 버튼이 화면에 보일 때까지 부드럽게 스크롤을 이동시킵니다 (선택사항이지만 안전함)
            driver.execute_script("arguments[0].scrollIntoView(true);", first_element)
            time.sleep(0.5)
            
            # 3. 자바스크립트로 강력하게 강제 클릭 실행
            # (앞선 작업 때문에 다른 투명한 레이어나 로딩 바에 가려져 있어도 무조건 뚫고 누릅니다)
            driver.execute_script("arguments[0].click();", first_element)
            print("🎯 업로드관리상품 누르기 완료!")

        except Exception as e:
            print("❌ 업로드관리상품 버튼을 누르지 못했습니다. 에러 내용:", e)




        # first_element = WebDriverWait(driver, 20).until(
        # EC.element_to_be_clickable((By.XPATH, '//*[@id="pmMove"]'))
        # )
        # first_element.click()
        # print("업로드관리상품 누르기  완료 ")
        
    else:
        print("☆ 하위 항목에 이미지가 없습니다.")
        # [조건 B] 삭제 
        ## TODO: 삭제하기 누르기 
        time.sleep(1)
        first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div[3]/button[1]'))
        )
        first_element.click()
        
        time.sleep(1)
        
        first_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/button[2]'))
        )
        first_element.click()
        
        print('========삭제왼료=========')
    
    


    
    
    # TODO: 우측 그룹 work_work 선택하기
def changeGruopTo(group_name: str):
    try:
        # 1. 셀렉트 박스 요소 찾기
        # 앞부분의 유동적인 /div[1]/div[1] 숫자를 제외하고 고정된 ID 구역(pdList)부터 추적합니다.
        select_xpath = '//*[@id="pdList"]/div/div/div/div/select'
        select_element = driver.find_element(By.XPATH, select_xpath)
        
        # 2. 셀레니움 Select 객체로 변환
        select_box = Select(select_element)
        
        # 3. 글자(텍스트) 내용이 'work_end'인 옵션을 선택합니다.
        # value 값인 "4104" 대신 눈에 보이는 글자 자체로 선택하므로 매우 직관적입니다.
        select_box.select_by_visible_text(group_name)
        print(f"🎯 우측 그룹 [{group_name}] 선택 완료!")
        
        # 반영 대기
        time.sleep(0.5)

    except Exception as e:
        print("❌ 셀렉트 박스 선택 중 오류 발생:", e)
        
        # [보완책] 만약 일반 Select 라이브러리가 먹히지 않는 사이트라면 아래 자바스크립트 방식을 시도합니다.
        try:
            print("자바스크립트로 강제 선택 및 변경(change) 이벤트를 발생시킵니다.")
            # value="4104" 값을 강제로 주입하고 사이트에 반영되도록 이벤트를 쏘아줍니다.
            driver.execute_script("""
                arguments[0].value = '4104';
                arguments[0].dispatchEvent(new Event('change'));
            """, select_element)
            print(f"🎯 자바스크립트로 [{gruopName}] 강제 선택 성공!")
        except Exception as je:
            print("강제 선택도 실패:", je)
    
    

   
           ##################  등록상품관리 시작 ####################
        
    #     # TODO: 우측 그룹 work_end 선택하기
    # try:
    #     # 1. 셀렉트 박스 요소 찾기
    #     # 앞부분의 유동적인 /div[1]/div[1] 숫자를 제외하고 고정된 ID 구역(pdList)부터 추적합니다.
    #     select_xpath = '//*[@id="pdList"]/div/div/div/div/select'
    #     select_element = driver.find_element(By.XPATH, select_xpath)
        
    #     # 2. 셀레니움 Select 객체로 변환
    #     select_box = Select(select_element)
        
    #     # 3. 글자(텍스트) 내용이 'work_end'인 옵션을 선택합니다.
    #     # value 값인 "4104" 대신 눈에 보이는 글자 자체로 선택하므로 매우 직관적입니다.
    #     select_box.select_by_visible_text("work_end")
    #     print("🎯 우측 그룹 'work_end' 선택 완료!")
        
    #     # 반영 대기
    #     time.sleep(0.5)

    # except Exception as e:
    #     print("❌ 셀렉트 박스 선택 중 오류 발생:", e)
        
    #     # [보완책] 만약 일반 Select 라이브러리가 먹히지 않는 사이트라면 아래 자바스크립트 방식을 시도합니다.
    #     try:
    #         print("자바스크립트로 강제 선택 및 변경(change) 이벤트를 발생시킵니다.")
    #         # value="4104" 값을 강제로 주입하고 사이트에 반영되도록 이벤트를 쏘아줍니다.
    #         driver.execute_script("""
    #             arguments[0].value = '4104';
    #             arguments[0].dispatchEvent(new Event('change'));
    #         """, select_element)
    #         print("🎯 자바스크립트로 'work_end' 강제 선택 성공!")
    #     except Exception as je:
    #         print("강제 선택도 실패:", je)
    
    
# 3. 프로그램의 실제 시작점 (가장 마지막에 실행)
if __name__ == "__main__":
    # 1. 크롬 디버깅 연결
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=chrome_options)
    main()

    
    
''' 탭키 누르면 기능 
print("⏸️ [크롬 대기] 크롬 창을 클릭한 상태에서 키보드의 'Tab' 키를 누르면 다음으로 넘어갑니다...")

while True:
    try:
        # 1. 크롬 창의 활성화된 요소(혹은 가장 기본 바닥인 html 태그)를 잡습니다.
        active_element = driver.switch_to.active_element
        
        # 2. 자바스크립트로 현재 사용자가 실시간으로 누른 마지막 키를 추적합니다.
        # 크롬 창 내부에서 Tab 키(KeyCode 9)가 감지되었는지 확인합니다.
        last_key = driver.execute_script("return window.lastPressedKey;")
        
        # 3. 최초 1회, 브라우저가 키를 기억할 수 있도록 도청(이벤트 리스너) 장치를 심어둡니다.
        driver.execute_script("""
            if (!window.hasKeyTracker) {
                window.hasKeyTracker = true;
                window.lastPressedKey = null;
                document.addEventListener('keydown', function(e) {
                    if (e.key === 'Tab') {
                        window.lastPressedKey = 'Tab';
                    }
                });
            }
        """)
        
        # 4. 사용자가 크롬에서 Tab을 눌렀다면 루프를 탈출하고 다음 명령을 실행합니다.
        if last_key == 'Tab':
            # 다음 회차를 위해 감지된 키 기록을 다시 비워줍니다.
            driver.execute_script("window.lastPressedKey = null;")
            print("▶️ 크롬 창에서 'Tab' 키 입력 확인! 다음 명령을 시작합니다.")
            break
            
        # 크롬 창의 과부하를 막기 위해 0.1초씩 아주 짧게 쉬면서 검사합니다.
        time.sleep(0.1)
        
    except Exception as e:
        print("키 감지 중 잠시 오류 발생 (대기 지속):", e)
        time.sleep(0.5)


'''