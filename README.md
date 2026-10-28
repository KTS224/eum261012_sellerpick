# eum261012_sellerpick


```python
checkbox = driver.find_element(
    By.XPATH,
    '//input[@type="checkbox" and @data-spall]'
)

        if checkbox.is_selected():
            checkbox.click()
            print("체크 해제 완료")
        else:
            print("이미 체크 해제 상태입니다.")
```
