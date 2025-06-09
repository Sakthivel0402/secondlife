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
did = form.getvalue("id")

# Fetch patient data
q = """select * from patient where id='%s'""" % (did)
cur.execute(q)
res = cur.fetchall()
pname = res[0][1]
pgender = res[0][4]
pcity = res[0][13]

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Appointment Status</title>

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

        .status-approved {
            background-color: #d4edda;
            color: #155724;
        }

        .status-rejected {
            background-color: #f8d7da;
            color: #721c24;
        }

        .patient-info-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 20px;
            margin-bottom: 20px;
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

print(f"""
<body>
    <div class="" id="wrapper">
        <!-- Sidebar -->
        <div class="" id="sidebar">
            <div class="sidebar-header">
                <h3 class="text-center">Patient Dashboard</h3>
            </div>

            <div class="sidebar-content">
                <ul class="list-unstyled components">
                    <li>
                        <a href="patientindex.py?id={did}">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="active">
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled show" id="appointmentSubmenu">
                            <li>
                                <a href="patientreq.py?id={did}"><i class="bi bi-file-earmark-plus"></i> Request</a>
                            </li>
                            <li class="active">
                                <a href="patientstatus.py?id={did}" style="text-decoration: underline #2d5b83 2px;"><i class="bi bi-list-check"></i> Status</a>
                            </li>
                        </ul>
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

                <div class="patient-info-card">
                    <div class="row">
                        <div class="col-md-8">
                            <h2 style="color: var(--primary-color);">{pname}'s Appointments</h2>
                            <p class="lead">View and manage your appointment status</p>
                        </div>
                        <div class="col-md-4 text-end">
                            <p><strong>Gender:</strong> {pgender}</p>
                            <p><strong>Location:</strong> {pcity}</p>
                        </div>
                    </div>
                </div>

                <div class="table-container">
                    <h3 style="color: var(--secondary-color);">Your Appointment History</h3>
                    <div class="table-responsive">
                        <table class="table table-striped table-hover align-middle">
                            <thead class="table-dark">
                                <tr>
                                    <th>#</th>
                                    <th>Registered On</th>
                                    <th>Service Type</th>
                                    <th>Consult With</th>
                                    <th>Appointment Date</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
""")

# Fetch aware appointments
e = """select * from aware where patient='%s'""" % (res[0][1])
cur.execute(e)
ret = cur.fetchall()

# Fetch addicted appointments
o = """select * from addicted where patient='%s'""" % (res[0][1])
cur.execute(o)
ret1 = cur.fetchall()


si = 1
for i in ret:

    formatted_date = i[7]

    # Determine status badge
    status_class = "status-pending"
    if i[8] == "Approved":
        status_class = "status-approved"
    elif i[8] == "Rejected":
        status_class = "status-rejected"

    print(f"""
    <tr>
        <td>{si}</td>
        <td>{formatted_date}</td>
        <td>Awareness Program</td>
        <td>{i[2]}</td>
        <td>{i[4]}</td>
        """)
    if i[8] == "Completed":
        print(f"""<td><a href="./patient_com.py?id={did}" class="btn btn-primary">More options</a></td>""")
    else:
        print(f"""<td>{i[8]}</td>""")
    print(f"""
    </tr>
    """)
    si += 1

for i in ret1:



    # Determine status badge
    status_class = "status-pending"
    if i[9] == "Approved":
        status_class = "status-approved"
    elif i[9] == "Rejected":
        status_class = "status-rejected"

    print(f"""
    <tr>
        <td>{si}</td>
        <td>{i[8]}</td>
        <td>Addiction Treatment</td>
        <td>{i[2]}</td>
        <td>{i[5]}</td>
        
        """)
    if i[9]=="Completed":
        print(f"""<td><a href="./patient_com.py?id={did}" class="btn btn-primary">More options</a></td>""")
    else:
        print(f"""<td>{i[9]}</td>""")
    print(f"""
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