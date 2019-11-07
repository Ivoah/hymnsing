<?php
error_reporting(-1);
ini_set('display_errors', 'On');
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Trinity Hymnal</title>
        <link rel="stylesheet" type="text/css" href="style.css">

        <script src="https://unpkg.com/feather-icons"></script>

        <nav class="topnav" id="myTopnav">
            <a href="#home" class="active">Home</a>
            <a href="#news">News</a>
            <a href="#contact">Contact</a>
            <a href="#about">About</a>
            <a href="javascript:void(0);" class="icon" onclick="myFunction()">
                <i class="fa fa-bars"></i>
            </a>
        </nav>
    </head>
    <body>
        <h1><a href="/">Trinity Hymnal</a></h1>
        <a href="/history">History</a>
        <hr>
        <table>
            <?php
                include("auth.php");

                $db = new mysqli($dbhost, $dbuser, $dbpassword, $dbdb);
                if ($db->connect_errno) {
                    die("Connection failed: " . $db->connect_error);
                }

                $hymns = $db->query("SELECT * from hymns");

                $sec = "";
                $subsec = "";
                while ($hymn = $hymns->fetch_assoc()) {
                    if ($hymn["section"] != $sec || $hymn["subsection"] != $subsec) {
                        $sec = $hymn["section"];
                        $subsec = $hymn["subsection"];
                        echo("</table><h3>$sec: $subsec</h3><table>");
                    }
                    echo("<tr><td>{$hymn["num"]}</td><td><a href=\"{$hymn["num"]}\">{$hymn["title"]}</a></td>\n");
                }
            ?>
        </table>
    </body>
</html>
