%rebase('templates/base.tpl')
%include('templates/search.tpl')

<div id="hymn-tables">
    %for section in sections:
        <table>
            <thead><tr><th colspan="4">{{section[0]['section']}}: {{section[0]['subsection']}}</th></tr></thead>
            <tbody>
                %for hymn in section[1]:
                    %include('templates/innertable.tpl')
                %end
            </tbody>
        </table>
    %end
</div>
