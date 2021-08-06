## Usage
```bash
poetry install
poetry run python diningcity_sms_to_ics.py -h
echo "【DiningCity】预订成功，2021-01-01 12:00于 桥洞下面 114514位。预订号：xxxxxxx。 出示预订二维码核销：https://dwz.cn/xxxxxx 祝您用餐愉快！ 查看更多餐厅：https://dwz.cn/xxxxxx - 餐厅周" | poetry run python diningcity_sms_to_ics.py my.ics
poetry run python diningcity_sms_to_ics.py very_long_input.txt my.ics

```
