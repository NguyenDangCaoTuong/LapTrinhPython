# **ỨNG DỤNG THUẬT TOÁN K-MEANS TRONG PHÂN TÍCH PHÂN KHÚC KHÁCH HÀNG**

# 1. Giới thiệu dự án

Customer Segmentation Analysis là dự án ứng dụng Machine Learning để phân nhóm khách hàng dựa trên dữ liệu nhân khẩu học và hành vi tiêu dùng. Dự án sử dụng thuật toán K-Means Clustering kết hợp với kỹ thuật giảm chiều dữ liệu PCA (Principal Component Analysis) để xác định các nhóm khách hàng tiềm năng, từ đó hỗ trợ đưa ra các chiến lược Marketing mục tiêu hiệu quả.

Điểm nổi bật của dự án:

* Xử lý dữ liệu chuyên sâu: Tính toán độ tuổi, tổng chi tiêu, tổng số con cái từ dữ liệu thô.

*	Kỹ thuật Feature Engineering: Sử dụng One-Hot Encoding cho dữ liệu định danh và StandardScaler để chuẩn hóa dữ liệu số.

*	Phân cụm đa chiều: Sử dụng PCA để giảm chiều dữ liệu xuống 2D, giúp trực quan hóa kết quả phân cụm một cách rõ ràng trên biểu đồ.

# 2. Cấu trúc thư mục

Dự án được tổ chức đơn giản, thuận tiện cho việc chạy và kiểm thử:

Plaintext

CUSTOMER_SEGMENTATION/

│

├── Mall_Customers.csv   # Tập dữ liệu đầu vào (Input Dataset)

├── main.py              # Mã nguồn chính (Data Pipeline & Modeling)

├── requirements.txt     # Danh sách các thư viện cần cài đặt

└── README.md            # Tài liệu hướng dẫn sử dụng

# 3. Mô tả dữ liệu (Mall_Customers.csv)

Tập dữ liệu bao gồm các thông tin chi tiết về khách hàng:

-	Thông tin nhân khẩu học:

    *	Year_Birth: Năm sinh (Dùng để tính tuổi).

    *	Education: Trình độ học vấn (Graduation, PhD, Master...).

    *	Marital_Status: Tình trạng hôn nhân (Married, Single, Together...).

    *	Income: Thu nhập hàng năm của hộ gia đình.

    *	Kidhome / Teenhome: Số lượng trẻ nhỏ và thanh thiếu niên trong gia đình.

    *	Dt_Customer: Ngày khách hàng bắt đầu đăng ký thành viên.

-	Hành vi tiêu dùng (Chi tiêu trong 2 năm qua):

    *	MntWines: Chi tiêu cho rượu vang.

    *	MntFruits: Chi tiêu cho trái cây.

    *	MntMeatProducts: Chi tiêu cho thịt.

    *	MntFishProducts: Chi tiêu cho thủy sản.

    *	MntSweetProducts: Chi tiêu cho đồ ngọt.

    *	MntGoldProds: Chi tiêu cho vàng/trang sức.

-	Hành vi mua sắm:

    *	NumWebPurchases, NumStorePurchases...: Số lượng đơn hàng qua web, tại cửa hàng.

# 4. Yêu cầu cài đặt

**Môi trường**

-	Python 3.8 trở lên.

**Cài đặt thư viện**

Bạn cần cài đặt các thư viện được liệt kê trong requirements.txt. Mở Terminal (hoặc CMD/PowerShell) tại thư mục dự án và chạy lệnh:

```
pip install -r requirements.txt
```

Nếu cài đặt thủ công, vui lòng chạy lệnh sau:

```
pip install pandas matplotlib scikit-learn
```

# 5. Quy trình xử lý (Workflow)

File main.py thực hiện quy trình phân tích theo các bước sau:

**1.	Thu thập dữ liệu (Data Ingestion):** Đọc file Mall_Customers.csv.

**2.	Làm sạch dữ liệu (Data Cleaning):**

  *	Loại bỏ các giá trị bị thiếu (Missing values).

**3.	Feature Engineering (Tạo đặc trưng mới):**

  *	Age: Tính tuổi dựa trên Year_Birth (Giả định năm hiện tại là 2014 theo dữ liệu).

  *	Total_Spending: Tổng chi tiêu của tất cả các danh mục sản phẩm.

  *	Total_Children: Tổng số con trong gia đình.

  *	Family_Size: Tổng số thành viên trong gia đình.

**4.	Mã hóa dữ liệu (Encoding):**

  *	Sử dụng One-Hot Encoding để chuyển đổi các cột phân loại (Education, Marital_Status) thành dạng số.

**5.	Chuẩn hóa (Scaling):**

  *	Sử dụng StandardScaler để đưa các biến về cùng một miền giá trị, giúp thuật toán K-Means hoạt động chính xác hơn.

**6.	Giảm chiều dữ liệu (PCA):**

  *	Áp dụng PCA để giảm số lượng chiều dữ liệu xuống còn 2 thành phần chính (PCA1, PCA2) phục vụ cho việc vẽ biểu đồ.

**7.	Phân cụm (Clustering):**

  *	Chạy thuật toán K-Means với số cụm k=4.

**8.	Trực quan hóa (Visualization):**

  *	Vẽ biểu đồ phân tán (Scatter Plot) hiển thị các cụm khách hàng và tâm cụm (Centroids).

# 6. Hướng dẫn chạy chương trình

Để thực thi dự án, hãy làm theo các bước sau:

**Bước 1:** Mở Terminal và di chuyển đến thư mục dự án:

```
cd duong/dan/den/CUSTOMER_SEGMENTATION
```

**Bước 2:** Chạy file main.py:

```
python main.py
```

**Bước 3:** Xem kết quả:

  *	Màn hình Terminal sẽ hiển thị:

    *	Thông tin dữ liệu (Info, Shape).

    *	Số lượng giá trị thiếu (Missing values).

    *	Thống kê đặc trưng trung bình của từng cụm (Cluster Summary).

  *	Một cửa sổ đồ họa sẽ bật lên hiển thị biểu đồ phân cụm khách hàng.

