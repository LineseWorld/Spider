# 实现一个可输入参数计算成本、利润的小程序
# -*- coding:utf-8 -*-
import tkinter as tk


def get_price(cost: float, profit: float, extra_expenses: float, roi: float) -> float:
    return roi * (profit + cost + extra_expenses) / (roi - 1)


# 调用Tk()创建主窗口
root_window = tk.Tk()
# 给主窗口起一个名字，也就是窗口的名字
root_window.title('Linese成本计算器')

# 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
root_window.geometry('450x400')


cost_label = tk.Label(root_window, text="成本", font=('宋体', 15))
price_label = tk.Label(root_window, text="售价", font=('宋体', 15))
extra_label = tk.Label(root_window, text="额外成本", font=('宋体', 15))
roi_label = tk.Label(root_window, text="投产比", font=('宋体', 15))
profit_label = tk.Label(root_window, text="利润", font=('宋体', 15))

cost_label.place(x=40, y=40)
price_label.place(x=100, y=40)
extra_label.place(x=160, y=40)
roi_label.place(x=250, y=40)
profit_label.place(x=370, y=40)

cost_entry = tk.Entry(root_window)
cost_entry.place(x=40, y=70, width=40)

price_entry = tk.Entry(root_window)
price_entry.place(x=100, y=70, width=40)

extra_entry = tk.Entry(root_window)
extra_entry.place(x=160, y=70, width=40)

roi_entry = tk.Entry(root_window)
roi_entry.place(x=250, y=70, width=40)


def get_profit():
    cost = float(cost_entry.get())
    price = float(price_entry.get())
    extra_expenses = float(extra_entry.get()) + price * 0.05
    roi = float(roi_entry.get())
    result = round(price - price / roi - cost - extra_expenses, 2)
    ans_profit.config(text=result)


button1 = tk.Button(root_window, text="得到", font=('宋体', 10), command=get_profit)
button1.place(x=310, y=70)
ans_profit = tk.Label()
ans_profit.place(x=370, y=70)

# -------------------------------------------------------------------

cost_label2 = tk.Label(root_window, text="成本", font=('宋体', 15))
profit_label2 = tk.Label(root_window, text="利润", font=('宋体', 15))
extra_label2 = tk.Label(root_window, text="额外成本", font=('宋体', 15))
roi_label2 = tk.Label(root_window, text="投产比", font=('宋体', 15))
price_label2 = tk.Label(root_window, text="定价", font=('宋体', 15))

cost_label2.place(x=40, y=140)
profit_label2.place(x=100, y=140)
extra_label2.place(x=160, y=140)
roi_label2.place(x=250, y=140)
price_label2.place(x=370, y=140)

cost_entry2 = tk.Entry(root_window)
cost_entry2.place(x=40, y=170, width=40)

profit_entry2 = tk.Entry(root_window)
profit_entry2.place(x=100, y=170, width=40)

extra_entry2 = tk.Entry(root_window)
extra_entry2.place(x=160, y=170, width=40)

roi_entry2 = tk.Entry(root_window)
roi_entry2.place(x=250, y=170, width=40)


def get_price():
    cost = float(cost_entry2.get())
    profit = float(profit_entry2.get())
    extra_expenses = float(extra_entry2.get())
    roi = float(roi_entry2.get())
    result = round(roi * (profit + cost + extra_expenses) / (roi - 1), 2)
    result = result + 0.05 * result
    ans_price2.config(text=result)


button2 = tk.Button(root_window, text="得到", font=('宋体', 10), command=get_price)
button2.place(x=310, y=170)
ans_price2 = tk.Label()
ans_price2.place(x=370, y=170)

# -------------------------------------------------------------------

cost_label3 = tk.Label(root_window, text="成本", font=('宋体', 15))
profit_label3 = tk.Label(root_window, text="利润", font=('宋体', 15))
extra_label3 = tk.Label(root_window, text="额外成本", font=('宋体', 15))
price_label3 = tk.Label(root_window, text="定价", font=('宋体', 15))
roi_label3 = tk.Label(root_window, text="投产比", font=('宋体', 15))

cost_label3.place(x=40, y=240)
profit_label3.place(x=100, y=240)
extra_label3.place(x=160, y=240)
price_label3.place(x=250, y=240)
roi_label3.place(x=370, y=240)

cost_entry3 = tk.Entry(root_window)
cost_entry3.place(x=40, y=270, width=40)

profit_entry3 = tk.Entry(root_window)
profit_entry3.place(x=100, y=270, width=40)

extra_entry3 = tk.Entry(root_window)
extra_entry3.place(x=160, y=270, width=40)

price_entry3 = tk.Entry(root_window)
price_entry3.place(x=250, y=270, width=40)


def get_price():
    cost = float(cost_entry3.get())
    profit = float(profit_entry3.get())
    price = float(price_entry3.get())
    extra_expenses = float(extra_entry3.get()) + 0.05 * price

    result = round(price / (price - profit - cost - extra_expenses), 3)
    ans_roi.config(text=result)


button3 = tk.Button(root_window, text="得到", font=('宋体', 10), command=get_price)
button3.place(x=310, y=270)
ans_roi = tk.Label()
ans_roi.place(x=370, y=270)

cal_label = tk.Label(root_window, text="基于以下公式计算:\n 利润=(售价-售价/投产比-成本-额外成本)", font=('宋体', 15))
cal_label.place(x=20, y=330)

# 开启主循环，让窗口处于显示状态
root_window.mainloop()
