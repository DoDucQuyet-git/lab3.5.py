import os
import re
from datetime import datetime

# =========================
# 1. TÁCH BÀI
# =========================
def parse_exercises(text):
    pattern = r"Bài\s*(\d+):(.+?)(?=Bài\s*\d+:|$)"
    matches = re.findall(pattern, text, re.S)

    return [{"id": num, "content": content.strip().lower()} for num, content in matches]


# =========================
# 2. SINH CODE OFFLINE
# =========================
def generate_code(ex):
    content = ex["content"]

    # ===== BÀI CHIA HẾT =====
    if "chia hết cho 2" in content and "3" in content:
        return f"""# Bai {ex['id']}
n = int(input("Nhap so nguyen duong: "))

if n % 2 == 0 and n % 3 == 0:
    print("Chia het cho ca 2 va 3")
elif n % 2 == 0:
    print("Chia het cho 2")
elif n % 3 == 0:
    print("Chia het cho 3")
else:
    print("Khong chia het cho 2 va 3")
"""

    # ===== PHƯƠNG TRÌNH BẬC 2 =====
    if "phương trình bậc 2" in content:
        return f"""# Bai {ex['id']}
import math

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a == 0:
    if b != 0:
        print("Phuong trinh bac 1, x =", -c/b)
    else:
        print("Vo nghiem")
else:
    delta = b*b - 4*a*c

    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        print("Nghiem kep x =", -b/(2*a))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
"""

    # ===== SỐ NGUYÊN TỐ =====
    if "số nguyên tố" in content:
        return f"""# Bai {ex['id']}
n = int(input("Nhap n: "))

if n < 2:
    print("Khong phai so nguyen to")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Khong phai so nguyen to")
            break
    else:
        print("La so nguyen to")
"""

    # ===== MẶC ĐỊNH =====
    return f"""# Bai {ex['id']}
# Chua ho tro dang bai nay
print("Chua ho tro bai nay")
"""


# =========================
# 3. TẠO FILE
# =========================
def create_files(exercises):
    if not os.path.exists("output"):
        os.makedirs("output")

    files = []

    for ex in exercises:
        filename = f"output/Bai{ex['id']}.py"

        print(f"⏳ Dang tao {filename} ...")

        code = generate_code(ex)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        files.append(filename)

    return files


# =========================
# 4. PUSH GITHUB
# =========================
def git_push():
    os.system("git add .")
    os.system(f'git commit -m "auto generate {datetime.now()}"')
    os.system("git push")


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    text = """
    Bài 4: Viết chương trình nhập một số nguyên dương và kiểm tra xem số đó có chia hết cho 2 hoặc cho 3 hoặc cả hai hay không?
    Bài 5: Viết chương trình giải phương trình bậc 2: a*x*x + b*x + c = 0.
    """

    exercises = parse_exercises(text)

    files = create_files(exercises)

    print("✅ Đã tạo file:", files)

    git_push()