#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="secondlife")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

    <style>
        :root {
            --primary-color: #2d5b83;
            --secondary-color: #1a3a5e;
            --accent-color: #4a90e2;
            --light-color: #f8f9fa;
            --dark-color: #343a40;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            color: #333;
        }

        .navbar-custom {
            background-color: white;
            border-bottom: 3px solid var(--primary-color);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            min-height: 80px;
        }

        .navbar-custom .navbar-nav > li > a {
            color: var(--dark-color);
            margin-top: 22px;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.3s ease;
            padding: 10px 15px;
            border-radius: 4px;
        }

        .navbar-custom .navbar-nav > li > a:hover,
        .navbar-custom .navbar-nav > li > a:focus {
            background-color: var(--primary-color);
            color: white !important;
        }

        .navbar-brand img {
            height: 50px;
            width: auto;
            transition: all 0.3s ease;
        }

        .navbar-brand img:hover {
            transform: scale(1.05);
        }

        .dropdown-menu {
            border-radius: 0;
            border: 1px solid rgba(0, 0, 0, 0.1);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .dropdown-menu > li > a {
            color: var(--dark-color);
            padding: 10px 20px;
            transition: all 0.3s ease;
        }

        .dropdown-menu > li > a:hover {
            background-color: var(--primary-color);
            color: white !important;
        }

        .content-box {
            max-height: 580px;
            overflow-y: auto;
            scrollbar-width: none;
            -ms-overflow-style: none;
            padding: 15px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }

        .content-box::-webkit-scrollbar {
            display: none;
        }

        .panel {
            border-radius: 8px;
            box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            border: none;
            transition: transform 0.3s ease;
        }

        .panel:hover {
            transform: translateY(-5px);
        }

        .panel-heading {
            border-radius: 8px 8px 0 0 !important;
            background-color: var(--primary-color) !important;
            color: white !important;
            padding: 15px 20px;
            border-bottom: none;
        }

        .panel-title {
            font-weight: 600;
            font-size: 18px;
        }

        .panel-body {
            padding: 20px;
            background-color: white;
            border-radius: 0 0 8px 8px;
        }

        .btn-primary {
            background-color: var(--primary-color);
            border-color: var(--primary-color);
            padding: 8px 20px;
            border-radius: 4px;
            transition: all 0.3s ease;
        }

        .btn-primary:hover {
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
            transform: translateY(-2px);
        }

        h1 {
            color: var(--primary-color);
            margin-bottom: 30px;
            font-weight: 700;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }

        .footer-custom {
            background-color: var(--primary-color);
            color: white;
            padding: 25px 0;
            margin-top: 40px;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
        }

        .footer-custom a {
            color: white;
            transition: all 0.3s ease;
        }

        .footer-custom a:hover {
            color: #ddd;
            text-decoration: none;
        }

        .success-story-img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 4px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .awareness-img {
            width: 100%;
            max-height: 200px;
            object-fit: contain;
            border-radius: 4px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .divider {
            border-left: 2px solid #eee;
            height: 100%;
        }

        @media (max-width: 768px) {
            .divider {
                border-left: none;
                border-top: 2px solid #eee;
                margin: 30px 0;
                padding-top: 20px;
            }

            .navbar-brand img {
                height: 40px;
            }

            .content-box {
                max-height: 400px;
            }
        }
    </style>
</head>

<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-default navbar-fixed-top navbar-custom">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#myNavbar" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href=""><img style="width:300px !important; height:300px !important; margin-top:-110px !important;" src="image/logo.png"></a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                            <i class="fas fa-sign-in-alt"></i> Login <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="patientlogin.py"><i class="fas fa-user-injured"></i> Patient</a></li>
                            <li><a href="doctorlogin.py"><i class="fas fa-user-md"></i> Doctor</a></li>
                            <li><a href="adminlogin.py"><i class="fas fa-user-shield"></i> Admin</a></li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                            <i class="fas fa-user-plus"></i> Register <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="patientreg.py"><i class="fas fa-procedures"></i> Patient</a></li>
                            <li><a href="volunteerreg.py"><i class="fas fa-hands-helping"></i> Volunteer</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container-fluid" style="margin-top: 100px;">
        <div class="row">
            <div class="col-md-8">
                <h1 class="text-center"><i class="fas fa-bullhorn"></i> Awareness Programs</h1>
                <div class="content-box" id="success-stories-container">""")

b = """select * from awarep where status='Initiated'"""
cur.execute(b)
program = cur.fetchall()
for i in program:
    print(f"""
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title text-center">{i[1]}</h3>
                        </div>
                        <div class="panel-body">
                            <div class="row">
                                <div class="col-md-7">
                                    <p><strong><i class="fas fa-map-marker-alt"></i> Location:</strong> {i[3]}</p>
                                    <p><strong><i class="far fa-clock"></i> Timing:</strong> {i[4]} - {i[5]}</p>
                                    <p><strong><i class="fas fa-user-tie"></i> Conducted by:</strong> {i[8]}</p>
                                    <button class="btn btn-primary" onclick="reg{i[0]}();">
                                        <i class="fas fa-user-plus"></i> Register
                                    </button>
                                </div>
                                <div class="col-md-5">
                                    <img src="awareprogramimages/{i[9]}" class="img-responsive awareness-img" alt="Program Image">
                                </div>
                            </div>
                        </div>
                    </div>
                    <script>
                        function reg{i[0]}(){{
                            location.href="volunteerreg.py?id={i[1]}";
                        }}
                    </script>""")

print("""
                </div>
            </div>

            <div class="col-md-1 divider hidden-xs hidden-sm"></div>

            <div class="col-md-3">
                <h1 class="text-center"><i class="fas fa-star"></i> Success Stories</h1>
                <div class="content-box" id="another-container">""")

d = """select * from succsto"""
cur.execute(d)
sucsto = cur.fetchall()
for b in sucsto:
    print(f"""
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title">{b[1]}</h3>
                        </div>
                        <div class="panel-body">
                            <blockquote style="font-style: italic; border-left: 3px solid var(--primary-color); padding-left: 15px;">
                                "{b[2]}"
                            </blockquote>
                        </div>
                    </div>""")

print("""
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer-custom">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <p class="text-center">&copy; 2023 SecondLife. All Rights Reserved.</p>
                    <p class="text-center">
                        <a href="#"><i class="fab fa-facebook-f fa-lg mx-2"></i></a>
                        <a href="#"><i class="fab fa-twitter fa-lg mx-2"></i></a>
                        <a href="#"><i class="fab fa-instagram fa-lg mx-2"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in fa-lg mx-2"></i></a>
                    </p>
                </div>
            </div>
        </div>
    </footer>

    <!-- JavaScript Libraries -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <script>
        // Function to auto-scroll the divs
        function autoScroll() {
            // First div scrolling
            let container1 = document.getElementById('success-stories-container');
            if (container1) {
                let scrollAmount1 = container1.scrollHeight - container1.clientHeight;
                let currentTime1 = 0;
                let increment1 = 20;
                let duration1 = 15000;

                let animateScroll1 = function() {
                    currentTime1 += increment1;
                    let val1 = Math.easeInOutQuad(currentTime1, 0, scrollAmount1, duration1);
                    container1.scrollTop = val1;

                    if (currentTime1 >= duration1) {
                        container1.scrollTop = 0;
                        currentTime1 = 0;
                    } else {
                        setTimeout(animateScroll1, increment1);
                    }
                };
                animateScroll1();
            }

            // Second div scrolling
            let container2 = document.getElementById('another-container');
            if (container2) {
                let scrollAmount2 = container2.scrollHeight - container2.clientHeight;
                let currentTime2 = 0;
                let increment2 = 20;
                let duration2 = 15000;

                let animateScroll2 = function() {
                    currentTime2 += increment2;
                    let val2 = Math.easeInOutQuad(currentTime2, 0, scrollAmount2, duration2);
                    container2.scrollTop = val2;

                    if (currentTime2 >= duration2) {
                        container2.scrollTop = 0;
                        currentTime2 = 0;
                    } else {
                        setTimeout(animateScroll2, increment2);
                    }
                };
                animateScroll2();
            }
        }

        // Easing function for smooth scrolling
        Math.easeInOutQuad = function(t, b, c, d) {
            t /= d / 2;
            if (t < 1) return (c / 2) * t * t + b;
            t--;
            return (-c / 2) * (t * (t - 2) - 1) + b;
        };

        // Call the autoScroll function when the page loads
        window.onload = function() {
            autoScroll();
        };

        // Smooth scrolling for all links
        $(document).ready(function(){
            $("a").on('click', function(event) {
                if (this.hash !== "") {
                    event.preventDefault();
                    var hash = this.hash;
                    $('html, body').animate({
                        scrollTop: $(hash).offset().top
                    }, 800, function(){
                        window.location.hash = hash;
                    });
                }
            });
        });
    </script>
</body>

</html>
""")