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

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aware Program Management</title>

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
            padding: 20px;
            margin-top: 20px;
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

        .status-badge {
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .status-pending {
            background-color: #fff3cd;
            color: #856404;
        }

        .status-completed {
            background-color: #d4edda;
            color: #155724;
        }

        .status-active {
            background-color: #d1ecf1;
            color: #0c5460;
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

        function assignEvent(id) {
            location.href = "awareproassign.py?id=" + id;
        }

        function viewVolunteers(id) {
            location.href = "awareassignedvol.py?id=" + id;
        }

        function markCompleted(id) {
            if(confirm("Are you sure you want to mark this event as completed?")) {
                document.getElementById("completeForm"+id).submit();
            }
        }
    </script>
</head>
""")

print("""
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
                        <a href="#awareSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle">
                            <i class="bi bi-megaphone"></i> Aware Program
                        </a>
                        <ul class="collapse list-unstyled show" id="awareSubmenu">
                            <li>
                                <a href="awarepro.py"><i class="bi bi-plus-circle"></i> Add</a>
                            </li>
                            <li class="active">
                                <a href="awarepro_exis.py" style="text-decoration: underline #2d5b83 2px;"><i class="bi bi-person-check"></i> Assign Volunteer</a>
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
                <a href="javascript:logout()" class="logout-btn d-block ">
                    <i class="bi bi-box-arrow-right"></i> Logout
                </a>
            </div>
        </div>

        <!-- Page Content -->
        <div id="content">
            <div class="container-fluid">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i>
                </button>

                <h1 style="color: var(--primary-color);">Aware Program Management</h1>
                <p class="lead">Manage awareness programs and volunteer assignments</p>

                <div class="table-container">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h3 style="color: var(--secondary-color);">Current Programs</h3>
                        <a href="awarepro.py" class="btn btn-primary">
                            <i class="bi bi-plus-circle"></i> Add New Program
                        </a>
                    </div>

                    <div class="table-responsive">
                        <table class="table table-striped table-hover align-middle">
                            <thead class="table-dark">
                                <tr>
                                    <th>#</th>
                                    <th>Event Name</th>
                                    <th>Doctor Assigned</th>
                                    <th>Event Date</th>
                                    <th>Event Timing</th>
                                    <th>Volunteer</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
""")

# Fetch aware programs data
b = """select * from awarep"""
cur.execute(b)
awap = cur.fetchall()

si = 1
for i in awap:
    # Determine status badge class based on status
    status_class = "status-pending"
    status_text = "Pending"
    if "Completed" in str(i[9]):  # Assuming status is in column 9
        status_class = "status-completed"
        status_text = "Completed"
    elif "Active" in str(i[9]):
        status_class = "status-active"
        status_text = "Active"

    print(f"""
    <tr>
        <td>{si}</td>
        <td><strong>{i[1]}</strong></td>
        <td>{i[8] if i[8] else 'Not assigned'}</td>
        <td>{i[2]}</td>
        <td>{i[4]} to {i[5]}</td>
        <td>
            <button class="btn btn-outline-primary btn-sm" onclick="viewVolunteers('{i[0]}')">
                <i class="bi bi-people-fill"></i> View Volunteers
            </button>
        </td>
        <td>
            <span class="status-badge {status_class}">{status_text}</span>
        </td>
        <td>
            <div class="d-flex gap-2">
                <button class="btn btn-primary btn-sm" onclick="assignEvent('{i[0]}')">
                    <i class="bi bi-person-plus"></i> Assign
                </button>
                <form id="completeForm{i[0]}" method="post" style="display: inline;">
                    <input type="hidden" name="ID" value="{i[0]}">
                    <button type="button" class="btn btn-success btn-sm" onclick="markCompleted('{i[0]}')">
                        <i class="bi bi-check-circle"></i> Complete
                    </button>
                </form>
            </div>
        </td>
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
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")

# Handle form submission for marking as completed
sub = form.getvalue("submit")
id = form.getvalue("ID")
if sub is not None:
    b = """update awarep set status='Completed' where id='%s'""" % (id)
    cur.execute(b)
    con.commit()
    print("""
    <script>
    location.href="awarepro_exis.py";
    </script>
    """)