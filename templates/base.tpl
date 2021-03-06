<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        %try:
            <title>{{title}}</title>
        %except NameError:
            <title>Trinity Hymnal</title>
        %end

        <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
        <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
        <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

        <link href="https://fonts.googleapis.com/css?family=Roboto:100,400&display=swap" rel="stylesheet">

        <link rel="stylesheet" type="text/css" href="css/misc.css">
        <link rel="stylesheet" type="text/css" href="css/nav.css">
        <link rel="stylesheet" type="text/css" href="css/table.css">
        <link rel="stylesheet" type="text/css" href="css/heart.css">
        <link rel="stylesheet" type="text/css" href="css/login.css">
        
        <script type="text/javascript" src="js/hymnsing.js"></script>
    </head>

    <body>
        <nav>
            <a href="/" class="title">Trinity Hymnal</a>
            <div class="spacer"></div>
            <a href="/history">History</a>
            %if is_admin:
                <a href="/login" style="background-color: rgb(239, 83, 80)">Logout</a>
            %else:
                <a href="/login" onclick="sessionStorage.setItem('prev', location.href)">Admin</a>
            %end
        </nav>
        <div id="main">
            {{!base}}
        </div>
    </body>
</html>
