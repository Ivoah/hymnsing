%from urllib.parse import quote

%title = hymn['title']

%rebase('templates/base.tpl')

<h2 class="hymn-title">#{{hymn['num']}}: {{hymn['title']}}</h2>

<div class="mb-25"><a href="https://hymnary.org/search?qu={{quote(hymn['title'])}}" target="_blank">Search Hymnary</a>
</div>
<audio controls src="https://hymnsing.ivoah.net/audio/Th2_{{'{:0>3}'.format(hymn['num'])}}.mp3">Your browser does not
    support audio playback</audio>

<h3>History</h3>
%if is_admin:
    <input type="text" id="datepicker" placeholder="Select Date">
    <button class="clickable" onclick="addHymn({{hymn['num']}})">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M0 0h24v24H0z" fill="none" />
            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" />
        </svg>
    </button>
    <br />
    <br />
%end

<table class="table">
    %for day in history:
        <tr>
            <td class="clickable" onclick="window.location.href = '/history#{{day['date'].isoformat()}}'">
                {{day['date'].strftime('%A %B %d, %Y')}}</td>
        </tr>
    %end
</table>
