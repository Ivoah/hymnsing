%rebase('templates/base.tpl')

<a href="/history.png"><img src="/history.png"></a>

%for day in history:
    <h3 id="{{day[0].isoformat()}}">{{day[0].strftime('%A %B %d, %Y')}}</h3>
    <table>
        %for hymn in day[1].strip('|').split('|'):
            <tr>
                <td>{{hymn}}</td>
                <td><a href="/{{hymn}}">{{hymns[int(hymn) - 1]['title']}}</a></td>
            </tr>
        %end
    </table>
%end
