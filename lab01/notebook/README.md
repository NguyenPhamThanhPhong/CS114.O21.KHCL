Nhận xét:
    -Kết quả thay đổi dựa vào độ sáng của ảnh chụp
    -Kết quả thay đổi dựa vào góc chụp, và size ảnh (do khi resize sẽ ép về dạng 28x28)
    -Kết quả thay đổi dựa vào chữ viết, do kết quả train chỉ áp dụng cho 1 số hình nhất định
    -    Vd: 1 hình que thẳng đứng, 7 không có dấu gạch lưng, 9 không có nét cong ở dưới...
    -Kết quả thay đổi dựa vào màu nền, nếu dùng giấy ô ly, không đạt hiệu quả

Giải thích các hàm đã chỉnh sửa: Hàm run_example() và hàm load_image()

hàm load_image gồm có các parameter sau : (filename, alpha=0.85, beta=2, threshold=130, dilation_kernel_size=3)

trong đó: 
+ file name là tên file
+ alpha là đối số của contrast (độ tương phản)
+ beta là giá trị tăng thử cho pixel, có thể xem là giá trị tạm để dùng cho "cv2.convertScaleAbs", đối số này khiến từng pixel tăng hoặc giảm 1 đơn vị
+ threshold là ngưỡng để mà quyết định tính nhị phân của pixel

trong hàm "load_img":
    +đã load opencv (cv2)
    +b1 đọc ảnh chuyển thành dạng trắng đen ( chỉ có 1 kênh màu k còn rgb)
    +b2 scale ảnh với alpha & beta: alpha là độ tương phản, beta = dộ tăng giảm pixel
    +b3 threshold cái ảnh: quyết định tính trắng đen của pixel dựa trên ngưỡng chọn là 130 (nghĩa là >130 sẽ là 0 (trắng), <= 130 là đen, do parameter 255 nghĩa là sẽ revert trằng -> đen, đen-> trắng)
    +b4 định nghĩa 1 kernel để giản nở: đã đặt cho "dilation_kernel_size=3", dãn phần trắng xung qua 3px
    +b5 resize - reshape lại cho đúng dạng (1,28,28,1): phần còn lại giữ nguyên

hàm run_example():
    load ảnh lần lượt từ directory real_test1-> real_test6
    ở mỗi folder sẽ load ảnh từ 0.jpg -> 9.jpg
    kiểm tra ảnh có match với tên hay không (do tên đã đặt vậy để dễ check Kết quả)
    Load ảnh, và confidence của mỗi ảnh để kiểm tra
    Kết quả cuối cùng: accuracy đúng = 60%, đúng 36/60