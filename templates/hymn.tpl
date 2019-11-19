%from urllib.parse import quote

%rebase('templates/base.tpl')

<h2>#{{hymn['num']}}: {{hymn['title']}}</h2>

<a href="https://hymnary.org/search?qu={{quote(hymn['title'])}}">Search Hymnary</a>
<br />
<audio controls src="/audio/Th2_{{'{:0>3}'.format(hymn['num'])}}.mp3">Your browser does not support audio playback</audio>

<h3>History</h3>
<table>
    %for day in history:
        <tr>
            <td><a href="/history#{{day['date'].isoformat()}}">{{day['date'].strftime('%A %B %d, %Y')}}</a></td>
        </tr>
    %end
</table>
