<?php
error_reporting(-1);
ini_set('display_errors', 'On');
?>

<!DOCTYPE html>
<html>

<head>
    <title>Trinity Hymnal</title>
    <!-- style -->
    <link rel="stylesheet" type="text/css" href="style.css">

    <!-- fonts -->
    <link href="https://fonts.googleapis.com/css?family=Raleway&display=swap" rel="stylesheet">

    <!-- icons -->
    <script src="https://unpkg.com/feather-icons"></script>

    <!-- top nav bar -->
    <div class="navBarWrapper">
        <div class="top bar">
            <ul class="left">
                <li class="title"><a href="">Trinity Hymnal</a></li>
            </ul>
            <ul class="right">
                <li class="buttons"><a class="iconLink" href="">History</a></li>
                <li class="buttons"> <a href="" class="otherPages">Admin</a></li>
            </ul>
        </div>
    </div>
</head>

<body>
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
                echo ("</table><h3>$sec: $subsec</h3><table>");
            }
            echo ("<tr><td>{$hymn["num"]}</td><td><a href=\"hymn.php?num={$hymn["num"]}\">{$hymn["title"]}</a></td>\n");
        }
        ?>
    </table>
</body>

</html>