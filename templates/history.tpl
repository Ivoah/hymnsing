%rebase('templates/base.tpl')

<a href="/history.png"><img src="/history.png"></a>
%for day in history:
    <h3 id="{{day[0]['date'].isoformat()}}">{{day[0]['date'].strftime('%A %B %d, %Y')}}</h3>
    <table>
        %for hymn in day[1]:
            <tr>
                <td>{{hymn['num']}}</td>
                <td><a href="/{{hymn['num']}}">{{hymn['title']}}</a></td>
            </tr>
        %end
    </table>
%end
