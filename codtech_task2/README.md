*A Script and a Sample Report*

#COMPANY NAME:CODTECH IT SOLUTIONS

#NAME:SUJAL VENGURLEKAR

#INTERN ID:CT06DR2365

#DOMAIN:PYTHON PROGRAMMING

#DURATION:4 WEEKS

#MENTOR:NEELA SANTOSH

#TASK_2 DISCRIPTION

This project is developed as part of CodTech Internship – Task 2.
The objective of this task is to automatically generate a formatted PDF report by reading data from a file, analyzing it, 
and presenting the results in a structured format using Python libraries.
The system reads student data from a CSV file, performs basic data analysis such as calculating average, highest, and lowest marks, 
and generates a professional PDF report without any manual intervention.

# Objectives
To read structured data from an external file
To analyze the data programmatically
To generate a formatted PDF report automatically
To understand file handling, data processing, and PDF generation in Python

# Tools & Technologies Used
Programming Language: Python
IDE / Platform: Visual Studio Code (VS Code)
Libraries Used:
pandas – for reading and analyzing CSV data
reportlab – for creating and formatting PDF reports

# Input File Description (data.csv)
The input file is a CSV (Comma Separated Values) file containing student names and their marks.
Sample Format:
Csv
Name,Marks
Sujal,85
Amit,78
Neha,92
Riya,88
Name → Student name
Marks → Marks obtained by the student
This file acts as the data source for report generation.

# Working of the Code (report_generator.py)
>Importing Required Libraries

import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
pandas is used to read and process CSV data.
reportlab is used to create and format the PDF report.

> Reading Data from CSV File

data = pd.read_csv("data.csv")
This reads the data from data.csv and stores it in a pandas DataFrame for further analysis.

>Data Analysis

average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()
The program calculates:
Average marks
Highest marks
Lowest marks
These values are later displayed in the PDF report.

>Creating the PDF Report

pdf = canvas.Canvas("output_report.pdf", pagesize=A4)
A new PDF file named output_report.pdf is created.
The A4 page size is used for professional formatting.

>Adding Content to the PDF
Title of the report
Statistical analysis results
Student-wise marks list
The content is added using drawString() method with appropriate fonts and spacing.

> Saving the PDF

pdf.save()
This finalizes and saves the generated PDF report.

> How to Run the Project

Step : Run the Script
python report_generator.py

# Output
A PDF file named output_report.pdf is generated automatically.
The report includes:
Title
Average, highest, and lowest marks
Individual student performance

# Applications of This Project

>Automated student result reports

>Internship and academic project reporting

>Business and sales data reporting

>Attendance and performance summaries

# Conclusion

This project demonstrates how Python can be used to automate report generation by combining data analysis and document creation. 
It reduces manual effort, improves accuracy, and produces professional reports efficiently. 
The use of libraries like pandas and reportlab makes the system flexible and scalable for real-world applications.

# Output
<img width="1783" height="988" alt="Image" src="https://github.com/user-attachments/assets/8d47d34e-b42c-454b-b597-07b3a65ad0c8" />
