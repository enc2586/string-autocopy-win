import keyboard
import pyperclip
import tkinter as tk
from tkinter import scrolledtext


def parse_coupons(string):
    coupons = []
    for line in string.split("\n"):
        coupon = line.strip()
        if len(coupon) > 1:
            coupons.append(coupon)

    return coupons


class CouponApp:

    def __init__(self, root):
        self.root = root
        self.root.title("여러 줄 자동 복사기")

        bold_font = ("Malgun Gothic", 10, "bold")

        self.label = tk.Label(
            root,
            text="문자열 여러 줄을 붙여넣고 [시작]을 누르세요.\nCtrl+B를 누를 때마다 다음 줄을 자동으로 복사합니다.\n빈 문자열, 양 끝 공백은 자동 무시합니다.",
            font=bold_font,
        )
        self.label.pack(pady=10)

        self.text_box = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=50, height=10
        )
        self.text_box.pack(pady=10)  # this textbox is for parsing

        self.parse_button = tk.Button(
            root, text="시작", command=self.toggle_parsing, font=bold_font
        )
        self.parse_button.pack(pady=10)

        self.status_label = tk.Label(root, text="상태: 대기중", font=bold_font)
        self.status_label.pack(pady=10)

        self.new_label = tk.Label(root, text="현재 문자열:", font=bold_font)
        self.new_label.pack(side=tk.LEFT, padx=5)

        self.left_button = tk.Button(
            root, text="<", font=bold_font, command=self.prev_coupon
        )
        self.left_button.pack(side=tk.LEFT, padx=5)

        self.right_button = tk.Button(
            root, text=">", font=bold_font, command=self.next_coupon
        )
        self.right_button.pack(side=tk.LEFT, padx=5)

        self.coupon_display = tk.Entry(root, width=50)
        self.coupon_display.pack(pady=10)

        self.parsing = False
        self.lines = []
        self.index = -1
        self.cycle = 0

    def prev_coupon(self):
        if self.index > 0:
            self.index -= 1
        else:
            self.cycle -= 1
            self.index = len(self.lines) - 1

        pyperclip.copy(self.lines[self.index])
        self.coupon_display.delete(0, tk.END)
        self.coupon_display.insert(tk.END, self.lines[self.index])

        num_digits = len(str(len(self.lines)))
        self.new_label.config(
            text=f"{self.index + 1:0{num_digits}d}/{len(self.lines)}, {self.cycle+1}회전째"
        )

    def next_coupon(self):
        if self.index < len(self.lines) - 1:
            self.index += 1
        else:
            self.index = 0
            self.cycle += 1

        pyperclip.copy(self.lines[self.index])
        self.coupon_display.delete(0, tk.END)
        self.coupon_display.insert(tk.END, self.lines[self.index])

        num_digits = len(str(len(self.lines)))
        self.new_label.config(
            text=f"{self.index + 1:0{num_digits}d}/{len(self.lines)}, {self.cycle+1}회전째",
            bg="yellow" if (self.cycle + self.index) % 2 == 0 else "white",
        )

    def toggle_parsing(self):
        if self.parsing:
            self.stop_parsing()
        else:
            self.start_parsing()

    def start_parsing(self):
        self.index = -1
        self.cycle = 0
        self.parsing = True

        # parse textbox content by parse_coupons function
        self.lines = parse_coupons(self.text_box.get("1.0", tk.END))

        self.status_label.config(text=f"상태: 작동중({len(self.lines)}개 인식)")
        self.parse_button.config(text="중지")

        # set content of self.text_box to the lines, separated by newlines
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, "\n".join(self.lines))

        keyboard.add_hotkey("ctrl+b", self.next_coupon)
        self.next_coupon()

    def stop_parsing(self):
        self.parsing = False
        self.status_label.config(text="상태: 대기중")
        self.parse_button.config(text="시작")
        keyboard.remove_hotkey("ctrl+b")


root = tk.Tk()
app = CouponApp(root)
root.mainloop()
