Sure buddy! ❤️ Here is your complete Python Activity – University Scholarship Allocation System, arranged in the format required for your practical record.

# 1. University Scholarship Allocation

## 1. Problem Statement

Design a Python program to allocate university scholarships based on students' aggregate marks, subject-wise minimum marks, attendance percentage, and annual family income.

The program should identify eligible students, rank them according to aggregate marks, and resolve ties using attendance percentage. Students who satisfy all the eligibility conditions will be selected for the scholarship.

## 2. Algorithm

1. Start the program.
2. Read the number of students.
3. Enter each student's name.
4. Read aggregate marks.
5. Read marks in three subjects.
6. Read attendance percentage.
7. Read annual family income.
8. Check the eligibility conditions:
   - Aggregate marks must be at least 75.
   - Each subject mark must be at least 40.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹3,00,000.
9. Add eligible students to the list.
10. Sort eligible students based on aggregate marks.
11. If aggregate marks are equal, rank the student with higher attendance first.
12. Display the eligible students with their ranks.
13. Stop the program.

## 3. Flowchart

[Bab 4. Struktur Keputusan - HackMD](https://images.openai.com/static-rsc-4/EV4HwxHtW_tHtLyGdGKXoOvYKYh6K8GWXaB8OoJ52729Ik7R_Mr-LyoYg5oTYrAJ3kfAjZ4uoSDka2hvEmNtVuTfCnQNA33VRjirqGcVA_lZ1rrsS8W42xxKyhHb2Z50H2tUb0JwuoZHzC0TJmk055aLc0uiMIbPaCYqzsJ5qUI?purpose=inline)

[hackmd.io](https://hackmd.io/OQjQ-gqVSBiggUx8g_Bu7g?utm_source=chatgpt.com)

## 4. Python Source Code

```
# University Scholarship Allocation Systemn = int(input("Enter number of students: "))students = []for i in range(n):    print("\nEnter details of student", i + 1)    name = input("Enter student name: ")    marks = int(input("Enter aggregate marks: "))    m1 = int(input("Enter subject 1 marks: "))    m2 = int(input("Enter subject 2 marks: "))    m3 = int(input("Enter subject 3 marks: "))    attendance = float(input("Enter attendance percentage: "))    income = int(input("Enter annual family income: "))    if (marks >= 75 and m1 >= 40 and m2 >= 40        and m3 >= 40 and attendance >= 75        and income <= 300000):        students.append([name, marks, attendance])# Sort students based on marks and attendancestudents.sort(key=lambda x: (x[1], x[2]), reverse=True)print("\n--- SCHOLARSHIP ELIGIBLE STUDENTS ---")if len(students) == 0:    print("No students are eligible for scholarship.")else:    for i in range(len(students)):        print("\nRank:", i + 1)        print("Name:", students[i][0])        print("Aggregate Marks:", students[i][1])        print("Attendance:", students[i][2])print("\nScholarship Allocation Completed!")
```

## 5. Sample Output

```
Enter number of students: 3

Enter details of student 1
Enter student name: Nayana
Enter aggregate marks: 90
Enter subject 1 marks: 85
Enter subject 2 marks: 90
Enter subject 3 marks: 88
Enter attendance percentage: 95
Enter annual family income: 200000

Enter details of student 2
Enter student name: Priya
Enter aggregate marks: 85
Enter subject 1 marks: 80
Enter subject 2 marks: 85
Enter subject 3 marks: 90
Enter attendance percentage: 90
Enter annual family income: 250000

Enter details of student 3
Enter student name: Rahul
Enter aggregate marks: 60
Enter subject 1 marks: 50
Enter subject 2 marks: 55
Enter subject 3 marks: 60
Enter attendance percentage: 80
Enter annual family income: 200000

--- SCHOLARSHIP ELIGIBLE STUDENTS ---

Rank: 1
Name: Nayana
Aggregate Marks: 90
Attendance: 95.0

Rank: 2
Name: Priya
Aggregate Marks: 85
Attendance: 90.0

Scholarship Allocation Completed!
```

## 6. Mermaid Flowchart Code

You can copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_e7\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_e7\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_e7\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_e7\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_e7\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e7\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_e7\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_e7\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_e7\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_e7\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_e7\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_e7\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e7\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e7\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_e7\_ p{margin:0;}#chatgpt-mermaid-\_r_e7\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e7\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e7\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e7\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_e7\_ .label text,#chatgpt-mermaid-\_r_e7\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e7\_ .node rect,#chatgpt-mermaid-\_r_e7\_ .node circle,#chatgpt-mermaid-\_r_e7\_ .node ellipse,#chatgpt-mermaid-\_r_e7\_ .node polygon,#chatgpt-mermaid-\_r_e7\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_e7\_ .rough-node .label text,#chatgpt-mermaid-\_r_e7\_ .node .label text,#chatgpt-mermaid-\_r_e7\_ .image-shape .label,#chatgpt-mermaid-\_r_e7\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_e7\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_e7\_ .rough-node .label,#chatgpt-mermaid-\_r_e7\_ .node .label,#chatgpt-mermaid-\_r_e7\_ .image-shape .label,#chatgpt-mermaid-\_r_e7\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_e7\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_e7\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e7\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e7\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_e7\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_e7\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_e7\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_e7\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_e7\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_e7\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_e7\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e7\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e7\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_e7\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_e7\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_e7\_ .icon-shape,#chatgpt-mermaid-\_r_e7\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_e7\_ .icon-shape p,#chatgpt-mermaid-\_r_e7\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_e7\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_e7\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_e7\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_e7\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_e7\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_e7\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_e7\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_e7\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_e7\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e7\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_e7\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_e7\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_e7\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_e7\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_e7\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_e7\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_e7\_ .node rect,#chatgpt-mermaid-\_r_e7\_ .node circle,#chatgpt-mermaid-\_r_e7\_ .node ellipse,#chatgpt-mermaid-\_r_e7\_ .node polygon,#chatgpt-mermaid-\_r_e7\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_e7\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_e7\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_e7\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_e7\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_e7\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of studentsEnter student detailsEnter marks, attendance andincomeAggregate = 75?Each subject = 40?Student not eligibleAttendance = 75%?Income <= 300000?Add student to eligible listMore students?Sort by marks and attendanceDisplay student rankingStopYesNoYesNoYesNoYesNoYesNo

## 7. Result

The University Scholarship Allocation System was successfully implemented using Python. The program checks student eligibility based on marks, attendance, and family income, ranks eligible students, and displays the scholarship allocation list.

Practical tip: Write these seven sections in the same order in your record. The Python code is kept beginner-friendly and uses basic concepts such as loops, conditions, lists, and sorting. ❤️
