%rebase('templates/base.tpl')
<div class="container mt-lg-5">
    <div class="active-pink-4 mb-4">
        <input class="form-control" type="search" placeholder="Search" aria-label="Search" aria-controls="hymns">
    </div>
</div>
<table class="table">
    <%sec = ''
            subsec = ''
            for hymn in hymns:
                if hymn['section'] != sec or hymn['subsection'] != subsec:
                    sec = hymn['section']
                    subsec = hymn['subsection']%>
</table>

<table id="hymns" class="table table-borderless table-hover w-auto my-lg-5">
    <thead class="red lighten-1 white-text"><tr><th colspan="2" align="center">{{sec}}: {{subsec}}</th></tr></thead>
    %end
    <tr class="clickable-row" onclick="window.location.href = '{{hymn['#']}}';">
        <td>{{hymn['#']}}</td>
        <td>{{hymn['title']}}</td>
    </tr>
    %end
</table>

<!-- <table id="hymns" class="table table-borderless table-hover w-auto">
    <%sec = ''
            subsec = ''
            for hymn in hymns:
                if hymn['section'] != sec or hymn['subsection'] != subsec:
                    sec = hymn['section']
                    subsec = hymn['subsection']%>
                    <tr class="black white-text">{{sec}}: {{subsec}}</tr>
                    %end
                <tr class="clickable-row" onclick="window.location.href = '{{hymn['#']}}';">
                    <td>{{hymn['#']}}</td>
                    <td>{{hymn['title']}}</td>
                </tr>
                 %end
</table> -->