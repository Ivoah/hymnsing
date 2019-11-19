%rebase('templates/base.tpl')
%include('templates/search.tpl')

<div id="hymn-tables">
    %for section in sections:
        <table class="table table-borderless table-hover w-25 my-5">
            <thead class="hymns-section-head red lighten-1 white-text"><tr><th colspan="2" align="center">{{section[0]['section']}}: {{section[0]['subsection']}}</th></tr></thead>
            <tbody>
                %for hymn in section[1]:
                    <tr class="hymns clickable-row" onclick="window.location.href='{{hymn['num']}}';">
                        <td>{{hymn['num']}}</td>
                        <td>{{hymn['title']}}</td>
                    </tr>
                %end
            </tbody>
        </table>
    %end
</div>
