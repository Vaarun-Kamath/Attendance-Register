# Attendance Register Web Application
This Python script is a simple web application created using Streamlit that allows you to maintain an attendance register for students. It provides a user-friendly interface for recording student attendance, viewing attendance records, and adding new student entries. The script uses Excel files for data storage and manipulation.

## Features
### Student Attendance Recording
- **Student Selection:** You can select a student from the list of registered students.
- **Date Entry:** Enter the date for which you want to record attendance.
- **Duration Slider:** Slide to specify the duration of the class in minutes.
- **Class Start Time:** Choose the class start time using a dropdown menu with AM/PM options.
- **Attendance Status:** Mark students as "Present" or "Absent."
- **Comments:** Add optional comments for each attendance entry.

### Attendance Record Display
- **View Records:** You can select a student and view their attendance records in a tabular format. If no records exist for a student, it will display a message indicating no records found.
### New Student Entry
- **Add New Student:** You can add a new student's name to the list of registered students. The script will update the list of students and allow you to record attendance for the new student.

## Usage
1) **Select Student:** Choose the student for whom you want to record attendance.
2) **Date Selection:** Select the date for which you want to record attendance.
3) **Duration:** Use the slider to set the duration of the class in minutes.
4) **Class Start Time:** Choose the class start time from the dropdown menu.
5) **Attendance Status:** Mark the student as "Present" or "Absent."
6) **Comments:** Optionally, add comments for the attendance entry.
7) **Submit:** Click the "Submit" button to record the attendance. The data will be saved in an Excel file named "AttendanceRecord.xlsx."
8) **View Records:** You can view the attendance records for a specific student by selecting the student and clicking the "Show Records" button.
9) **Add New Student:** If you have a new student, enter their name in the "New Student Entry" section and click the "Add" button to register them. The new student's name will be added to the list of registered students.

## Dependencies
- **Streamlit:** Used to create the web application.
- **Pandas:** Used for data handling and manipulation.
- **DateTime:** Used for date and time operations.
- **Calendar:** Used to get day and month names.

## Data Storage
The attendance data is stored in an Excel file named "AttendanceRecord.xlsx." Each student's attendance is recorded on a separate sheet within the Excel file, making it easy to manage and view attendance records.


## Authors
Varun Kamath

## License
This project is licensed under the MIT License - see the LICENSE file for details.
