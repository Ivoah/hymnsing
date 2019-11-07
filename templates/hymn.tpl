%from urllib.parse import quote

%rebase('templates/base.tpl')

%hymn = hymns[int(hymn) - 1]
<h2>#{{hymn['#']}}: {{hymn['title']}}</h2>

<a href="https://hymnary.org/search?qu={{quote(hymn['title'])}}">Search Hymnary</a>
<br />
<audio controls src="/audio/Th2_{{'{:0>3}'.format(hymn['#'])}}.mp3">Your browser does not support audio playback</audio>

<h3>History</h3>
<table>
    %for day in history:
        <tr>
            <td><a href="/history#{{day[0].isoformat()}}">{{day[0].strftime('%A %B %d, %Y')}}</a></td>
        </tr>
    %end
</table>
