#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb
from datetime import datetime
import smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()
vname = form.getvalue("id")


print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volunteer Assignment</title>

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

        .table-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 30px;
            width:1200px !important;
            margin-top: 30px;
            max-width: 800px;
        }

        .logo-img {
            height: 80px;
            transition: all 0.3s;
        }

        .logo-img:hover {
            transform: scale(1.05);
        }

        .program-title {
            color: var(--primary-color);
            margin-bottom: 20px;
            font-weight: 600;
        }

        .volunteer-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
        }

        .volunteer-table th {
            background-color: var(--primary-color);
            color: white;
            padding: 12px 15px;
            text-align: left;
        }

        .volunteer-table td {
            padding: 12px 15px;
            border-bottom: 1px solid #dee2e6;
        }

        .volunteer-table tr:last-child td {
            border-bottom: none;
        }

        .volunteer-table tr:hover td {
            background-color: rgba(41, 91, 131, 0.05);
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
                                <a href="doctoradd.py">
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
                    <li class="active">
                        <a href="#awareSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-megaphone"></i> Aware Program
                        </a>
                        <ul class="collapse list-unstyled show" id="awareSubmenu">
                            <li>
                                <a href="awarepro.py"><i class="bi bi-plus-circle"></i> Add</a>
                            </li>
                            <li class="active">
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
            <div class="container-fluid mt-5">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i> Toggle Menu
                </button>

                

                
                    <h3 class="program-title">Volunteers Assigned to: {}</h3>
                    <div class="table-responsive">
                        <table class="table volunteer-table">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Volunteer Name</th>
                                </tr>
                            </thead>
                            <tbody>
""".format(vname))

# Fetch and display assigned volunteers
b = """select * from awarepdetail where AName='%s'""" % (vname)
cur.execute(b)
awap = cur.fetchall()

si = 1
for i in awap:
    print(f"""
                            <tr>
                                <td>{si}</td>
                                <td>{i[2]}</td>
                            </tr>
    """)
    si += 1

print("""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")