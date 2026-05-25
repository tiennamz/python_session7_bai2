'''transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction.strip()

parts = transaction.split("-")

student_name = parts[0].title()
course_code = parts[1]
amount = parts[2]
status = parts[3].upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", amount, "VND")
print("Trạng thái:", status)

- transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu do do strip() tạo ra 1 bản sao hoàn toàn mới ở các ô nhớ khác nhau 
- Chuỗi giao dịch thực tế được phân tách bằng ký tự "|"
- transaction.split("-") là sai do trong chuỗi k hề có dấu "-"
- cần .strip() lại từng phần sau khi split() để cắt khoảng trắng bị thừa
- cần chuyển amount từ chuỗi sang số trước khi định dạng tiền thì mới có thể format đc dữ liệu và thực hiện tính toán nếu có

'''
transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "



parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print(f"Số tiền: {amount:,} VND")
print("Trạng thái:", status)