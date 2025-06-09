#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb
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
    <title>Admin Dashboard</title>

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

        .table-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            margin-top: 30px;
            padding: 20px;
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
            padding: 10px 20px;
            transition: all 0.3s;
            text-decoration:none;
            border-left: 3px solid transparent !important;
        }

        .logout-btn:hover {
            background-color: rgba(220, 53, 69, 0.1) !important;
            border-left: 3px solid #dc3545 !important;
            transition: all 0.3s;
        }

        .logout-btn i {
            color: #dc3545 !important;
        }

        .dropdown-menu {
            background-color: var(--sidebar-color);
            border: 1px solid #dee2e6;
            border-radius: 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 0;
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
""")

print("""
<body>
    <div class="" id="wrapper">
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

                    <li>
                        <a href="#doctorSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-person-badge-fill"></i> Doctor
                        </a>
                        <ul class="collapse list-unstyled" id="doctorSubmenu">
                            <li>
                                <a href="doctoradd.py"><i class="bi bi-person-plus"></i> Add Doctor</a>
                            </li>
                            <li>
                                <a href="doctorexis.py"><i class="bi bi-list-ul"></i> Existing Doctors</a>
                            </li>
                        </ul>
                    </li>

                    <li class="active">
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled show" id="appointmentSubmenu">
                            <li class="active">
                                <a href="patientoff_new.py" style="text-decoration: underline #2d5b83 2px;"><i class="bi bi-file-earmark-plus"></i> New</a>
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
                            <h1 style="text-align:center; color: var(--primary-color);">New Appointments</h1>

            <div class="container-fluid">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i>
                </button>

                <div class="table-container">
""")

# Addicted Patients Table
b = """select * from addicted where status='Requested' and mode='offline'"""
cur.execute(b)
res = cur.fetchall()
b2 = """select * from doctor where role='Physician'"""
cur.execute(b2)
doc2 = cur.fetchall()

print("""
    <h3 class="mt-4" style="color: var(--secondary-color);">Addicted Patients</h3>
    <div class="table-responsive">
        <table class="table table-striped table-hover">
            <thead class="thead-dark">
                <tr>
                    <th>SINO</th>
                    <th>Registered On</th>
                    <th>Patient</th>
                    <th>Current Doctor</th>
                    <th>Consult With</th>
                    <th>Consult On</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
""")

si = 1
if res == ():
    print("""<tr><td colspan="7" class="text-danger text-center">No data found.</td></tr>""")
else:
    for i in res:
        timestamp_string = str(i[8])
        datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d %H:%M:%S.%f")
        formatted_date = datetime_object.strftime("%d-%m-%Y")

        print(f"""
        <tr>
            <td>{si}</td>
            <td>{formatted_date}</td>
            <td>{i[1]}</td>
            <td>{i[11]}</td>
            <td>
                <form method="post">
                    <select class="form-select" name="CHANGE2">
                        <option value="{i[2]}">{i[2]}</option>""")

        for q in doc2:
            print(f"""
                        <option value="{q[1]}">{q[1]} ({q[15]})</option>""")

        print(f"""
                    </select>
                </form>
            </td>
            <td>{i[5]}</td>
            <td>
                <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#addictedModal{i[0]}">
                    Confirm
                </button>
            </td>
        </tr>
        """)
        si += 1




    # Modal for each row
    print(f"""
    <!-- Modal for Addicted Patient {i[0]} -->
    <div class="modal fade" id="addictedModal{i[0]}" tabindex="-1" aria-labelledby="addictedModalLabel{i[0]}" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="addictedModalLabel{i[0]}">Appointment Confirmation</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form method="post">
                        <input type="hidden" value="{i[0]}" name="ID">
                        <p>Are you sure you want to confirm this appointment?</p>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                            <input type="submit" class="btn btn-primary" value="Confirm" name="SUB">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    """)

print("""
                            </tbody>
                        </table>
                    </div>
""")

# Aware Patients Table
e = """select * from aware where status='Requested' and mode='offline'"""
cur.execute(e)
ret = cur.fetchall()
b = """select * from doctor where role='Aware'"""
cur.execute(b)
doc = cur.fetchall()

print("""
                    <h3 class="mt-5" style="color: var(--secondary-color);">Aware Patients</h3>
                    <div class="table-responsive">
                        <table class="table table-striped table-hover">
                            <thead class="thead-dark">
                                <tr>
                                    <th>SINO</th>
                                    <th>Registered On</th>
                                    <th>Patient</th>
                                    <th>Current Doctor</th>
                                    <th>Consult With</th>
                                    <th>Consult On</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
""")

si = 1
for i in ret:
    timestamp_string = str(i[7])
    datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d %H:%M:%S.%f")
    formatted_date = datetime_object.strftime("%d-%m-%Y")
    print(f"""
    <tr>
        <td>{si}</td>
        <td>{formatted_date}</td>
        <td>{i[1]}</td>
        <td>{i[10]}</td>
        <td>
            <select class="form-select" name="CHANGE">
                <option value="{i[2]}">{i[2]}</option>
    """)
    for j in doc:
        print(f"""
                <option value="{j[1]}">{j[1]}</option>
    """)
    print(f"""
            </select>
        </td>
        <td>{i[4]}</td>
        <td>
            <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#awareModal{i[0]}">
                Confirm
            </button>
        </td>
    </tr>
    """)
    si += 1

    # Modal for each row
    print(f"""
    <!-- Modal for Aware Patient {i[0]} -->
    <div class="modal fade" id="awareModal{i[0]}" tabindex="-1" aria-labelledby="awareModalLabel{i[0]}" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="awareModalLabel{i[0]}">Appointment Confirmation</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form method="post">
                        <input type="hidden" value="{i[0]}" name="ID2">
                        <p>Are you sure you want to confirm this appointment?</p>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                            <input type="submit" class="btn btn-primary" value="Confirm" name="SUB2">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    """)

print("""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

# Handle form submissions
sub = form.getvalue("SUB")
doc2 = form.getvalue("CHANGE2")
id = form.getvalue("ID")
if sub is not None:
    j = """update addicted set doctor='%s',status='Pending' where id='%s'""" % (doc2, id)
    cur.execute(j)
    con.commit()
    print("""
    <script>
    location.href="patientoff_new.py";
    </script>
    """)

sub2 = form.getvalue("SUB2")
doc = form.getvalue("CHANGE")
id2 = form.getvalue("ID2")
if sub2 is not None:
    j = """update aware set doctor='%s',status='Pending' where id='%s'""" % (doc, id2)
    cur.execute(j)
    con.commit()
    print("""
    <script>
    location.href="patientoff_new.py";
    </script>
    """)