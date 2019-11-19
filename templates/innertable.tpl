<tr class="hymns">
        <td class="clickable-row" onclick="window.location.href = '{{hymn['num']}}'">{{hymn['num']}}</td>
        <td class="clickable-row" style="width: 60%" onclick="window.location.href = '{{hymn['num']}}'">{{hymn['title']}}</td>
        <td class="heart table-hover-darker {{'liked' if hymn['num'] in likes else ''}}" num={{hymn['num']}}></td>
        <td class="likes" style="text-align:right; vertical-align: middle; max-width: 90px;">{{hymn['likes'] or 0}} like{{'' if hymn['likes'] == 1 else 's'}}</td>
</tr>
