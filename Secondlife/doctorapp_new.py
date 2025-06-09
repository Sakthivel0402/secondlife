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
q = """select * from doctor where id='%s'""" % (did)
cur.execute(q)
res = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Dashboard</title>

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
            padding : 10px 20px;
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
                <h3 class="text-center">Doctor Dashboard</h3>
            </div>

            <div class="sidebar-content">
               <ul class="list-unstyled components">
                    <li >
                        <a href="doctorindex.py?id={did}" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="active">
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled show" id="appointmentSubmenu">
                            <li class="active">
                                <a href="doctorapp_new.py?id={did}"><i class="bi bi-file-earmark-plus"></i> New</a>
                            </li>
                            <li >
                                <a href="doctorapp_old.py?id={did}"><i class="bi bi-check-circle"></i> Completed</a>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href="#leaveSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-calendar-x"></i> Leave
                        </a>
                        <ul class="collapse list-unstyled" id="leaveSubmenu">
                            <li>
                                <a href="doctor_leave.py?id={did}"><i class="bi bi-envelope"></i> New</a>
                            </li>
                            <li>
                                <a href="leave_status.py?id={did}"><i class="bi bi-check-circle"></i> Accepted</a>
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
""")

if res[0][13] == "aware":
    l = """Select * from addicted where doctor='%s' and status='Pending'""" % (res[0][1])
    cur.execute(l)
    add = cur.fetchall()
    print(add)

    print("""
                <div class="table-container">
                    <h2 style="color: var(--primary-color);">Patients</h2>
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="table-primary">
                                <tr>
                                    <th>SINO</th>
                                    <th>Patient</th>
                                    <th>Gender</th>
                                    <th>Addicted on</th>
                                    <th>Addicted for</th>
                                    <th>Consult on</th>
                                    <th>Status</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
    """)

    si = 1
    for i in add:
        print(f"""
        <tr>
            <td>{si}</td>
            <td>{i[1]}</td>
            <td>{i[6]}</td>
            <td>{i[3]}</td>
            <td>{i[4]}</td>
            <td>{i[5]}</td>
            <td><span class="status-badge status-pending">{i[9]}</span></td>
            <td>
                <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#myModal{i[0]}">
                    <i class="bi bi-check-circle"></i> Complete
                </button>
            </td>
        </tr>
        """)
        si += 1

        print(f"""
        <!-- Modal -->
        <div class="modal fade" id="myModal{i[0]}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header bg-primary text-white">
                        <h5 class="modal-title" id="exampleModalLabel">Appointment Completion</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form method="post">
                            <input type="hidden" value="{i[0]}" name="ID">
                            <div class="mb-3">
                                <label class="form-label">Consultation Notes</label>
                                <textarea class="form-control" name="FEED" rows="3" placeholder="Description about consultation" required></textarea>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <input type="submit" class="btn btn-primary" value="Submit" name="SUB">
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
    """)

    sub = form.getvalue("SUB")
    id = form.getvalue("ID")
    Feed = form.getvalue("FEED")
    if sub is not None:
        j = """update addicted set status='Completed',feed='%s' where id='%s'""" % (Feed, id)
        cur.execute(j)
        con.commit()
        print(f"""
        <script>
        location.href="doctorapp_new.py?id={did}";
        </script>
        """)

if res[0][13] == "Physician":
    n = """Select * from aware where doctor='%s' and status='Pending'""" % (res[0][1])
    cur.execute(n)
    aware = cur.fetchall()



    print("""
                <div class="table-container mt-4">
                    <h2 style="color: var(--primary-color);">Aware Patients</h2>
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead class="table-primary">
                                <tr>
                                    <th>SINO</th>
                                    <th>Patient</th>
                                    <th>Gender</th>
                                    <th>Consult with</th>
                                    <th>Consult on</th>
                                    <th>Status</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
    """)

    si = 1
    for i in aware:
        print(f"""
        <tr>
            <td>{si}</td>
            <td>{i[1]}</td>
            <td>{i[5]}</td>
            <td>{i[3]}</td>
            <td>{i[4]}</td>
            <td><span class="status-badge status-pending">{i[8]}</span></td>
            <td>
                <button class="btn btn-success btn-sm" data-bs-toggle="modal" data-bs-target="#myModala{i[0]}">
                    <i class="bi bi-check-circle"></i> Confirm
                </button>
            </td>
        </tr>
        """)
        si += 1

        print(f"""
        <!-- Modal -->
        <div class="modal fade" id="myModala{i[0]}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header bg-primary text-white">
                        <h5 class="modal-title" id="exampleModalLabel">Appointment Confirmation</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form method="post">
                            <input type="hidden" value="{i[0]}" name="ID2">
                            <div class="mb-3">
                                <label class="form-label">Consultation Notes</label>
                                <textarea class="form-control" name="FEED2" rows="3" placeholder="Description about consultation" required></textarea>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <input type="submit" class="btn btn-primary" value="Submit" name="SUB2">
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
    """)

    sub2 = form.getvalue("SUB2")
    id2 = form.getvalue("ID2")
    Feed2 = form.getvalue("FEED2")

    if sub2 is not None:
        from datetime import datetime

        current_date = datetime.now().strftime("%d-%m-%Y")

        j = "UPDATE aware SET status=%s, feed=%s, appointtime=%s WHERE id=%s"
        cur.execute(j, ('Completed', Feed2, current_date, id2))
        con.commit()

        print(f"""
        <script>
        location.href="doctorapp_new.py?id={did}";
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