# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS 

*NAME*: AKULA PRANAY KUMAR

*INTERN ID*: CT04WJ109 

*DOMAIN*: PYTHON PROGRAMMING 
I 
*DURATION*: 4 WEEEKS 

*MENTOR*: NEELA SANTHOSH KUMAR


This project is a Python-based data automation tool that reads structured student performance data from an external file and converts it into a neatly formatted PDF report. It demonstrates how to use Python’s data handling and document generation capabilities to create a practical solution for academic reporting and administrative purposes.

This program is especially helpful for teachers, educational coordinators, school administrators, and data entry operators who need to generate score reports for multiple students quickly and consistently. It reduces manual work and ensures uniformity across reports.

The system takes data from a standard CSV file containing a list of student names and their corresponding scores. It then processes this data and creates a structured PDF report that lists each student and their score line by line. The entire process is automated, fast, and accurate.


TOOLS AND TECHNOLOGIES USED:

The following technologies and Python libraries were used in building this project:

PYTHON 3.X: The primary programming language used to create the script.

PANDAS: A powerful Python library used for reading and processing structured data. In this project, it is used to read the CSV file and store the student records in a structured format (DataFrame).

FPDF: A Python library used to generate PDF files programmatically. It provides functions for adding text, formatting layouts, and saving PDF documents.

These libraries were chosen because they are open source, beginner-friendly, and widely used in real-world data analysis and reporting applications.


PLATFORM:

This project was developed and tested on a Windows 11 machine using Visual Studio Code as the code editor. The scripts were executed through the integrated terminal in VS Code. However, the project is platform-independent and can be run on any system with Python installed, including Linux and macOS environments.


FEATURES:

AUTOMATIC DATA READING: Reads data from a CSV file containing student names and scores.

ERROR HANDLING: Includes basic file-not-found error handling to alert the user if the input file is missing.

FORMATTED REPORT: Generates a clean and simple PDF report listing each student's name alongside their score.

EASY TO UPDATE: Simply modifying the contents of the input CSV file updates the report content without touching the script.

LIGHTWEIGHT DEPENDENCIES: Only two external libraries are required, making the script easy to install and manage.


POSSIBLE USE CASES:

EDUCATIONAL REPORTING:
Schools, colleges, and tuition centers can use this script to automatically generate score reports for exams, quizzes, or tests.

TRAINING ASSESSMENT:
Training institutes and corporate skill development programs can use this system to evaluate trainee performance and generate participant score reports.

AUTOMATED ADMIN TASKS:
Replaces manual report writing with a faster, consistent, and automated approach to generating score summaries.

ACADEMIC PROJECTS:
This project can be included in student portfolios as a demonstration of practical Python skills, especially in the areas of file handling, data analysis, and document automation.

OFFICE AND HR USE:
With slight modifications, this system can be adapted to generate employee performance summaries, attendance reports, or task completion stats in an organizational setup.


HOW IT WORKS:

The user places a file named student_scores.csv in the same folder as the script.

The script reads the file using pandas and extracts each row, which includes a student’s name and score.

Each entry is added to the PDF using FPDF with formatted spacing and consistent font.

The script saves the output as score_report.pdf in the same directory and prints a confirmation message to the terminal.


GETTING STARTED:

To run this project:

Ensure Python is installed on your system.

Install the required libraries using pip: pip install pandas fpdf

Place your student_scores.csv file in the project folder.

Run the Python script: python task2_report_generation.py

Open the generated score_report.pdf file to view the results.


This project is simple, powerful, and easily customizable. It is ideal for automating small but time-consuming reporting tasks in both academic and professional environments.

##OUTPUT
