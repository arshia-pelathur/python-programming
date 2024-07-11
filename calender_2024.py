import streamlit as st
import calendar

def create_calendar():
    cal = calendar.TextCalendar(calendar.SUNDAY)
    year_calendar = cal.formatyear(2024, 2, 1, 1, 3)
    return year_calendar

def main():
    st.markdown(
        """
        <style>
        .calendar-container {
            background-color: black;
            color: orange;
            font-family: 'Courier New', Courier, monospace;
            white-space: pre;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    year_calendar = create_calendar()

    st.markdown(f'<div class="calendar-container">{year_calendar}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
