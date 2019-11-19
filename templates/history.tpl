%rebase('templates/base.tpl')

<a href="/history.png"><img src="/history.png"></a>
%for day in history:
    <h3 id="{{day['date'].isoformat()}}">{{day['date'].strftime('%A %B %d, %Y')}}</h3>
    <table>
        %for hymn in day['hymns'].strip('|').split('|'):
            <tr>
                <td>{{hymn}}</td>
                <td><a href="/{{hymn}}">{{hymns[int(hymn) - 1]['title']}}</a></td>
            </tr>
        %end
    </table>
%end
