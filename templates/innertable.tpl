<tr>
        <td class="clickable" onclick="window.location.href = '{{hymn['num']}}'">{{hymn['num']}}</td>
        <td class="clickable" onclick="window.location.href = '{{hymn['num']}}'">{{hymn['title']}}</td>
        <td class="clickable heart {{'liked' if hymn['num'] in likes else ''}}" num={{hymn['num']}}></td>
        <td>{{hymn['likes'] or 0}} like{{'' if hymn['likes'] == 1 else 's'}}</td>
</tr>
