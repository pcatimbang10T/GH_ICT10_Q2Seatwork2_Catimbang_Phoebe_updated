from pyscript import document

def calculate_grade(event):
    # Get values from inputs
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    sci = float(document.getElementById("sciGrade").value)
    math = float(document.getElementById("mathGrade").value)
    eng = float(document.getElementById("engGrade").value)
    ict = float(document.getElementById("ictGrade").value)
    fil = float(document.getElementById("filGrade").value)
    mapeh = float(document.getElementById("mapehGrade").value)
    cat = float(document.getElementById("catGrade").value)
    tle = float(document.getElementById("tleGrade").value)

    subjects = ["Science", "Math", "English", "ICT", "Filipino", "MAPEH", "CAT", "TLE"]
    units = (5, 5, 4, 5, 4, 3, 2, 4)
    grades = [sci, math, eng, ict, fil, mapeh, cat, tle]

    total_units = sum(units)
    weighted_sum = sum(grades[i] * units[i] for i in range(len(grades)))
    gwa = weighted_sum / total_units

    output = document.getElementById("output")
    output.innerHTML = f"""
        <h3>Student Info</h3>
        Name: {fname} {lname}<br>
        Subjects: {subjects}<br>
        Grades: {grades}<br>
        <b>General Weighted Average:</b> {gwa:.2f}<br>
    """
    # pass or fail
    if gwa > 75:
        msg = "Congratulations! You passed!"
    else:
        msg = "Unfortunately, you failed."
    output.innerHTML += f"<p>{msg}</p>"