#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, os
import cgitb, string, random, smtplib
from datetime import datetime

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Registration</title>

    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">

    <style>
        :root {
            --primary-color: #2d5b83;
            --secondary-color: #1a3a5e;
            --sidebar-color: #ffffff;
            --sidebar-header-color: #2d5b83;
            --accent-color: #4a90e2;
            --light-color: #f8f9fa;
            --dark-color: #212529;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
            min-height: 100vh;
        }

        #sidebar {
            background-color: var(--sidebar-color);
            color: var(--dark-color);
            height: 100vh;
            position: fixed;
            width: 280px;
            transition: all 0.3s;
            z-index: 1000;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
            border-right: 1px solid #dee2e6;
            display: flex;
            flex-direction: column;
        }

        #sidebar .sidebar-header {
            padding: 20px;
            background-color: var(--sidebar-header-color);
            color: white;
        }

        #sidebar .sidebar-content {
            flex: 1;
            overflow-y: auto;
        }

        #sidebar ul.components {
            padding: 20px 0;
            display: flex;
            flex-direction: column;
        }

        #sidebar ul li a {
            padding: 12px 20px;
            color: var(--dark-color);
            display: block;
            transition: all 0.3s;
            border-left: 3px solid transparent;
            text-decoration: none !important;
        }

        #sidebar ul li a:hover {
            background-color: rgba(41, 91, 131, 0.1);
            color: var(--primary-color);
            text-decoration: none;
            border-left: 3px solid var(--primary-color);
        }

        #sidebar ul li.active > a {
            background-color: rgba(41, 91, 131, 0.1);
            color: var(--primary-color);
            border-left: 3px solid var(--primary-color);
            font-weight: 500;
        }

        #sidebar ul li a i {
            margin-right: 10px;
            width: 20px;
            text-align: center;
            color: var(--primary-color);
        }

        .dropdown-toggle::after {
            display: inline-block;
            margin-left: 0.255em;
            vertical-align: 0.255em;
            content: "";
            border-top: 0.3em solid;
            border-right: 0.3em solid transparent;
            border-bottom: 0;
            border-left: 0.3em solid transparent;
            color: var(--primary-color);
        }

        .dropdown-menu {
            background-color: var(--sidebar-color);
            border: 1px solid #dee2e6;
            border-radius: 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .dropdown-item {
            color: var(--dark-color);
            padding: 10px 20px;
            text-decoration: none;
        }

        .dropdown-item:hover {
            background-color: rgba(41, 91, 131, 0.1);
            color: var(--primary-color);
        }

        #content {
            margin-left: 280px;
            padding: 20px;
            transition: all 0.3s;
            min-height: 100vh;
        }

        .navbar {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 15px 0;
        }

        .form-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 30px;
            margin-top: 30px;
        }

        .logo-img {
            height: 50px;
            transition: all 0.3s;
        }

        .logo-img:hover {
            transform: scale(1.05);
        }

        .logout-btn {
            color: #dc3545 !important;
            border-left: 3px solid transparent !important;
            text-decoration: none !important;
             padding: 10px 20px;
        }

        .logout-btn:hover {
            background-color: rgba(220, 53, 69, 0.1) !important;
            border-left: 3px solid #dc3545 !important;
        }

        .logout-btn i {
            color: #dc3545 !important;
        }

        .form-title {
            color: var(--primary-color);
            margin-bottom: 30px;
            text-align: center;
            font-weight: 600;
        }

        @media (max-width: 768px) {
            #sidebar {
                margin-left: -280px;
            }

            #sidebar.active {
                margin-left: 0;
            }

            #content {
                margin-left: 0;
            }

            #content.active {
                margin-left: 280px;
            }
        }
    </style>

    <script>
        function logout() {
            location.href = "index.py";
        }

        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('active');
            document.getElementById('content').classList.toggle('active');
        }
    </script>
</head>

<body>
    <div class="d-flex" id="wrapper">
        <!-- Sidebar -->
        <div class="" id="sidebar">
            <div class="sidebar-header">
                <h3 class="text-center">Admin Dashboard</h3>
            </div>

            <div class="sidebar-content">
                <ul class="list-unstyled components">
                    <li>
                        <a href="adminindex.py">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li>
                        <a href="patientexis.py">
                            <i class="bi bi-people-fill"></i> Patient List
                        </a>
                    </li>

                    <li class="active">
                        <a href="#doctorSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle">
                            <i class="bi bi-person-badge-fill"></i> Doctor
                        </a>
                        <ul class="collapse list-unstyled show" id="doctorSubmenu">
                            <li class="active">
                                <a href="doctoradd.py" style="text-decoration: underline #2d5b83 2px;">
                                    <i class="bi bi-person-plus"></i> Add Doctor
                                </a>
                            </li>
                            <li>
                                <a href="doctorexis.py"><i class="bi bi-list-ul"></i> Existing Doctors</a>
                            </li>
                        </ul>
                    </li>

                    <li>
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled" id="appointmentSubmenu">
                            <li>
                                <a href="patientoff_new.py"><i class="bi bi-file-earmark-plus"></i> New</a>
                            </li>
                            <li>
                                <a href="patientoff_exis.py"><i class="bi bi-check-circle"></i> Accepted</a>
                            </li>
                            <li>
                                <a href="patientoff_old.py"><i class="bi bi-archive"></i> Completed</a>
                            </li>
                        </ul>
                    </li>

                    <li>
                        <a href="#awareSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-megaphone"></i> Aware Program
                        </a>
                        <ul class="collapse list-unstyled" id="awareSubmenu">
                            <li>
                                <a href="awarepro.py"><i class="bi bi-plus-circle"></i> Add</a>
                            </li>
                            <li>
                                <a href="awarepro_exis.py"><i class="bi bi-person-check"></i> Assign Volunteer</a>
                            </li>
                        </ul>
                    </li>

                    <li>
                        <a href="#leaveSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-calendar-x"></i> Leave
                        </a>
                        <ul class="collapse list-unstyled" id="leaveSubmenu">
                            <li>
                                <a href="leave_accept.py"><i class="bi bi-envelope"></i> Requests</a>
                            </li>
                            <li>
                                <a href="leave_old.py"><i class="bi bi-clock-history"></i> History</a>
                            </li>
                        </ul>
                    </li>

                    <li>
                        <a href="rehab_add.py">
                            <i class="bi bi-building"></i> Rehabilation Center
                        </a>
                    </li>
                </ul>
            </div>

            <!-- Logout Button at the bottom of the sidebar -->
            <div class="sidebar-footer mb-3">
                <a href="javascript:logout()" class="logout-btn d-block">
                    <i class="bi bi-box-arrow-right"></i> Logout
                </a>
            </div>
        </div>

        <!-- Page Content -->
        <div id="content">
             <button class="btn btn-primary d-lg-none" onclick="toggleSidebar()">
                        <i class="bi bi-list"></i>
                    </button>

            <div class="container-fluid">
                <div class="form-container">
                    <h1 class="form-title">Doctor Registration</h1>
                    <form id="rehabForm" method="post" enctype="multipart/form-data">
                        <div class="form-group row mb-4">
                            <div class="col-md-4">
                                <label for="name" class="form-label">Full Name</label>
                                <input type="text" class="form-control" id="name" name="NAME" required>
                            </div>

                            <div class="col-md-4">
                                <label for="email" class="form-label">Email</label>
                                <input type="email" class="form-control" id="email" name="EMAIL" required>
                            </div>

                            <div class="col-md-4">
                                <label for="rehab" class="form-label">Rehabilitation Center</label>
                                <select class="form-select" name="REH" required>""")

b = """select * from rehab"""
cur.execute(b)
reh = cur.fetchall()
for i in reh:
    print(f"""
                                    <option value="{i[1]}">{i[1]}</option>""")

print("""
                                </select>
                            </div>
                        </div>

                        <div class="form-group row mb-4">
                            <div class="col-md-3">
                                <label for="dob" class="form-label">Date of Birth</label>
                                <input type="date" class="form-control" id="dob" name="DOB" required>
                            </div>

                            <div class="col-md-3">
                                <label for="gender" class="form-label">Gender</label>
                                <select class="form-select" id="gender" name="GENDER" required>
                                    <option value="male">Male</option>
                                    <option value="female">Female</option>
                                    <option value="other">Other</option>
                                </select>
                            </div>

                            <div class="col-md-3">
                                <label for="phno" class="form-label">Phone Number</label>
                                <input type="text" class="form-control" id="phno" name="PHNO" required>
                            </div>

                            <div class="col-md-3">
                                <label for="jd" class="form-label">Join Date</label>
                                <input type="date" class="form-control" name="JOINDATE" required>
                            </div>
                        </div>

                        <div class="form-group row mb-4">
                            <div class="col-md-3">
                                <label for="med" class="form-label">Medical License Number</label>
                                <input type="text" class="form-control" id="med" name="MEDI" required>
                            </div>

                            <div class="col-md-3">
                                <label for="yog" class="form-label">Year of Graduation</label>
                                <input type="text" class="form-control" id="yog" name="YOG" required>
                            </div>

                            <div class="col-md-3">
                                <label for="degree" class="form-label">Degree</label>
                                <select class="form-select" name="DEGREE" required>
                                    <option value="mbbs">MBBS (Bachelor of Medicine, Bachelor of Surgery)</option>
                                    <option value="md">MD (Doctor of Medicine)</option>
                                    <option value="ms">MS (Master of Surgery)</option>
                                    <option value="dm">DM (Doctorate of Medicine)</option>
                                    <option value="mch">MCh (Master of Chirurgiae)</option>
                                    <option value="dnb">DNB (Diplomate of National Board)</option>
                                    <option value="Psychologist">Psychologist</option>
                                </select>
                            </div>

                            <div class="col-md-3">
                                <label for="pic" class="form-label">Profile Image</label>
                                <input type="file" class="form-control" id="pic" name="PIC" required>
                            </div>
                        </div>

                        <div class="form-group row mb-4">
                            <div class="col-md-12">
                                <label for="aoa" class="form-label">Role</label>
                                <select class="form-select" id="awareOrAddicted" name="AOA" required>
                                    <option value="None">Select Role</option>
                                    <option value="aware">Counselor</option>
                                    <option value="Physician">Physician</option>
                                </select>
                            </div>
                        </div>

                        <div id="awareForContainer" class="form-group row mb-4" style="display:none;">
                            <div class="col-md-12">
                                <label for="awarefor" class="form-label">Experience</label>
                                <select class="form-select" id="awareFor" name="AWAREFOR">
                                    <option value="less1">Less than 1 year</option>
                                    <option value="1year">1 year</option>
                                    <option value="2year">2 years</option>
                                    <option value="more2">2+ years</option>
                                </select>
                            </div>
                        </div>

                        <div id="addictionTypeContainer" class="form-group row mb-4" style="display:none;">
                            <div class="col-md-6">
                                <label for="Specialization" class="form-label">Specialization</label>
                                <select class="form-select" id="addictionType" name="SPECIALIZATION">
                                    <option value="cardiologist">Cardiologist</option>
                                    <option value="neurologist">Neurologist</option>
                                    <option value="dermatologist">Dermatologist</option>
                                    <option value="oncologist">Oncologist</option>
                                    <option value="orthopedic_surgeon">Orthopedic Surgeon</option>
                                    <option value="gastroenterologist">Gastroenterologist</option>
                                    <option value="pulmonologist">Pulmonologist</option>
                                    <option value="endocrinologist">Endocrinologist</option>
                                </select>
                            </div>

                            <div class="col-md-6">
                                <label for="exp" class="form-label">Experience</label>
                                <select class="form-select" id="exp" name="EXP">
                                    <option value="rehabilitation">Less than 1 year</option>
                                    <option value="1year">1 year</option>
                                    <option value="2year">2 years</option>
                                    <option value="more2">2+ years</option>
                                </select>
                            </div>
                        </div>

                        <div class="form-group row mb-4">
                            <div class="col-md-6">
                                <label for="doorno" class="form-label">Door No</label>
                                <input type="text" class="form-control" id="doorno" name="DOORNO" required>
                            </div>

                            <div class="col-md-6">
                                <label for="address1" class="form-label">Address Line 1</label>
                                <input type="text" class="form-control" id="address1" name="ADD1" required>
                            </div>
                        </div>

                        <div class="form-group row mb-4">
                            <div class="col-md-6">
                                <label for="address2" class="form-label">Address Line 2</label>
                                <input type="text" class="form-control" id="address2" name="ADD2">
                            </div>

                            <div class="col-md-6">
                                <label for="city" class="form-label">City</label>
                                <input type="text" class="form-control" id="city" name="CITY" required>
                            </div>
                        </div>

                        <div class="form-group row mb-4">
                            <div class="col-md-6">
                                <label for="state" class="form-label">State</label>
                                <input type="text" class="form-control" id="state" name="STATE" required>
                            </div>

                            <div class="col-md-6">
                                <label for="country" class="form-label">Country</label>
                                <input type="text" class="form-control" id="country" name="COUNTRY" required>
                            </div>
                        </div>

                        <div class="row mt-4">
                            <div class="col-md-6 text-end">
                                <button type="submit" class="btn btn-primary px-4" name="SUBMIT">Submit</button>
                            </div>

                            <div class="col-md-6">
                                <a href="adminindex.py" class="btn btn-danger px-4">Cancel</a>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap 5 JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

    <script>
        $(document).ready(function () {
            $('#awareOrAddicted').change(function () {
                var awareForContainer = $('#awareForContainer');
                var addictionTypeContainer = $('#addictionTypeContainer');

                if (this.value === 'aware') {
                    awareForContainer.show();
                    addictionTypeContainer.hide();
                } else if (this.value === 'Physician') {
                    awareForContainer.hide();
                    addictionTypeContainer.show();
                } else {
                    awareForContainer.hide();
                    addictionTypeContainer.hide();
                }
            });
        });
    </script>
</body>
</html>
""")
sub=form.getvalue("SUBMIT")
if sub!= None:
    name = form.getvalue('NAME')
    email = form.getvalue('EMAIL')
    dob = form.getvalue('DOB')
    gender = form.getvalue('GENDER')
    reha=form.getvalue("REH")
    jd=form.getvalue("JOINDATE")
    phno = form.getvalue('PHNO')
    degree= form.getvalue('DEGREE')
    medical_license = form.getvalue('MEDI')
    yog = form.getvalue('YOG')
    role = form.getvalue('AOA')
    aware_for = form.getvalue('AWAREFOR')
    specialization = form.getvalue('SPECIALIZATION')
    exp = form.getvalue('EXP')
    doorno = form.getvalue('DOORNO')
    address1 = form.getvalue('ADD1')
    address2 = form.getvalue('ADD2')
    city = form.getvalue('CITY')
    state = form.getvalue('STATE')
    country = form.getvalue('COUNTRY')
    pic = form['PIC']
    timestamp_string = str(dob)
    datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d")
    formatted_date = datetime_object.strftime("%d-%m-%Y")
    timestamp_string2 = str(jd)
    datetime_object2 = datetime.strptime(timestamp_string2, "%Y-%m-%d")
    formatted_date2 = datetime_object2.strftime("%d-%m-%Y")
    if pic.filename:

        folder_path = 'doctor_pics'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        pic_path = os.path.join(folder_path, pic.filename)
        with open(pic_path, 'wb') as f:
            f.write(pic.file.read())
        q = """
                INSERT INTO Doctor (Name, Email, DOB, Gender,Joindate, 
                                    Phone,Degree, MedicalLicense, YearOfGraduation, 
                                    ProfilePic, Role, Experience, Specialization, 
                                    YearsOfExperience, DoorNo, Address1, Address2, 
                                    City, State, Country,reh)
                VALUES ('%s',  '%s', '%s', '%s', '%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')
            """%(name, email,formatted_date, gender,formatted_date2,phno,degree, medical_license, yog, pic_path, role, aware_for,specialization, exp, doorno, address1, address2, city,state, country,reha)
        cur.execute(q)
        con.commit()
        print("""
        <script>
        alert("Registration success");
        </script>
        """)