#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()
aid = form.getvalue("id")
b = """select * from awarep where id='%s'""" % (aid)
cur.execute(b)
awaredetails = cur.fetchall()
d = """select * from volunteer"""
cur.execute(d)
vol = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assign Volunteers - Admin Dashboard</title>

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
            border-left: 3px solid transparent !important;
            text-decoration: none !important;
        }

        .logout-btn:hover {
            background-color: rgba(220, 53, 69, 0.1) !important;
            border-left: 3px solid #dc3545 !important;
        }

        .logout-btn i {
            color: #dc3545 !important;
        }

        .transparent-navbar {
            background-color: transparent !important;
            box-shadow: none !important;
        }

        .availability-badge {
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .available {
            background-color: #d4edda;
            color: #155724;
        }

        .unavailable {
            background-color: #f8d7da;
            color: #721c24;
        }

        .form-check-input:checked {
            background-color: var(--primary-color);
            border-color: var(--primary-color);
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

        function toggleAll(source) {
            const checkboxes = document.querySelectorAll('input[name="CB"]');
            checkboxes.forEach(checkbox => {
                checkbox.checked = source.checked;
            });
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
                                <a href="leave_accept.py"><i class="bi bi-envelope"></i> Request</a>
                            </li>
                            <li>
                                <a href="leave_old.py"><i class="bi bi-clock-history"></i> Old</a>
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
            <div class="container-fluid">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i>
                </button>

                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h1 style="color: var(--primary-color);">Assign Volunteers</h1>
                </div>

                <div class="alert alert-info">
                    <i class="bi bi-info-circle"></i> You are assigning volunteers for: <strong>%s</strong>
                </div>
""" % awaredetails[0][1])

print("""
                <div class="table-container">
                    <form method="post">
                        <div class="table-responsive">
                            <table class="table table-hover">
                                <thead class="table-primary">
                                    <tr>
                                        <th width="50px">
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" name="ALL" id="selectAll" onclick="toggleAll(this)">
                                            </div>
                                        </th>
                                        <th>SINO</th>
                                        <th>Volunteer Name</th>
                                        <th>Availability</th>
                                        <th>City</th>
                                    </tr>
                                </thead>
                                <tbody>
""")

si = 1
for i in vol:
    availability_class = "available" if i[4] == "Yes" else "unavailable"
    availability_text = "Available" if i[4] == "Yes" else "Unavailable"

    print(f"""
    <tr>
        <td>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" name="CB" value="{i[1]}" id="volunteer{i[0]}" {'disabled' if i[4] != 'Yes' else ''}>
            </div>
        </td>
        <td>{si}</td>
        <td>{i[1]}</td>
        <td><span class="availability-badge {availability_class}">{availability_text}</span></td>
        <td>{i[6]}</td>
    </tr>
    """)
    si += 1

print("""
                                </tbody>
                            </table>
                        </div>
                        <div class="text-end mt-3">
                            <button type="submit" name="SUB" value="Submit" class="btn btn-primary">
                                <i class="bi bi-send"></i> Assign Selected Volunteers
                            </button>
                        </div>
                    </form>
                </div>
""")

all = form.getvalue("ALL")
sub = form.getvalue("SUB")
cb = form.getvalue("CB")

if sub is not None:
    if all is not None:
        for i in vol:
            if i[4] == "Yes":  # Only assign available volunteers
                b = """INSERT INTO awarepdetail(AName, Volunteer) VALUES('%s', '%s')""" % (awaredetails[0][1], i[1])
                cur.execute(b)
                con.commit()
        print("""
        <script>
        alert("All available volunteers assigned successfully");
        location.href="awarepro_exis.py";
        </script>
        """)
    elif cb:
        if isinstance(cb, list):
            for cv in cb:
                d = """INSERT INTO awarepdetail(AName, Volunteer) VALUES('%s', '%s')""" % (awaredetails[0][1], cv)
                cur.execute(d)
                con.commit()
        else:
            d = """INSERT INTO awarepdetail(AName, Volunteer) VALUES('%s', '%s')""" % (awaredetails[0][1], cb)
            cur.execute(d)
            con.commit()
        print("""
        <script>
        alert("Selected volunteers assigned successfully");
        location.href="awarepro_exis.py";
        </script>
        """)
    else:
        print("""
        <script>
        alert("Please select at least one volunteer");
        </script>
        """)

print("""
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")