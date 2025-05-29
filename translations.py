translations = {
    # UI Labels
    "app_title": "מחשבון הנחות לצריכה",
    "csv_file_path": "נתיב קובץ CSV:",
    "browse_button": "בחר",
    "select_type": "בחר סוג:",
    "start_hour": "שעת התחלה (0-23):",
    "end_hour": "שעת סיום (1-24):",
    "discount": "הנחה:",
    "select_days": "בחר ימים בשבוע:",
    "submit_button": "חשב",
    "days_of_week": ["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"],
    "type_options": {
        "DAILY": "יומי",
        "WEEKLY": "שבועי"
    },

    # Messages
    "result_title": "תוצאה",
    "result_message": "📊 תוצאת חישוב הנחה\n\n• צריכה כוללת: {total} קוט\"ש\n• צריכה עם הנחה {period} קוט\"ש\n• הנחה מחושבת לתקופה: {discount}%",
    "error_title": "שגיאה",

    # Validation Errors
    "invalid_type": "סוג לא חוקי. יש לבחור יומי או שבועי.",
    "missing_hours": "חובה לציין שעת התחלה ושעת סיום בטווח השעות.",
    "invalid_hours": "שעת התחלה חייבת להיות בין 0 ל-23, ושעת סיום בין 1 ל-24.",
    "daily_has_days": "לא ניתן לבחור ימים כאשר הסוג הוא יומי.",
    "weekly_missing_days": "כאשר הסוג הוא שבועי, יש לבחור לפחות יום אחד.",
    "invalid_day": "יום לא חוקי: {day}. הימים חייבים להיות בין 1 ל-7 (1=ראשון).",
    "non_consecutive_time_error": "כאשר הימים אינם רציפים, שעת ההתחלה חייבת להיות קטנה או שווה לשעת הסיום."
}
