%from urllib.parse import quote

%rebase('templates/base.tpl')

<h2 class="mt-5">#{{hymn['num']}}: {{hymn['title']}}</h2>

<div class="my-5"><a href="https://hymnary.org/search?qu={{quote(hymn['title'])}}">Search Hymnary</a></div>
<audio controls src="/audio/Th2_{{'{:0>3}'.format(hymn['num'])}}.mp3">Your browser does not support audio playback</audio>

<h3 class="mt-5">History</h3>

<table class="table table-borderless table-hover mt-3 w-auto">
    %for day in history:
        <tr>
            <td><a href="/history#{{day['date'].isoformat()}}">{{day['date'].strftime('%A %B %d, %Y')}}</a></td>
        </tr>
    %end
</table>
