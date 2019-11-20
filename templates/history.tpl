%rebase('templates/base.tpl')

<a href="/history.png"><img src="/history.png"></a>

%include('templates/search.tpl')
<div id="hymn-tables">
    %for day in history:
    <table class="table table-borderless table-hover w-25 my-5">
            <thead id="{{day[0]['date'].isoformat()}}" class="hymns-section-head red lighten-1 white-text">
                <tr><th colspan="4">{{day[0]['date'].strftime('%A %B %d, %Y')}}</th></tr>
            </thead>

        <tbody>
            %for hymn in day[1]:
                %include('templates/innertable.tpl')
            %end
            </tbody>
    </table>
    %end
</div>
