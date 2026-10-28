# eum261012_sellerpick


~

checkbox = driver.find_element(
            By.XPATH,
            '/html/body/div[4]/div[2]/div[2]/div[4]/div/div[4]/div[1]/div/label/input'
        )

        if checkbox.is_selected():
            checkbox.click()
            print("체크 해제 완료")
        else:
            print("이미 체크 해제 상태입니다.")
~
