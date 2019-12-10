%rebase('templates/base.tpl')

%include('templates/search.tpl')

<svg width="600" height="500"></svg>
<link rel="stylesheet" href="css/d3.css">
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="js/history.js"></script>

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
