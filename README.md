#  **ỨNG DỤNG THUẬT TOÁN K-MEANS TRONG PHÂN TÍCH PHÂN KHÚC KHÁCH HÀNG**
# 1. Giới thiệu
Dự án này tập trung vào phân tích và phân khúc khách hàng dựa trên bộ dữ liệu hành vi tiêu dùng, nhân khẩu học và lịch sử mua sắm. Thông qua các kỹ thuật tiền xử lý dữ liệu, phân tích khám phá (EDA) và học máy không giám sát (Unsupervised Learning), nhóm sử dụng thuật toán K-Means Clustering kết hợp với PCA (Principal Component Analysis) để
*	Hiểu rõ đặc điểm của từng nhóm khách hàng
*	Hỗ trợ doanh nghiệp xây dựng chiến lược marketing và chăm sóc khách hàng hiệu quả hơn
# 2. Công nghệ và thư viện sử dụng
*	Ngôn ngữ: Python 3.10+
*	Thư viện chính:
    *	numpy
    *	pandas
    *	matplotlib
    *	scikit-learn

Danh sách chi tiết được quản lý trong file requirements.txt.
# 3. Dữ liệu sử dụng
*	Tên file: Mall_Customers.csv
*	Mô tả:
    * Dữ liệu bao gồm thông tin nhân khẩu học (tuổi, thu nhập, trình độ học vấn, tình trạng hôn nhân)
    * Hành vi mua sắm (chi tiêu theo từng danh mục, số lần mua online/cửa hàng, phản hồi chiến dịch marketing)
# 4. Quy trình thực hiện
**4.1. Tiền xử lý dữ liệu**
*	Kiểm tra và loại bỏ giá trị thiếu
*	Chuẩn hóa định dạng ngày tháng
*	Tạo các biến mới:
    *	Tuổi (Age)
    *	Tổng chi tiêu (Total_Spending)
    *	Tổng số con (Total_Children)
    *	Thời gian gắn bó với doanh nghiệp (Customer_Since)
**4.2 Phân tích khám phá dữ liệu (EDA)**
*	Phân phối tuổi, thu nhập, mức chi tiêu
*	Phân tích mối tương quan giữa các biến
*	So sánh hành vi chi tiêu theo:
    *	Trình độ học vấn
    *	Tình trạng hôn nhân
    *	Nhóm tuổi
**4.3 Phân cụm khách hàng**
*	Chuẩn hóa dữ liệu bằng StandardScaler
*	Sử dụng Elbow Method và Silhouette Score để xác định số cụm tối ưu
*	Áp dụng thuật toán K-Means với số cụm được lựa chọn
**4.4 Trực quan hóa kết quả**
*	Giảm chiều dữ liệu bằng PCA (2D)
*	Trực quan hóa các cụm khách hàng và tâm cụm (centroid)
# 5. Kết quả
*	Khách hàng được chia thành các nhóm có đặc điểm rõ ràng về:
    *	Độ tuổi
    *	Thu nhập
    *	Hành vi mua sắm
*	Kết quả giúp doanh nghiệp:
    *	Xác định nhóm khách hàng tiềm năng
    *	Đề xuất chiến lược marketing phù hợp cho từng phân khúc
# 6. Phân công công việc nhóm
| STT | Họ và tên | MSSV | Phân công công việc | Mức độ hoàn thành |
|:---:|:---|:---:|:---|:---:|
| 1 | **Bùi Quang Hòa** | 24110213 | Làm mã nguồn và viết Chương 3 | 100% |
| 2 | **Võ Thành Phát** | 24110300 | Tìm tài liệu và viết Chương 1 | 100% |
| 3 | **Nguyễn Ngọc Thiện** | 24110335 | Làm mã nguồn và viết Chương 2 | 100% |
| 4 | **Lý Đông Thịnh** | 24110337 | Làm mã nguồn và viết Chương 3 | 100% |
| 5 | **Nguyễn Đặng Cao Trường** | 24110375 | Tìm tài liệu, viết phần Mở đầu và Kết luận | 100% |
________________________________________
## 7. Hướng dẫn chạy chương trình
**Bước 1:** Cài đặt các thư viện cần thiết:
pip install -r requirements.txt
**Bước 2:** Chạy chương trình chính:
python main.py
Lưu ý: Đảm bảo file Mall_Customers.csv nằm cùng thư mục với file mã nguồn main.py.
________________________________________
## 8. Kết luận
Dự án đã áp dụng thành công các kỹ thuật phân tích dữ liệu và học máy không giám sát để phân khúc khách hàng. Kết quả đạt được mang tính thực tiễn cao và có thể mở rộng trong tương lai bằng cách:
•	Thử nghiệm các thuật toán phân cụm khác (DBSCAN, Hierarchical Clustering)
•	Tích hợp thêm dữ liệu thời gian thực
•	Xây dựng dashboard trực quan
________________________________________
Nhóm thực hiện – Ngành Công nghệ Thông tin

