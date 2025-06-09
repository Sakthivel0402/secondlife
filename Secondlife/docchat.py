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
patientname2 = form.getvalue("id2")
cur.execute(f"""select Name from patient where id='{patientname2}'""")
patientname=cur.fetchone()

b="""select * from doctor where id='%s'"""%(did)
cur.execute(b)
doc=cur.fetchall()

# Reset unread messages count
b = """update chat set p='0' where patient='%s' and doctor='%s'""" % (patientname[0], doc[0][1])
cur.execute(b)
con.commit()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Chat</title>

    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            --primary-color: #2d5b83;
            --secondary-color: #1a3a5e;
            --sidebar-color: #ffffff;
            --sidebar-header-color: #2d5b83;
            --accent-color: #4a90e2;
            --light-color: #f8f9fa;
            --dark-color: #212529;
            --doctor-message: #d1e7dd;
            --patient-message: #e2e3e5;
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

        /* Chat Container Styles */
        .chat-container {
            max-width: 1200px;
            margin: 0 auto;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }

        .chat-header {
            background-color: var(--primary-color);
            color: white;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .chat-header h4 {
            margin: 0;
            font-weight: 500;
        }

        .chat-body {
            height: 75vh;
            overflow-y: auto;
            padding: 20px;
            background-color: #f8f9fa;
            display: flex;
            flex-direction: column;
        }

        .message {
            max-width: 70%;
            margin-bottom: 15px;
            padding: 12px 15px;
            border-radius: 12px;
            position: relative;
            word-wrap: break-word;
        }

        .message-patient {
            align-self: flex-start;
            background-color: var(--patient-message);
            border-top-left-radius: 4px;
        }

        .message-doctor {
            align-self: flex-end;
            background-color: var(--doctor-message);
            border-top-right-radius: 4px;
        }

        .message-time {
            font-size: 0.75rem;
            color: #6c757d;
            margin-top: 5px;
            text-align: right;
        }

        .chat-footer {
            background-color: white;
            padding: 15px 20px;
            border-top: 1px solid #dee2e6;
        }

        .message-input {
            border-radius: 20px;
            padding: 10px 20px;
            border: 1px solid #ced4da;
        }

        .send-btn {
            border-radius: 20px;
            padding: 10px 25px;
            background-color: var(--primary-color);
            border: none;
        }

        .send-btn:hover {
            background-color: var(--secondary-color);
        }

        .back-btn {
            border-radius: 20px;
            padding: 8px 15px;
        }

        /* Scrollbar styling */
        .chat-body::-webkit-scrollbar {
            width: 8px;
        }

        .chat-body::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }

        .chat-body::-webkit-scrollbar-thumb {
            background: #c1c1c1;
            border-radius: 10px;
        }

        .chat-body::-webkit-scrollbar-thumb:hover {
            background: #a8a8a8;
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

            .message {
                max-width: 85%;
            }
        }
    </style>
</head>
""")

print("""
<body>
    <div id="wrapper">
        <!-- Sidebar -->
        <div id="sidebar">
            <div class="sidebar-header">
                <h3 class="text-center">Doctor Dashboard</h3>
            </div>

            <div class="sidebar-content">
                <ul class="list-unstyled components">
                    <li>
                        <a href="doctorindex.py?id=%s">
                            <i class="bi bi-speedometer2"></i> Dashboard
                        </a>
                    </li>
                    <li class="active">
                        <a href="#appointmentSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle">
                            <i class="bi bi-calendar-check"></i> Appointment
                        </a>
                        <ul class="collapse list-unstyled show" id="appointmentSubmenu">
                            <li><a href="doctorapp_new.py?id=%s"><i class="bi bi-file-earmark-plus"></i> New</a></li>
                            <li class="active"><a href="doctorapp_old.py?id=%s"><i class="bi bi-check-circle"></i> Completed</a></li>
                        </ul>
                    </li>
                    <li >
                        <a href="#leaveSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle" style="text-decoration: underline #2d5b83 2px;">
                            <i class="bi bi-calendar-x"></i> Leave
                        </a>
                        <ul class="collapse list-unstyled " id="leaveSubmenu">
                            <li><a href="doctor_leave.py?id=%s"><i class="bi bi-envelope"></i> New</a></li>
                            <li><a href="leave_status.py?id=%s"><i class="bi bi-clock-history"></i> Status</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div class="sidebar-footer mb-3">
                <a href="doctorlogin.py" class="logout-btn d-block ">
                    <i class="bi bi-box-arrow-right"></i> Logout
                </a>
            </div>
        </div>
        </div>

        <!-- Page Content -->
        <div id="content">
            <div class="container-fluid">
                <div class="chat-container">
                    <div class="chat-header">
                        <h4><i class="fas fa-user-injured me-2"></i> Chat with %s</h4>
                        <button class="btn btn-light back-btn" onClick="location.href='doctorapp_old.py?id=%s';">
                            <i class="fas fa-arrow-left me-1"></i> Back
                        </button>
                    </div>

                    <div class="chat-body" id="chatBody">
""" % (did, did, did, did, did, patientname[0], did))

# Fetch and display chat messages
reciee = """select * from chat where patient='%s' and doctor='%s'""" % (patientname[0], doc[0][1])
cur.execute(reciee)
messages = cur.fetchall()

for message in messages:
    if message[4] == "Patient":
        print("""
        <div class="message message-patient">
            <div class="message-text">%s</div>
            <div class="message-time">%s</div>
        </div>""" % (message[3], message[8]))
    elif message[4] == "Doctor":
        print("""
        <div class="message message-doctor">
            <div class="message-text">%s</div>
            <div class="message-time">%s</div>
        </div>""" % (message[3], message[8]))

print("""
                    </div>

                    <div class="chat-footer">
                        <form method="post" class="d-flex">
                            <input type="hidden" name="PATIENT" value="%s">
                            <input type="hidden" name="DOCTOR" value="%s">
                            <input type="text" class="form-control message-input flex-grow-1 me-2" 
                                   placeholder="Type your message..." name="MESSAGE" required>
                            <input type="submit" class="btn btn-primary send-btn" name="SEND"
                               value="Send">
                            
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <script>
        // Auto-scroll to bottom of chat
        function scrollToBottom() {
            const chatBody = document.getElementById('chatBody');
            chatBody.scrollTop = chatBody.scrollHeight;
        }

        // Scroll to bottom on page load
        window.onload = scrollToBottom;

        // Auto-refresh chat every 5 seconds
        setInterval(function() {
            $.ajax({
                url: window.location.href,
                cache: false,
                success: function(data) {
                    const newChatBody = $(data).find('#chatBody').html();
                    $('#chatBody').html(newChatBody);
                    scrollToBottom();
                }
            });
        }, 5000);
    </script>
</body>
</html>
""" % (patientname[0], doc[0][1]))

# Process message sending
send = form.getvalue("SEND")
if send != None:
        doctor = form.getvalue("DOCTOR")
        patient = form.getvalue("PATIENT")
        message = form.getvalue("MESSAGE")

        # Insert new message
        b = """INSERT INTO chat(patient, doctor, message, sender, d) 
               VALUES('%s', '%s', '%s', 'Doctor', 'yes')""" % (patient, doctor, message)
        cur.execute(b)
        con.commit()
        print("""
                <script>
                window.location.href("docchat.py?id=%s&id2=%s");
                </script>
                """ % (did, patientname[0]))

        # Update message timestamp
        max_id_query = "SELECT MAX(id) FROM chat"
        cur.execute(max_id_query)
        max_id = cur.fetchone()[0]

        timestamp_string = str(datetime.now())
        datetime_object = datetime.strptime(timestamp_string, "%Y-%m-%d %H:%M:%S.%f")
        formatted_date = datetime_object.strftime("%H:%M | %d-%m-%Y")

        hv = """UPDATE chat SET mtime='%s' WHERE id='%s'""" % (formatted_date, max_id)
        cur.execute(hv)
        con.commit()

        # Update unread count
        bd = """SELECT * FROM chat WHERE patient='%s' AND doctor='%s'""" % (patient, doctor)
        cur.execute(bd)
        um = cur.fetchall()


        uum = 1
        uuum = str(uum)

        d = """UPDATE chat SET d='%s' WHERE patient='%s' AND doctor='%s'""" % (uuum, patient, doctor)
        cur.execute(d)
        con.commit()


        print("""
        <script>
        window.location.href("docchat.py?id=%s&id2=%s");
        </script>
        """ % (did, patientname[0]))