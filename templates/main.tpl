%rebase('templates/base.tpl')
<a href="/history">History</a>
<hr>
<table>
    <%sec = ''
    subsec = ''
    for hymn in hymns:
        if hymn['section'] != sec or hymn['subsection'] != subsec:
            sec = hymn['section']
            subsec = hymn['subsection']%>
            </table>
            <h3>{{sec}}: {{subsec}}</h3>
            <table>
        %end
        <tr>
            <td>{{hymn['#']}}</td>
            <td><a href="/{{hymn['#']}}">{{hymn['title']}}</a></td>
        </tr>
    %end
</table>
