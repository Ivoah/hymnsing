%rebase('templates/base.tpl')

<a href="/history.png"><img src="/history.png"></a>
%for day in history:
<table class="table table-borderless table-hover w-25 my-5">
        <thead id="{{day[0]['date'].isoformat()}}" class="hymns-section-head red lighten-1 white-text">
            <tr><th colspan="2" align="center">{{day[0]['date'].strftime('%A %B %d, %Y')}}</th></tr>
        </thead>

    <tbody>
        %for hymn in day[1]:
            <tr class="hymns clickable-row" onclick="window.location.href = '{{hymn['num']}}'">
                <td>{{hymn['num']}}</td>
                <td>{{hymn['title']}}</td>
            </tr>
        %end
        </tbody>
</table>
%end