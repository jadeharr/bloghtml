#!/usr/bin/env python3
"""Second page of website."""

import cgi
import cgitb
import pymysql

cgitb.enable()


def main():
    """Create web page."""
    print("Content-Type: text/html;charset=utf-8")
    print()

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
        position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .jumbotron {
            display: flex;
            align-items: center;
            background-image: url("https://format-com-cld-res.cloudinary.c\
om/image/private/s--AknKrISZ--/c_limit,g_center,h_1200,w_65535/a_auto,fl_k\
eep_iptc.progressive,q_95/203804-11191584-Thea_and_Jimmy_Wedding_Blog-10\
9_jpg.jpg");
            background-size: cover;
            height: 400px;
            text-shadow:
                -1.75px -1.75px 0 #556B2F,
                1.75px -1.75px 0 #556B2F,
                -1.75px 1.75px 0 #556B2F,
                1.75px 1.75px 0 #556B2F;
            color: #ffffff;
}

        .jumbotron h2 {
            font-size: 60px;
            font-weight: 700;
            margin: 0;
            color: #FFFAF0;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

        footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
    </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost/~jade/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost/~jade/cooking.py">
                            Cooking
                        </a>
                        <a href="http://localhost/~jade/travel.py">
                            Travel
                        </a>
                        <a href="http://localhost/~jade/plants.py">
                            Plants
                        </a>
                        <a href="http://localhost/~jade/photography.py">
                            Photography
                        </a>
                        <a href="http://localhost/~jade/decorating.py">
                            Decorating
                        </a>
                        <a href="http://localhost/~jade/books.py">
                            Books
                        </a>
                        <a href="http://localhost/~jade/blog.py">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
""")

    body_middle = ("""\
    <section class="jumbotron">
        <div class="container">
            <div class="row text-center">
                <h2>Decorating</h2>
            </div>
        </div>
    </section>
""")

    body_end = ("""\
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    print(head)
    print(body_start)
    print(body_middle)
    print(body_end)

if __name__ == "__main__":
    main()
