import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from translations import translations as t


def get_type_key_by_value(value: str, mapping: dict) -> str:
    for k, v in mapping.items():
        if v == value:
            return k
    return None

def is_consecutive(days: list) -> bool:
    if len(days) <= 1:
        return True
    for i in range(len(days) - 1):
        if (days[i] % 7) + 1 != days[i+1]:
            return False
    return True

def validate_input(input_obj: dict) -> None:
    errors = []
    input_type = input_obj.get('type')
    days_of_week = input_obj.get('daysOfWeeks', [])
    if input_obj.get('hourRange') is None:
        input_obj['hourRange'] = {}
    hour_range = input_obj.get('hourRange')

    if input_type not in ['DAILY', 'WEEKLY']:
        errors.append(t["invalid_type"])

    start_time = hour_range.get('startTime', 0)
    end_time = hour_range.get('endTime', 24)
    if start_time is None or end_time is None:
        errors.append(t["missing_hours"])
    else:
        if not (0 <= start_time <= 23) or not (1 <= end_time <= 24):
            errors.append(t["invalid_hours"])

    if input_type == 'DAILY':
        if days_of_week:
            errors.append(t["daily_has_days"])
    elif input_type == 'WEEKLY':
        if not days_of_week:
            errors.append(t["weekly_missing_days"])
        else:
            for day in days_of_week:
                if not 1 <= day <= 7:
                    errors.append(t["invalid_day"].format(day=day))

            if not is_consecutive(days_of_week) and start_time > end_time:
                errors.append(t["non_consecutive_time_error"])

    if errors:
        raise ValueError("\n".join(errors))

def load_and_preprocess(csv_path):
    df = pd.read_csv(
        csv_path,
        names=['date', 'time', 'consumption'],
        parse_dates={'datetime': ['date', 'time']},
        dayfirst=True,
        skiprows=12
    )
    df = df.set_index('datetime')
    hourly_df = df.resample('H').sum().reset_index()
    hourly_df['hour'] = hourly_df['datetime'].dt.hour
    hourly_df['date'] = hourly_df['datetime'].dt.date
    hourly_df['day'] = (hourly_df['datetime'].dt.weekday + 1) % 7 + 1
    return hourly_df

def calculate_period_consumption(hourly_df: pd.DataFrame, filter: dict) -> float:
    start_hour = filter['hourRange'].get('startTime', 0)
    end_hour = filter['hourRange'].get('endTime', 24)
    days = filter.get('daysOfWeeks', [])
    consecutive = is_consecutive(days)

    filtered = hourly_df[hourly_df['day'].isin(days)] if filter['type'] == 'WEEKLY' else hourly_df.copy()

    if filter['type'] == 'WEEKLY':
        if consecutive:
            first_day, last_day = days[0], days[-1]
            mask = (
                ((filtered['day'] == first_day) & (filtered['hour'] >= start_hour)) |
                ((filtered['day'] == last_day) & (filtered['hour'] < end_hour)) |
                (~filtered['day'].isin([first_day, last_day]))
            )
        else:
            mask = (filtered['hour'] >= start_hour) & (filtered['hour'] < end_hour)
    else:
        if start_hour > end_hour:
            mask = (filtered['hour'] >= start_hour) | (filtered['hour'] < end_hour)
        else:
            mask = (filtered['hour'] >= start_hour) & (filtered['hour'] < end_hour)
        if end_hour == 24:
            mask |= (filtered['hour'] == 23)

    filtered = filtered[mask]
    period_consumption = filtered['consumption'].sum()
    return period_consumption

def calculate_total_discount(total_consumption: float, period_consumption: float, discount_for_period: float) -> float:
    if total_consumption == 0:
        return 0.0
    period_ratio = (period_consumption / total_consumption)
    return round(period_ratio * discount_for_period, 2)

def build_ui():
    def update_days_visibility(*args):
        selected_type_value = type_dropdown.get()
        _type = get_type_key_by_value(selected_type_value, t["type_options"])
        if _type == "WEEKLY":
             days_frame.pack()
             start_hour_input.delete(0, "end")
             start_hour_input.insert(0, "0")
             end_hour_input.delete(0, "end")
             end_hour_input.insert(0, "24")
        else:
            days_frame.forget()
            start_hour_input.delete(0, "end")
            start_hour_input.insert(0, "7")
            end_hour_input.delete(0, "end")
            end_hour_input.insert(0, "17")
       

    def on_submit():
        try:
            selected_type_value = type_dropdown.get()
            _type = get_type_key_by_value(selected_type_value, t["type_options"])
            start_hour = int(start_hour_input.get())
            end_hour = int(end_hour_input.get())
            discount = float(discount_input.get())
            days = [i+1 for i, var in enumerate(day_vars) if var.get()] if _type == "WEEKLY" else []

            user_input = {
                "type": _type,
                "hourRange": {"startTime": start_hour, "endTime": end_hour},
                "daysOfWeeks": days
            }

            validate_input(input_obj=user_input)
            hourly_df = load_and_preprocess(csv_path=csv_path.get())
            total_consumption = hourly_df['consumption'].sum()
            period_consumption = calculate_period_consumption(hourly_df=hourly_df, filter=user_input)

            discount_for_period = calculate_total_discount(total_consumption, period_consumption, discount)  

            result_message = t["result_message"].format(
                total=round(total_consumption, 2),
                period=round(period_consumption, 2),
                discount=round(discount_for_period, 2)
            )
            messagebox.showinfo(t["result_title"], result_message)
        except Exception as e:
            messagebox.showerror(t["error_title"], str(e))

    root = tk.Tk()
    root.title(t["app_title"])
    root.geometry("600x400")

    csv_path = tk.StringVar()
    tk.Label(root, text=t["csv_file_path"]).pack()
    csv_frame = tk.Frame(root)
    csv_frame.pack()
    tk.Entry(csv_frame, textvariable=csv_path, width=50).pack(side="left")

    def browse_file():
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            csv_path.set(path)

    tk.Button(csv_frame, text=t["browse_button"], command=browse_file).pack(side="left")

    # Type Dropdown
    tk.Label(root, text=t["select_type"]).pack()

    type_values = list(t["type_options"].values())
    type_var = tk.StringVar(value=type_values[0])
    type_dropdown = ttk.Combobox(root, values=type_values, state="readonly", textvariable=type_var)
    type_dropdown.pack()
    type_var.trace_add("write", update_days_visibility)

    # Start Hour
    tk.Label(root, text=t["start_hour"]).pack()
    start_hour_input = tk.Spinbox(root, from_=0, to=23, width=5)
    start_hour_input.delete(0, "end")
    start_hour_input.insert(0, "7")
    start_hour_input.pack()

    # End Hour
    tk.Label(root, text=t["end_hour"]).pack()
    end_hour_input = tk.Spinbox(root, from_=1, to=24, width=5)
    end_hour_input.delete(0, "end")
    end_hour_input.insert(0, "17")
    end_hour_input.pack()

    # Discount Input
    tk.Label(root, text=t["discount"]).pack()
    discount_input = tk.Entry(root)
    discount_input.insert(0, "10")
    discount_input.pack()

    # Days of Week Checkboxes
    days_frame = tk.Frame(root)
    day_vars = []
    for day_name in t["days_of_week"]:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(days_frame, text=day_name, variable=var)
        cb.pack(side="left")
        day_vars.append(var)

    update_days_visibility()  # Initially hide days_frame if needed

    # Submit Button
    tk.Button(root, text=t["submit_button"], command=on_submit).pack()

    root.mainloop()

if __name__ == "__main__":
    build_ui()
