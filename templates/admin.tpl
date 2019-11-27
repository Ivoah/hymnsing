%rebase('templates/base.tpl')

<div class="centered" style="display: flex;">
    <div class="input">
        <input type="password" id="input" class="input-text" autofocus="autofocus" placeholder="Admin Password">
        <label for="input" class="input-label">Admin Password</label>
    </div>
    <svg class="clickable" width="42" height="42" viewBox="0 0 24 24" onclick="alert('Login logic goes here')">
        <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8-8-8z" />
    </svg>
</div>