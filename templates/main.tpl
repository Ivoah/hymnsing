%rebase('templates/base.tpl')
<div class="container mt-5">
    <div class="active-black mb-4">
        <input id="hymn-search" class="form-control" type="search" placeholder="Search" aria-label="Search" aria-controls="hymns">
    </div>
</div>

<div id="hymn-tables">
    <table>
        <%sec = ''
        subsec = ''
        for hymn in hymns:
            if hymn['section'] != sec or hymn['subsection'] != subsec:
                sec = hymn['section']
                subsec = hymn['subsection']%>
                </table>
    
                <table class="table table-borderless table-hover w-auto my-5">
                    <thead class="red lighten-1 white-text"><tr><th colspan="2" align="center">{{sec}}: {{subsec}}</th></tr></thead>
            %end
            <tr class="clickable-row" onclick="window.location.href = '{{hymn['#']}}';">
                <td>{{hymn['#']}}</td>
                <td>{{hymn['title']}}</td>
            </tr>
        %end
    </table>
</div>