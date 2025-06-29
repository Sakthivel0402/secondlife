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
    <title>Patient Appointments</title>

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
            margin-top: 30px;
        }

        .appointment-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
        }

        .appointment-table th {
            background-color: var(--primary-color);
            color: white;
            padding: 12px 15px;
            text-align: left;
        }

        .appointment-table td {
            padding: 12px 15px;
            border-bottom: 1px solid #dee2e6;
            vertical-align: middle;
        }

        .appointment-table tr:last-child td {
            border-bottom: none;
        }

        .appointment-table tr:hover td {
            background-color: rgba(41, 91, 131, 0.05);
        }

        .btn-chat {
            background-color: #28a745;
            color: white;
            padding: 8px 15px;
            border-radius: 4px;
            transition: all 0.3s;
        }

        .btn-chat:hover {
            background-color: #218838;
            color: white;
        }

        .btn-success-story {
            background-color: #17a2b8;
            color: white;
            padding: 8px 15px;
            border-radius: 4px;
            transition: all 0.3s;
        }

        .btn-success-story:hover {
            background-color: #138496;
            color: white;
        }

        .badge-notification {
            position: relative;
            top: -10px;
            right: -5px;
            background-color: #dc3545;
            color: white;
            border-radius: 50%;
            padding: 3px 6px;
            font-size: 12px;
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
                <h3 class="text-center">Patient Dashboard</h3>
            </div>

            <div class="sidebar-content">
                <ul class="list-unstyled components">
                    <li>
                        <a href="patientindex.py?id=%s">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="active">
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled show" id="appointmentSubmenu">
                            <li>
                                <a href="patientreq.py?id=%s">
                                    <i class="bi bi-file-earmark-plus"></i> Request
                                </a>
                            </li>
                            <li class="active">
                                <a href="patientstatus.py?id=%s">
                                    <i class="bi bi-clock-history"></i> Status
                                </a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div class="sidebar-footer mb-3">
                <a href="javascript:logout()" class="logout-btn d-block">
                    <i class="bi bi-box-arrow-right"></i> Logout
                </a>
            </div>
        </div>
        </div>

        <!-- Page Content -->
        <div id="content">
            <div class="container-fluid">
                <button class="btn btn-primary d-lg-none mb-3" onclick="toggleSidebar()">
                    <i class="bi bi-list"></i> Toggle Menu
                </button>

               

                <div class="table-container">
                    <h3 style="color: var(--primary-color); margin-bottom: 20px;">Completed Appointments</h3>
                    <div class="table-responsive">
                        <table class="table appointment-table">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Consult With</th>
                                    <th>Consult Date</th>
                                    <th>Doctor Feedback</th>
                                    <th>Success Story</th>
                                    <th>Chat</th>
                                </tr>
                            </thead>
                            <tbody>
""" % (did, did, did))

# Fetch and tag aware appointments
e = """SELECT * FROM aware WHERE status='Completed' AND id='%s'""" % (res[0][0])
cur.execute(e)
aware_appointments = [('aware', row) for row in cur.fetchall()]

# Fetch and tag addicted appointments
o = """SELECT * FROM addicted WHERE status='Completed' AND id='%s'""" % (res[0][0])
cur.execute(o)
addicted_appointments = [('addicted', row) for row in cur.fetchall()]


si = 1
for source, app in aware_appointments + addicted_appointments:
    if source == 'aware':
        timestamp_string = str(app[7])
    else:  # addicted
        timestamp_string = str(app[8])

    try:
        datetime_object = datetime.strptime(timestamp_string, "%d-%m-%Y")
        formatted_date = datetime_object.strftime("%d-%m-%Y")
    except ValueError:
        formatted_date = "Invalid date"

    # Check for unread messages
    b = """SELECT * FROM chat WHERE patient='%s' AND doctor='%s'""" % (pname, app[2])
    cur.execute(b)
    chat_data = cur.fetchall()
    unread_count = chat_data[0][6] if chat_data and chat_data[0][6] != "0" else 0

    print(f"""
    <tr>
        <td>{si}</td>
        <td>{app[2]}</td>
        <td>{formatted_date}</td>
        <td>{timestamp_string}</td>
        <td>
            <button class="btn btn-success-story" onclick="location.href='success_story.py?id={did}'">
                <i class="bi bi-pencil-square"></i> Share
            </button>
        </td>
        <td>
            <button class="btn btn-chat" onclick="location.href='patient_chat.py?id={did}&id2={app[2]}'">
                <i class="bi bi-chat-left-text"></i> Chat
                {f'<span class="badge-notification">{unread_count}</span>' if unread_count else ''}
            </button>
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