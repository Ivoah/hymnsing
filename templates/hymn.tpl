%from urllib.parse import quote

%rebase('templates/base.tpl')

<h2>#{{hymn['num']}}: {{hymn['title']}}</h2>

<div><a href="https://hymnary.org/search?qu={{quote(hymn['title'])}}">Search Hymnary</a></div>
<!-- <audio controls src="/audio/Th2_{{'{:0>3}'.format(hymn['num'])}}.mp3">Your browser does not support audio playback</audio> -->
<audio controls src="https://hymnsing.ivoah.net/audio/Th2_{{'{:0>3}'.format(hymn['num'])}}.mp3">Your browser does not support audio playback</audio>

<h3>History</h3>
%if is_admin:
    <input type="text" id="datepicker"> <button onclick="addHymn({{hymn['num']}})">Add to history</button>
%end

<table class="table">
    %for day in history:
        <tr>
            <td><a href="/history#{{day['date'].isoformat()}}">{{day['date'].strftime('%A %B %d, %Y')}}</a></td>
        </tr>
    %end
</table>
