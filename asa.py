import pandas as pd

# Thử đọc tệp CSV với mã hóa 'ISO-8859-1'
try:
    df = pd.read_csv('t_cuaong.csv', encoding='ISO-8859-1')
except UnicodeDecodeError:
    print("Failed to decode with ISO-8859-1 encoding.")
    # Bạn có thể thử các mã hóa khác nếu cần

# Kiểm tra dữ liệu
print(df.head())

# Melting DataFrame để tạo dữ liệu 1 chiều theo thứ tự tháng
df_monthly = pd.DataFrame()

for month in df["THÁNG"]:
    temp_df = df[df["THÁNG"] == month].melt(id_vars=["THÁNG"], var_name="Ngày", value_name="Giá trị")
    df_monthly = pd.concat([df_monthly, temp_df], axis=0)

# Loại bỏ giá trị NaN
df_monthly.dropna(subset=["Giá trị"], inplace=True)

# Đặt lại chỉ mục
df_monthly.reset_index(drop=True, inplace=True)

# Lưu dữ liệu mới ra tệp CSV (nếu cần)
df_monthly.to_csv('monthly_sequence.csv', index=False)

# Hiển thị kết quả
print(df_monthly.head())