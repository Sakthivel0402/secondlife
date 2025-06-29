#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
form = cgi.FieldStorage()
did = form.getvalue("id")
q = """select * from patient where id='%s'""" % (did)
cur.execute(q)
res = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Dashboard</title>

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

        .welcome-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 30px;
            margin-top: 30px;
            border: none;
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

        .transparent-navbar {
            background-color: transparent !important;
            box-shadow: none !important;
        }

        .rehab-card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            padding: 20px;
            margin-top: 20px;
            border: none;
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

        /* Animation for searching */
        @keyframes dots {
            0%, 20% { content: "."; }
            40% { content: ".."; }
            60% { content: "..."; }
            80%, 100% { content: ""; }
        }

        .searching::after {
            content: "";
            animation: dots 1.5s steps(1, end) infinite;
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
                    <li class="active">
                        <a href="adminindex.py?id={did}">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="dropdown-submenu">
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="true" class="dropdown-toggle" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled " id="appointmentSubmenu">
                            <li>
                                <a href="patientreq.py?id={did}"><i class="bi bi-file-earmark-plus"></i> Request</a>
                            </li>
                            <li>
                                <a href="patientstatus.py?id={did}"><i class="bi bi-check-circle"></i> Status</a>
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

                <div class="welcome-card text-center">
                    <h1 style="color: var(--primary-color);">Welcome <span style="color: var(--dark-color);">{res[0][1]}</span></h1>
                    <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#passwordModal">
                        <i class="bi bi-key"></i> Change Password
                    </button>
                </div>

                <!-- Password Change Modal -->
                <div class="modal fade" id="passwordModal" tabindex="-1" aria-labelledby="passwordModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="passwordModalLabel">Change Password</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form method="post">
                                    <div class="mb-3">
                                        <label for="newPassword" class="form-label">New Password</label>
                                        <input type="password" class="form-control" id="newPassword" name="NPASS" required>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <input type="submit" class="btn btn-primary" value="Change Password" name="SUBMIT">
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
""")

search_sql = "SELECT * FROM rehab WHERE Cloc LIKE %s"
cur.execute(search_sql, ("%" + res[0][12] + "%",))
search_results = cur.fetchall()

print(f"""
                <div class="rehab-card text-center">
                    <h2 style="color: var(--primary-color); margin-bottom: 20px;">Nearby Rehabilitation Center</h2>
                    <button id="findButton" class="btn btn-primary">
                        <i class="bi bi-search"></i> Find Nearby Centers
                    </button>
                    <div id="loadingMessage" class="mt-3" style="display:none;">
                        <div class="spinner-border text-primary" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                        <p class="searching mt-2">Searching for rehabilitation centers</p>
                    </div>
                    <div id="result" class="mt-4" style="display:none;">
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">{search_results[0][1]}</h5>
                                <p class="card-text">
                                    <i class="bi bi-geo-alt"></i> {search_results[0][4]}, {search_results[0][3]}, {search_results[0][2]}
                                </p>
                                <p class="card-text"><i class="bi bi-telephone"></i> {search_results[0][6]}</p>
                            </div>
                        </div>
                    </div>
                </div>
""")

print("""
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

    <script>
        document.getElementById('findButton').addEventListener('click', function() {
            // Show loading indicator
            document.getElementById('loadingMessage').style.display = 'block';

            // Hide results if previously shown
            document.getElementById('result').style.display = 'none';

            // Disable button during search
            this.disabled = true;

            // Simulate search delay (in a real app, this would be an AJAX call)
            setTimeout(function() {
                // Hide loading indicator
                document.getElementById('loadingMessage').style.display = 'none';

                // Show results
                document.getElementById('result').style.display = 'block';

                // Re-enable button
                document.getElementById('findButton').disabled = false;
            }, 2000);
        });
    </script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
""")

npass = form.getvalue("NPASS")
sub = form.getvalue("SUBMIT")
if sub is not None:
    b = """Update patient set Password='%s' where id='%s'""" % (npass, res[0][0])
    cur.execute(b)
    con.commit()
    print("""
    <script>
    alert("Password changed successfully, login again");
    window.location.href="patientlogin.py";
    </script>
    """)